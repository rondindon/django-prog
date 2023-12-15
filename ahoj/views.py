from django.shortcuts import render 
from . import urls
# Create your views here. 
def ahoj(request): 
      
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "ahoj/index.html") 