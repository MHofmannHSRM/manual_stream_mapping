from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse
from utilities.choices import ChoiceSet


class SignalTypeChoices(ChoiceSet):
    key = 'Endpoint.signal_type'  # todo anderer key -> allgemeiner?

    CHOICES = [
        ('video', 'Video', 'red'),
        ('audio', 'Audio', 'blue'),
        ('metadata', 'Metadata', 'yellow'),
    ]


class SwitchMethodChoices(ChoiceSet):
    key = 'Endpoint.switch_method'  # todo anderer key -> allgemeiner?

    CHOICES = [
        ('sips_merge', 'SiPs Merge', 'red'),
        ('sips_split', 'SiPs Split', 'green'),
    ]


class FormatTypeChoices(ChoiceSet):
    key = 'Format.type'  # todo anderer key -> allgemeiner?

    CHOICES = [
        ('audio', 'Audio', 'red'),
        ('video', 'Video', 'blue'),
        ('metadata', 'Metadata', 'yellow'),
        ('ect', 'Ect.', 'green')
    ]


class FpsChoices(ChoiceSet):
    key = 'Format.fps'  # todo anderer key -> allgemeiner?

    CHOICES = [
        ('i25', 'i25'),
        ('p25', 'p25'),
        ('i50', 'i50'),
        ('p50', 'p50'),
        ('i30', 'i30'),
        ('p30', 'p30'),
        ('i60', 'i60'),
        ('p60', 'p60'),
    ]


# model for internal processing units of devices -> has senders and receivers
class Format(NetBoxModel):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=FormatTypeChoices, null=True, blank=True)
    res_h = models.PositiveIntegerField(null=True, blank=True)
    res_w = models.PositiveIntegerField(null=True, blank=True)
    fps = models.CharField(choices=FpsChoices, null=True, blank=True)
    audio_ch = models.PositiveIntegerField(null=True, blank=True)
    comments = models.TextField(blank=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_multicast_stream_mapping:format', args=[self.pk])


# model for internal processing units of devices -> has senders and receivers
class Processor(NetBoxModel):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(to='dcim.Device', on_delete=models.CASCADE, related_name='+') # todo related_name='+' um keine beziehung rückwärst zu erstellen
    module = models.ForeignKey(to='dcim.Module', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    sender_count = models.PositiveIntegerField(default=0, null=True, blank=True) # todo logik zähler
    receiver_count = models.PositiveIntegerField(default=0, null=True, blank=True) # liste -> darin verlinkung
    description = models.CharField(max_length=500, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    # TODO NMOS? -> Port?
    # TODO Journal?

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_multicast_stream_mapping:processor', args=[self.pk])


# model for internal processing units of devices -> has senders and receivers
class Endpoint(NetBoxModel):
    name = models.CharField(max_length=100)
    processor = models.ForeignKey(to=Processor, on_delete=models.CASCADE) # todo löschmodus?
    ip = models.OneToOneField(to='ipam.IPAddress', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    max_bandwidth = models.FloatField(null=True, blank=True)
    supported_formats = models.ManyToManyField(to=Format, blank=True)
    switch_method = models.CharField(choices=SwitchMethodChoices, null=True, blank=True)
    signal_type = models.CharField(choices=SignalTypeChoices, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("name",)
        # todo unique_together = ('access_list', 'index') ?

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_multicast_stream_mapping:endpoint', args=[self.pk])

    # todo farben klappen nicht
    def get_signal_type_color(self):
        return SignalTypeChoices.colors.get(self.signal_type)

    # todo switch method


# model for internal processing units of devices -> has senders and receivers
class Stream(NetBoxModel):
    name = models.CharField(max_length=100)
    processor = models.PositiveIntegerField(default=0) #  todo pflicht
    sender = models.CharField(max_length=12, default='???')
    receivers = models.CharField(max_length=12, default='???') # todo plural
    bandwidth = models.CharField()
    signal_type = models.CharField() # todo choice: Audio, Video, ANC, Mix???
    protocol = models.CharField() # todo choice
    format = models.CharField() # todo choice
    audio_channels = models.CharField() # todo choice
    comments = models.TextField(blank=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_multicast_stream_mapping:stream', args=[self.pk])




# # model for multicast sender inside processor -> only one per stream!
# class MulticastSender(NetBoxModel):
#     name = models.CharField(max_length=100)
#
#     default_action = models.CharField(max_length=30)
#
#     comments = models.TextField(blank=True)
#
#     # mapping to foreign key: related parent model, action, attribute in related model
#     # action: when deleting sender (CASCADE -> alle darunter löschen; PROTECT -> nicht löschen, wenn sender existieren
#     #-> TODO vllt. bei streams?)
#     processor = models.ForeignKey(to=Processor, on_delete=models.CASCADE, related_name='senders')
#
#     # index -> order in list todo
#     index = models.PositiveIntegerField()
#
#     # optional -> blank = true TODO char array field
#     # formats = models.CharField(max_length=50, blank=True)
#     formats = ArrayField(base_field=models.CharField(), blank=True, null=True)
#
#     # todo -> choice set
#     # action = models.CharField(max_length=30)
#     description = models.CharField(max_length=500, blank=True)
#
#     # alphabetical ordering for model instances
#     class Meta:
#         ordering = ("name",)
#         # todo
#         # ordering = ('access_list', 'index')
#         # unique_together = ('access_list', 'index')
#
#     # method to control, how model is converted into string
#     def __str__(self):
#         return self.name
