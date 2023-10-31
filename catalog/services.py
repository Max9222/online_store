from django.conf import settings
from django.core.cache import cache


def get_catalog_cache(self):
    if settings.CACHE_ENABLED:
        key = f'possibilities_list{self.object.pk}'
        possibilities_list = cache.get(key)
        if possibilities_list is None:
            possibilities_list = self.object.possibilities_set.all()
            cache.set(key, possibilities_list)
    else:
        possibilities_list = self.object.possibilities_set.all()

    return possibilities_list