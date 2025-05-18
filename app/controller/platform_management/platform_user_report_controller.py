from extensions import db
from app.entity.user_profile import UserProfile
from app.entity.user_account import UserAccount
from sqlalchemy import func, case
from datetime import datetime

class PlatformUserReportController:
    @staticmethod
    def generate_user_report(group_by='day'):
        if group_by == 'week':
            date_label = func.date_format(UserAccount.created_at,'%x-W%v' ) 
        elif group_by == 'month':
            date_label = func.date_format(UserAccount.created_at, '%Y-%m')
        else:
            date_label = func.date_format(UserAccount.created_at, '%Y-%m-%d')

        results = db.session.query(
            UserProfile.user_type,
            date_label.label('period'),
            func.count(UserProfile.id).label('total_users'),
            func.sum(case((UserAccount.is_suspended == True, 1), else_=0)).label('suspended_users'),
            func.sum(case((UserAccount.is_suspended == False, 1), else_=0)).label('active_users')
        ).join(UserAccount, UserProfile.id == UserAccount.id
        ).group_by('period', UserProfile.user_type
        ).order_by('period', UserProfile.user_type).all()

        return [
            {
                'user_type': row.user_type,
                'period': row.period,
                'total_users': row.total_users,
                'active_users': row.active_users,
                'suspended_users': row.suspended_users
            }
            for row in results
        ]