from django.urls import path
from .views import FacultyListCreate, FacultyDelete

urlpatterns = [
    path('faculties/', FacultyListCreate.as_view(), name='faculty-list-create'),
    path('faculty/<int:id>/', FacultyDelete.as_view(), name='faculty-delete'),
]
