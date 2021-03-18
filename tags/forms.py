from django import forms
from tags.models import Tag


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'info', 'related_tags')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'create-tag-name-input form-control'}),
            'info': forms.Textarea(attrs={'class': 'create-tag-info-input form-control',
                                          'rows': '4'}),
            'related_tags': forms.SelectMultiple(attrs={'class': 'create-tag-related-input',
                                                        'id': 'id_tags', 'hidden': True})
        }
