from rest_framework import routers
from .viewsets import PacienteViewSets,AgendarExamenViewSets

router = routers.SimpleRouter()
router.register('paciente', PacienteViewSets)
router.register('AgendarExamen', AgendarExamenViewSets)



urlpatterns = router.urls