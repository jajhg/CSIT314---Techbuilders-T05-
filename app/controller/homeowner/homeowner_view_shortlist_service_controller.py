from app.entity.shortlist import Shortlist
from app.entity.cleaning_services import CleaningService
from app import db

class HomeownerViewShortlistController:
    @staticmethod
    def get_shortlisted_services(homeowner_id):
        return db.session.query(CleaningService).join(Shortlist).filter(
            Shortlist.homeowner_id == homeowner_id
        ).all()