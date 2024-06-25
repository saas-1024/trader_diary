from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class SpotDeal(models.Model):
    date_deal = models.DateTimeField('Date deal', auto_now=True)
    asset_name = models.CharField('Криптовалюта', max_length=16)
    asset_price = models.DecimalField(default=0, max_digits=32, decimal_places=10)
    asset_amount = models.DecimalField(default=0, max_digits=32, decimal_places=10)
    usd_amount = models.DecimalField(default=0, max_digits=16, decimal_places=10)
    comission = models.DecimalField(default=0, max_digits=16, decimal_places=10)
    trade_side = models.CharField('Сторона сделки', max_length=4, default='buy')  # B - buy, S - sell
    comment = models.CharField('Комментарий сделки', max_length=128)
    exchange = models.CharField('Криптобиржа', max_length=64)
    user_deal = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='user_deals'
    )

    class Meta:
        ordering = ['-date_deal']

    def __str__(self):
        return f'{self.asset_name} ({self.pk})'

    def get_absolute_url(self):
        return reverse('watch_spot_deals', kwargs={'deal_id': self.pk})

    def edit_deal(self):  # TO DO: This function is still won't work
        print("Test function call")
        return reverse('edit_spot_deal', kwargs={'deal_id': self.pk})

    def save_deal(self):
        pass
