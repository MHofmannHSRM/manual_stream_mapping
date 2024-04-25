from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField # TODO
from .models import Processor, Sender, Receiver, Stream, Format
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

# TODO validierungen, widgets, ...


class ProcessorForm(NetBoxModelForm):

    class Meta:
        model = Processor
        fields = ('name', 'device', 'module', 'sender_count', 'receiver_count', 'description', 'comments', 'tags')


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


class SenderForm(NetBoxModelForm):

    class Meta:
        model = Sender
        fields = ('name', 'processor', 'sender_ip', 'signal_type', 'supported_formats', 'switch_method',
                  'max_bandwidth_out', 'tags', 'description', 'comments')


class SenderFilterForm(NetBoxModelFilterSetForm):
    model = Sender

    # access_list = forms.ModelMultipleChoiceField( TODO -> für sender/receiver
    #     queryset=AccessList.objects.all(),
    #     required=False
    # )
    #
    # index = forms.IntegerField(
    #     required=False
    # )


class ReceiverForm(NetBoxModelForm):

    class Meta:
        model = Receiver
        fields = ('name', 'processor', 'receiver_ip', 'signal_type', 'supported_formats', 'switch_method',
                  'max_bandwidth_in', 'tags', 'description', 'comments')


class ReceiverFilterForm(NetBoxModelFilterSetForm):
    model = Receiver

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

