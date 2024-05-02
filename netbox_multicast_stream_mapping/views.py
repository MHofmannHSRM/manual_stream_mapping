from netbox.views import generic

from utilities.views import ViewTab, register_model_view
from . import filtersets, forms, models, tables
from .models import Processor, Endpoint
from dcim.models import Device
from .tables import EndpointTable, ProcessorTable
from django.db.models import Count


# detail view
class ProcessorView(generic.ObjectView):
    queryset = models.Processor.objects.all()


# list view
class ProcessorListView(generic.ObjectListView):
    queryset = models.Processor.objects.annotate(endpoint_count=Count('endpoint'))# TODO
    table = tables.ProcessorTable
    filterset = filtersets.ProcessorFilterSet
    filterset_form = forms.ProcessorFilterForm


# edit view
class ProcessorEditView(generic.ObjectEditView):
    queryset = models.Processor.objects.all()
    form = forms.ProcessorForm


# delete view
class ProcessorDeleteView(generic.ObjectDeleteView):
    queryset = models.Processor.objects.all()

# ----------------------------------------------------------------------------------------------------------------------


# detail view
class EndpointView(generic.ObjectView):
    queryset = models.Endpoint.objects.all()


# list view
class EndpointListView(generic.ObjectListView):
    queryset = models.Endpoint.objects.all()
    table = tables.EndpointTable
    filterset = filtersets.EndpointFilterSet
    filterset_form = forms.EndpointFilterForm


# edit view
class EndpointEditView(generic.ObjectEditView):
    queryset = models.Endpoint.objects.all()
    form = forms.EndpointForm


# delete view
class EndpointDeleteView(generic.ObjectDeleteView):
    queryset = models.Endpoint.objects.all()


# ----------------------------------------------------------------------------------------------------------------------


# detail view
class StreamView(generic.ObjectView):
    queryset = models.Stream.objects.all()


# list view
class StreamListView(generic.ObjectListView):
    queryset = models.Stream.objects.all()
    # für logik
    # queryset = models.AccessList.objects.annotate(rule_count=Count('rules'))
    table = tables.StreamTable
    filterset = filtersets.StreamFilterSet
    filterset_form = forms.StreamFilterForm


# edit view
class StreamEditView(generic.ObjectEditView):
    queryset = models.Stream.objects.all()
    form = forms.StreamForm


# delete view
class StreamDeleteView(generic.ObjectDeleteView):
    queryset = models.Stream.objects.all()


# ----------------------------------------------------------------------------------------------------------------------


# detail view
class FormatView(generic.ObjectView):
    queryset = models.Format.objects.all()


# list view
class FormatListView(generic.ObjectListView):
    queryset = models.Format.objects.all()
    table = tables.FormatTable
    # filterset = filtersets.StreamFilterSet
    # filterset_form = forms.StreamFilterForm


# edit view
class FormatEditView(generic.ObjectEditView):
    queryset = models.Format.objects.all()
    form = forms.FormatForm


# delete view
class FormatDeleteView(generic.ObjectDeleteView):
    queryset = models.Format.objects.all()


# endpoint view for devices
# todo bobbel mit anzahl für gerät
@register_model_view(model=Device, name='Processors', path='processors')
class DeviceProcessorView(generic.ObjectChildrenView):
    queryset = Device.objects.all()
    child_model = Processor
    table = tables.ProcessorTable
    filterset = filtersets.ProcessorFilterSet
    template_name = 'netbox_multicast_stream_mapping/processor_list.html' # TODO
    # template_name = 'dcim/device_list.html' # TODO

    tab = ViewTab(
        label="Processors",
        weight=100,
        badge=lambda obj: Processor.objects.filter(device=obj).count(),
        # permission="netbox_dns.view_zone", # TODO
        # badge=lambda obj: len(obj.zones),
    )

    def get_children(self, request, instance):
        # hier logik
        return Processor.objects.filter(device=instance).annotate(endpoint_count=Count('endpoint'))



# class ProcessorEndpointView(generic.ObjectChildrenView):
#     queryset = Processor.objects.all()
#     child_model = Endpoint
#     table = tables.EndpointTable
#     filterset = filtersets.EndpointFilterSet
#     template_name = 'netbox_multicast_stream_mapping/processor_list.html' # TODO
#     # template_name = 'dcim/device_list.html' # TODO
#
#     def get_children(self, request, instance):
#         # hier logik
#         return Endpoint.objects.filter(device=instance)


@register_model_view(models.Processor, name='endpoints', path='endpoints')
class EndpointChildView(generic.ObjectChildrenView):
    queryset = models.Processor.objects.all().prefetch_related('endpoint_set')
    child_model = models.Endpoint
    table = tables.EndpointTable
    template_name = "netbox_multicast_stream_mapping/processor_list.html" # todo
    hide_if_empty = False
    tab = ViewTab(
        label='Endpunkte',
        badge=lambda obj: obj.endpoint_set.count(),
        permission='myplugin.view_endpoint'
    )

    def get_children(self, request, parent):
        return parent.endpoint_set.all()



# @register_model_view(model=Device, name='Endpoints', path='endpoints')
# class EndpointListView(generic.ObjectListView):
#     queryset = models.Sender.objects.all().union(models.Receiver.objects.all()) # todo
#     table = tables.SenderTable
#     filterset = filtersets.SenderFilterSet
#     filterset_form = forms.SenderFilterForm
#
#     # tab = ViewTab(
#     #     label="Stream Endpoints",
#     #     weight=100, )
#
#














    # def get_queryset(self):
    #     device_id = self.kwargs.get('device_id')
    #     if device_id:
    #         device = get_object_or_404(Device, pk=device_id)
    #         return device.processor.all()
    #     return Processor.objects.none()

    # def get_children(self, request, parent):
    #     return parent.get_child_ranges().restrict(request.user, 'view').prefetch_related('tenant__group', )

    # def get_children(self, request, parent):
    #     return Zone.objects.filter(
    #         Q(registrant=parent)
    #         | Q(admin_c=parent)
    #         | Q(tech_c=parent)
    #         | Q(billing_c=parent)
    #     )

    # def get_extra_context(self, request, instance):


# TODO URL
# @register_model_view(model=Processor, name='Endpoints', path='some-other-stuff')
# class EndpointView(generic.ObjectView):
# # class EndpointView(generic.ObjectChildrenView):
#
#     # queryset = models.SystemTemplate.objects.all()
#     # child_model = models.System
#     # table = tables.SystemTable
#     # template_name = 'generic/object_children.html'
#
#     tab = ViewTab(
#         label='Endpoints',
#         # badge=lambda obj: Stuff.objects.filter(site=obj).count(), # TODO
#         # badge='0',
#         # weight =
#         # permission='myplugin.view_stuff'
#     )
#
#     # def get_children(self, request, parent):
#     #     return self.child_model.objects.filter(system_template=parent)
#
#     def get(self, request, pk):
#         # TODO
#         return render(request, "myplugin/mytabview.html", context={"tab": self.tab, }, )


# TODO urls path('system-templates/<int:pk>/systems', views.SystemTemplateSystemsView.as_view(), name='systemtemplate_systems')



