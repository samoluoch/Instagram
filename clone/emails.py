from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .tokens import activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode

def activation_email(user, current_site, receiver):
    subject = 'Activate your account'

    message = render_to_string('registration/activate.html', {
        'user':user,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':activation_token.make_token(user),
    })

    email = EmailMessage(subject, message, to=[receiver])
    email.send()