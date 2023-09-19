from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import UserDetails
from typing import List

class UserDetailsDAO(GeneralDAO):
    """
    Realization of UserDetails data access layer.
    """
    _domain_type = UserDetails

    def find_by_user_id(self, user_id: int) -> List[object]:
        """
        Gets UserDetails objects from the database table by user_id.
        :param user_id: user_id value
        :return: search objects
        """
        return self._session.query(UserDetails).filter(UserDetails.user_id == user_id).all()
