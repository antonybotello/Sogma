from django.shortcuts import render

def inicio (request):

    context = {
        
    }

    return render (request, 'index.html', context)