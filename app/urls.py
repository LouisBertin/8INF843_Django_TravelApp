from . import views
from django.urls import include, path
from app.registration.registration import SignUp

urlpatterns = [
    path('', views.index, name='index'),
    # post
    path('post/create', views.PostCreate.as_view(), name='post_create'),
    path('post/details/<int:id>', views.post_details, name='post_details'),
    path('post/details/<int:id>/reserve', views.post_reserve, name='post_reserve'),
    # reservation
    path('reservations/', views.reservations_list, name='reservations_list'),

    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('preferences/', views.update_profile, name='preferences_update'),
]
