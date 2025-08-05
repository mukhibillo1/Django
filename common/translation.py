from modeltranslation.translator import translator, TranslationOptions
from .models import News, NewsCategory, NewsTag, Region 
from modeltranslation.translator import register, TranslationOptions

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','category','type','tags','region','cover','video','file','time_to_read','views','content','published_at','slug')

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(NewsTag)
class NewsTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)

