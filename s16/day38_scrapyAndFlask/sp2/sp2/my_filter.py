from scrapy.utils.request import request_fingerprint

class MyDupeFilter(object):
    def __init__(self):
        self.visited = set()

    @classmethod
    def from_settings(cls, settings):
        return cls()

    def request_seen(self, request):
        fp = request_fingerprint(request)
        if fp in self.visited:
            return True
        self.visited.add(fp)

    def open(self):  # can return deferred
        pass

    def close(self, reason):  # can return a deferred
        pass

    def log(self, request, spider):  # log that a request has been filtered
        pass