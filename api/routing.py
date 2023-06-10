from django.urls import re_path
from .consumers import URLConsumerCreate, URLConsumerGet, URLConsumerDelete

websocket_urlpatterns = [
    re_path("ws/url/", URLConsumerCreate.as_asgi()),
    re_path("ws/url_get/", URLConsumerGet.as_asgi()),
    re_path("ws/url_delete/", URLConsumerDelete.as_asgi())
]
