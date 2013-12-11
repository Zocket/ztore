'''
Created on Dec 11, 2013

@author: Yelei
'''
from catalog.models import Category
from ztore import settings

def ztore(request):
    return {
        'active_categories': Category.objects.filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }