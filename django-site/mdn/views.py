from django.http import HttpResponse
from django.template import loader


def index(request, name):
    template = loader.get_template('index.html')
    context = {
        'name': name,
    }
    return HttpResponse(template.render(context, request))
