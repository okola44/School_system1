from django.urls.conf import include, path 
from rest_framework import routers, urlpatterns
from .views import StudentViewSet,TrainerViewSet,CoursesViewSet,EventsViewSet

router=routers.DefaultRouter()
router.register(r"students",StudentViewSet)
router.register(r"trainers",TrainerViewSet)
router.register(r"courses",CoursesViewSet)
router.register(r"events",EventsViewSet)



urlpatterns=[
    path("",include(router.urls)),
]
