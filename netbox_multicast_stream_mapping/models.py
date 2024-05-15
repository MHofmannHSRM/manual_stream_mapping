from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from utilities.choices import ChoiceSet
from netbox.models import NetBoxModel


# Choices --------------------------------------------------------------------------------------------------------------

# Choices for Endpoint Type -> Sender or Receiver?
class EndpointTypeChoices(ChoiceSet):
    key = 'Endpoint.endpoint_type'

    CHOICES = [
        ('sender', 'Sender', 'green'),
        ('receiver', 'Receiver', 'blue'),
    ]


# Choices for Signal Type of Endpoint
class SignalTypeChoices(ChoiceSet):
    key = 'Endpoint.signal_type'

    CHOICES = [
        ('video', 'Video', 'red'),
        ('audio', 'Audio', 'blue'),
        ('metadata', 'Metadata', 'yellow'),
    ]


# Choices for switch method (ST 2022-7)
class SwitchMethodChoices(ChoiceSet):
    key = 'Endpoint.switch_method'

    CHOICES = [
        ('sips_merge', 'SiPs Merge', 'red'),
        ('sips_split', 'SiPs Split', 'green'),
    ]


# Choices for Signal Type of Format Preset
class FormatTypeChoices(ChoiceSet):
    key = 'Format.type'

    CHOICES = [
        ('video', 'Video', 'red'),
        ('audio', 'Audio', 'blue'),
        ('metadata', 'Metadata', 'yellow'),
        ('ect', 'Ect.', 'green')
    ]


# choices for framerates in Format Presets
class FpsChoices(ChoiceSet):
    key = 'Format.fps'

    CHOICES = [
        ('i25', 'i25'), # todo framerate hinten als zahl, nicht fieldrate! -> nachschauen, wie korrekt?
        ('p25', 'p25'),
        ('i50', 'i50'),
        ('p50', 'p50'),
        ('i30', 'i30'),
        ('p30', 'p30'),
        ('i60', 'i60'), # TODO fractional? wie behandeln? korrekt! ansprechen! -> sollte auch rein!!
        ('p60', 'p60'), # todo HFR auch?
        # todo 100, 120
    ]


# Models ---------------------------------------------------------------------------------------------------------------

# model format presets -> are supported for endpoints
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

    def get_format_type_color(self):
        return FormatTypeChoices.colors.get(self.type) # todo


# model for internal processing units of devices -> has senders and receivers
class Processor(NetBoxModel): # todo device spalte anzahl an enpoints oder procs?
    name = models.CharField(max_length=100) # todo in tabellenansicht aus gerät auch device namen anzeigen?
    device = models.ForeignKey(to='dcim.Device', on_delete=models.CASCADE, related_name='+') # todo related_name='+' um keine beziehung rückwärst zu erstellen
    module = models.ForeignKey(to='dcim.Module', on_delete=models.CASCADE, related_name='+', null=True, blank=True) # todo logik -> modul muss zu device gehören
    description = models.CharField(max_length=500, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_multicast_stream_mapping:processor', args=[self.pk])


# model for internal processing units of devices -> has senders and receivers
class Endpoint(NetBoxModel):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(to='dcim.Device', on_delete=models.CASCADE, null=True, related_name='+') # todo related_name='+' um keine beziehung rückwärst zu erstellen
    processor = models.ForeignKey(to=Processor, on_delete=models.CASCADE)
    endpoint_type = models.CharField(choices=EndpointTypeChoices, null=True) # todo farben als plakette
    primary_ip = models.OneToOneField(to='ipam.IPAddress', on_delete=models.SET_NULL, related_name='+', blank=True, null=True) # todo gleiche ip mehrfach! oder range?
    secondary_ip = models.OneToOneField(to='ipam.IPAddress', on_delete=models.SET_NULL, related_name='+', blank=True, null=True)
    max_bandwidth = models.FloatField(null=True, blank=True)
    supported_formats = models.ManyToManyField(to=Format, blank=True) # todo filter basiert auf signal type?
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

    def get_signal_type_color(self):
        return SignalTypeChoices.colors.get(self.signal_type)


# model for internal processing units of devices -> has senders and receivers
class Stream(NetBoxModel):
    name = models.CharField(max_length=100)
    sender = models.ForeignKey(to=Endpoint, on_delete=models.CASCADE, related_name="sent_streams")
    receivers = models.ManyToManyField(to=Endpoint, related_name="received_streams")
    bandwidth = models.FloatField(null=True, blank=True)
    signal_type = models.CharField(choices=SignalTypeChoices, null=True, blank=True)
    protocol = models.CharField(max_length=100, blank=True)  # todo choice -> welche?
    formats = models.ManyToManyField(to=Format, blank=True)
    comments = models.TextField(blank=True)
    description = models.CharField(max_length=500, blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_multicast_stream_mapping:stream', args=[self.pk])
