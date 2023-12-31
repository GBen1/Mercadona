from django.db import models


# Create your models here.
from django.utils.text import slugify

class Articles(models.Model):
    libelle = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True)
    owner = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    prix = models.FloatField()
    prix_final = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", null=True)
    categorie = models.CharField(max_length=1000)
    promotion = models.BooleanField(default=False)
    debut_promo = models.DateField(blank=True, null=True)
    fin_promo = models.DateField(blank=True, null=True)
    pourcentage_promo = models.FloatField(blank=True, null=True)
   

 

    def save (self,*args,**kwargs):

        if not self.slug:
            self.slug = slugify(self.libelle)
        
        if not self.prix_final and self.promotion is True:
            self.prix_final = self.prix  - (self.prix * (self.pourcentage_promo / 100))

        super().save(*args,**kwargs)

    
#class Client(models.Model):