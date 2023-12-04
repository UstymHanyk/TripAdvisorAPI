from t08_flask_mysql.app.my_project.auth.service import place_owners_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class PlaceOwnersController(GeneralController):
    """
    Realization of Place Owners controller.
    """
    _service = place_owners_service

    def insert_new_place_owner_pair(self, place_id, owner_id):
        result = self._service.insert_new_place_owner_pair(place_id, owner_id)
        return result