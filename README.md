# API BPM Project

Application Django REST Framework pour la gestion des ressources humaines et assurances.

## Configuration requise

- Python 3.8+
- Django 5.2
- Django REST Framework 3.16.0+

## Installation

1. Clonez le dépôt
```
git clone <url-du-repo>
cd bpm_project
```

2. Installez les dépendances
```
pip install -r requirements.txt
```

3. Appliquez les migrations
```
python manage.py migrate
```

4. Créez un superutilisateur
```
python manage.py createsuperuser
```

5. Lancez le serveur
```
python manage.py runserver
```

## Modèles de données

L'application gère les entités suivantes:

- **Employe**: nom, prenom, dateNaissance, adresse, telephone, email
- **Beneficiaire**: nom, prenom, relationEmploye, dateNaissance
- **ConseillerRH**: nom, prenom, email, poste
- **Appel**: dateAppel, motif, etatAppel
- **Notification**: typeNotification, dateEnvoi, statut
- **CompagnieAssurance**: nomCompagnie, adresse, emailCompagnie
- **Courriel**: destinataire, sujet, contenu, dateEnvoi

Relations:
- Un Employe peut avoir plusieurs Beneficiaires et plusieurs Appels
- Un Appel est passé par un ConseillerRH vers un Employe
- Un Appel peut déclencher une ou plusieurs Notifications vers une CompagnieAssurance
- Un ConseillerRH peut envoyer plusieurs Courriels

## Utilisation de l'API

L'API est accessible aux points de terminaison suivants:

- Employés: `http://localhost:8000/api/employes/`
- Bénéficiaires: `http://localhost:8000/api/beneficiaires/`
- Conseillers RH: `http://localhost:8000/api/conseillers/`
- Compagnies d'assurance: `http://localhost:8000/api/compagnies/`
- Appels: `http://localhost:8000/api/appels/`
- Notifications: `http://localhost:8000/api/notifications/`
- Courriels: `http://localhost:8000/api/courriels/`
- Administration: `http://localhost:8000/admin/`
- Interface d'authentification API: `http://localhost:8000/api-auth/login/`

## Structure des endpoints

### GET /api/tasks/
Récupère la liste de toutes les tâches.

### POST /api/tasks/
Crée une nouvelle tâche.

Exemple de corps de requête:
```json
{
  "title": "Nouvelle tâche",
  "description": "Description de la tâche",
  "completed": false
}
```

### GET /api/tasks/{id}/
Récupère les détails d'une tâche spécifique.

### PUT /api/tasks/{id}/
Met à jour tous les champs d'une tâche.

### PATCH /api/tasks/{id}/
Met à jour partiellement une tâche.

### DELETE /api/tasks/{id}/
Supprime une tâche. 