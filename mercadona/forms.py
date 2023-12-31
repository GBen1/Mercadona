from django import forms
from admuser.models import Articles
import time
from datetime import datetime
import _strptime
from datetime import date

CATEGORIE = (
   
    ("Fruits","Fruits"),
    ("Legumes","Legumes"),
    ("Cosmetics","Cosmetics"),
    ("Home","Home"),   
    ("Pets","Pets"),  

)

class FilterForm(forms.Form):
   categorie_article = forms.ChoiceField(choices=CATEGORIE,required=True,widget=forms.RadioSelect())
   promotion = forms.BooleanField(required=False, initial=False)

#class LoginForm(forms.Form):
 #   Nom_d_utilisateur = forms.CharField(max_length=15,required=True)
  #  Mot_de_passe = forms.CharField(min_length=8,widget=forms.PasswordInput())

class PromotionForm(forms.Form):
    promotion = forms.BooleanField(required=False, initial=False)
    debut_promotion = forms.DateField(required=False, widget = forms.SelectDateWidget)
    fin_promotion = forms.DateField(required=False, widget = forms.SelectDateWidget)
    pourcentage_promotion = forms.FloatField(min_value=1,required=False, initial="")

    def clean(self):
     fin_promotion = self.cleaned_data.get("fin_promotion")
     debut_promotion = self.cleaned_data.get("debut_promotion")
     promotion = self.cleaned_data.get("promotion")
     pourcentage_promotion = self.cleaned_data.get("pourcentage_promotion")

         
     if str(debut_promotion) < str(date.today()):
        raise forms.ValidationError("La date de début de la promotion doit être ultérieure à la date du jour") 
     elif  str(debut_promotion) > str(fin_promotion):
         raise forms.ValidationError("La date de début de la promotion doit être inférieure à la date de fin") 
     elif promotion is False and debut_promotion is not None:
        raise forms.ValidationError("Il faut cocher la case Promotion pour enregister une promotion") 
     elif promotion is True and pourcentage_promotion is None :
         raise forms.ValidationError("Il faut renseigner un pourcentage de promotion pour enregister une promotion") 
     elif promotion is True and debut_promotion is None:
        raise forms.ValidationError("Il faut renseigner une date de début de promotion pour enregister une promotion") 
     elif promotion is True and fin_promotion is None:
       raise forms.ValidationError("Il faut renseigner une date de fin de promotion pour enregister une promotion") 
     return self.cleaned_data

class ArticleForm(forms.Form):

    #owner
   # Magasin = forms.CharField(max_length=100,required=True)
    #email = forms.EmailField()
    #password = forms.CharField(min_length=8,widget=forms.PasswordInput())
    #libelle 
    Libelle_Article = forms.CharField(max_length=1000,required=True)
    #slug = forms.SlugField(blank=True,required=True)
    #categorie
    categorie_article = forms.ChoiceField(choices=CATEGORIE,required=True,initial="",widget=forms.RadioSelect())

    #decription
    description_article = forms.CharField(max_length=1000,required=True, widget =forms.Textarea())

    #prix
    prix_article = forms.FloatField(min_value=0.5,required=True)

    image = forms.ImageField(required=True)
 
  #  promotion = forms.BooleanField(required=False, initial=False)
  #  debut_promotion = forms.DateField(required=False, widget = forms.SelectDateWidget)
  #  fin_promotion = forms.DateField(required=False, widget = forms.SelectDateWidget)
   # pourcentage_promotion = forms.FloatField(min_value=1,required=False, initial="")

#def clean_password(self):
#        password = self.cleaned_data.get("password")
#        #sc_list = list('[@_!#$%^&*()<>?/\|}{~:]')
#   
#        maj=[c for c in password if c.isupper()]
#        min=[c for c in password if c.islower()]
#        numb=[c for c in password if c.isdigit()]
#        
#        if (len(maj) == 0 or len(min) == 0) and len(numb) == 0:
#          
#          raise forms.ValidationError([
#                forms.ValidationError('Le mot de passe doit contenir des majuscules et des minuscules'),
#                forms.ValidationError('Le mot de passe doit contenir au moins un chiffre'),
#                        ])
#          
#        elif len(maj) == 0 or len(min) == 0:
#            raise forms.ValidationError("Le mot de passe doit contenir des majuscules et des minuscules")
#        elif len(numb) == 0:
#            raise forms.ValidationError("Le mot de passe doit contenir au moins un chiffre")
#      #  elif password not in sc_list:
#        #    raise forms.ValidationError("Le mot de passe doit contenir au moins un caractère spécial '[@_!#$%^&*()<>?/\|}{~:]'")
#        return password

    def clean_image(self):
    # fin_promotion = self.cleaned_data.get("fin_promotion")
     #debut_promotion = self.cleaned_data.get("debut_promotion")
    # promotion = self.cleaned_data.get("promotion")
    # pourcentage_promotion = self.cleaned_data.get("pourcentage_promotion")
     image = self.cleaned_data.get("image")
     sc_list = list('àáâæçèéêëìíîïñòóôœùúûüýÿÀÁÂÆÇÈÉÊËÌÍÎÏÑÒÓÔŒÙÚÛÜÝŸß·’“”«»•–—±×÷²³€†‡')
     count=[c for c in image if c in sc_list]
     
     if len(count) == 0:
         return image
     raise forms.ValidationError("Il y a des caractères interdit dans le nom du fichier que vous essayez d' uploader - accents interdit") 
     
     
    
    # if str(debut_promotion) < str(date.today()):
   #     raise forms.ValidationError("La date de début de la promotion doit être ultérieure à la date du jour") 
   #  elif  str(debut_promotion) > str(fin_promotion):
    #     raise forms.ValidationError("La date de début de la promotion doit être inférieure à la date de fin") 
    # elif promotion is False and debut_promotion is not None:
    #    raise forms.ValidationError("Il faut cocher la case Promotion pour enregister une promotion") 
    # elif promotion is True and pourcentage_promotion is None :
   #      raise forms.ValidationError("Il faut renseigner un pourcentage de promotion pour enregister une promotion") 
    # elif promotion is True and debut_promotion is None:
   #     raise forms.ValidationError("Il faut renseigner une date de début de promotion pour enregister une promotion") 
   #  elif promotion is True and fin_promotion is None:
   #     raise forms.ValidationError("Il faut renseigner une date de fin de promotion pour enregister une promotion") 
   #  elif   ascii > 0:
   #     raise forms.ValidationError("Il y a des caractères interdit dans le nom du fichier que vous essayez d' uploader - accents interdit") 
   #  return self.cleaned_data
  
