from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField # TODO
from .models import Processor, Endpoint, Stream, Format
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

# TODO validierungen, widgets, ...


class ProcessorForm(NetBoxModelForm):

    class Meta:
        model = Processor
        fields = ('name', 'device', 'module', 'description', 'comments', 'tags')


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

    class Meta:
        model = Endpoint
        fields = ('name', 'processor', 'endpoint_type', 'primary_ip', 'secondary_ip', 'max_bandwidth', 'signal_type',
                  'supported_formats', 'switch_method', 'tags', 'description', 'comments')


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

    class Meta:
        model = Stream
        fields = ('name', 'processor', 'sender', 'receivers', 'bandwidth', 'format', 'signal_type',
                  'protocol', 'audio_channels', 'comments', 'description', 'tags') # todo updated?


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

    class Meta:
        model = Format
        fields = ('name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'comments', 'description', 'tags')




# TODO choicefields usw.
# class AccessListRuleForm(NetBoxModelForm):
#     access_list = DynamicModelChoiceField(
#         queryset=AccessList.objects.all()
#     )
#     source_prefix = DynamicModelChoiceField(
#         queryset=Prefix.objects.all()
#     )
#     destination_prefix = DynamicModelChoiceField(
#         queryset=Prefix.objects.all()
#     )

