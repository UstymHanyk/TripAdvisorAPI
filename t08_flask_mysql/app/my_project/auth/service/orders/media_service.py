from t08_flask_mysql.app.my_project.auth.dao import media_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class MediaService(GeneralService):
    """
    Realization of Media service.
    """
    _dao = media_dao
