from django.shortcuts import render

from .models import FAQ


def faqs(request):
    template = 'faqs/faqs.html'
    context = {
        'faqs': faqs,
    }

    return render(request, template, context)
