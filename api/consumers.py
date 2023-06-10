
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    DeleteModelMixin
)
from .online import Online

from .models import URL, User
from .serializers import URLSerializer
from url_short.settings import HOST


class URLConsumerCreate(Online, GenericAsyncAPIConsumer, CreateModelMixin):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def perform_create(self, serializer, **kwargs):
        url = URL.objects.create(creator=self.scope['user'], original_url=serializer.data.get('original_url'))
        url.cuttly = f'{HOST}/{url.id}'
        return url


class URLConsumerGet(Online, GenericAsyncAPIConsumer, RetrieveModelMixin):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class URLConsumerDelete(Online, GenericAsyncAPIConsumer, DeleteModelMixin):
    queryset = URL.objects.all()