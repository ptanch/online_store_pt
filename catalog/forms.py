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
                    f"{field_label} не может содержать запрещённое слово: 'word'"
                )

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        self._validate_forbidden_words(name, "Название")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        self._validate_forbidden_words(description, "Описание")
        return description
