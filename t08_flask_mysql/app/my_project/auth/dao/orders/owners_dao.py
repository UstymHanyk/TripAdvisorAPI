from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Owner
from typing import List

class OwnerDAO(GeneralDAO):
    """
    Realization of Owner data access layer for TripAdvisor's owners.
    """
    _domain_type = Owner

    def find_by_email(self, email: str) -> List[object]:
        """
        Gets owner objects from the database table by email.
        :param email: email value
        :return: search objects
        """
        return self._session.query(Owner).filter(Owner.email == email).all()

    def find_by_contact_number(self, contact_number: str) -> List[object]:
        """
        Gets owner objects from the database table by contact number.
        :param contact_number: contact number value
        :return: search objects
        """
        return self._session.query(Owner).filter(Owner.contact_number == contact_number).all()

