from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_multicast_stream_mapping'


router = NetBoxRouter()
router.register('processors', views.ProcessorViewSet)
router.register('senders', views.SenderViewSet)
router.register('receivers', views.ReceiverViewSet)
router.register('streams', views.StreamViewSet)
router.register('formats', views.FormatViewSet)


urlpatterns = router.urls

# TODO base_URL -> Einheitlich!
