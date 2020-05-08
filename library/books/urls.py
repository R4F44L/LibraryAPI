from . import views
from django.urls import include, path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("books", views.BookViewSet, basename="books")
router.register("authors", views.AuthorViewSet, basename="authors")


urlpatterns = router.urls
