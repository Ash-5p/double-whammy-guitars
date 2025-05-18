from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import FAQ
from .forms import FAQForm


def view_and_add_faqs(request):
    """
    Display a list of all instances of :model:`faqs.FAQ`.
    Display an instance of :form:`faqs.FAQForm` if the user is a superuser.

    **Context**

    ``faqs``
        All instances of :model:`faqs.FAQ`.
    ``form``
        An instance of :form:`faqs.FAQForm`.

    **Template:**

    :template:`faqs/faqs.html`
    """
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


@login_required
def edit_faq(request, faq_id):
    """
    Modify a single isntance of :model:`faqs.FAQ` if the user is a superuser.
    Display an instance of :form:`faqs.FAQForm` if the user is a superuser.

    **Context**

    ``faq``
        A single isntance of :model:`faqs.FAQ`.
    ``form``
        An instance of :form:`faqs.FAQForm`.

    **Template:**

    :template:`faqs/edit_faq.html`
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, pk=faq_id)
    if request.method == 'POST':
        form = FAQForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated FAQ!')
            return redirect(reverse('faqs'))
        else:
            messages.error(
                request,
                'Failed to update FAQ. Please ensure the form is valid.')
    else:
        form = FAQForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    template = 'faqs/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """
    Delete a single isntance of :model:`faqs.FAQ` if the user is a superuser.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FAQ, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ deleted!')
    return redirect(reverse('faqs'))
