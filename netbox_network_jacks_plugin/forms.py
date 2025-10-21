from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import networkjacks


class networkjacksForm(NetBoxModelForm):
    class Meta:
        model = networkjacks
        fields = ("name", "tags")
