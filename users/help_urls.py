from django.urls import path
from users import views as user_views

urlpatterns = [
    path('', user_views.help, name='help'),
]