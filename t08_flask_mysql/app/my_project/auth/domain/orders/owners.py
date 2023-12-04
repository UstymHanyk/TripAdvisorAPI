from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Owner(db.Model):
    __tablename__ = "owners"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    contact_number = db.Column(db.String(45), nullable=False)

    owner_places = db.relationship("PlaceOwner", backref="owner")

    def __repr__(self) -> str:
        return f"Owner(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', contact_number='{self.contact_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        places_info = [{"name": place_owner_pair.place.name,
                      "description": place_owner_pair.place.description
                      } for place_owner_pair in self.owner_places]
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'contact_number': self.contact_number,
            "places_info": places_info
        }

    @staticmethod
    def create_from_dto(place_dict: Dict[str, Any]) :
        if 'id' in place_dict:
            return Owner(
                **place_dict
            )
        else:
            return Owner(
                **{k: v for k, v in place_dict.items() if k != 'id'}
            )