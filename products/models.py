from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=700, verbose_name="Имя категории")
    slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"


class Subcategory(models.Model):
    cat = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=700, verbose_name="Имя подкатегории")
    slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:subcategory_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Подкатегории"
        verbose_name = "Подкатегория"


class Product(models.Model):
    subcat = models.ForeignKey("Subcategory", on_delete=models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(max_length=700, verbose_name="Имя товара")
    description = models.TextField(null=True, verbose_name="Описание товара")
    slug = models.SlugField(unique=True, blank=True, verbose_name='Слаг')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"


class Characteristic(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name="Товар")
    label = models.CharField(max_length=300, verbose_name="Имя характеристики")
    value = models.CharField(max_length=300, verbose_name="Значение характеристики")
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return f"{self.label[:10]} - {self.value[:10]}"
    
    class Meta:
        verbose_name_plural = "Характеристики"
        verbose_name = "Характеристика"


class ImageProduct(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField(blank=True, verbose_name="Изображение")
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')
    
    def __str__(self):
        return self.image

    class Meta:
        verbose_name_plural = "Изображения"
        verbose_name = "Изображение"