from django.shortcuts import render

def contact(request):
    ctx = {

    }
    return render(request, 'contact/contact.html', ctx)

