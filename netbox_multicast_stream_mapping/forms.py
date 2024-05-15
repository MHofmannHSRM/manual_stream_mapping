from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
from utilities.forms import add_blank_choice
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import *
from dcim.models import Device, Module
from ipam.models import IPAddress # todo korrekt oder range?


# Format ---------------------------------------------------------------------------------------------------------------

class FormatForm(NetBoxModelForm):
    comments = CommentField()

    fieldsets = (
        ('Format', ('name', 'type', 'description')),
        ('Technical Parameter', ('res_h', 'res_w', 'fps', 'audio_ch')),
        ('Tags', ('tags',)),
    )

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

    name = forms.CharField(required=False)
    type = forms.ChoiceField(choices=add_blank_choice(FormatTypeChoices), required=False)
    res_h = forms.IntegerField(label='Vertical Resolution', required=False, min_value=0)
    res_w = forms.IntegerField(label='Horizontal Resolution', required=False, min_value=0)
    fps = forms.ChoiceField(label='Frame Rate', choices=add_blank_choice(FpsChoices), required=False)
    audio_ch = forms.IntegerField(label='Number of Audio Channels', required=False, min_value=0)
    description = forms.CharField(required=False)


class FormatBulkEditForm(NetBoxModelBulkEditForm):
    model = Format

    name = forms.CharField(required=False)
    type = forms.ChoiceField(choices=add_blank_choice(FormatTypeChoices), required=False)
    res_h = forms.IntegerField(label='Vertical Resolution', required=False, min_value=0)
    res_w = forms.IntegerField(label='Horizontal Resolution', required=False, min_value=0)
    fps = forms.ChoiceField(label='Frame Rate', choices=add_blank_choice(FpsChoices), required=False)
    audio_ch = forms.IntegerField(label='Number of Audio Channels', required=False, min_value=0)
    description = forms.CharField(required=False)
    comments = CommentField(required=False)

    fieldsets = (
        ('Format', ('name', 'type', 'description')),
        ('Technical Parameter', ('res_h', 'res_w', 'fps', 'audio_ch')),
    )

    nullable_fields = ('description', 'comments')


# Processor ------------------------------------------------------------------------------------------------------------

class ProcessorForm(NetBoxModelForm):
    comments = CommentField()

    fieldsets = (
        ('Processor', ('name', 'device', 'module', 'description')),
        ('Tags', ('tags',)),
    )

    class Meta:
        model = Processor

        fields = ('name', 'device', 'module', 'description', 'tags', 'comments')


class ProcessorFilterForm(NetBoxModelFilterSetForm):
    model = Processor

    name = forms.CharField(required=False) # todo muss eindeutig
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    module = DynamicModelChoiceField(queryset=Module.objects.all(), required=False)
    description = forms.CharField(required=False)


class ProcessorBulkEditForm(NetBoxModelBulkEditForm):
    model = Processor

    # todo felder anpassen
    name = forms.CharField(required=False) # todo muss eindeutig
    description = forms.CharField(required=False)
    comments = CommentField(required=False)
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    module = DynamicModelChoiceField(queryset=Module.objects.all(), required=False)

    fieldsets = (
        ('Processor', ('name', 'device', 'module', 'description')),
    )

    nullable_fields = ('description', 'comments')


# Endpoint -------------------------------------------------------------------------------------------------------------

class EndpointForm(NetBoxModelForm): # todo verbose?
    # site = DynamicModelChoiceField(queryset=Site.objects.all())
    comments = CommentField()

    fieldsets = (
        ('Endpoint', ('name', 'device', 'processor', 'description')),
        ('Technical Parameters', ('endpoint_type', 'supported_formats', 'signal_type', 'switch_method')),
        ('Network Parameters', ('primary_ip', 'secondary_ip', 'max_bandwidth')),
        ('Tags', ('tags',)),
    )

    class Meta:
        model = Endpoint

        fields = ('name', 'device', 'processor', 'endpoint_type', 'signal_type', 'primary_ip', 'secondary_ip',
                  'max_bandwidth', 'supported_formats', 'switch_method', 'description',  'tags', 'comments')

        labels = {
            'primary_ip': 'Primary IP Address',
            'secondary_ip': 'Secondary IP Address',
            'max_bandwidth': 'Max. Bandwidth (Mbps)',
            'signal_type': 'Signal Type',
            'switch_method': 'Switch Method (2022-7)',
        }


