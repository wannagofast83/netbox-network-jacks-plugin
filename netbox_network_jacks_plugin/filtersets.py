from netbox.filtersets import NetBoxModelFilterSet
from .models import networkjacks


# class networkjacksFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = networkjacks
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
