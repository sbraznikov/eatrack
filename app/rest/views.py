from django.http import HttpResponse, QueryDict
import models
import datetime


def eating(request, id=None):
    if request.method == 'GET':
        data = models.read_eatings()
    if request.method == 'POST':
        data = models.create_eating(request.POST)
    if request.method == 'PUT':
        body_params = QueryDict(request.raw_post_data, encoding=request.encoding)
        data = models.update_eating(body_params, id)
    if request.method == 'DELETE':
        data = models.remove_eating(id)
    return HttpResponse(data, mimetype='application/json')
