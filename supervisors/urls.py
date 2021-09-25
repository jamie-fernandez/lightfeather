from rest_framework.routers import DefaultRouter
from .views import SupervisorListView

router = DefaultRouter()
router.register(r'|supervisors|supervisor',
                SupervisorListView, basename='supervisors')


urlpatterns = router.urls
