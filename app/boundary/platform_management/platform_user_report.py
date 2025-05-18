from flask import render_template, request
from app.controller.platform_management.platform_user_report_controller import PlatformUserReportController
from flask import Response
import csv
from io import StringIO

class PlatformUserReport:
    def display_report(self):
        group_by = request.args.get('group_by', 'month')  # default to monthly
        report_data = PlatformUserReportController.generate_user_report(group_by=group_by)
        return render_template('platform_user_report.html', report=report_data, group_by=group_by)
    
    def download_report_csv(self, group_by='monthly'):
        report_data = PlatformUserReportController.generate_user_report(group_by)

        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['Period', 'User Type', 'Total Users', 'Active Users', 'Suspended Users'])

        for row in report_data:
            writer.writerow([
                row['period'],
                row['user_type'],
                row['total_users'],
                row['active_users'],
                row['suspended_users']
            ])

        output.seek(0)
        return Response(output, mimetype='text/csv',
                        headers={"Content-Disposition": f"attachment;filename=userreport{group_by}.csv"})