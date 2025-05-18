from app.entity.cleaning_services import CleaningService
from extensions import db

class HomeownerSearchController:
    @staticmethod
    def get_filter_options():
        days = db.session.query(
            CleaningService.available_day
        ).distinct().all()
        
        slots = db.session.query(
            CleaningService.time_slot
        ).distinct().all()
        
        types = db.session.query(
            CleaningService.type_of_cleaning
        ).distinct().all()
        
        return {
            'available_days': [day[0] for day in days],
            'time_slots': [slot[0] for slot in slots],
            'cleaning_types': [t[0] for t in types]
        }

    @staticmethod
    def search_services(filters):
        query = CleaningService.query
        
        if filters.get('available_day'):
            query = query.filter(CleaningService.available_day == filters['available_day'])
        if filters.get('time_slot'):
            query = query.filter(CleaningService.time_slot == filters['time_slot'])
        if filters.get('type_of_cleaning'):
            query = query.filter(CleaningService.type_of_cleaning == filters['type_of_cleaning'])
            
        return query.all()