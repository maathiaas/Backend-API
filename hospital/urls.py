from rest_framework import routers
from .viewsets import PacienteViewSets,AgendarExamenViewSets, TipoExamenViewSets, EspacialistaViewSets, ExamenViewSets

router = routers.SimpleRouter()
router.register('paciente', PacienteViewSets)
router.register('agendarexamen', AgendarExamenViewSets)
router.register('tipoexamen', TipoExamenViewSets)
router.register('especialista', EspacialistaViewSets)
router.register('examen', ExamenViewSets)



urlpatterns = router.urls