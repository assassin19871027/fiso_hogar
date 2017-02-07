from django import template

register = template.Library()

@register.filter('get_image_name')
def get_image_name(image):
    temp = image.split('.')
    name = temp[0]
    return name

@register.filter('get_number')
def get_number(images):
    i = 0;
    for value in images:
        i = i + 1;
    return i
