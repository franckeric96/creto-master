from django.shortcuts import render

# Create your views here.








from django.shortcuts import render
# from blog.models import Article
from account.forms import NewsletterForm
from .models import NewsLetter
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    
    n_form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        n_form = NewsletterForm(request.POST)
        
        
        if n_form.is_valid():
            n_form.save()
            return HttpResponseRedirect(request.path_info)

        else:
            messages.warning(request, 'veuillez entrer ue addresse email valide svp')
        
    
    datas= {
        'n_form': n_form,
        

    }
    return render(request, 'website/index.html', datas)

def contacts(request):
    n_form = NewsletterForm()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        n_form = NewsletterForm(request.POST)
        
        
        if n_form.is_valid():
            n_form.save()
            return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, 'veuillez entrer ue addresse email valide svp')
        
        
        
    
    datas= {
        'n_form': n_form,
    }
    return render(request, 'website/contacts.html', datas)


def about(request):
    return render(request, 'website/about.html')




