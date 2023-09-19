from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Place
from typing import List

class PlaceDAO(GeneralDAO):
    """
    Realization of Place data access layer for TripAdvisor's places.
    """
    _domain_type = Place

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets place objects from the database table by name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Place).filter(Place.name == name).all()

    def find_by_city(self, city: str) -> List[object]:
        """
        Gets place objects from the database table by city.
        :param city: city value
        :return: search objects
        """
        return self._session.query(Place).filter(Place.city == city).all()

    def find_by_country(self, country: str) -> List[object]:
        """
        Gets place objects from the database table by country.
        :param country: country value
        :return: search objects
        """
        return self._session.query(Place).filter(Place.country == country).all()

    def find_by_category(self, category: str) -> List[object]:
        """
        Gets place objects from the database table by category.
        :param category: category value
        :return: search objects
        """
        return self._session.query(Place).filter(Place.category == category).all()

    def find_by_coordinates(self, latitude: float, longitude: float) -> List[object]:
        """
        Gets place objects from the database table by latitude and longitude.
        :param latitude: latitude value
        :param longitude: longitude value
        :return: search objects
        """
        return self._session.query(Place).filter(Place.latitude == latitude, Place.longitude == longitude).all()

