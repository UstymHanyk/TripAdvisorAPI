from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from t08_flask_mysql.app.my_project.auth.controller import payment_options_controller
from t08_flask_mysql.app.my_project.auth.domain import PaymentOptions

payment_options_bp = Blueprint('payment_options', __name__, url_prefix='/payment-options')

@payment_options_bp.get('')
def get_all_payment_options() -> Response:
    payment_options = payment_options_controller.find_all()
    return make_response(jsonify(payment_options), HTTPStatus.OK)

@payment_options_bp.post('')
def create_payment_option() -> Response:
    content = request.get_json()
    payment_option = PaymentOptions.create_from_dto(content)
    payment_options_controller.create(payment_option)
    return make_response(jsonify(payment_option.put_into_dto()), HTTPStatus.CREATED)

@payment_options_bp.get('/<int:payment_id>')
def get_payment_option(payment_id: int) -> Response:
    payment_option = payment_options_controller.find_by_id(payment_id)
    if payment_option:
        return make_response(jsonify(payment_option), HTTPStatus.OK)
    return make_response(jsonify({"error": "Payment option not found"}), HTTPStatus.NOT_FOUND)

@payment_options_bp.put('/<int:payment_id>')
def update_payment_option(payment_id: int) -> Response:
    content = request.get_json()
    payment_option = PaymentOptions.create_from_dto(content)
    payment_options_controller.update(payment_id, payment_option)
    return make_response("Payment option updated", HTTPStatus.OK)

@payment_options_bp.patch('/<int:payment_id>')
def patch_payment_option(payment_id: int) -> Response:
    content = request.get_json()
    payment_options_controller.patch(payment_id, content)
    return make_response("Payment option updated", HTTPStatus.OK)

@payment_options_bp.delete('/<int:payment_id>')
def delete_payment_option(payment_id: int) -> Response:
    payment_options_controller.delete(payment_id)
    return make_response("Payment option deleted", HTTPStatus.OK)
