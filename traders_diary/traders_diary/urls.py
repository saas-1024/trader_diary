from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from spot_deals.views import *
from spot_deals.urls import *

router = routers.SimpleRouter()
router.register(r'spot_deals', SpotDealsViewSet)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # port_number/api/spot_deals/{id}
    # path('api/spot_deals/<int:pk>', SpotDealsAPIView.as_view()),
    # path('api/spot_deals/<int:pk>', SpotDealCRUDView.as_view())
]
