from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

# Create your models here.
class Project(models.Model):
    nom = models.CharField(max_length=200, default="Nou Projecte")
    descripcion = models.TextField(blank=True, null=True, default="Nou Projecte")
    scrum_master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="scrum_master")
    product_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product_owner")
    grup = models.ForeignKey(Group, on_delete=models.CASCADE,)
    def __str__(self):
        return self.nom


class Sprint(models.Model):
    projecte = models.ForeignKey(Project, on_delete=models.CASCADE,)
    data_inici = models.DateField()
    data_final = models.DateField()
    hores = models.IntegerField(default=0, help_text="Hores")

class Spec(models.Model):
    descripcion = models.TextField()
    DIFICULTAT = (
        ("D", "Desconocido"),
        ("B", "Baja"),
        ("M", "Media"),
        ("A", "Alta"),
    )
    dificultat = models.CharField(max_length=1, choices=DIFICULTAT, default="D")
    hores = models.IntegerField(default=0)

    projecte = models.ForeignKey(Project, on_delete=models.CASCADE,)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.descripcion