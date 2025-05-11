from django.shortcuts import render, redirect, reverse

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ A view to return the newsletter page & form """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message was successfully submitted!')
            send_confirmation_email(contact)
            return redirect(reverse('contact'))
        else:
            messages.error(
                request,
                'Message failed to send. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def send_confirmation_email(contact):
    """ Send the user a confirmation email """
    subject = render_to_string(
        'contact/confirmation_emails/confirmation_email_subject.txt',
        {'contact': contact}
    )
    body = render_to_string(
        'contact/confirmation_emails/confirmation_email_body.txt',
        {'contact': contact}
    )
    send_mail(
        subject.strip(),
        body,
        settings.DEFAULT_FROM_EMAIL,
        [contact.email]
    )
