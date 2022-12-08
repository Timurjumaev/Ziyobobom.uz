from .models import Yangilik
from modeltranslation.translator import TranslationOptions,register

@register(Yangilik)
class YangilikTranslationOptions(TranslationOptions):
    fields = ('sarlavha', 'matn')