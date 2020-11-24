from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import Category, Question, Quiz, Answer


@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Quiz)
class QuizAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title']


class AnswerInLine(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_correct']


@admin.register(Question)
class QuestionAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    fields = ['title', 'quiz']
    list_display = ['title', 'quiz', 'updated_time']
    inlines = [AnswerInLine, ]


@admin.register(Answer)
class QuizAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['answer_text', 'is_correct', 'question']
