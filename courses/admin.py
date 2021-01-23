from django.contrib import admin
from .models import Subject, Course, Module, Choice

admin.site.site_header = "E Learning Admin"
admin.site.site_title = "E Learning Admin Portal"
admin.site.index_title = "Welcome to E Learning Admin Interface"

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module

admin.site.register(Choice)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
