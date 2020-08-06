from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:fetch>", views.fetch, name="fetch"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("newentry", views.new_entry, name="new_entry"),
    path("editpage/<str:page>", views.edit, name="editpage"),
    path("updated", views.save_edit, name = "save_edit"),
    path("random", views.rand, name = "random")
    
]
