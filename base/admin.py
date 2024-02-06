from django.contrib import admin
from django.utils.html import format_html
from base.models import *

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'sub_type', 'jshshir', 'phone1', 'key_button']
    search_fields = ['name', 'jshshir', 'phone1']
    list_filter = ['type', 'sub_type', 'jshshir', 'phone1', 'key']

    def key_button(self, obj):
        if obj.key:
            change_url = f'/{obj.key}'
            return format_html('<a target="_blank" class="btn btn-success" href="{}" download style="padding: 1px 5px;"><i class="fas fa-download"></i></a>', change_url)
        return None
    key_button.short_description = 'Kalit'

class KeyAdmin(admin.ModelAdmin):
    list_display = ['client', 'name', 'type', 'key_exp']

class ActionHistoryAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]

admin.site.register(Task)
admin.site.register(Access)
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Client, ClientAdmin)
admin.site.register(Upload)
admin.site.register(SMS)
admin.site.register(SMStext)
admin.site.register(Notes)
admin.site.register(subscriptions)
admin.site.register(telegramPost)
admin.site.register(Bot_user)
admin.site.register(Template)
admin.site.register(Key, KeyAdmin)
admin.site.register(ActionHistory, ActionHistoryAdmin)
