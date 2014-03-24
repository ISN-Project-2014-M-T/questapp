from django.contrib import admin
from gamequest.quest.models import Stage, Choice, PlayerRecord

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

class PlayerRecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['email']}),
    ]
    list_display = ('name', 'id')



admin.site.register(Stage, StageAdmin)
admin.site.register(PlayerRecord, PlayerRecordAdmin)