import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn, TagColumn, ManyToManyColumn

from .models import Processor, Sender, Receiver, Stream, Format


class FormatTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = ChoiceFieldColumn()
    res_h = tables.Column(verbose_name='Vertical Resolution')
    res_w = tables.Column(verbose_name='Horizontal Resolution')
    fps = ChoiceFieldColumn(verbose_name='Frame Rate')
    audio_ch = tables.Column(verbose_name='Number of Audio Channels')
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Format
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'description', 'tags')


class ProcessorTable(NetBoxTable):
    name = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    module = tables.Column(linkify=True)
    sender_count = tables.Column(verbose_name='Number of Senders') # todo counter cache field
    receiver_count = tables.Column(verbose_name='Number of Receivers') # todo counter cache field
    description = tables.Column()
    comments = tables.Column()
    tags = TagColumn() # TODO -> Verlinkung -> Filter?
    # tags = TagColumn(url_name='tag')

    class Meta(NetBoxTable.Meta):
        model = Processor
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'device', 'module', 'sender_count', 'receiver_count', 'description', 'comments',
                  'tags') # todo updated?
        default_columns = ('name', 'device', 'module', 'sender_count', 'receiver_count', 'tags', 'description')


class SenderTable(NetBoxTable):
    name = tables.Column(linkify=True)
    processor = tables.Column(linkify=True)
    sender_ip = tables.Column(linkify=True, verbose_name='Sender IP-Adress')
    max_bandwidth_out = tables.Column(verbose_name='Max. Bandwidth (Mbps)')
    supported_formats = ManyToManyColumn()
    switch_method = tables.Column(verbose_name='Switch Method (2022-7)')
    signal_type = ChoiceFieldColumn(verbose_name='Signal Type')
    description = tables.Column()
    comments = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Sender
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'processor', 'signal_type', 'sender_ip', 'max_bandwidth_out',
                  'supported_formats', 'switch_method',  'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'processor', 'signal_type', 'sender_ip', 'supported_formats', 'tags', 'description')


class ReceiverTable(NetBoxTable):
    name = tables.Column(linkify=True)
    processor = tables.Column(linkify=True)
    receiver_ip = tables.Column(linkify=True, verbose_name='Receiver IP-Adress')
    max_bandwidth_in = tables.Column(verbose_name='Max. Bandwidth (Mbps)')
    supported_formats = ManyToManyColumn()
    switch_method = ChoiceFieldColumn(verbose_name='Switch Method (2022-7)')
    signal_type = ChoiceFieldColumn(verbose_name='Signal Type')
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Receiver
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'processor', 'signal_type',  'receiver_ip', 'max_bandwidth_in',
                  'supported_formats', 'switch_method', 'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'processor', 'signal_type', 'receiver_ip', 'supported_formats', 'tags', 'description')


class StreamTable(NetBoxTable):
    name = tables.Column(linkify=True)
    processor = tables.Column()
    sender = tables.Column()
    receivers = tables.Column() # todo ändern
    bandwidth = tables.Column() #rechtschreibfehler überall
    format = tables.Column()
    signal_type = tables.Column()
    protocol = tables.Column()
    audio_channels = tables.Column()
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Stream
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'processor', 'sender', 'receivers', 'bandwidth', 'format', 'signal_type',
                  'protocol', 'audio_channels', 'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'signal_type', 'sender', 'receivers', 'description', 'tags')

