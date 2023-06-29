from django import forms


class BalanceAdditionForm(forms.Form):
    amount = forms.FloatField(label='Amount')


class CurrencyForm(forms.Form):
    currency = forms.ChoiceField(choices=[('euro-to-leva', 'Convert Euro to Leva'),
                                          ('leva-to-euro', 'Convert Leva to Euro'),
                                          ('euro-to-pound', 'Convert Euro to Pound'),
                                          ('pound-to-euro', 'Convert Pound to Euro'),
                                          ('leva-to-pound', 'Convert Leva to Pound'),
                                          ('pound-to-leva', 'Convert Pound to Leva'),
                                          ('dollars-to-euro', 'Convert Dollars to Euro'),
                                          ('euro-to-dollars', 'Convert Euro to Dollars'),
                                          ('dollars-to-leva', 'Convert Dollars to Leva'),
                                          ('leva-to-dollars', 'Convert Leva to Dollars'),
                                          ('pound-to-dollars', 'Convert Pound to Dollars'),
                                          ('dollars-to-pound', 'Convert Dollars to Pound')])

