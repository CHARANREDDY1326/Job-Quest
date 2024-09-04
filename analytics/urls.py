from django.urls import path
from . import views


urlpatterns=[
    path('analytics/',views.render_analytics, name='analytics')
]