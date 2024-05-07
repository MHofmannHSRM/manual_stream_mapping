from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import *
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
from dcim.models import Device, Module
from ipam.models import IPAddress # todo korrekt oder range?
from utilities.forms import add_blank_choice


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


class ProcessorBulkEditForm(NetBoxModelBulkEditForm):
    # todo felder anpassen
    name = forms.CharField(required=False) # todo muss eindeutig
    description = forms.CharField(required=False)
    comments = CommentField(required=False)
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    module = DynamicModelChoiceField(queryset=Module.objects.all(), required=False)

    model = Processor
    # fieldsets = ((None, ('name')),)
    # nullable_fields = ()


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


class EndpointBulkEditForm(NetBoxModelBulkEditForm):
    # todo felder anpassen -> feiheiten, konsistenz reihenfolge/gliederung?
    name = forms.CharField(required=False)  # todo muss eindeutig
    processor = DynamicModelChoiceField(queryset=Processor.objects.all(), required=False)
    endpoint_type = forms.ChoiceField(choices=add_blank_choice(EndpointTypeChoices), required=False)
    primary_ip = DynamicModelChoiceField(queryset=IPAddress.objects.all(), required=False)
    secondary_ip = DynamicModelChoiceField(queryset=IPAddress.objects.all(), required=False)
    max_bandwidth = forms.FloatField(required=False)
    # supported_formats = todo
    switch_method = forms.ChoiceField(choices=add_blank_choice(SwitchMethodChoices), required=False)
    signal_type = forms.ChoiceField(choices=add_blank_choice(SignalTypeChoices), required=False)
    description = forms.CharField(required=False)
    comments = CommentField(required=False)

    model = Endpoint
    # fieldsets = ((None, ('name')),)
    # nullable_fields = ()


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


class StreamBulkEditForm(NetBoxModelBulkEditForm):
    # todo felder anpassen -> feiheiten, konsistenz reihenfolge/gliederung?
    model = Stream
    # fieldsets = ((None, ('name')),)
    # nullable_fields = ()



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

class FormatFilterForm(NetBoxModelFilterSetForm):
    model = Format
# todo filter


class FormatBulkEditForm(NetBoxModelBulkEditForm):
    # todo felder anpassen -> feiheiten, konsistenz reihenfolge/gliederung?
    model = Format
    # fieldsets = ((None, ('name')),)
    # nullable_fields = ()
