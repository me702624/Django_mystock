from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10)  # Fixed the typo in 'max_length'

    def __str__(self):  # Corrected the method name and added proper indentation
        return self.ticker
