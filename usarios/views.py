from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# from urllib import response
# from django.shortcuts import redirect, render
# from ..models import ErrModel
# from django.contrib import messages
# # from .forms import SnipitForm
# from errworld.forms import ErrForm

# monkey= datetime.datetime.now()
def index(request):
    #    all_err = ErrModel.objects.all()     
       return render(request, "users/index.html", {
            #    "navbar":"index", "all_objs": all_err
  })
        
# def add_err(request):
#         # snipForm = SnipitForm()
#         if request.method == "POST": 
#                 lang_name =request.POST["language_name"]
#                 err_title=request.POST["snip_title"]
#                 fixer_code= request.POST["language_code"]
#                 os_tech= request.POST["short_description"]
#                 snipit = ErrModel(lang_name=lang_name,err_title=err_title,fixer_code=fixer_code,os_tech=os_tech)
#                 snipit.save()
            
              
#                 messages.info(request, "successfully saved error")
#                 return redirect("users/index.html")
               
#         return render(request, "users/add_snip.html", {
                
#                 "navbar":"add_error"
#                 })


# def edit_err(request,id):
#  Selected_err = ErrModel.objects.get(id=id)
#  forms = ErrForm(request.POST, instance=Selected_err)
#  if forms.is_valid():
#         forms.save()
#  return render(request, "users/edit.html",{"navbar":"edit","vu":Selected_err}) 