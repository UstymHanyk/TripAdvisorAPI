from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import User
from typing import List

class UserDAO(GeneralDAO):
    """
    Realization of User data access layer for TripAdvisor's users.
    """
    _domain_type = User

    def find_by_email(self, email: str) -> List[object]:
        """
        Gets user objects from the database table by email.
        :param email: email value
        :return: search objects
        """
        return self._session.query(User).filter(User.email == email).all()

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets user objects from the database table by name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(User).filter(User.name == name).all()

