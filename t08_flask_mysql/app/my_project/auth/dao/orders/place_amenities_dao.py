from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import PlaceAmenity
from typing import List

class PlaceAmenityDAO(GeneralDAO):
    """
    Data Access Object for handling operations related to place amenities.
    """
    _domain_type = PlaceAmenity

    def find_by_place_id(self, place_id: int) -> List[PlaceAmenity]:
        """
        Retrieve PlaceAmenity objects by place ID.
        """
        return self._session.query(PlaceAmenity).filter(PlaceAmenity.place_id == place_id).all()

    def find_by_amenity_id(self, amenity_id: int) -> List[PlaceAmenity]:
        """
        Retrieve PlaceAmenity objects by amenity ID.
        """
        return self._session.query(PlaceAmenity).filter(PlaceAmenity.amenity_id == amenity_id).all()
