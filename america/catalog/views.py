from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView
from django.views.generic.list import ListView

from models import RegionalCenter

class HomeView(TemplateView):
  template_name = "home.html"

class RegionalCenterListView(ListView):
  #queryset = RegionalCenter.objects.all()
  model = RegionalCenter
  context_object_name = 'regional_centers'

class RegionalCenterDetailView(DetailView):
  model = RegionalCenter
  context_object_name = 'regional_center'
