from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Удаляет все данные и создаёт тестовые категории и продукты"

    def handle(self, *args, **kwargs):
        """Удаляет все продукты и категории, потом создает новые"""

        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.WARNING("Все данные удалены!"))

        phones = Category.objects.create(name="Смартфоны", description="Новое поступление")
        laptops = Category.objects.create(name="Ноутбуки", description="Скидка 10%")
        self.stdout.write(self.style.SUCCESS("Категории созданы."))

        Product.objects.create(name="Iphone 17 Pro", description="Orange, 512 GB", price=189000, category=phones)
        Product.objects.create(name="Google Pixel 10 Pro", description="Obsidian, 256 GB", price=109000,
                               category=phones)
        Product.objects.create(name="Apple MacBook Air 13", description="16GB/256GB Midnight", price=110000,
                               category=laptops)
        Product.objects.create(name="ASUS ZenBook S16", description="24Gb/1Tb SSD White", price=155000,
                               category=laptops)

        self.stdout.write(self.style.SUCCESS("Тестовые продукты созданы."))
