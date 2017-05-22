from django.shortcuts import render
from django.views.generic import TemplateView
from .tables import *
from .models import *
from django_tables2 import RequestConfig
from rest_framework.views import APIView #API
from rest_framework.response import Response #API
from rest_framework import status #API
from .serializers import ApplicationSerializer #API
from django.shortcuts import get_object_or_404

# Create your views here.
class ApplicationListTableView(TemplateView):
    template_name = "applicationlist/applicationlist.html"

    def get_queryset(self, **kwargs):
        return Application.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ApplicationListTableView, self).get_context_data(**kwargs)
        table = ApplicationListTable(self.get_queryset(**kwargs))
        table.exclude = ('id')
        RequestConfig(self.request).configure(table)
        RequestConfig(self.request, paginate={'per_page':Application.objects.count()}).configure(table)
        context['table'] = table
        return context

# Lists all applications or create a new one
class ApplicationList(APIView):
  
  def get(self, request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)
  
  def post(self):
    pass
