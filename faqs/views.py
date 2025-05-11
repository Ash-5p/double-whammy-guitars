from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import FAQ
from .forms import FAQForm


# def faqs(request):

#     faqs = FAQ.objects.all()

#     template = 'faqs/faqs.html'
#     context = {
#         'faqs': faqs,
#     }

#     return render(request, template, context)


def view_and_add_faqs(request):
    """ Add an FAQ to the FAQs page """
    if not request.user.is_superuser and request.method == 'POST':
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FAQForm(request.POST, request.FILES)
        if form.is_valid():
            faq = form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request,
                'Failed to add FAQ. Please ensure the form is valid.')
    else:
        form = FAQForm()

    faqs = FAQ.objects.all()

    template = 'faqs/faqs.html'
    context = {
        'faqs': faqs,
        'form': form,
    }

    return render(request, template, context)
