# -*- encoding: utf-8 -*-
import django_tables2 as tables
from django_tables2.utils import A
from .models import *

class ApplicationListTable(tables.Table):
    datadeal_url = tables.TemplateColumn('<a href="{{record.applicationDataDeal}}">Link</a>', verbose_name="Data aftale")
    riskeval_url = tables.TemplateColumn('<a href="{{record.applicationRiskEvaluation}}">Link</a>', verbose_name="Risiko evaluering")
    edit = tables.LinkColumn('applicationlist_edit', text='Edit', args=[A('applicationId')], orderable=False)

    class Meta:
        model = Application
        fields = 'edit', \
                 'applicationName', \
                 'applicationSystem', \
                 'applicationSystemOwner', \
                 'applicationSystemOwnerContact', \
                 'applicationDescription', \
                 'applicationContainsPersonData',\
                 'applicationClassification', \
                 'datadeal_url', \
                 'riskeval_url',


        attrs = {'class': 'table table-striped table-bordered table-hover table-condensed'}