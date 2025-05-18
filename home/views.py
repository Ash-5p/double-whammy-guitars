from django.shortcuts import render


def index(request):
    """
    Render home page.

    **Template:**

    :template:`home/index.html`
    """
    return render(request, 'home/index.html')
