from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id', ondelete='CASCADE'), nullable=False)

    text = db.Column(db.String(100))
    date = db.Column(db.Date)
    rating = db.Column(db.Float)

    review_media = db.relationship('Media', backref='review')

    def __repr__(self) -> str:
        return f"Review(id={self.id}, user_id={self.user_id}, place_id={self.place_id}, text='{self.text}', " \
               f"date={self.date}, rating={self.rating})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text,
            'date': str(self.date),
            'rating': self.rating
        }

    @staticmethod
    def create_from_dto(review_dict: Dict[str, Any]) :
        return Review(
            user_id=review_dict['user_id'],
            place_id=review_dict['place_id'],
            text=review_dict.get('text'),
            date=review_dict.get('date'),
            rating=review_dict.get('rating')
        )
