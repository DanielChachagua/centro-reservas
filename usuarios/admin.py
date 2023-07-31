from django.contrib import admin
from .models import User, Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email','user_group')
    search_fields =('user__groups__name',)

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Perfil, PerfilAdmin)

admin.site.register(User)