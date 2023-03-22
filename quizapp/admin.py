from django.contrib import admin
from quizapp.models import QuizCategory,QuizQuestion

@admin.register(QuizCategory)
class PostAdmin(admin.ModelAdmin):
    list_display = ("detail",)

@admin.register(QuizQuestion)
class PostAdmin(admin.ModelAdmin):
    list_display = ("category",)