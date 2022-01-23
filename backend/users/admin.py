from django.contrib import admin

<<<<<<< HEAD
from users.models import User
=======
from foodgram.settings import EMPTY_STRING
from users.models import Follow, User

admin.ModelAdmin.empty_value_display = EMPTY_STRING
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
=======
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    search_fields = ('username', 'email',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('author', 'user',)
    search_fields = ('author', 'user',)
>>>>>>> 95bcf922c94704f68c7b12b96c323ec885446dd0
