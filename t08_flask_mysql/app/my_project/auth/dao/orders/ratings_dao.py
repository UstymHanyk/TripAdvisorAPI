from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Rating
from typing import List

class RatingDAO(GeneralDAO):
    """
    Realization of Rating data access layer for TripAdvisor's ratings.
    """
    _domain_type = Rating

    def find_by_place_id(self, place_id: int) -> List[object]:
        """
        Gets ratings objects from the database table by place_id.
        :param place_id: place_id value
        :return: search objects
        """
        return self._session.query(Rating).filter(Rating.place_id == place_id).all()

    def find_by_overall_rating(self, overall_rating: float) -> List[object]:
        """
        Gets ratings objects from the database table by overall_rating.
        :param overall_rating: overall_rating value
        :return: search objects
        """
        return self._session.query(Rating).filter(Rating.overall_rating == overall_rating).all()

    def find_by_cleanliness_rating(self, cleanliness_rating: float) -> List[object]:
        """
        Gets ratings objects from the database table by cleanliness_rating.
        :param cleanliness_rating: cleanliness_rating value
        :return: search objects
        """
        return self._session.query(Rating).filter(Rating.cleanliness_rating == cleanliness_rating).all()

    def find_by_service_rating(self, service_rating: float) -> List[object]:
        """
        Gets ratings objects from the database table by service_rating.
        :param service_rating: service_rating value
        :return: search objects
        """
        return self._session.query(Rating).filter(Rating.service_rating == service_rating).all()

    def find_by_value_rating(self, value_rating: float) -> List[object]:
        """
        Gets ratings objects from the database table by value_rating.
        :param value_rating: value_rating value
        :return: search objects
        """
        return self._session.query(Rating).filter(Rating.value_rating == value_rating).all()

