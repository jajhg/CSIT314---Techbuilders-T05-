from extensions import db
from sqlalchemy import func
from app.entity.service_views     import ServiceViews   # your model class
from app.entity.shortlist         import Shortlist
from app.entity.cleaning_services import CleaningService


class CleanerViewTrackingController:
    @staticmethod
    def get_view_counts(cleaner_id):

        # Subquery: views per service
        view_counts = (
            db.session.query(
                ServiceViews.service_id,
                func.count(ServiceViews.id).label("views")
            )
            .group_by(ServiceViews.service_id)
            .subquery()
        )

        # Subquery: shortlists per service
        shortlist_counts = (
            db.session.query(
                Shortlist.service_id,
                func.count(Shortlist.id).label("shortlists")
            )
            .group_by(Shortlist.service_id)
            .subquery()
        )

        # Main query joins cleaner's services to both subqueries
        rows = (
            db.session.query(
                CleaningService.title,
                func.coalesce(view_counts.c.views, 0).label("views"),
                func.coalesce(shortlist_counts.c.shortlists, 0).label("shortlists")
            )
            .outerjoin(view_counts,   view_counts.c.service_id   == CleaningService.id)
            .outerjoin(shortlist_counts, shortlist_counts.c.service_id == CleaningService.id)
            .filter(CleaningService.cleaner_id == cleaner_id)
            .order_by(CleaningService.title)
            .all()
        )

        return [
            {"title": r.title, "views": r.views, "shortlists": r.shortlists}
            for r in rows
        ]