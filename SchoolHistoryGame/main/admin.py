from django.contrib import admin

from .models import HistoryList
# Register your models here.

class AdminHistory(admin.ModelAdmin):
    list_display = ('date', 'text')


admin.site.register(HistoryList,AdminHistory)