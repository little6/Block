from django.shortcuts import render

from monitor.models import MonitorTask


def monitor_list(request):
    tasks = MonitorTask.objects.all()
    return render(request, 'monitor/list.html', locals())


def monitor_create(request):
    return render(request, 'monitor/create.html', locals())
