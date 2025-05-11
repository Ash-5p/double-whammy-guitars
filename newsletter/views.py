from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import NewsletterForm


def newsletter(request):
    """ A view to return the newsletter page & form """
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            newsletter = form.save()
            messages.success(request, 'Successfully signed up to newsletter!')
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Newsletter subscription failed. Please ensure the form is valid.')
    else:
        form = NewsletterForm()

    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
