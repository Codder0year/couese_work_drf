from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}

class Habit(models.Model):
    PERIOD_CHOICES = (
        (True, 'Каждый день'),
        (False, 'Раз в неделю'),
    )

    MOOD_CHOICES = (
        (True, 'Позитивная'),
        (False, 'Негативная'),
    )

    VISIBILITY_CHOICES = (
        (True, 'Открытая'),
        (False, 'Закрытая'),
    )

    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=150, verbose_name='Место')
    target_time = models.TimeField(verbose_name='Время выполнения привычки')
    task = models.CharField(max_length=150, verbose_name='Задача')
    duration_minutes = models.PositiveSmallIntegerField(verbose_name='Продолжительность (в минутах)')
    repeat_daily = models.BooleanField(default=False, choices=PERIOD_CHOICES, verbose_name='Частота выполнения')
    is_positive = models.BooleanField(default=True, choices=MOOD_CHOICES, verbose_name='Тип настроения')
    is_public = models.BooleanField(default=True, choices=VISIBILITY_CHOICES, verbose_name='Доступность',)
    associated_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    reward = models.CharField(max_length=150, **NULLABLE, verbose_name='Бонус')

    def str(self):
        return f'Привычка: {self.task} в {self.target_time}, место: {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-id']