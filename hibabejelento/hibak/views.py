from django.shortcuts import render
from .models import Hiba, Alkalmazott,ErtesitettAlkalmazott
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate count of some of the main objects
    hibak_szama=Hiba.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'hibak_szama':hibak_szama},
    )


from django.views import generic

class HibaReszleteiView(generic.DetailView):
    model = Hiba

class HibaListaView(generic.ListView):
    model = Hiba


from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import HibaBejelentoForm
from django.core.mail import send_mail

@login_required
def hiba_bejelentes(request):
    """
    View function for renewing a specific BookInstance by librarian
    """
    #hiba=get_object_or_404(Hiba)
    

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = HibaBejelentoForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            			    
            hiba = form.save(commit=True)
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            hiba.nev = form.cleaned_data['nev']
            hiba.cim = form.cleaned_data['cim']
            hiba.kapcsolattarto_email = form.cleaned_data['kapcsolattarto_email']
            hiba.leiras = form.cleaned_data['leiras']
            form.save()
            emailTo = ErtesitettAlkalmazott.objects.all()
            for i in range(len(emailTo)):
                send_mail('Hiba bejelentes tortent','Ezt az uzenetet csak az Ertesitett Alkalmazott-ak kapjak meg','minipek.gn@gmail.com',[emailTo[i].alkalmazott.email],fail_silently=False,)
            send_mail('Hibabejelenteset fogadtuk','A hiba elharitassal kapcsolatban tovabbi ertesiteseket fog kapni','tesztemailepuzbau@gmail.com',[form.cleaned_data['kapcsolattarto_email']],fail_silently=False,)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('hibalista') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = HibaBejelentoForm()

    return render(request, 'hibak/hibabejelentes.html', {'form': form})