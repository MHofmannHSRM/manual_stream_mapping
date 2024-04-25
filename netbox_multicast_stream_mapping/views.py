from netbox.views import generic
from . import filtersets, forms, models, tables


# detail view
class ProcessorView(generic.ObjectView):
    queryset = models.Processor.objects.all()


# list view
class ProcessorListView(generic.ObjectListView):
    queryset = models.Processor.objects.all()
    # für logik
    # queryset = models.AccessList.objects.annotate(rule_count=Count('rules'))
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
class SenderView(generic.ObjectView):
    queryset = models.Sender.objects.all()


# list view
class SenderListView(generic.ObjectListView):
    queryset = models.Sender.objects.all()
    # für logik
    # queryset = models.AccessList.objects.annotate(rule_count=Count('rules'))
    table = tables.SenderTable
    filterset = filtersets.SenderFilterSet
    filterset_form = forms.SenderFilterForm


# edit view
class SenderEditView(generic.ObjectEditView):
    queryset = models.Sender.objects.all()
    form = forms.SenderForm


# delete view
class SenderDeleteView(generic.ObjectDeleteView):
    queryset = models.Sender.objects.all()


# ----------------------------------------------------------------------------------------------------------------------


# detail view
class ReceiverView(generic.ObjectView):
    queryset = models.Receiver.objects.all()


# list view
class ReceiverListView(generic.ObjectListView):
    queryset = models.Receiver.objects.all()
    # für logik
    # queryset = models.AccessList.objects.annotate(rule_count=Count('rules'))
    table = tables.ReceiverTable
    filterset = filtersets.ReceiverFilterSet
    filterset_form = forms.ReceiverFilterForm


# edit view
class ReceiverEditView(generic.ObjectEditView):
    queryset = models.Receiver.objects.all()
    form = forms.ReceiverForm


# delete view
class ReceiverDeleteView(generic.ObjectDeleteView):
    queryset = models.Receiver.objects.all()

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
