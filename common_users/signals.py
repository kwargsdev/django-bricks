import os
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Profil
from common_utilities.middleware import get_current_user
#from crum import get_current_user
#from allauth.account.adapter import get_adapter
#from allauth.account.models import EmailAddress

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        requesting_user = get_current_user()
        Profil.objects.create(user=instance, created_by=requesting_user)
    # Ajouter au groupe Superadmin si applicable
    if instance.is_superuser:
        try:
            admin_group = Group.objects.get(name='Superadmin')
            instance.groups.add(admin_group)
        except Group.DoesNotExist:
            pass
    else:
        try:
            admin_group = Group.objects.get(name='Utilisateur')
            instance.groups.add(admin_group)
        except Group.DoesNotExist:
            pass

DEFAULT_USER_PHOTO = 'user_default.jpg'
DEFAULT_COMPANY_PHOTO = "company_default.jpg"

@receiver(pre_save, sender=Profil)
def auto_delete_old_photo_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False    
    # Tente de récupérer l'instance existante de la base de données
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False

    # Compare l'ancienne valeur du champ 'photo' avec la nouvelle
    if old_instance.photo and old_instance.photo != instance.photo:
        if old_instance.photo.name == DEFAULT_USER_PHOTO or old_instance.photo.name == DEFAULT_COMPANY_PHOTO:
                    # Si c'est le fichier par défaut, on ne fait rien (on saute la suppression)
                    return
        # Supprime l'ancien fichier du système de fichiers
        if os.path.isfile(old_instance.photo.path):
            old_instance.photo.delete(save=False)