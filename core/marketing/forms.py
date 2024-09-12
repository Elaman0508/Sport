from django import forms


class PaymentForm(forms.Form):
    cardholder_name = forms.CharField(max_length=100)
    card_number = forms.CharField(max_length=20)
    expiry_date = forms.CharField(max_length=7)  # MM/YY
    cvv = forms.CharField(max_length=4)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
