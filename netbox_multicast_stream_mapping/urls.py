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
    path('processors/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='processor_changelog',
         kwargs={'model': models.Processor}),


    # MulticastSender
    path('senders/', views.SenderListView.as_view(), name='sender_list'),
    path('senders/add/', views.SenderEditView.as_view(), name='sender_add'),
    path('senders/<int:pk>/', views.SenderView.as_view(), name='sender'),
    path('senders/<int:pk>/edit/', views.SenderEditView.as_view(), name='sender_edit'),
    path('senders/<int:pk>/delete/', views.SenderDeleteView.as_view(), name='sender_delete'),
    path('senders/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sender_changelog',
         kwargs={'model': models.Sender}),

    # MulticastReceiver
    path('receivers/', views.ReceiverListView.as_view(), name='receiver_list'),
    path('receivers/add/', views.ReceiverEditView.as_view(), name='receiver_add'),
    path('receivers/<int:pk>/', views.ReceiverView.as_view(), name='receiver'),
    path('receivers/<int:pk>/edit/', views.ReceiverEditView.as_view(), name='receiver_edit'),
    path('receivers/<int:pk>/delete/', views.ReceiverDeleteView.as_view(), name='receiver_delete'),
    path('receivers/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='receiver_changelog',
         kwargs={'model': models.Receiver}),

    # MulticastStream
    path('streams/', views.StreamListView.as_view(), name='stream_list'),
    path('streams/add/', views.StreamEditView.as_view(), name='stream_add'),
    path('streams/<int:pk>/', views.StreamView.as_view(), name='stream'),
    path('streams/<int:pk>/edit/', views.StreamEditView.as_view(), name='stream_edit'),
    path('streams/<int:pk>/delete/', views.StreamDeleteView.as_view(), name='stream_delete'),
    path('streams/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='stream_changelog',
         kwargs={'model': models.Stream}),
)
