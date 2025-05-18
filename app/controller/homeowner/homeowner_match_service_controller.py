from extensions import db
from datetime import datetime
from app.entity.service_matches import ServiceMatches
from app.entity.cleaning_services import CleaningService

class HomeownerMatchServiceController:

    @staticmethod
    def create_match(service_id, homeowner_id):
        # Get the cleaner who owns this service
        service = CleaningService.query.filter_by(id=service_id).first()
        if not service:
            return False, "Service not found"

        match = ServiceMatches(
            service_id=service_id,
            homeowner_id=homeowner_id,
            cleaner_id=service.cleaner_id,  # assuming field exists
            match_date=datetime.utcnow()
        )
        db.session.add(match)
        db.session.commit()
        return True, "Matched successfully"