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
            sender_subject = form.cleaned_data['sender_subject']
            message = form.cleaned_data['message']
            full_message = "You have the following contact form submission from Maria Dong.com:\n\n"""
            full_message += f"\n\tFrom Sender: {sender_name}."
            full_message += f"\n\tSender's email: {sender_email}."
            full_message += f"\n\tSubject: {sender_subject}."
            full_message += f"\n\tMessage:\n\n\t{message}"
            message = full_message
            human = True

            try:
                send_mail(subject, message, from_email, ['maria@mariadong.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact/email.html", {'form': form})

def successView(request):
    return render(request, 'contact/success.html')