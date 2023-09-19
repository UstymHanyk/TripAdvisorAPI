from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import media_controller
from t08_flask_mysql.app.my_project.auth.domain import Media

media_bp = Blueprint('media', __name__, url_prefix='/media')

@media_bp.get('')
def get_all_media() -> Response:
    media = media_controller.find_all()
    return make_response(jsonify(media), HTTPStatus.OK)

@media_bp.get('/place/<int:place_id>')
def get_media_by_place(place_id: int) -> Response:
    media = media_controller.find_by_place_id(place_id)
    return make_response(jsonify(media), HTTPStatus.OK)

@media_bp.post('')
def create_media() -> Response:
    content = request.get_json()
    media = Media.create_from_dto(content)
    media_controller.create(media)
    return make_response(jsonify(media.put_into_dto()), HTTPStatus.CREATED)

@media_bp.get('/<int:media_id>')
def get_media(media_id: int) -> Response:
    media = media_controller.find_by_id(media_id)
    if media:
        return make_response(jsonify(media), HTTPStatus.OK)
    return make_response(jsonify({"error": "Media not found"}), HTTPStatus.NOT_FOUND)

@media_bp.put('/<int:media_id>')
def update_media(media_id: int) -> Response:
    content = request.get_json()
    media = Media.create_from_dto(content)
    media_controller.update(media_id, media)
    return make_response("Media updated", HTTPStatus.OK)

@media_bp.patch('/<int:media_id>')
def patch_media(media_id: int) -> Response:
    content = request.get_json()
    media_controller.patch(media_id, content)
    return make_response("Media updated", HTTPStatus.OK)

@media_bp.delete('/<int:media_id>')
def delete_media(media_id: int) -> Response:
    media_controller.delete(media_id)
    return make_response("Media deleted", HTTPStatus.OK)
