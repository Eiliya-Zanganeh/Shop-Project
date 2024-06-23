from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, template_name, context=None):
    try:
        message = render_to_string(template_name, context)
        plain_message = strip_tags(message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, [to], html_message=message)
    except:
        pass
