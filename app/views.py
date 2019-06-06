from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from app.models import Post, Preference


# Create your views here.
def index(request):
    result = str(10+10)

    context = {'result': result}
    return render(request, 'app/index.html', context)

class PreferenceUpdate(UpdateView):
    model = Preference
    template_name = 'user/preferences_update_form.html'
    success_url = '/'

class PostCreate(CreateView):
    model = Post
    template_name = 'user/post_create_form.html'
    success_url = '/'
