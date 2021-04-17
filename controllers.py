import http
import flask
import flask_rest_decorators as rd
import services
import utils

@rd.controller("/api/v1/tasks")
class TaskController:

    service = services.TaskService.get_instance()

    @rd.get("/")
    def list_all():
        page, size, order, filters = utils.parse_request_params(flask.request.args)
        response = TaskController.service.list_all(page,size,order,filters)
        return flask.jsonify(response), http.HTTPStatus.OK

    @rd.post("/")
    def create():
        body = flask.request.get_json()
        response = TaskController.service.create(body)
        return flask.jsonify(response), http.HTTPStatus.CREATED

    @rd.get("/<string:id>")
    def get_by_id(id):
        response = TaskController.service.get_by_id(id)
        return flask.jsonify(response), http.HTTPStatus.OK
    
    @rd.put("/<string:id>")
    def update_by_id(id):
        body = flask.request.get_json()
        response = TaskController.service.update_by_id(id, body)
        return flask.jsonify(response), http.HTTPStatus.OK

    @rd.delete("/<string:id>")
    def delete_by_id(id):
        TaskController.service.delete_by_id(id)
        return "", http.HTTPStatus.NO_CONTENT

