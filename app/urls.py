from . import views
from django.urls import include, path
from app.registration.registration import SignUp

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create', views.PostCreate.as_view(), name='post_create'),
    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('preferences/', views.update_profile, name='preferences_update'),
]
