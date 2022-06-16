from django import forms

from ships import models


class ShipForm(forms.ModelForm):
    class Meta:
        model = models.Ship
        fields = "__all__"
