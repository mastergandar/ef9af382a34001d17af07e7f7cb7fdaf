from __future__ import absolute_import, unicode_literals
from celery import shared_task
from sympy import symbols, sympify
from .models import Test
import datetime
import time
import matplotlib.pyplot as plt


@shared_task
def graph_func(func_id):
    bd = Test.objects
    time_now = datetime.datetime.now()
    bd.filter(GraphId__exact=func_id).update(GraphDateTime=time_now)
    t = symbols('t')
    x_func = []
    y_func = []
    name = 'func_' + str(func_id) + '.png'
    folder = 'media/func_folder/' + name
    filtred = bd.filter(GraphId__exact=func_id).values('GraphFunction', 'GraphInterval', 'GraphDt')
    for f in filtred:
        f = f
    t0 = [i for i in range(round(time.mktime(time_now.timetuple())) - f['GraphInterval'] * 86400,
                           round(time.mktime(time_now.timetuple())), f['GraphDt'] * 3600)]
    try:
        func = sympify(f['GraphFunction'])
        for x in t0:
            x_func.append(func.diff(t).subs(t, x))
            y_func.append(func.subs(t, x))
        plt.plot(y_func, x_func)
        plt.savefig(folder)
        bd.filter(GraphId__exact=func_id).update(GraphImage=name, GraphDateTime=time_now)
    except Exception as e:
        bd.filter(GraphId__exact=func_id).update(GraphImageEx=e, GraphDateTime=time_now)
