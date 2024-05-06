from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    # Processor
    path('processors/', views.ProcessorListView.as_view(), name='processor_list'),
    path('processors/add/', views.ProcessorEditView.as_view(), name='processor_add'),
    path('processors/<int:pk>/', views.ProcessorView.as_view(), name='processor'),
    path('processors/<int:pk>/edit/', views.ProcessorEditView.as_view(), name='processor_edit'),
    path('processors/<int:pk>/delete/', views.ProcessorDeleteView.as_view(), name='processor_delete'),
    path("processors/<int:pk>/endpoints/", views.EndpointChildView.as_view(), name="endpoint_children"), # todo andere überschrift in dieser ansicht
    path('processors/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='processor_changelog',
         kwargs={'model': models.Processor}),
    path('processors/delete/', views.ProcessorBulkDeleteView.as_view(), name='processor_bulk_delete'),

    # MulticastSender
    path('endpoints/', views.EndpointListView.as_view(), name='endpoint_list'),
    path('endpoints/add/', views.EndpointEditView.as_view(), name='endpoint_add'),
    path('endpoints/<int:pk>/', views.EndpointView.as_view(), name='endpoint'),
    path('endpoints/<int:pk>/edit/', views.EndpointEditView.as_view(), name='endpoint_edit'),
    path('endpoints/<int:pk>/delete/', views.EndpointDeleteView.as_view(), name='endpoint_delete'),
    path('endpoints/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='endpoint_changelog',
         kwargs={'model': models.Endpoint}),
    path('endpoints/delete/', views.EndpointBulkDeleteView.as_view(), name='endpoint_bulk_delete'),

    # MulticastStream
    path('streams/', views.StreamListView.as_view(), name='stream_list'),
    path('streams/add/', views.StreamEditView.as_view(), name='stream_add'),
    path('streams/<int:pk>/', views.StreamView.as_view(), name='stream'),
    path('streams/<int:pk>/edit/', views.StreamEditView.as_view(), name='stream_edit'),
    path('streams/<int:pk>/delete/', views.StreamDeleteView.as_view(), name='stream_delete'),
    path('streams/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='stream_changelog',
         kwargs={'model': models.Stream}),

    # Format Tags
    path('formats/', views.FormatListView.as_view(), name='format_list'),
    path('formats/add/', views.FormatEditView.as_view(), name='format_add'),
    path('formats/<int:pk>/', views.FormatView.as_view(), name='format'),
    path('formats/<int:pk>/edit/', views.FormatEditView.as_view(), name='format_edit'),
    path('formats/<int:pk>/delete/', views.FormatDeleteView.as_view(), name='format_delete'),
    path('formats/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='format_changelog',
         kwargs={'model': models.Format}),

    # tab device processor
    path("devices/<int:pk>/processors/", views.DeviceProcessorView.as_view(), name="device_processors"),

)
