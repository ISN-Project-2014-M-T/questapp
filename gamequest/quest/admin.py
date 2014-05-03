from django.contrib import admin

from gamequest.quest.models import Stage, Choice, monster


class monsterInline(admin.TabularInline):
    model = monster
    extra = 1

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class StageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Histoire à lire',               {'fields': ['history']}),
        ('Question à poser',               {'fields': ['question']}),
    ]
    inlines = [ChoiceInline, monsterInline]
    list_display = ('name', 'id')


admin.site.register(Stage, StageAdmin)
