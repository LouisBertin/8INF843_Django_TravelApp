from django.shortcuts import render


# Create your views here.
def index(request):
    result = str(10+10)

    context = {'result': result}
    return render(request, 'app/index.html', context)
