from app.entity.cleaning_services import CleaningService
from extensions import db

class CleanerSearchController:
    @staticmethod
    def get_filter_options(cleaner_id):
        days = db.session.query(
            CleaningService.available_day
        ).filter_by(cleaner_id=cleaner_id).distinct().all()
        
        slots = db.session.query(
            CleaningService.time_slot
        ).filter_by(cleaner_id=cleaner_id).distinct().all()
        
        types = db.session.query(
            CleaningService.type_of_cleaning
        ).filter_by(cleaner_id=cleaner_id).distinct().all()
        
        return {
            'available_days': [day[0] for day in days],
            'time_slots': [slot[0] for slot in slots],
            'cleaning_types': [t[0] for t in types]
        }

    @staticmethod
    def search_services(cleaner_id, available_day=None, time_slot=None, type_of_cleaning=None):
        query = CleaningService.query.filter_by(cleaner_id=cleaner_id)
        
        if available_day:
            query = query.filter(CleaningService.available_day == available_day)
        if time_slot:
            query = query.filter(CleaningService.time_slot == time_slot)
        if type_of_cleaning:
            query = query.filter(CleaningService.type_of_cleaning == type_of_cleaning)
            
        return query.all()