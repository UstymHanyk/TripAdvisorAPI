from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Amenity
from typing import List

class AmenityDAO(GeneralDAO):
    """
    Data Access Object for handling operations related to amenities.
    """
    _domain_type = Amenity

    def find_by_id(self, amenity_id: int) -> Amenity:
        """
        Retrieve an Amenity object by its ID.
        """
        return self._session.query(Amenity).filter(Amenity.id == amenity_id).first()

