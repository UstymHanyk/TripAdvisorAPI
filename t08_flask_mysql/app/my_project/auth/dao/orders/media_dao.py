from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Media
from typing import List

class MediaDAO(GeneralDAO):
    """
    Realization of Media data access layer for TripAdvisor's review media.
    """
    _domain_type = Media

    def find_by_review_id(self, review_id: int) -> List[object]:
        """
        Gets media objects from the database table by review ID.
        :param review_id: review ID value
        :return: search objects
        """
        return self._session.query(Media).filter(Media.review_id == review_id).all()

    def find_by_type(self, media_type: str) -> List[object]:
        """
        Gets media objects from the database table by media type.
        :param media_type: media type value
        :return: search objects
        """
        return self._session.query(Media).filter(Media.type == media_type).all()

