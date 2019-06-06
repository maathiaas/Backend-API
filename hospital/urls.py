from rest_framework import routers
from .viewsets import PacienteViewSets

router = routers.SimpleRouter()
router.register('paciente', PacienteViewSets)


urlpatterns = router.urls