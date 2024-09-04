from django.urls import path, include
from . import views
urlpatterns = [
    # ... other patterns
    path('my_preferences/',views.match_and_display,name='my_preferences')  # Example path and inclusion
]