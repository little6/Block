from django.conf import settings
from django.core.cache import cache

from analysis.services import TrackingService
from apm.apmstatsd import statsd
from articles.constants import ARTICLE_CATEGORY_CHOICES
from articles.models import Article
from utils.server import server_info


def categories(request):
    _categories = cache.get('categories')
    if not _categories:
        _categories = []
        for category in ARTICLE_CATEGORY_CHOICES:
            _categories.append({
                'identify': category[0],
                'name': category[1],
                'count': Article.objects.filter(category=category[0]).count()
            })
        cache.set('categories', _categories, 43200)
    context = {'categories': _categories}

    return context

def site_info(request):
    statsd.incr('pageview')

    site_analysis = cache.get('site_analysis')
    if not site_analysis:
        site_analysis = {
            'pageview': TrackingService.pageview_report(),
            'server': server_info(),
        }
        cache.set('site_analysis', site_analysis, 43200)
    context = {
        'analysis': site_analysis,
        'site': {
            'domain': settings.DOMAIN,
            'cur_full_url': "{0}://{1}{2}".format(request.scheme, request.get_host(), request.path)
        }
    }
    return context
