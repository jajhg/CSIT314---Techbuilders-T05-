from extensions import db
from sqlalchemy import or_
from datetime import datetime
from app.entity.service_matches       import ServiceMatches
from app.entity.cleaning_services   import CleaningService
from app.entity.user_account        import UserAccount

class HomeownerMatchHistoryController:
    @staticmethod
    def list_matches(homeowner_id, text=None, date_from=None, date_to=None):
        q = (
            db.session.query(
                ServiceMatches,
                CleaningService.title.label("service_title"),
                UserAccount.username.label("cleaner_name")
            )
            .join(CleaningService, CleaningService.id == ServiceMatches.service_id)
            .join(UserAccount,   UserAccount.id   == ServiceMatches.cleaner_id)
            .filter(ServiceMatches.homeowner_id == homeowner_id)
        )

        if text:
            like = f"%{text.strip()}%"
            q = q.filter(or_(
                CleaningService.title.ilike(like),
                UserAccount.username.ilike(like)
            ))

        if date_from:
            q = q.filter(ServiceMatches.match_date >= date_from)
        if date_to:
            q = q.filter(ServiceMatches.match_date <= date_to)

        q = q.order_by(ServiceMatches.match_date.desc())

        return [
            {
                "match_date"   : m.match_date.strftime('%Y-%m-%d %H:%M'),
                "service_title": title,
                "cleaner_name" : cleaner
            }
            for m, title, cleaner in q.all()
        ]