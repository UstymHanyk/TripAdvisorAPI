from t08_flask_mysql.app.my_project.auth.service import media_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class MediaController(GeneralController):
    """
    Realization of Media controller.
    """
    _service = media_service

    def insert_10_new_media(self):
        result = self._service.insert_10_new_media()
        return result

    def insert_new_media_parametrized(self, review_id, type, url, upload_date):
        result = self._service.insert_new_media_parametrized(review_id, type, url, upload_date)
        return result
