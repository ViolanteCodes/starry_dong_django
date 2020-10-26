from django.shortcuts import render

# Create your views here.

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from mysite.settings import get_secret

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Form Submission from MariaDong.com'
            sender_email = form.cleaned_data['sender_email']
            from_email = 'maria@mariadong.com'
            sender_name = form.cleaned_data['sender_name']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['maria@mariadong.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')