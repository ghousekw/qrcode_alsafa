from django.contrib import admin
from .models import *

# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    search_fields = ('id', 'university_name', 'university_code')


admin.site.register(User, UserAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
    search_fields = ('id', 'university_name', 'university_code')
    

admin.site.register(Company, CompanyAdmin)