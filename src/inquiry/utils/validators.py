import re
from django import forms

def validate_customer_name(value):
    if not re.match(r'^[a-zA-Z]{2,}$', value):
        raise forms.ValidationError("Customer name should contain only letters and be at least 2 characters long.")