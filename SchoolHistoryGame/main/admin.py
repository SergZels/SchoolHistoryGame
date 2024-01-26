from django.contrib import admin
from .models import HistoryList,Subtopics,SubtopicsContent,MainContent
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class AdminSubtopicsContentInline(NestedStackedInline):
    model = SubtopicsContent
    extra = 1
    fk_name = 'subtopics'

class AdminSubtopicsInline(NestedStackedInline):
    model = Subtopics
    extra = 1
    fk_name = 'history_list'
    inlines = [AdminSubtopicsContentInline]



# class AdminSubtopics(admin.ModelAdmin):
#     inlines = [AdminSubtopicsContentInline]
#     list_display = ('pk', 'title','history_list')
#class AdminMainContent(admin.ModelAdmin):
#      list_display = ('pk','type')

# class AdminSubtopicsContent(admin.ModelAdmin):
#
#     list_display = ('pk','type', 'subtopics')
#     list_filter = ("subtopics",)


class AdminMainContenInline(NestedStackedInline):
    model = MainContent
    extra = 1
    fk_name = 'history_list'


class AdminHistory(NestedModelAdmin):
    save_on_top = True
    inlines = [AdminMainContenInline,AdminSubtopicsInline]
    list_display = ('date', 'text','pk')

admin.site.register(HistoryList,AdminHistory)
#admin.site.register(Subtopics,AdminSubtopics)





