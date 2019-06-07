from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
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
    fields = ('title', 'passengers_nb', 'departure', 'arrival', )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def post_details(request, id):
    is_reserved = False
    post = Post.objects.get(id=id)
    preference = post.user.preference

    if request.user.is_authenticated:
        is_reserved = Reservation.objects.filter(post=post, user_passenger=request.user).exists()

    context = {
        'post': post,
        'is_reserved': is_reserved,
        'preference': preference
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


def post_delete(request, id):
    Post.objects.get(id=id).delete()

    return redirect('reservations_list')


# Reservations
def reservations_list(request):
    reservations = Reservation.objects.all().filter(user_passenger=request.user)
    posts = Post.objects.all().filter(user=request.user)

    context = {
        'reservations': reservations,
        'posts': posts
    }
    return render(request, 'reservations/list.html', context)


# Search
class SearchResultsView(ListView):
    model = Post
    template_name = 'post/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
                Q(departure__icontains=query) | Q(arrival__icontains=query)
            )

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
