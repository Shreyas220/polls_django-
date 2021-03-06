from django.contrib import admin

# Register your models here.
from .models import Questions, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['questions_text']}),
    ('Date Information', {'fields': ['pub_date'],'classes': ['collapse']}),]
    inlines = [ChoiceInline]



#admin.site.register(Questions)
#admin.site.register(Choice)
admin.site.register(Questions,QuestionsAdmin)