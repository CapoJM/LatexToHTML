from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cambio(models.Model):
    # This is a table we might use for a database
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    ARTICLE = "ART"
    ANSWER = "ANS"
    TYPE_CHOICES = [
    (ARTICLE, "Article"),
    (ANSWER, "Answer")
    ]
    tipo = models.CharField(max_length = 3, choices=TYPE_CHOICES, default=ARTICLE)

    latex = models.TextField()
    html = models.TextField(null = True, blank=True)

    def __str__(self):
        return str(self.user) + " | " + str(self.date)
