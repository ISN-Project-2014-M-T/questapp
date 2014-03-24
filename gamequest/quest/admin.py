from django.contrib import admin
from gamequest.quest.models import Stage, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class StageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Histoire à lire',               {'fields': ['history']}),
        ('Question à poser',               {'fields': ['question']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('name', 'id')


admin.site.register(Stage, StageAdmin)