from . import views
from django.urls import include, path
from django.conf.urls import url
from app.registration.registration import SignUp

urlpatterns = [
    path('', views.index, name='index'),
    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),
    path('preferences/', views.PreferenceUpdate.as_view(), name='preferences_update'),
]
