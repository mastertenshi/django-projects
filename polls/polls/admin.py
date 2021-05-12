from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'published_date', 'was_published_recently', 'id')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)