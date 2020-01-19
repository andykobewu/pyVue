from django.contrib import admin

# Register your models here.
from django.contrib import admin
from caseapi.models import Case


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'casename')  # 在后台列表下显示的字段
