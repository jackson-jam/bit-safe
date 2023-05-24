from django.shortcuts import render

# Create your views here.
# users/views.py

from django.shortcuts import render
from django.db.models import Q
from .models import User


def user_search(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(name__icontains=query)
    else:
        users = []
    return render(request, 'user_search.html', {'users': users, 'query': query})

