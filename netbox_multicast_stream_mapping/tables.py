import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn, TagColumn

from .models import Processor, Sender, Receiver, Stream


class ProcessorTable(NetBoxTable):
    name = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    module = tables.Column(linkify=True)
    sender_count = tables.Column() # todo counter cache field
    receiver_count = tables.Column() # todo counter cache field
    description = tables.Column()
    comments = tables.Column()
    tags = TagColumn() # TODO -> Verlinkung -> Filter?
    # tags = TagColumn(url_name='tag')

    class Meta(NetBoxTable.Meta):
        model = Processor
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'device', 'module', 'sender_count', 'receiver_count', 'description', 'comments',
                  'tags') # todo updated?
        default_columns = ('name', 'device', 'module', 'sender_count', 'receiver_count', 'description', 'tags')


class SenderTable(NetBoxTable):
    name = tables.Column(linkify=True)
    processor = tables.Column(linkify=True)
    sender_ip = tables.Column()
    max_bandwidth_out = tables.Column(verbose_name='Max. Bandwidth (Mbps)')
    supported_formats = tables.Column()
    signal_type = tables.Column()
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Sender
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'processor', 'sender_ip', 'max_bandwidth_out',
                  'supported_formats', 'signal_type', 'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'processor', 'sender_ip', 'supported_formats', 'description', 'tags')


class ReceiverTable(NetBoxTable):
    name = tables.Column(linkify=True)
    processor = tables.Column(linkify=True)
    receiver_ip = tables.Column()
    receiver_port = tables.Column()
    max_bandwidth_in = tables.Column()
    supported_formats = tables.Column()
    signal_type = tables.Column()
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Receiver
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'processor', 'receiver_ip', 'max_bandwidth_in',
                  'supported_formats', 'signal_type', 'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'processor', 'receiver_ip', 'supported_formats', 'description', 'tags')


class StreamTable(NetBoxTable):
    name = tables.Column(linkify=True)
    processor = tables.Column()
    sender = tables.Column()
    receivers = tables.Column()
    bandwidth = tables.Column() #rechtschreibfehler überall
    format = tables.Column()
    signal_type = tables.Column()
    protocol = tables.Column()
    audio_channels = tables.Column()
    comments = tables.Column()
    description = tables.Column()
    tags = TagColumn()  # TODO -> Verlinkung -> Filter?

    class Meta(NetBoxTable.Meta):
        model = Receiver
        # template_name = 'utilities/tables/netbox_table.html' TODO
        fields = ('pk', 'id', 'name', 'processor', 'sender', 'receivers', 'bandwidth', 'format', 'signal_type',
                  'protocol', 'audio_channels', 'comments', 'description', 'tags') # todo updated?
        default_columns = ('name', 'signal_type', 'sender', 'receivers', 'description', 'tags')
