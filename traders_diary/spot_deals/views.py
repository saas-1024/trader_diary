from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser, User

from .models import SpotDeal
from .serializers import SpotDealSerializer

# menu = ["О сервисе", "Добавить сделку", "Техподдержка", "Логин"]
menu = [
    {'title': 'О сервисе', 'url_name': 'about'},
    {'title': 'Добавить сделку', 'url_name': 'add_spot_deal'},
    {'title': 'Техподдержка', 'url_name': 'contact'},
    {'title': 'Логин', 'url_name': 'login'},
    ]


def index(request):  # Display all spot deals on main page ordered by date of deal
    spot_deals = SpotDeal.objects.all()
    context = {
        'deals': spot_deals,  # deals передается в темплейт
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'spot_deals/index.html', context=context)


def about(request):
    return render(request, 'spot_deals/about.html', {'menu': menu, 'title': 'О сервисе'})


def add_spot_deal(request):  # User page to add new spot deal

    # print(deal_to_watch)
    context = {
        # 'deals': deal_to_watch,
        'menu': menu,
        'title': 'Добавление сделки'
    }
    return render(request, 'spot_deals/deal_to_add.html', context=context)


def watch_spot_deals(request, deal_id):  # Display the chosen spot deal
    deal_to_watch = SpotDeal.objects.filter(pk=deal_id)
    # print(deal_to_watch)
    context = {
        'deals': deal_to_watch,
        'menu': menu,
        'title': 'Просмотр сделки'
    }
    return render(request, 'spot_deals/deal_to_watch.html', context=context)
    # return HttpResponse(f"Просмотр спотовых сделок с id = {deal_id}")


def spot_deals_buys(request):  # All BUYS orders
    spot_deals_buys_list = SpotDeal.objects.filter(trade_side="buy")
    context = {
        'deals': spot_deals_buys_list,
        'menu': menu,
        'title': 'Спотовые покупки'
    }
    return render(request, 'spot_deals/spot_buys.html', context=context)


def spot_deals_sells(request):  # All SELL orders
    spot_deals_sells_list = SpotDeal.objects.filter(trade_side="sell")
    context = {
        'deals': spot_deals_sells_list,
        'menu': menu,
        'title': 'Спотовые продажи'
    }
    return render(request, 'spot_deals/spot_sells.html', context=context)


def edit_spot_deal(request, deal_id):  # EDIT chosen deal
    spot_deal_edit = SpotDeal.objects.filter(pk=deal_id)
    context = {
        'deals': spot_deal_edit,
        'menu': menu,
        'title': 'Редактирование сделки'
    }
    return render(request, 'spot_deals/edit_spot_deal.html', context=context)
    # return HttpResponse("Редактирование спотовой сделки")


def contact(request):  # Technical support contacts
    return HttpResponse("Техподдержка")


def login(request):  # Authorization page
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class SpotDealsViewSet(viewsets.ModelViewSet):
    queryset = SpotDeal.objects.all()
    serializer_class = SpotDealSerializer

