from django.db import models

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=255, default="")  # Добавьте значение по умолчанию

    def __str__(self):
        return self.faculty_name
