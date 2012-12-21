#encoding=utf-8
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'dreamLog'}

@view_config(route_name='echo')
def echo(request):
    return Response(request.matchdict['var'])