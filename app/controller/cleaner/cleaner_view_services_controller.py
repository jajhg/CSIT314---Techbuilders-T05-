from app.entity.cleaning_services import CleaningService

class CleanerServiceController:
    @staticmethod
    def get_services(cleaner_id):
        return CleaningService.query.filter_by(cleaner_id=cleaner_id).all()
    
    @staticmethod
    def get_service(service_id, cleaner_id):
        return CleaningService.query.filter_by(id=service_id, cleaner_id=cleaner_id).first()
