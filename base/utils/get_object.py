from base.models import *
from django.db.models import Model
from django.forms.models import model_to_dict


def get_bot_user_id_by_client(client):
    if client.bot_user:
        return client.bot_user.user_id
    else:
        return None
    

def get_changed_values(instance):
    changed_values = {}

    try:
        original_instance = instance.__class__.objects.get(pk=instance.pk)
    except instance.__class__.DoesNotExist:
        # Handle the case where the instance is new and not yet saved
        original_instance = None

    if original_instance:
        for field in instance._meta.fields:
            field_name = field.name
            if field_name == 'last_profile':
                continue
            old_value = getattr(original_instance, field_name)
            new_value = getattr(instance, field_name)
            if old_value != new_value:
                changed_values[field_name] = {
                    'eski qiymat': old_value,
                    'yangi qiymat': new_value
                }

    return changed_values
