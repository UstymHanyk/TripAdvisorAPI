from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class PaymentOptions(db.Model):
    __tablename__ = "payment_options"

    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user_id = db.Column(db.Integer)
    card_number = db.Column(db.String(50), nullable=False)
    card_cvv = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"PaymentOptions(payment_id={self.payment_id}, user_id={self.user_id}, card_number='{self.card_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'payment_id': self.payment_id,
            'user_id': self.user_id,
            'card_number': self.card_number,
            'card_cvv': self.card_cvv,
            'expiration_date': self.expiration_date
        }

    @staticmethod
    def create_from_dto(payment_dict: Dict[str, Any]):
        return PaymentOptions(
            user_id=payment_dict['user_id'],
            card_number=payment_dict['card_number'],
            card_cvv=payment_dict['card_cvv'],
            expiration_date=payment_dict['expiration_date'],
        )