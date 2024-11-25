from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),  # Ensure this matches your app name
]
