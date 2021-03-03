from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleScope, Scope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        check_main = False
        for form in self.forms:
            if check_main and form.cleaned_data.get('is_main', False):
                raise ValidationError('Основным может быть только один раздел')
            elif form.cleaned_data.get('is_main', False):
                check_main = True
        if check_main is False:
                raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleScopeInline,)


class ScopeAdmin(admin.ModelAdmin):
    inlines = (ArticleScopeInline,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Scope, ScopeAdmin)