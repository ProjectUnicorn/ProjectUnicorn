from django.shortcuts import render
from django.views.generic import TemplateView
from .tables import *
from .models import *

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
        context['table'] = table
        return context
