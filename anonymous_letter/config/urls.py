from rest_framework.routers import SimpleRouter

from letter.views import LetterViewSet

router = SimpleRouter()

router.register('letters', LetterViewSet)


urlpatterns = router.urls
