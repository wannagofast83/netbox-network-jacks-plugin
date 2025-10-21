from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class networkjacks(NetBoxModel):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_network_jacks_plugin:networkjacks", args=[self.pk])
