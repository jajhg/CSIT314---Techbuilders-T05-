from app import db
from app.entity.cleaning_services import CleaningService
from app.entity.user_account import UserAccount

class HomeownerView:
    @staticmethod
    def get_service_details(service_id):
        """Get service and cleaner details for viewing"""
        service = CleaningService.query.get(service_id)
        cleaner = UserAccount.query.get(service.cleaner_id) if service else None
        return service, cleaner