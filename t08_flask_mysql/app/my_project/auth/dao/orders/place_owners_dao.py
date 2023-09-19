from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import PlaceOwner
from typing import List

class PlaceOwnerDAO(GeneralDAO):
    """
    Realization of PlaceOwner data access layer for TripAdvisor's place_owners.
    """
    _domain_type = PlaceOwner

    def find_by_place_id(self, place_id: int) -> List[object]:
        """
        Gets place_owner objects from the database table by place_id.
        :param place_id: place_id value
        :return: search objects
        """
        return self._session.query(PlaceOwner).filter(PlaceOwner.place_id == place_id).all()

    def find_by_owner_id(self, owner_id: int) -> List[object]:
        """
        Gets place_owner objects from the database table by owner_id.
        :param owner_id: owner_id value
        :return: search objects
        """
        return self._session.query(PlaceOwner).filter(PlaceOwner.owner_id == owner_id).all()

