from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Place(db.Model):
    __tablename__ = "places"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    country = db.Column(db.String(45), nullable=False)
    latitude = db.Column(db.DECIMAL(9, 6), nullable=True)
    longitude = db.Column(db.DECIMAL(9, 6), nullable=True)
    description = db.Column(db.TEXT, nullable=True)
    category = db.Column(db.String(45), nullable=True)
    working_hours = db.Column(db.String(45), nullable=True)


    def __repr__(self) -> str:
        return f"Place(id={self.id}, name='{self.name}', city='{self.city}', country='{self.country}', latitude={self.latitude}, longitude={self.longitude}, description='{self.description}', category='{self.category}', working_hours='{self.working_hours}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'country': self.country,
            'latitude': float(self.latitude) if self.latitude is not None else None,
            'longitude': float(self.longitude) if self.longitude is not None else None,
            'description': self.description,
            'category': self.category,
            'working_hours': self.working_hours
        }

    @staticmethod
    def create_from_dto(place_dict: Dict[str, Any]) :
        if 'id' in place_dict:
            return Place(
                **place_dict
            )
        else:
            return Place(
                **{k: v for k, v in place_dict.items() if k != 'id'}
            )