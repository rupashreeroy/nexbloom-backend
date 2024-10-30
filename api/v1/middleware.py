# myapp/middleware.py

from django.utils.deprecation import MiddlewareMixin

class CustomCSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "script-src 'self' chrome-extension:;"
        return response
