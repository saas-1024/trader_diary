from django.urls import path, re_path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('add_spot_deal/', add_spot_deal, name='add_spot_deal'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('spot_deals/<int:deal_id>', watch_spot_deals, name='watch_spot_deals'),
    path('spot_deals/edit/<int:deal_id>', edit_spot_deal, name='edit_spot_deal'),
    path('spot_deals/buys', spot_deals_buys, name='spot_deals_buys'),
    path('spot_deals/sells', spot_deals_sells, name='spot_deals_sells'),
]
