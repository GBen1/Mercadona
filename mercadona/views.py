from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
#from mercadona.forms import LoginForm
from mercadona.forms import ArticleForm
from mercadona.forms import PromotionForm
from mercadona.forms import FilterForm
from admuser.models import Articles

date = datetime.today()

def index(request):
    form = FilterForm(request.POST)

    data = Articles.objects.order_by('-id')

    if request.method == "POST":
       if form.is_valid():
        if form.cleaned_data["promotion"] == False:
         data = Articles.objects.filter(categorie=request.POST['categorie_article']).order_by('-id')
         return render(request,"index.html",{"form":form,"data":data})
        else:
         data = Articles.objects.filter(categorie=request.POST['categorie_article']).filter(promotion=True).order_by('-id')
         return render(request,"index.html",{"form":form,"data":data})
    form = FilterForm()
    return render(request,"index.html",{"form":form,"data":data})


def profile(request):
 data = Articles.objects.filter(owner=request.user.username).order_by('-id')
 form = ArticleForm(request.POST,request.FILES)
 form2 = PromotionForm(request.POST,request.FILES)
 if request.method == "POST":

  user = request.user.username

  if 'promotion' in request.POST:
    if form2.is_valid():
      Article = Articles.objects.get(id=request.POST['pk'])
      Article.promotion= form2.cleaned_data["promotion"]
      Article.debut_promo = form2.cleaned_data["debut_promotion"]
      Article.fin_promo= form2.cleaned_data["fin_promotion"]
      Article.pourcentage_promo = form2.cleaned_data["pourcentage_promotion"]                
      Article.save()

      #return HttpResponse("L'article a bien été créé")
    return render(request,"admuser/profile.html", {"form":form,"form2":form2, "user":request.user.username,"data":data})
  
  else:     
     
     if form.is_valid():
      

      Article = Articles(
		    libelle = form.cleaned_data["Libelle_Article"] ,
		    owner = user ,
		    description = form.cleaned_data["description_article"] ,
		    prix = form.cleaned_data["prix_article"] ,
	      categorie = form.cleaned_data["categorie_article"] ,
        image  = form.cleaned_data["image"],
	       )
      Article.save()
      #return HttpResponse("L'article a bien été créé")
     return render(request,"admuser/profile.html", {"form":form, "form2":form2,"user":request.user.username,"data":data})

 form = ArticleForm()
 return render(request,"admuser/profile.html", {"form":form,"form2":form2,"user":request.user.username,"data":data})
 


#def login(request):
 #   if request.method == "POST":
 #     form = LoginForm(request.POST)
 #     if form.is_valid():       
 #      return HttpResponse("Login ok")
 #    return render(request,"login.html", {"form":form})
#    form = LoginForm()
  #  return render(request,"login.html", {"form":form})

   

def vue_de_test(request):
    return HttpResponse("<h1>Vue de test </h1>")

