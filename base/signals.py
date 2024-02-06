from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from base.models import ActionHistory, Client
from base.utils.get_object import get_changed_values

@receiver(pre_save, sender=Client)
def save_client_action_history(sender, instance, **kwargs):
    changed_values = get_changed_values(instance)
    if changed_values:
        ActionHistory.objects.create(
            profile=instance.last_profile,  # You can set the user based on your authentication system
            client_id = instance.pk,
            model_name=sender.__name__,
            action_type='update',
            changed_values=str(changed_values)
        )

# @receiver(pre_save, sender=Client)
# def save_client_action_history(sender, instance, **kwargs):
#     user = kwargs.get('user', None)
#     print(user)
#     changed_values = get_changed_values(instance)
#     if changed_values:
#         ActionHistory.objects.create(
#             profile=instance.last_profile,  # You can set the user based on your authentication system
#             client_id = instance.pk,
#             model_name=sender.__name__,
#             action_type='update' if kwargs.get('created') is False else 'create',
#             changed_values=str(changed_values)
#         )
