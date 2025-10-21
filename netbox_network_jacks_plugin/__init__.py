"""Top-level package for NetBox network-jacks Plugin."""

__author__ = """Michael McClure"""
__email__ = "michael-mcclure@uiowa.edu"
__version__ = "0.1.0"


from netbox.plugins import PluginConfig


class networkjacksConfig(PluginConfig):
    name = "netbox_network_jacks_plugin"
    verbose_name = "NetBox network-jacks Plugin"
    description = "NetBox plugin for network-jacks."
    version = "version"
    base_url = "netbox_network_jacks_plugin"


config = networkjacksConfig
