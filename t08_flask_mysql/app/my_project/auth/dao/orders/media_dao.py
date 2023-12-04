from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Media
from typing import List
from sqlalchemy import text

class MediaDAO(GeneralDAO):
    """
    Realization of Media data access layer for TripAdvisor's review media.
    """
    _domain_type = Media

    def insert_new_media_parametrized(self, media_review_id, media_type, media_url, media_upload_date):
        try:
            self._session.execute(text(
                f"CALL InsertIntoMedia({media_review_id}, '{media_type}', '{media_url}', '{media_upload_date}')",
            ))
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"

    def insert_10_new_media(self):
        try:
            self._session.execute(text("CALL Insert10NewMedia()"))
            self._session.commit()
            return "Insert successful"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
