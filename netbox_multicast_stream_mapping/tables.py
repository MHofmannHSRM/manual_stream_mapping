import django_tables2 as tables
from django_tables2.utils import A
from netbox.tables import NetBoxTable, ChoiceFieldColumn, TagColumn, ManyToManyColumn, columns
from .models import *
# todo actions?


class FormatTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = ChoiceFieldColumn() # todo button color
    res_h = tables.Column(verbose_name='Vertical Resolution')
    res_w = tables.Column(verbose_name='Horizontal Resolution')
    fps = ChoiceFieldColumn(verbose_name='Frame Rate')
    audio_ch = tables.Column(verbose_name='Number of Audio Channels')
    port = tables.Column(verbose_name='Network Port')
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Format
        fields = (
            'pk', 'id', 'name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'port', 'comments', 'description', 'tags'
        ) # todo updated?
        default_columns = ('name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'port', 'description', 'tags')


class ProcessorTable(NetBoxTable):
    name = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    module = tables.Column(linkify=True)
    endpoint_count = tables.LinkColumn(
            'plugins:netbox_multicast_stream_mapping:endpoint_children',  # URL-Name der Endpoint-Tabelle
            args=[A("pk")],
            verbose_name='Number of Endpoints')
    description = tables.Column()
    comments = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter? # tags = TagColumn(url_name='tag')

    class Meta(NetBoxTable.Meta):
        model = Processor
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'device', 'module', 'endpoint_count', 'description', 'comments', 'tags') # todo updated?
        default_columns = ('name', 'device', 'endpoint_count', 'tags', 'description')


class EndpointTable(NetBoxTable):
    name = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    processor = tables.Column(linkify=True)
    interface = tables.Column(linkify=True)
    endpoint_type = tables.Column(verbose_name='Endpoint Type') # todo button
    primary_ip = tables.Column(linkify=True, verbose_name='Primary IP Address')
    secondary_ip = tables.Column(linkify=True, verbose_name='Secondary IP Address')
    max_bandwidth = tables.Column(verbose_name='Max. Bandwidth (Mbps)')
    supported_formats = ManyToManyColumn(verbose_name='Supported Formats')
    switch_method = tables.Column(verbose_name='Switch Method (2022-7)') # todo button
    signal_type = ChoiceFieldColumn(verbose_name='Signal Type')
    description = tables.Column()
    comments = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Endpoint
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = (
            'pk', 'id', 'name', 'processor', 'interface', 'endpoint_type', 'primary_ip', 'secondary_ip',
            'max_bandwidth', 'supported_formats',  'signal_type', 'comments', 'description', 'tags'
        )  # todo updated?
        default_columns = ('name', 'endpoint_type', 'signal_type', 'description',  'device', 'processor',
                           'switch_method', 'supported_formats', 'primary_ip', 'secondary_ip', 'tags')


class StreamTable(NetBoxTable):
    name = tables.Column(linkify=True)
    sender = tables.Column(linkify=True)
    receivers = tables.Column() # todo ändern
    bandwidth = tables.Column() #rechtschreibfehler überall
    signal_type = tables.Column() #todo button
    protocol = tables.Column()
    formats = tables.Column()
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Stream
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = (
            'pk', 'id', 'name', 'sender', 'receivers', 'bandwidth', 'signal_type', 'protocol', 'formats', 'comments',
            'description', 'tags'
        ) # todo updated?
        default_columns = ('name', 'signal_type', 'sender', 'receivers', 'description', 'tags')
