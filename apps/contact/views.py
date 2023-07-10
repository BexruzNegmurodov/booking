from django.shortcuts import render, redirect
from .models import Leave_Message
from .forms import Leave_MessageForm


def contact(request):
    form = Leave_MessageForm()
    if request.method == 'POST':
        form = Leave_MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:contact')
    ctx = {
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)
