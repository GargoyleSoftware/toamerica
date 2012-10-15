from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.views.generic.list import ListView

from models import RegionalCenter

def home(request):
  return HttpResponse('hello world')

class RegionalCenterListView(ListView):
  #queryset = RegionalCenter.objects.all()
  model = RegionalCenter
  context_object_name = 'regional_centers'

class RegionalCenterDetailView(DetailView):
  model = RegionalCenter
  context_object_name = 'regional_center'
