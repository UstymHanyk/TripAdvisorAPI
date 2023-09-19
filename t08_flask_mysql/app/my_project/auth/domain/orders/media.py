from typing import Dict, Any
from t08_flask_mysql.app.my_project import db





class Media(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    type = db.Column(db.String(45))
    url = db.Column(db.String(200))
    upload_date = db.Column(db.DATE)

    def __repr__(self) -> str:
        return f"Media(id={self.id}, review_id={self.review_id}, " \
               f"type={self.type}, url={self.url}, upload_date={self.upload_date})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'review_id': self.review_id,
            'type': self.type,
            'url': self.url,
            'upload_date': str(self.upload_date)
        }

    @staticmethod
    def create_from_dto(place_dict: Dict[str, Any]) :
        if 'id' in place_dict:
            return Media(
                **place_dict
            )
        else:
            return Media(
                **{k: v for k, v in place_dict.items() if k != 'id'}
            )