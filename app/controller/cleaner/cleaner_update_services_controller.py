from extensions import db
from app.entity.cleaning_services import CleaningService
from app.entity.enums import CleaningType, SupplyOption, TimeSlot
from app.entity.service_category import ServiceCategory

class ServiceUpdateController:
    @staticmethod
    def get_service_for_update(service_id, cleaner_id):
        return CleaningService.query.filter_by(id=service_id, cleaner_id=cleaner_id).first()

    @staticmethod
    def update_service(service_id, cleaner_id, service_data):
        try:
            service = CleaningService.query.filter_by(id=service_id, cleaner_id=cleaner_id).first()
            if not service:
                return False, "Service not found"
            
            service.title = service_data['title']
            service.description = service_data['description']
            service.location = service_data['location']
            service.postal_code = service_data['postal_code']
            service.rate = float(service_data['rate'])
            service.rate_type = service_data['rate_type']
            service.min_hours = int(service_data.get('min_hours', 0))
            service.days_available = service_data.get('available_day', '')
            service.time_slots = service_data.get('time_slot', '')
            service.type_of_cleaning = service_data.get('type_of_cleaning', '')
            service.supplies = service_data.get('supplies', 'No')
            service.languages = service_data.get('languages', '')
            
            db.session.commit()
            return True, "Service updated successfully"
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_update_form_options():
        return {
            'cleaning_types':  [
                {'value': cat.category_name, 'label': cat.category_name}
                for cat in ServiceCategory.query.all()
            ],
            'supply_options': [{'value': so.name, 'label': so.value} for so in SupplyOption],
            'time_slots': [{'value': ts.name, 'label': ts.value} for ts in TimeSlot],
            'week_days': [
                {'value': 'mon', 'label': 'Monday'},
                {'value': 'tue', 'label': 'Tuesday'},
                {'value': 'wed', 'label': 'Wednesday'},
                {'value': 'thu', 'label': 'Thursday'},
                {'value': 'fri', 'label': 'Friday'},
                {'value': 'sat', 'label': 'Saturday'},
                {'value': 'sun', 'label': 'Sunday'}
            ]
        }
    