import json

from celery import current_app
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Test
from .forms import TestForm
from .tasks import graph_func


# Create your views here.


def new(request):
    bd = Test.objects
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()

            cleaned_info = form.cleaned_data
            filtred = bd.filter(GraphFunction__exact=cleaned_info['GraphFunction'],
                                GraphInterval__exact=cleaned_info['GraphInterval'],
                                GraphDt__exact=cleaned_info['GraphDt']).values('GraphId')
            for f in filtred:
                f = f
            task = graph_func.delay(f['GraphId'])
            bd.filter(GraphFunction__exact=cleaned_info['GraphFunction'],
                      GraphInterval__exact=cleaned_info['GraphInterval'],
                      GraphDt__exact=cleaned_info['GraphDt']).update(GraphFuncId=task.id)
            print(current_app.AsyncResult(task.id))
            while True:
                if current_app.AsyncResult(task.id).ready():
                    break
            return redirect('/test')
        else:
            HttpResponse("Form is invalid!!!")
    else:
        form = TestForm()

    data = {
        'form': form,
        'result': bd.all(),
    }
    return render(request, "newapp/index.html", data)

