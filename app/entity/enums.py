# app/entity/enums.py
from enum import Enum

class CleaningType(Enum):
    REGULAR = "Regular Cleaning"
    DEEP = "Deep Cleaning"
    POST_RENOVATION = "Post-renovation"
    MOVE_IN_OUT = "Move-in/out"
    OFFICE = "Office Cleaning"

class SupplyOption(Enum):
    YES = "Yes"
    NO = "No"
    OPTIONAL = "Optional"

class TimeSlot(Enum):
    MORNING = "Morning (8AM-12PM)"
    AFTERNOON = "Afternoon (12PM-5PM)"
    EVENING = "Evening (5PM-9PM)"