from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from app.forms import PreferenceForm
from app.models import Post, Preference


# Create your views here.
def index(request):
    result = str(10+10)

    context = {'result': result}
    return render(request, 'app/index.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = PreferenceForm(request.POST, instance=request.user.preference)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/')
    else:
        profile_form = PreferenceForm(instance=request.user.preference)
    return render(request, 'user/preference.html', {
        'profile_form': profile_form
    })


class PostCreate(CreateView):
    model = Post
    template_name = 'user/post_create_form.html'
    success_url = '/'
