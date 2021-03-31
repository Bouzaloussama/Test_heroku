from django.shortcuts import render

# Create your views here.



def Ontologie(request):

    name = "oussama2"
    last_name = "bouzal"

    context = {
        'concepts' : name,
        'termes'   : last_name,

    }

    return render(request, 'bas1.html', context)