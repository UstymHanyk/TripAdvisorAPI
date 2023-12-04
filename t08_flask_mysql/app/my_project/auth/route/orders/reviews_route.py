from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import reviews_controller
from t08_flask_mysql.app.my_project.auth.domain import Review

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews_bp.get('')
def get_all_reviews() -> Response:
    reviews = reviews_controller.find_all()
    return make_response(jsonify(reviews), HTTPStatus.OK)


@reviews_bp.get('/average')
def get_average_rating() -> Response:
    rt = reviews_controller.get_average_review_rating()
    return make_response("Average rating - " + str(rt), HTTPStatus.OK)


@reviews_bp.post('')
def create_review() -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    reviews_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@reviews_bp.get('/<int:review_id>')
def get_review(review_id: int) -> Response:
    review = reviews_controller.find_by_id(review_id)
    return make_response(jsonify(review), HTTPStatus.OK)


@reviews_bp.put('/<int:review_id>')
def update_review(review_id: int) -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    reviews_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)


@reviews_bp.patch('/<int:review_id>')
def patch_review(review_id: int) -> Response:
    content = request.get_json()
    reviews_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)


@reviews_bp.delete('/<int:review_id>')
def delete_review(review_id: int) -> Response:
    reviews_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
