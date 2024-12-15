from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dancer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    style = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="dancers")

    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="festivals")

    def __str__(self):
        return self.name
