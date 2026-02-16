from django.contrib import admin
from .models import Project, Skill, Like, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "tech_stack")


admin.site.register(Like)
admin.site.register(Comment)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percent", "level", "order")
    list_editable = ("percent", "level", "order")
    ordering = ("order", "name")
    search_fields = ("name",)
