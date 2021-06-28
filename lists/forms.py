from django import forms
from django.forms import ModelForm

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(ModelForm):
    class Meta:
        model = Item

        fields = ('text',)

        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control input-lg',
            }),
        }

        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }

    def save(self, for_list):
        self.instance.list = for_list

        return super().save()
