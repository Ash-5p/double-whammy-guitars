from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """
    Display the currently logged in user's profile
    Returns an isntance of :model:`profiles.UserProfile`.

    Renders an isntance of :form:`profiles.UserProfileForm`.
    Allows user to edit their isntance of :model:`profiles.UserProfile`.

    Allows user to view all instances of :model:`checkout.Order` created
    by the currently logged in user.


    **Context**

    ``form``
        A single instance of :form:`profiles.UserProfileForm`.
    ``orders``
        All instances of :model:`checkout.Order` created by the user.
    ``on_profile_page``
        Returns on_profile_page = True for use in DTL tags.

    **Template:**

    :template:`profiles/profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Displays a single instance of :model:`checkout.Order` created
    by the currently logged in user.

    **Context**

    ``orders``
        A single instance of :model:`checkout.Order` created by the user.
    ``from_profile``
        Returns from_profile = True for use in DTL tags.

    **Template:**

    :template:`checkout/checkout_success.html`
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
