from django import forms


class UrlForm(forms.Form):
    to_be_scrapped = forms.URLField(
        required=True,
        widget=forms.URLInput(
            attrs={'placeholder': 'Insira o link da página aqui'}
        )
    )
