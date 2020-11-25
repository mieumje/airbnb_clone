from django.urls import path
from blogs import views as views

app_name = "blogs"

urlpatterns = [
    path("posts/", views.BlogView.as_view(), name="posts"),
    path("<int:pk>/", views.BlogDetail.as_view(), name="detail"),
]
