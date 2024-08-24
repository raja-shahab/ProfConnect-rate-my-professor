from django.urls import path
from .views import index, add_professors, get_professor_recommendation

urlpatterns = [
    path('', index, name='homepage'),
    path('add_professors/', add_professors, name='add_professors'),
    path('professor_recommendations/', get_professor_recommendation, name='get_professor_recommendation'),
]
