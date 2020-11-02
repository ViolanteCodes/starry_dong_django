from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email', required=True)
    sender_name = forms.CharField(label='Your Name', required=True)
    sender_subject = forms.CharField(label='Your Subject', required=True)
    message = forms.CharField(label='What would you like to say?', widget=forms.Textarea, required=True)
    captcha = CaptchaField()
