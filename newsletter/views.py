from django.shortcuts import render, redirect, reverse

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

from .forms import NewsletterForm


def newsletter(request):
    """
    Returns an instance of :form:`newsletter.NewsletterForm`.

    **Context**

    ``form``
        A single instances of :form:`newsletter.NewsletterForm`.

    **Template:**

    :template:`newsletter/newsletter.html`
    """

    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            newsletter = form.save()
            messages.success(request, 'Successfully signed up to newsletter!')
            send_confirmation_email(newsletter.email)
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Newsletter subscription failed.'
                ' Please ensure the form is valid.')
    else:
        form = NewsletterForm()

    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def send_confirmation_email(cust_email):
    """ Send the user a confirmation email """
    subject = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_subject.txt'
    )
    body = render_to_string(
        'newsletter/confirmation_emails/confirmation_email_body.txt'
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
