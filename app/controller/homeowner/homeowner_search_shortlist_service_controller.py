from app.entity.shortlist import Shortlist
from app.entity.cleaning_services import CleaningService
from app import db

class HomeownerSearchShortlistController:
    @staticmethod
    def search_shortlist(homeowner_id, keyword):
        return db.session.query(CleaningService).join(Shortlist).filter(
            Shortlist.homeowner_id == homeowner_id,
            CleaningService.title.ilike(f'%{keyword}%')
        ).all()