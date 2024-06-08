from django.db.models import DateTimeField, CharField, ForeignKey, CASCADE, ImageField, SlugField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(verbose_name=_('category_name'), max_length=255)
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class New(TranslatableModel):
    translations = TranslatedFields(
        title=CharField(verbose_name=_('new_title'), max_length=255),
        description=CKEditor5Field(verbose_name=_('new_description'), config_name='extends')
    )
    slug = SlugField(verbose_name=_('new_slug'), unique=True, blank=True, editable=False)
    image = ImageField(upload_to='news/images', verbose_name=_('new_image'))
    category = ForeignKey('apps.Category', CASCADE, 'categories', verbose_name=_('new_category'))
    author = ForeignKey('apps.User', CASCADE, verbose_name=_('new_author'))
    created_at = DateTimeField(verbose_name=_('created_at'), auto_now_add=True)
    updated_at = DateTimeField(verbose_name=_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if force_update is True:
            self.slug = slugify(self.translations.fields.get('title'))
        return super().save(force_insert, force_update, using, update_fields)

    def created_at_new(self):
        return self.created_at.strftime('%d.%m.%Y')
