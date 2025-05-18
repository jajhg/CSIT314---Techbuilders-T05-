from extensions import db
from app.entity.cleaning_services import CleaningService
from app.entity.enums import CleaningType, SupplyOption, TimeSlot
from app.entity.service_category import ServiceCategory

class ServiceController:
    @staticmethod
    def create_service(cleaner_id, service_data):
        try:
            new_service = CleaningService(
                cleaner_id=cleaner_id,
                title=service_data['title'],
                description=service_data['description'],
                location=service_data['location'],
                postal_code=service_data['postal_code'],
                rate=float(service_data['rate']),
                rate_type=service_data['rate_type'],
                min_hours=int(service_data.get('min_hours', 0)),
                days_available=service_data.get('available_day', ''),
                time_slots=service_data.get('time_slot', ''),
                cleaning_types=service_data.get('type_of_cleaning', ''),
                supplies=service_data.get('supplies', 'No'),
                languages=service_data.get('languages', '')
            )
            
            db.session.add(new_service)
            db.session.commit()
            return True, "Service created successfully"
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_service_form_options():
        return {
            'cleaning_types': [
                {'value': category.category_name, 'label': category.category_name}
                for category in ServiceCategory.query.all()
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