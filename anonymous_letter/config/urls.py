from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import SimpleRouter

from letter.views import LetterViewSet

router = SimpleRouter()

router.register('letters', LetterViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + router.urls
