from django.contrib import admin
from .models import Employe, Beneficiaire, ConseillerRH, CompagnieAssurance, Appel, Notification, Courriel

# Register your models here.
admin.site.register(Employe)
admin.site.register(Beneficiaire)
admin.site.register(ConseillerRH)
admin.site.register(CompagnieAssurance)
admin.site.register(Appel)
admin.site.register(Notification)
admin.site.register(Courriel)
