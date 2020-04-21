from flask import Response, request
from database.models import Task
from flask_restful import Resource

class TasksApi(Resource):
    def get(self):
        tasks = Task.objects().to_json()
        return Response(tasks, mimetype="application/json", status=200)

    def post(self):
        print(request)
        body = request.get_json()
        task =  Task(**body).save()
        id = task.id
        return {'id': str(id)}, 200
        
class TaskApi(Resource):
    def put(self, id):
        body = request.get_json()
        Task.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        task = Task.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        task = Task.objects.get(id=id).to_json()
        return Response(task, mimetype="application/json", status=200)