from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField # TODO
from .models import Processor, Endpoint, Stream, Format
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

# TODO validierungen, widgets, ...


class ProcessorForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = Processor
        fields = ('name', 'device', 'module', 'description', 'tags', 'comments')


class ProcessorFilterForm(NetBoxModelFilterSetForm):
    model = Processor

    # access_list = forms.ModelMultipleChoiceField( TODO -> für sender/receiver
    #     queryset=AccessList.objects.all(),
    #     required=False
    # )
    #
    # index = forms.IntegerField(
    #     required=False
    # )


class EndpointForm(NetBoxModelForm): # todo verbose?
    # site = DynamicModelChoiceField(queryset=Site.objects.all())
    comments = CommentField()
    # fieldsets = ( # todo fieldsets?
    #     ('Model Stuff', ('name', 'status', 'site', 'tags')),
    #     ('Tenancy', ('tenant_group', 'tenant')),
    # )

    class Meta:
        model = Endpoint
        fields = ('name', 'processor', 'endpoint_type', 'signal_type', 'primary_ip', 'secondary_ip', 'max_bandwidth',
                  'supported_formats', 'switch_method', 'description',  'tags', 'comments')
        labels = {
            'primary_ip': 'Primary IP Address',
            'secondary_ip': 'Secondary IP Address',
            'max_bandwidth': 'Max. Bandwidth (Mbps)',
            'signal_type': 'Signal Type',
            'switch_method': 'Switch Method (2022-7)',
        }


class EndpointFilterForm(NetBoxModelFilterSetForm):
    model = Endpoint

    # access_list = forms.ModelMultipleChoiceField( TODO -> für sender/receiver
    #     queryset=AccessList.objects.all(),
    #     required=False
    # )
    #
    # index = forms.IntegerField(
    #     required=False
    # )


class StreamForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = Stream
        fields = ('name', 'sender', 'receivers', 'bandwidth', 'signal_type', 'protocol', 'formats', 'description',
                  'tags', 'comments')


class StreamFilterForm(NetBoxModelFilterSetForm):
    model = Stream

    # access_list = forms.ModelMultipleChoiceField( TODO -> für sender/receiver
    #     queryset=AccessList.objects.all(),
    #     required=False
    # )
    #
    # index = forms.IntegerField(
    #     required=False
    # )


class FormatForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = Format
        fields = ('name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'description', 'tags', 'comments')
        labels = {
            'res_h': 'Vertical Resolution',
            'res_w': 'Horizontal Resolution',
            'fps': 'Frame Rate',
            'audio_ch': 'Number of Audio Channels',
        }
