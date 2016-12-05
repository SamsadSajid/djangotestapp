from django import template

register = template.Library()

@register.inclusion_tag('facebookinfo/object_information.html')
def object_information(object, type):
    # import pdb; pdb.set_trace()
    return {
        'id': object['id'],
        'name': object['name'],
        'type': type
    }

@register.inclusion_tag('facebookinfo/post_information.html')
def post_information(post):
    return {
     'post': post,
    }
