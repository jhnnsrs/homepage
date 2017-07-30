import json

from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'tasks': json.dumps({
            'tasks': [
                'Create new django app',
                'Expose the data over the REST API',
                'Create new ng-controller',
                '...'
            ]
        })
    }

    return render(request, 'app/index.html', context)