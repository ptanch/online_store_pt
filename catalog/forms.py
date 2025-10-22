from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    FORBIDDEN_WORDS = (
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
)

    def _validate_forbidden_words(self, field_value, field_label):
        """
        Вспомогательный метод для проверки наличия запрещённых слов.
        Проверка не чувствительна к регистру.
        """
        for word in self.FORBIDDEN_WORDS:
            if word.lower() in field_value.lower():
                raise ValidationError(
                    f"{field_label} не может содержать запрещённое слово: '{word}'"
                )

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        self._validate_forbidden_words(name, "Название")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        self._validate_forbidden_words(description, "Описание")
        return description

    @ staticmethod
    def _validate_price(price):
        if price is None:
            raise ValidationError('Цена должна быть указана')
        if price <= 0:
            raise ValidationError('Цена не может быть меньше нуля')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')

        if price == 0 and ('бесплатно' in name.lower() or 'бесплатно' in description.lower()):
            raise ValidationError('Если цена 0, не указывайте слово "бесплатно" — это и так очевидно.')

        if price is not None:
            self._validate_price(price)

        return cleaned_data
