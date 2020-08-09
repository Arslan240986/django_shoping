from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product
from django.contrib.flatpages.models import FlatPage


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'unit')


@register(FlatPage)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('content', 'title')