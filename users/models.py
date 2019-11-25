from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    tokens_have = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 76 or img.width > 76:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)
