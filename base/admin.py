from django.contrib import admin

from base.models import *

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']

class KeyAdmin(admin.ModelAdmin):
    list_display = ['client', 'name', 'type', 'key_exp']

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
