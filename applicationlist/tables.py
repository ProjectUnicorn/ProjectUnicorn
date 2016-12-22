# -*- encoding: utf-8 -*-
import django_tables2 as tables
from .models import *

import logging
logger = logging.getLogger(__name__)


class ApplicationListTable(tables.Table):

    class Meta:
        model = Application
        sequence = 'applicationId','applicationName','applicationSystemOwner','applicationDescription','applicationOneNoteId'
        attrs = {'class': 'table table-striped table-bordered table-hover table-condensed'}
