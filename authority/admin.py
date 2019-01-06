from django.contrib import admin
from authority import models


# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'action', 'group')


admin.site.register(models.UserInfo)
admin.site.register(models.Role)
admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.PermissionGroup)
