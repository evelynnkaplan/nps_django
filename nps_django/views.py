from nps_django.models import Passholder, Pass, Park, Visit
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from nps_django.serializers import PassholderSerializer, PassSerializer, ParkSerializer, VisitSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.contrib import messages
from .forms import PassForm

def home(request):
  return render(request, 'home.html')

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

class UserPassView(APIView):
  def get(self, request, **kwargs):
    user_email = kwargs.get('email', None)
   
    user_pass_queryset = Pass.objects.filter(email=user_email)
    if len(user_pass_queryset) > 0:
      response = {}
      for up in user_pass_queryset:
        response[up.pass_id] = {
          'type': up.type, 
          'expiration_date': up.expiration_date
        }
    else:
      response = {}

    return Response(response)

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

class UserVisitView(APIView):
  def get(self, request, **kwargs):
    user_email = kwargs.get('email', None)
   
    passes = Pass.objects.filter(email=user_email)
    pks = []
    all_visits = []

    for item in passes:
      if item.passholder_primary != None and item.passholder_primary.pk not in pks:
        pks.append(item.passholder_primary.pk)

    for person in pks:
      personvisits = Visit.objects.filter(passholder__pk=person)
      for vis in personvisits:
        if vis not in all_visits:
          all_visits.append(vis)

    response = {}

    for vis in all_visits:
      response[f'{vis.pk}'] = f'{vis}'

    return Response(response)

