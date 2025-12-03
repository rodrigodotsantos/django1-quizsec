# signals.py (CORRETO e Simplificado)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile # Certifique-se de que a classe Profile está correta em models.py

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Se o usuário foi criado, crie o perfil associado
        Profile.objects.create(user=instance)
    # Aqui você pode adicionar a lógica de salvamento do Profile
    # caso haja campos no Profile que devam ser atualizados pelo User,
    # mas geralmente basta garantir que o Profile foi criado.
    # Exemplo (se Profile tiver um campo 'bio'):
    # instance.profile.bio = 'Nova bio'
    # instance.profile.save()