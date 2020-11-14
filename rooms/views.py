from django.views.generic import ListView, DetailView
from . import models

# Create your views here.


class HomeView(ListView):

    """ HomeView definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail definition """

    model = models.Room
