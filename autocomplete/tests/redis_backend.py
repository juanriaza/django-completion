from django.contrib.auth.models import User

from autocomplete.backends.redis_backend import RedisAutocomplete
from autocomplete.tests.base import AutocompleteTestCase
from autocomplete.tests.models import Blog, BlogProvider
from autocomplete.sites import AutocompleteSite


test_site = AutocompleteSite(RedisAutocomplete(prefix='test:ac:'))
test_site.register(Blog, BlogProvider)


class RedisBackendTestCase(AutocompleteTestCase):
    def test_suggest(self):
        test_site.store_providers()

        results = test_site.suggest('testing')
        self.assertEqual(sorted(results), [
            {'stored_title': 'testing python'}, 
            {'stored_title': 'testing python code'}, 
            {'stored_title': 'web testing python code'},
        ])
        
        results = test_site.suggest('unit')
        self.assertEqual(results, [{'stored_title': 'unit tests with python'}])
        
        results = test_site.suggest('')
        self.assertEqual(results, [])
        
        results = test_site.suggest('another')
        self.assertEqual(results, [])
