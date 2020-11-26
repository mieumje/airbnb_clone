from django.urls import path
from . import views


app_name = "psts"

urlpatterns = [
    path("list/", views.PstView.as_view(), name="list"),
    path("<int:pk>", views.PstDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
