from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404
from .tables import *
from .models import *
from .serializers import ApplicationSerializer #API
from .forms import *
from applicationlist.utils import *
from django_tables2 import RequestConfig
from rest_framework.views import APIView #API
from rest_framework.response import Response #API
from django.shortcuts import get_object_or_404

# Load applications as a table
class ApplicationListTableView(TemplateView):
    template_name = "applicationlist/applicationlist.html"

    def get_queryset(self, **kwargs):
        return Application.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ApplicationListTableView, self).get_context_data(**kwargs)
        table = ApplicationListTable(self.get_queryset(**kwargs))
        if 'authenticated' not in self.request.session:
            table.exclude = ('edit')
        RequestConfig(self.request).configure(table)
        RequestConfig(self.request, paginate={'per_page': Application.objects.count()}).configure(table)
        context['table'] = table
        return context


# Edit applications
def Edit(request, applicationId):
    instance = get_object_or_404(Application, applicationId=applicationId) # Get object or 404
    if 'authenticated' in request.session:
        if request.method == 'POST': # if HTTP POST method = something must have been saved.
            form = ApplicationForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                raise Http404
        else: # if anything else than POST method (Like GET)
            form = ApplicationForm(instance=instance)
            return render(request, 'applicationlist/applicationedit.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


'''

User views

'''
# Login
def Login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Check up against the Active Directory
            if CheckUserWithActiveDirectory(form.data['email'], form.data['password']):
                request.session['authenticated'] = True
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('#')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'applicationlist/login.html', {'form': form})

def Logout(request):
    if 'authenticated' not in request.session:
        HttpResponseRedirect('/')
    else:
        del request.session['authenticated']
    request.session.modified = True # Force the change in the session table
    return HttpResponseRedirect('/')


'''

API views

'''
# Lists all applications or create a new one
class ApplicationList(APIView):
  
  def get(self, request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)
  
  def post(self):
    pass

# Get single application
# api/application/<applicationId>
class ApplicationDetail(APIView):

    def get_object(self, id):
        return Application.objects.get(applicationId=id)

    def get(self, request, applicationId):
        snippet = self.get_object(applicationId)
        serializer = ApplicationSerializer(snippet)
        return Response(serializer.data)