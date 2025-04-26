from rest_framework import serializers
from .models import Employe, Beneficiaire, ConseillerRH, CompagnieAssurance, Appel, Notification, Courriel

class BeneficiaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiaire
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer):
    beneficiaires = BeneficiaireSerializer(many=True, read_only=True)
    
    class Meta:
        model = Employe
        fields = ['id', 'nom', 'prenom', 'dateNaissance', 'adresse', 'telephone', 'email', 'beneficiaires']

class ConseillerRHSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConseillerRH
        fields = '__all__'

class CompagnieAssuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompagnieAssurance
        fields = '__all__'

class AppelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appel
        fields = '__all__'
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class CourrielSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courriel
        fields = '__all__' 