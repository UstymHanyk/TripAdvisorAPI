from t08_flask_mysql.app.my_project.auth.dao import media_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class MediaService(GeneralService):
    """
    Realization of Media service.
    """
    _dao = media_dao
    def insert_10_new_media(self):
        result = self._dao.insert_10_new_media()
        return result

    def insert_new_media_parametrized(self, review_id, type, url, upload_date):
        result = self._dao.insert_new_media_parametrized(review_id, type, url, upload_date)
        return result