from django import forms


class WeatherSearch(forms.Form):
    start_city = forms.CharField()
    start_country = forms.CharField()
    end_city = forms.CharField()
    end_country = forms.CharField()

