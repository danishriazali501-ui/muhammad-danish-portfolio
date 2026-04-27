from django.contrib import admin
from .models import ContactMessage, Project, Skill, Service, VisitorCount, Resume


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    search_fields = ['name', 'email', 'subject']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'order', 'is_active']
    list_editable = ['percentage', 'order', 'is_active']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ['count', 'last_updated']
    readonly_fields = ['last_updated']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['file', 'uploaded_at']
    readonly_fields = ['uploaded_at']

