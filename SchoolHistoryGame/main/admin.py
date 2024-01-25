from django.contrib import admin
#import nested_admin
from .models import HistoryList,Subtopics,SubtopicsContent,MainContent


class AdminSubtopicsInline(admin.StackedInline):
    model = Subtopics
    extra = 0

class AdminSubtopicsContentInline(admin.StackedInline):
    model = SubtopicsContent
    extra = 0
class AdminSubtopics(admin.ModelAdmin):
    inlines = [AdminSubtopicsContentInline]
    list_display = ('pk', 'title','history_list')

class AdminSubtopicsContent(admin.ModelAdmin):

    list_display = ('pk','type', 'subtopics')
    list_filter = ("subtopics",)


class AdminMainContenInline(admin.StackedInline):
    model = MainContent
    extra = 0
class AdminMainContent(admin.ModelAdmin):
      list_display = ('pk','type')

class AdminHistory(admin.ModelAdmin):
    inlines = [AdminMainContenInline,AdminSubtopicsInline]
    list_display = ('pk','date', 'text')

admin.site.register(HistoryList,AdminHistory)
admin.site.register(Subtopics,AdminSubtopics)





