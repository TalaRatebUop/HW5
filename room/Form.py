from django import forms

class product(forms.Form):
    CATEGORY=[(1,"Food"),(2,"Snacks"),(3,"Drinks"),(4,"Hardware")]
    productName=forms.CharField(label="Product Name",label_suffix=":")
    Category=forms.ChoiceField(label="Category",label_suffix=":",choices=CATEGORY)
    description=forms.CharField(label="Description ",label_suffix=":")
    rate=forms.DecimalField(label="Rate",label_suffix=":")