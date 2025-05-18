from extensions import db
from app.entity.cleaning_services import CleaningService
from app.entity.service_matches import ServiceMatches  # Import the match model

class ServiceDeleteController:
    @staticmethod
    def delete_service(service_id, cleaner_id):
        try:
            print(f"Attempting to delete service {service_id} for cleaner {cleaner_id}")
            
            # First delete all related matches
            matches_deleted = ServiceMatches.query.filter_by(service_id=service_id).delete()
            print(f"Deleted {matches_deleted} related matches")
            
            # Then delete the service
            service = CleaningService.query.filter_by(id=service_id, cleaner_id=cleaner_id).first()
            
            if not service:
                print("Service not found or doesn't belong to this cleaner")
                return False, "Service not found or you don't have permission to delete it"
            
            print(f"Found service to delete: {service.title}")
            db.session.delete(service)
            db.session.commit()
            
            print("Service deleted successfully")
            return True, "Service deleted successfully"
            
        except Exception as e:
            db.session.rollback()
            print(f"Error deleting service: {str(e)}")
            return False, f"Error deleting service: {str(e)}"