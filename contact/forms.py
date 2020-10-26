from django import forms

class ContactForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email', required=True)
    sender_name = forms.CharField(label='Your Name', required=True)
    subject = forms.CharField(label='Your Subject', required=True)
    message = forms.CharField(label='What would you like to say?', widget=forms.Textarea, required=True)