from app.entity.shortlist import Shortlist
from app.entity.cleaning_services import CleaningService
from app import db
from sqlalchemy import or_

class HomeownerShortlistController:
    @staticmethod
    def get_shortlisted_services(homeowner_id, search_query=None):
        query = db.session.query(CleaningService).join(Shortlist).filter(
            Shortlist.homeowner_id == homeowner_id
        )
        if search_query:
            search = f"%{search_query}%"
            query = query.filter(CleaningService.title.ilike(search))
        return query.all()

    @staticmethod
    def add_to_shortlist(homeowner_id, service_id):
        existing = Shortlist.query.filter_by(
            homeowner_id=homeowner_id,
            service_id=service_id
        ).first()
        if existing:
            return False
        
        new_entry = Shortlist(
            homeowner_id=homeowner_id,
            service_id=service_id
        )
        db.session.add(new_entry)
        db.session.commit()
        return True