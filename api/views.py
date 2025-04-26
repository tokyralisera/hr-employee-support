from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Employe, Beneficiaire, ConseillerRH, CompagnieAssurance, Appel, Notification, Courriel
from .serializers import (
    EmployeSerializer, BeneficiaireSerializer, ConseillerRHSerializer,
    CompagnieAssuranceSerializer, AppelSerializer, NotificationSerializer, CourrielSerializer
)

# Create your views here.

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]

class BeneficiaireViewSet(viewsets.ModelViewSet):
    queryset = Beneficiaire.objects.all()
    serializer_class = BeneficiaireSerializer
    permission_classes = [IsAuthenticated]

class ConseillerRHViewSet(viewsets.ModelViewSet):
    queryset = ConseillerRH.objects.all()
    serializer_class = ConseillerRHSerializer
    permission_classes = [IsAuthenticated]

class CompagnieAssuranceViewSet(viewsets.ModelViewSet):
    queryset = CompagnieAssurance.objects.all()
    serializer_class = CompagnieAssuranceSerializer
    permission_classes = [IsAuthenticated]

class AppelViewSet(viewsets.ModelViewSet):
    queryset = Appel.objects.all()
    serializer_class = AppelSerializer
    permission_classes = [IsAuthenticated]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

class CourrielViewSet(viewsets.ModelViewSet):
    queryset = Courriel.objects.all()
    serializer_class = CourrielSerializer
    permission_classes = [IsAuthenticated]
