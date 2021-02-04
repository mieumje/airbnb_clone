from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from django_countries import countries
from . import models, forms


class PstView(ListView):

    """ HomeView Definition """

    model = models.Pst
    paginate_by = 10
    paginate_orphans = 2
    ordering = "created"
    context_object_name = "psts"


class PstDetail(DetailView):

    """ PstDetail Definition """

    model = models.Pst


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        pst_name = request.GET.get("pst_name")

        if pst_name:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                pst_name = form.cleaned_data.get("pst_name")
                pst_type = form.cleaned_data.get("pst_type")

                filter_args = {}

                if pst_name != "all":
                    filter_args["pst_name__contains"] = pst_name

                filter_args["pst_name"] = pst_name

                if pst_type is not None:
                    filter_args["pst_type"] = pst_type

                qs = models.Pst.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                psts = paginator.get_page(page)

                return render(request, "psts/search.html", {"form": form, "psts": psts})

        else:
            form = forms.SearchForm()

        return render(request, "psts/search.html", {"form": form})