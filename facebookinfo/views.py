from django.conf import settings
from django.shortcuts import render
import facebook
import json

def index(request):
    return render(request, 'facebookinfo/index.html')

def page(request, page_id):
    context = __get_data(__get_graph(), page_id, __get_fields(False), 'page')
    return render(request, 'facebookinfo/page.html', context)

def post(request, page_id, post_id):
    graph = __get_graph()
    id = "{0}_{1}".format(graph.get_object(page_id, fields='id')['id'], post_id)
    # fields = 'name, comments.limit(40){from, message, created_time, comments.limit(40){from, message, created_time}}'
    context = __get_data(graph, id, __get_fields(), 'post')
    return render(request, 'facebookinfo/post.html', context)

def __get_graph():
    try:
        return facebook.GraphAPI(access_token=settings.ACCESS_TOKEN, version='2.7')
    except Exception as e:
        context['message'] = e.__str__

def __get_data(graph, id, fields, object_name):
    context = {}
    try:
        object = graph.get_object(id, fields=fields)
        context[object_name] = object
    except Exception as e:
        context['message'] = e.__str__
    return context

# I had to limit to 20 because when there is too much data I get this error:
# https://github.com/mobolic/facebook-sdk/issues/281
def __get_fields(for_post=None):
    post_fields = 'comments.limit(20){from, message, created_time, comments.limit(20){from, message, created_time}}'
    if for_post is None:
        return 'name, {0}'.format(post_fields)
    else:
        # I used % format to avoid escaping { and }
        return 'name, id, posts.limit(20){name, created_time, %s}' % post_fields
