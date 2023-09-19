from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Rating(db.Model):
    __tablename__ = "ratings"

    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
    overall_rating = db.Column(db.DECIMAL(5, 2))
    cleanliness_rating = db.Column(db.DECIMAL(5, 2))
    service_rating = db.Column(db.DECIMAL(5, 2))
    value_rating = db.Column(db.DECIMAL(5, 2))

    def __repr__(self) -> str:
        return f"Rating(id={self.id}, place_id={self.place_id}, " \
               f"overall_rating={self.overall_rating}, cleanliness_rating={self.cleanliness_rating}, " \
               f"service_rating={self.service_rating}, value_rating={self.value_rating})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'place_id': self.place_id,
            'overall_rating': float(self.overall_rating),
            'cleanliness_rating': float(self.cleanliness_rating),
            'service_rating': float(self.service_rating),
            'value_rating': float(self.value_rating)
        }

    @staticmethod
    def create_from_dto(place_dict: Dict[str, Any]) :
        if 'id' in place_dict:
            return Rating(
                **place_dict
            )
        else:
            return Rating(
                **{k: v for k, v in place_dict.items() if k != 'id'}
            )
