from django.urls import reverse

def title(request):
    return {
        "title": getattr(request, "title", "Django | Chat"),
        "url_name": "{}:{}".format(request.resolver_match.app_name, request.resolver_match.url_name)
    }