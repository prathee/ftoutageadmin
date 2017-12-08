from django.shortcuts import render

# Create your views here.

from .models import Outage


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_outage = Outage.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get( 'num_visits', 0 )
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_outage': num_outage, 'num_visits': num_visits},
    )


from django.views import generic

class OutageListView( generic.ListView ):
    """
    Generic class-based view for a list of Outage.
    """
    model = Outage
    paginate_by = 10


class OutageDetailView( generic.DetailView ):
    """
    Generic class-based detail view for a Outage.
    """
    model = Outage


from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Classes created for the forms challenge
class OutageCreate( PermissionRequiredMixin, CreateView ):
    model = Outage
    fields = '__all__'
    initial = {'date_of_creation': '07/12/2017', }
    permission_required = 'OutageManagement.can_mark_active'


class OutageUpdate( PermissionRequiredMixin, UpdateView ):
    model = Outage
    fields = '__all__'
    permission_required = 'OutageManagement.can_mark_active'


class OutageDelete( PermissionRequiredMixin, DeleteView ):
    model = Outage
    success_url = reverse_lazy( 'OutageManagement' )
    permission_required = 'OutageManagement.can_mark_active'
