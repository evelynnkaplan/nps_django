from nps_django.models import Passholder, Pass, Park, Visit
from rest_framework import viewsets
from nps_django.serializers import PassholderSerializer, PassSerializer, ParkSerializer, VisitSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.contrib import messages
from .forms import PassForm

def registration(request):
  if request.method == 'POST':
    form = PassForm(request.POST)
    if form.is_valid():
      new_pass = form.save()
      messages.success(request, 'You successfully registered your pass. Go explore!')
      # return render(request, 'registration.html', {'form': form})
  else: 
    form = PassForm()
  return render(request, 'registration.html', {'form': form})

class PassholderViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows passholders to be viewed or edited.
  """
  queryset = Passholder.objects.all().order_by('last_name')
  serializer_class = PassholderSerializer 

class PassViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows passes to be viewed or edited.
  """
  queryset = Pass.objects.all().order_by('type')
  serializer_class = PassSerializer

class ParkViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows parks to be viewed or edited.
  """
  queryset = Park.objects.all().order_by('name')
  serializer_class = ParkSerializer

class VisitViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows visits to be viewed or edited.
  """
  queryset = Visit.objects.all().order_by('-date')
  serializer_class = VisitSerializer

