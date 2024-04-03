from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CJCForm
from .models import CJC


@login_required(login_url="login_url")
def info_view(request):
    template_name = "curd_app/info.html"
    form = CJCForm()
    if request.method == "POST":
        form = CJCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_view(request):
    template_name = "curd_app/show.html"
    obj = CJC.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = CJC.objects.get(id=pk)
    form = CJCForm(instance=obj)
    if request.method == "POST":
        form = CJCForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, "curd_app/hostel_info.html", context)


def delete_view(request, pk):
    obj = CJC.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, "curd_app/confirm.html")
