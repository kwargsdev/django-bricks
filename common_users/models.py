import os
import uuid
from PIL import Image
from django.db import models
from common_utilities.models import Cachet
from django.contrib.auth import get_user_model

User = get_user_model()

class Profil(Cachet):
    def profile_image_upload_to(instance, filename):
        app_slug = instance._meta.app_label
        user_id_folder = str(instance.user.pk)
        ext = filename.split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join(app_slug,user_id_folder,"avatar",new_filename)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    photo = models.ImageField(default='user_default.jpg', upload_to=profile_image_upload_to, verbose_name="Avatar")

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):
        if self.user.last_name and self.user.first_name:
            return self.user.get_full_name()
        else:
            return self.user.username