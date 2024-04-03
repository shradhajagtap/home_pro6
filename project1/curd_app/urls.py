from django.urls import path

from .views import info_view, show_view, update_view, delete_view

urlpatterns = [
    path("", info_view, name="info_url"),
    path("show/", show_view, name="show_url"),
    path("update/<int:pk>", update_view, name="update_url"),
    path("delete/<int:pk>", delete_view, name="delete_url"),
]