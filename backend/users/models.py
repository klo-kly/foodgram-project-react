from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from django.db.models import (CASCADE, CharField, EmailField, ForeignKey,
                              Model, UniqueConstraint)


class User(AbstractUser):
    email = EmailField('Почта', max_length=254, unique=True)
    username = CharField('Никнейм', max_length=150, unique=True, blank=True)
    first_name = CharField('Имя', max_length=150)
    last_name = CharField('Фамилия', max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ('-pk',)
=======
from django.db import models


class User(AbstractUser):
    """Кастомная модель юзера."""

    username = models.CharField(
        verbose_name='Логин',
        max_length=150,
        null=False,
        unique=True
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        unique=True,
        null=False,
        verbose_name='Адрес электронной почты'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Фамилия'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        ordering = ('username',)
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
<<<<<<< HEAD
        return self.username


class Subscribe(Model):
    user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик'
    )
    following = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            UniqueConstraint(
                fields=('user', 'following',),
                name='unique_subscribe',
            ),
        )
=======
        return f'{self.email}, {self.username}'


class Follow(models.Model):
    """Модель подписок(автор-подписчик)."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )

    class Meta:
        verbose_name = 'Подпискa'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'user',),
                name='unique_follow'
            ),
        )

    def __str__(self):
        return f'{self.author}, {self.user}'
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0
