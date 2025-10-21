from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class networkjacksView(generic.ObjectView):
    queryset = models.networkjacks.objects.all()


class networkjacksListView(generic.ObjectListView):
    queryset = models.networkjacks.objects.all()
    table = tables.networkjacksTable


class networkjacksEditView(generic.ObjectEditView):
    queryset = models.networkjacks.objects.all()
    form = forms.networkjacksForm


class networkjacksDeleteView(generic.ObjectDeleteView):
    queryset = models.networkjacks.objects.all()
