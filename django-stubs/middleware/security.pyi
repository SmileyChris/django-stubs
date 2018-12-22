from typing import Any, Optional, List

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin

class SecurityMiddleware(MiddlewareMixin):
    sts_seconds: int = ...
    sts_include_subdomains: bool = ...
    sts_preload: bool = ...
    content_type_nosniff: bool = ...
    xss_filter: bool = ...
    redirect: bool = ...
    redirect_host: Optional[str] = ...
    redirect_exempt: List[Any] = ...
    def process_request(self, request: WSGIRequest) -> Optional[HttpResponsePermanentRedirect]: ...
    def process_response(self, request: WSGIRequest, response: HttpResponse) -> HttpResponse: ...