from app.entity.homeowner_view import HomeownerView

class HomeownerViewServiceController:
    @staticmethod
    def get_service_details(service_id):
        return HomeownerView.get_service_details(service_id)