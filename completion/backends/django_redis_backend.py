from completion.backends.redis_backend import RedisAutocomplete
from redis_cache import get_redis_connection


class DjangoRedisAutocomplete(RedisAutocomplete):
    def __init__(self, prefix='autocomplete:', terminator='^'):
        self.prefix = prefix
        self.terminator = terminator
        self.client = self.get_connection()

    def get_connection(self):
        return get_redis_connection('default')