class EndpointFilterForm(NetBoxModelFilterSetForm):
    model = Endpoint

    name = forms.CharField(required=False)  # todo muss eindeutig
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    processor = DynamicModelChoiceField(queryset=Processor.objects.all(), required=False)
    endpoint_type = forms.ChoiceField(label='Endpoint Type', choices=add_blank_choice(EndpointTypeChoices), required=False)
    primary_ip = DynamicModelChoiceField(label='Primary IP Address', queryset=IPAddress.objects.all(), required=False)
    secondary_ip = DynamicModelChoiceField(label='Secondary IP Address', queryset=IPAddress.objects.all(), required=False)
    max_bandwidth = forms.FloatField(label='Max. Bandwidth (Mbps)', required=False)
    # supported_formats = todo
    switch_method = forms.ChoiceField(label='Switch Method (2022-7)', choices=add_blank_choice(SwitchMethodChoices), required=False)
    signal_type = forms.ChoiceField(label='Signal Type', choices=add_blank_choice(SignalTypeChoices), required=False)
    description = forms.CharField(required=False)

    # access_list = forms.ModelMultipleChoiceField( TODO -> für sender/receiver
    #     queryset=AccessList.objects.all(),
    #     required=False
    # )
    #
    # index = forms.IntegerField(
    #     required=False
    # )


class EndpointBulkEditForm(NetBoxModelBulkEditForm):
    model = Endpoint

    # todo felder anpassen -> feiheiten, konsistenz reihenfolge/gliederung?
    name = forms.CharField(required=False)  # todo muss eindeutig
    device = DynamicModelChoiceField(queryset=Device.objects.all(), required=False)
    processor = DynamicModelChoiceField(queryset=Processor.objects.all(), required=False)
    endpoint_type = forms.ChoiceField(label='Endpoint Type', choices=add_blank_choice(EndpointTypeChoices), required=False)
    primary_ip = DynamicModelChoiceField(label='Primary IP Address', queryset=IPAddress.objects.all(), required=False)
    secondary_ip = DynamicModelChoiceField(label='Secondary IP Address', queryset=IPAddress.objects.all(), required=False)
    max_bandwidth = forms.FloatField(label='Max. Bandwidth (Mbps)', required=False)
    supported_formats = forms.CharField(required=False) # todo
    switch_method = forms.ChoiceField(label='Switch Method (2022-7)', choices=add_blank_choice(SwitchMethodChoices), required=False)
    signal_type = forms.ChoiceField(label='Signal Type', choices=add_blank_choice(SignalTypeChoices), required=False)
    description = forms.CharField(required=False)
    comments = CommentField(required=False)

    fieldsets = (
        ('Endpoint', ('name', 'device', 'processor', 'description')),
        ('Technical Parameters', ('endpoint_type', 'supported_formats', 'signal_type', 'switch_method')),
        ('Network Parameters', ('primary_ip', 'secondary_ip', 'max_bandwidth')),
    )

    nullable_fields = ('description', 'comments')


# Stream/Flow ----------------------------------------------------------------------------------------------------------

class StreamForm(NetBoxModelForm):
    comments = CommentField()

    fieldsets = (
        ('Stream', ('name', 'sender', 'receivers', 'description')),
        ('Technical Parameters', ('bandwidth', 'signal_type', 'protocol', 'supported_formats')),
        ('Tags', ('tags',)),
    )

    class Meta:
        model = Stream
        fields = ('name', 'sender', 'receivers', 'bandwidth', 'signal_type', 'protocol', 'formats', 'description',
                  'tags', 'comments')


class StreamFilterForm(NetBoxModelFilterSetForm):
    model = Stream


class StreamBulkEditForm(NetBoxModelBulkEditForm):
    # todo felder anpassen -> feiheiten, konsistenz reihenfolge/gliederung?
    model = Stream

    name = forms.CharField(required=False)
    sender = DynamicModelChoiceField(queryset=Endpoint.objects.all(), required=False)
    receivers = DynamicModelChoiceField(queryset=Endpoint.objects.all(), required=False)
    bandwidth = forms.FloatField(label='Max. Bandwidth (Mbps)', required=False)
    signal_type = forms.ChoiceField(label='Signal Type', choices=add_blank_choice(SignalTypeChoices), required=False)
    protocol = forms.CharField(required=False)
    supported_formats = forms.CharField(required=False) # todo
    description = forms.CharField(required=False)
    comments = CommentField(required=False)

    fieldsets = (
        ('Stream', ('name', 'sender', 'receivers', 'description')),
        ('Technical Parameters', ('bandwidth', 'signal_type', 'protocol', 'supported_formats')),
    )

    nullable_fields = ('description', 'comments')
