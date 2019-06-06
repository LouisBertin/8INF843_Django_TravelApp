from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

from app.forms import PreferenceForm
from app.models import Post, Preference, Reservation


# Create your views here.
def index(request):
    posts = Post.objects.all()[:5]

    context = {
        'posts': posts,
    }
    return render(request, 'app/index.html', context)


# Posts
class PostCreate(CreateView):
    model = Post
    template_name = 'user/post_create_form.html'
    success_url = '/'
    fields = ('title', 'passengers_nb', 'departure', 'arrival', 'full')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def post_details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'post/details.html', context)


def post_reserve(request, id):
    post = Post.objects.get(id=id)

    reservation = Reservation.objects.create(user_passenger=request.user, post=post)
    reservation.save()

    request.user.money -= 10
    request.user.save()

    post.user.money += 10
    post.user.save()

    return redirect('/')


# Reservations
def reservations_list(request):
    reservations = Reservation.objects.all().filter(user_passenger=request.user)

    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/list.html', context)


# Preferences
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
