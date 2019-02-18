from django.contrib import admin
from core.models import *
# Register your models here.

class InlineSpec(admin.TabularInline):
    model = Spec
    extra = 1
class SprintAdmin(admin.ModelAdmin):
    list_display = ["projecte", "data_inici", "data_final", "hores"]

class SpecAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "projecte", "sprint", "developer"]


class ProjecteAdmin(admin.ModelAdmin):
    inlines = [InlineSpec,]
    

admin.site.register(Project, ProjecteAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Spec)
