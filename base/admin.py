from django.contrib import admin

from base.models import SMS, Access, Notes, Profile, SMStext, Service, Task, Client, Upload, subscriptions,telegramPost

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']
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
