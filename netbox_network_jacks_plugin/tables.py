import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import networkjacks


class networkjacksTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = networkjacks
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)
