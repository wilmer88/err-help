from django.http import HttpResponseRedirect
# from urllib import response
from django.shortcuts import redirect,render
from .models import ErrModel
from .forms import ErrForm
# from django.contrib import messages
# from errworld.forms import ErrForm

# monkey= datetime.datetime.now()
def index(request):
       all_err = ErrModel.objects.all()     
       return render(request, "users/index.html", {
               "navbar":"index", "estos": all_err
  })
        
def add(request):
        # snipForm = SnipitForm()
        if request.method == "POST": 
                lang_name =request.POST["lang_name"]
                err_title=request.POST["err_title"]
                fixer_code = request.POST["fixer_code"]
                os_tech = request.POST["os_tech"]
                snipit = ErrModel(lang_name=lang_name,err_title=err_title,fixer_code=fixer_code,os_tech=os_tech)
                snipit.save()
                return  HttpResponseRedirect("/")   
        return render(request, "users/add.html", {"navbar":"add"})

def edit(request,id):
 Selected_err = ErrModel.objects.get(id=id)
 forms = ErrForm(request.POST, instance=Selected_err)
 if forms.is_valid():
        forms.save() 
        return  HttpResponseRedirect("/")   
 return render(request, "users/edit.html",{"navbar":"edit","vu":Selected_err}) 

def delete(request,id):
        entry = ErrModel.objects.get(id=id)
        entry.delete()
        return  HttpResponseRedirect("/")   
