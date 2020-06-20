from django.contrib import admin
from users.models import AdminUser
from users.models import RegDoctor
from users.models import RegPatient
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(AdminUser, AccountAdmin)
admin.site.register(RegDoctor, AccountAdmin)
admin.site.register(RegPatient, AccountAdmin)
