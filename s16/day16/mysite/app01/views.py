from django.shortcuts import render

# Create your views here.


def time(request):
    import datetime
    tm = datetime.datetime.now()
    z = 10
    return render(request, 'time.html', locals())

