from flask import Response, request
from database.models import Task
from flask_restful import Resource

class UserTasksApi(Resource):

    def get(self, id):
        task = Task.objects(user_id=id).to_json()
        return Response(task, mimetype="application/json", status=200)