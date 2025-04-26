from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeViewSet, BeneficiaireViewSet, ConseillerRHViewSet,
    CompagnieAssuranceViewSet, AppelViewSet, NotificationViewSet, CourrielViewSet
)

router = DefaultRouter()
router.register(r'employes', EmployeViewSet)
router.register(r'beneficiaires', BeneficiaireViewSet)
router.register(r'conseillers', ConseillerRHViewSet)
router.register(r'compagnies', CompagnieAssuranceViewSet)
router.register(r'appels', AppelViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'courriels', CourrielViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 