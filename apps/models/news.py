from django.db.models import Model, DateTimeField, CharField, ForeignKey
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Category(Model):
    name = CharField(verbose_name=_('category_name'), max_length=255)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class New(Model):
    title = CharField(verbose_name=_('new_title'))
    description = CKEditor5Field(verbose_name=_('new_description'))
    author = ForeignKey('apps')
    created_at = DateTimeField(verbose_name=_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(verbose_name=_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')

    def created_at_new(self):
        return self.created_at.strftime('%d.%m.%Y')
