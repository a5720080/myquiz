from django.contrib import admin
from .models import Exam,Quiz,Choice

class ExamAdmin(admin.ModelAdmin):
   list_display = ['name','description','published']
   list_filter = ['published']
   search_fields = ('name', 'description')
   fieldsets = (
		(None, {'fields': ('name', 'description')}),
		('Option', {'fields': ('published',), 'classes': ('collapse',)}),
	)

class QuizInline(admin.TabularInline):
    model = Quiz
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice

class QuizAdmin(admin.ModelAdmin):
    inlines =[ChoiceInline]
	

admin.site.register(Exam,ExamAdmin)
admin.site.register(Quiz,QuizAdmin)
