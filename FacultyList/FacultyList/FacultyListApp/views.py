from rest_framework import generics
from .models import Faculty
from .serializers import FacultySerializer

class FacultyListCreate(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyDelete(generics.DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'id'
