from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('model_professor.urls')),  # Use the string 'model_professor.urls'
]
