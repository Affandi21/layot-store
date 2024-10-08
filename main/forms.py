from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["nama", "deskripsi", "stok", "harga"]

    def clean_product(self):
        nama = self.cleaned_data["nama"]
        return strip_tags(nama)

    def clean_deskripsi(self):
        deskripsi = self.cleaned_data["deskripsi"]
        return strip_tags(deskripsi)