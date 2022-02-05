from typing import TextIO
from django import forms
from .models import Plant, Shop
from django.forms import ModelForm, TextInput


class PlantAdd(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ["description", "image", "species", "shop"]
        labels = {"description": "Description", "image": "Image", "species": "Species"}
        widgets = {
            "species": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 500px; margin: 20px;",
                    "placeholder": "Name",
                }
            ),
            "description": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 500px; margin: 20px;",
                    "placeholder": "Description",
                }
            ),
            "image": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 500px; margin: 20px;",
                    "placeholder": "Image url",
                }
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     shop = Shop.objects.first()
    #     self.fields["shop_id"] = shop.id
