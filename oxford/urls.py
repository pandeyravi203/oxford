from django.urls import path
from . import views
from . import views
urlpatterns = [
    path('',views.get_word.as_view(),name='get_word'),
]