from rest_framework import routers
from .views import TaskViewSet

app_name = "tasks"

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [*router.urls]
