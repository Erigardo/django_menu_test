from django.db import models
from prompt_toolkit.widgets import MenuItem


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    #  ссылаеться на родительский элемент меню
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    #  menu определяет, к какому меню относится элемент
    menu = models.CharField(max_length=100)

    # регистрируем модель `MenuItem` в административном интерфейсе Django:

    # Надо вернуть имя родительского элемента, если он существует,
    # или пустую строку, если родительский элемент не указан.
    def __str__(self):
        if self.parent is not None:
            return f"{self.name} ({self.parent.name})"
        else:
            return self.name
