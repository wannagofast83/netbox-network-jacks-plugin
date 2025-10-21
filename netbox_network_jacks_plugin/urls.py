from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    path("network-jackss/", views.networkjacksListView.as_view(), name="networkjacks_list"),
    path("network-jackss/add/", views.networkjacksEditView.as_view(), name="networkjacks_add"),
    path("network-jackss/<int:pk>/", views.networkjacksView.as_view(), name="networkjacks"),
    path("network-jackss/<int:pk>/edit/", views.networkjacksEditView.as_view(), name="networkjacks_edit"),
    path("network-jackss/<int:pk>/delete/", views.networkjacksDeleteView.as_view(), name="networkjacks_delete"),
    path(
        "network-jackss/<int:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="networkjacks_changelog",
        kwargs={"model": models.networkjacks},
    ),
)
