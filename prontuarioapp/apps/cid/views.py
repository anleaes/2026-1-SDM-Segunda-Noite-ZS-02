from django.shortcuts import render
from .models import Cid
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .forms import CidForm
from .serializer import CidSerializer

# Create your views here.

class CidViewSet(viewsets.ModelViewSet):
    queryset = Cid.objects.all()
    serializer_class = CidSerializer  


def add_cid(request):
    template_name = 'cid/add_cid.html'
    context = {}

    if request.method == 'POST':
        form = CidForm(request.POST)

        if form.is_valid():
            cid = form.save(commit=False)
            cid.save()
            return redirect('cid:list_cid')

    form = CidForm()
    context['form'] = form
    return render(request, template_name, context)
