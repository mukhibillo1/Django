
import datetime
from datetime import date
from django.utils.deprecation import MiddlewareMixin
from .models import Visitor, PageCount  # ← TO‘G‘RILANDI

class VisitorCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        today = datetime.date.today()
        if not Visitor.objects.filter(ip_address=ip, date=today).exists():
            Visitor.objects.create(ip_address=ip, date=today)

class PageViewCounterMiddleware(MiddlewareMixin):
    def __init__(self, get_response):  # ← TO‘G‘RILANDI
        self.get_response = get_response

    def __call__(self, request):  # ← TO‘G‘RILANDI
        response = self.get_response(request)

        if request.path.startswith('/admin/') or request.path.startswith('/static/'):
            return response  

        today = date.today()
        pageview, created = PageCount.objects.get_or_create(date=today)
        pageview.count += 1
        pageview.save(update_fields=['count'])

        return response

