from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


processor_buttons = [
    PluginMenuButton(
        link='plugins:netbox_multicast_stream_mapping:processor_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

sender_button = [
    PluginMenuButton(
        link='plugins:netbox_multicast_stream_mapping:sender_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

receiver_button = [
    PluginMenuButton(
        link='plugins:netbox_multicast_stream_mapping:receiver_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

stream_button = [
    PluginMenuButton(
        link='plugins:netbox_multicast_stream_mapping:stream_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

format_button = [
    PluginMenuButton(
        link='plugins:netbox_multicast_stream_mapping:format_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_multicast_stream_mapping:processor_list',
        link_text='Processors',
        buttons=processor_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_multicast_stream_mapping:sender_list',
        link_text='Multicast Senders',
        buttons=sender_button
    ),
    PluginMenuItem(
        link='plugins:netbox_multicast_stream_mapping:receiver_list',
        link_text='Multicast Receivers',
        buttons=receiver_button
    ),
    PluginMenuItem(
        link='plugins:netbox_multicast_stream_mapping:stream_list',
        link_text='Multicast Streams',
        buttons=stream_button
    ),
    PluginMenuItem(
        link='plugins:netbox_multicast_stream_mapping:format_list',
        link_text='Format Tags',
        buttons=format_button
    ),
)
