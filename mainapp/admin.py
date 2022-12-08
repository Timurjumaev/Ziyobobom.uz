from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Yangilik)
class YangilikAdmin(TranslationAdmin):
    list_display = ("sarlavha","rasm","matn","sana","korish_soni")

