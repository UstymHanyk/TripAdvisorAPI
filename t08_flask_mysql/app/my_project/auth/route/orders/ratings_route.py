from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from t08_flask_mysql.app.my_project.auth.controller import ratings_controller
from t08_flask_mysql.app.my_project.auth.domain import Rating

ratings_bp = Blueprint('ratings', __name__, url_prefix='/ratings')

@ratings_bp.get('')
def get_all_ratings() -> Response:
    ratings = ratings_controller.find_all()
    return make_response(jsonify(ratings), HTTPStatus.OK)

@ratings_bp.post('')
def create_rating() -> Response:
    content = request.get_json()
    rating = Rating.create_from_dto(content)
    ratings_controller.create(rating)
    return make_response(jsonify(rating.put_into_dto()), HTTPStatus.CREATED)

@ratings_bp.get('/<int:rating_id>')
def get_rating(rating_id: int) -> Response:
    rating = ratings_controller.find_by_id(rating_id)
    if rating:
        return make_response(jsonify(rating), HTTPStatus.OK)
    return make_response(jsonify({"error": "Rating not found"}), HTTPStatus.NOT_FOUND)

@ratings_bp.put('/<int:rating_id>')
def update_rating(rating_id: int) -> Response:
    content = request.get_json()
    rating = Rating.create_from_dto(content)
    ratings_controller.update(rating_id, rating)
    return make_response("Rating updated", HTTPStatus.OK)

@ratings_bp.patch('/<int:rating_id>')
def patch_rating(rating_id: int) -> Response:
    content = request.get_json()
    ratings_controller.patch(rating_id, content)
    return make_response("Rating updated", HTTPStatus.OK)

@ratings_bp.delete('/<int:rating_id>')
def delete_rating(rating_id: int) -> Response:
    ratings_controller.delete(rating_id)
    return make_response("Rating deleted", HTTPStatus.OK)
