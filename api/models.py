from django.db import models

# Create your models here.

class Employe(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dateNaissance = models.DateField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Beneficiaire(models.Model):
    RELATION_CHOICES = [
        ('CONJOINT', 'Conjoint(e)'),
        ('ENFANT', 'Enfant'),
        ('PARENT', 'Parent'),
        ('AUTRE', 'Autre')
    ]
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    relationEmploye = models.CharField(max_length=20, choices=RELATION_CHOICES)
    dateNaissance = models.DateField()
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='beneficiaires')
    
    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.get_relationEmploye_display()})"

class ConseillerRH(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    poste = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class CompagnieAssurance(models.Model):
    nomCompagnie = models.CharField(max_length=100)
    adresse = models.TextField()
    emailCompagnie = models.EmailField()
    
    def __str__(self):
        return self.nomCompagnie

class Appel(models.Model):
    ETAT_CHOICES = [
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
        ('ANNULE', 'Annulé')
    ]
    
    dateAppel = models.DateTimeField(auto_now_add=True)
    motif = models.TextField()
    etatAppel = models.CharField(max_length=20, choices=ETAT_CHOICES, default='EN_COURS')
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE, related_name='appels')
    conseillerRH = models.ForeignKey(ConseillerRH, on_delete=models.CASCADE, related_name='appels')
    
    def __str__(self):
        return f"Appel du {self.dateAppel.strftime('%d/%m/%Y')} - {self.employe}"

class Notification(models.Model):
    TYPE_CHOICES = [
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('SYSTEME', 'Notification système')
    ]
    
    STATUS_CHOICES = [
        ('ENVOYEE', 'Envoyée'),
        ('RECUE', 'Reçue'),
        ('ECHEC', 'Échec')
    ]
    
    typeNotification = models.CharField(max_length=20, choices=TYPE_CHOICES)
    dateEnvoi = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ENVOYEE')
    appel = models.ForeignKey(Appel, on_delete=models.CASCADE, related_name='notifications')
    compagnieAssurance = models.ForeignKey(CompagnieAssurance, on_delete=models.CASCADE, related_name='notifications')
    
    def __str__(self):
        return f"{self.get_typeNotification_display()} du {self.dateEnvoi.strftime('%d/%m/%Y')}"

class Courriel(models.Model):
    destinataire = models.EmailField()
    sujet = models.CharField(max_length=200)
    contenu = models.TextField()
    dateEnvoi = models.DateTimeField(auto_now_add=True)
    conseillerRH = models.ForeignKey(ConseillerRH, on_delete=models.CASCADE, related_name='courriels')
    
    def __str__(self):
        return f"{self.sujet} - {self.dateEnvoi.strftime('%d/%m/%Y')}"
