from . import views
from django.urls import include, path
from app.registration.registration import SignUp

urlpatterns = [
    path('', views.index, name='index'),
    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
]