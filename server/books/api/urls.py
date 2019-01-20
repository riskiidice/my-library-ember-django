from .views import BookAPIView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', BookAPIView.as_view(), name='book-create'),
]
