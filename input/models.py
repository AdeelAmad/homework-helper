from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import uuid

answerfk = 1

class answer(models.Model):

    CLASSES = [
        ('APHG', 'AP Human Geo'),
        ('GEO', 'Geometry'),
        ('Spanish 1', 'Spanish 1'),
        ('English 1', 'English 1'),
        ('French 1', 'French 1'),
        ('Algebra 1', 'Algebra 1')
    ]

    # date_created = models.DateTimeField()
    class_for = models.CharField(max_length=15, choices=CLASSES)
    assignment_name = models.CharField(max_length=200)
    content = models.TextField()
    approval = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=answerfk)


    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})


    class Meta:
        permissions = [
            ("approve_answers", "Can approve answers"),
            ("create_answers", "Can create answers"),
        ]




class update(models.Model):

    date = models.CharField(max_length=10)
    changes = models.TextField()