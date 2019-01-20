from .views import BookAPIView, BookRudView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', BookAPIView.as_view(), name='book-create'),
    url(r'^(?P<id>\d+)', BookRudView.as_view(), name='book-rud')
]
