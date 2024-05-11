from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class User(AbstractUser):
    first_name = CharField(verbose_name=_('first_name'), max_length=50)
    last_name = CharField(verbose_name=_('last_name'), max_length=50)
    username = CharField(verbose_name=_('username'), max_length=50)
    bio = TextField(verbose_name=_('user_bio'), max_length=1024, blank=True, null=True)
    avatar = ResizedImageField(_('user_avatar'), size=[168, 168], crop=['middle', 'center'], upload_to='users/images',
                               null=True, blank=True, default='users/default_user.jpg')

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
