from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView
from django.shortcuts import render
from django.core.paginator import Paginator
from users import mixins as user_mixins
from . import models, forms


# Create your views here.


class BlogView(ListView):

    """ BlogView definition """

    model = models.Blog
    paginate_by = 12
    paginate_orphans = 2
    ordering = "created"
    context_object_name = "blogs"


class BlogDetail(DetailView):

    """ BlogDetail definition """

    model = models.Blog


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):

        category = request.GET.get("category")

        if category:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                post_type = form.cleaned_data.get("post_type")

                filter_args = {}

                if post_type is not None:
                    filter_args["post_type"] = post_type

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                blogs = paginator.get_page(page)

                return render(
                    request, "blogs/search.html", {"form": form, "blogs": blogs}
                )

        else:
            form = forms.SearchForm()

        return render(request, "blogs/search.html", {"form": form})


class EditView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Blog
    template_name = "blogs/blog_edit.html"
    fields = ("name", "description", "category", "post_type")

    def get_object(self, queryset=None):
        blog = super().get_object(queryset=queryset)
        if blog.host.pk != self.request.user.pk:
            raise Http404()
        return blog