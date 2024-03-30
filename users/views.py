from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import User, UserForm


class IndexView(generic.ListView):
    def get_queryset(self):
        return User.objects.order_by("first_name")


def edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST" and "save" in request.POST:
        f = UserForm(request.POST, instance=user)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse("users:index"))  
        else:  
            return render(request, "users/edit.html", {"form": f})
    elif request.method == "POST" and "delete" in request.POST:
        user.delete()
        return HttpResponseRedirect(reverse("users:index"))  
    else:
        f = UserForm(instance=user)
        return render(request, "users/edit.html", {"form": f})


def add(request):    
    if request.method == "POST":
        f = UserForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect(reverse("users:index"))  
        else:  
            return render(request, "users/add.html", {"form": f})
    else:
        f = UserForm()
        return render(request, "users/add.html", {"form": f})
