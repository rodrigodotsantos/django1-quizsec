from django.contrib import admin
from .models import Question, Profile, QuestionStat, QuizAttempt, AnsweredQuestion

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'difficulty', 'points', 'correct_option']
    list_filter = ['difficulty']
    search_fields = ['text']

admin.site.register([Profile, QuestionStat, QuizAttempt, AnsweredQuestion])
