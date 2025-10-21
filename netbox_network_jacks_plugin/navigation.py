from netbox.plugins import PluginMenuButton, PluginMenuItem


plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_network_jacks_plugin:networkjacks_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_network_jacks_plugin:networkjacks_list",
        link_text="network-jacks",
        buttons=plugin_buttons,
    ),
)
