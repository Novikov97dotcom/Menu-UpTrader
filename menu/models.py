"""Models for the menu app."""
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    """Menu item in a tree structure."""
    name: str = models.CharField(
        max_length=100,
        verbose_name=_('Name')
    )
    menu_name: str = models.CharField(
        max_length=100,
        verbose_name=_('Menu Name')
    )
    url: str = models.CharField(
        max_length=255,
        verbose_name=_('URL'),
        blank=True
    )
    named_url: str = models.CharField(
        max_length=255,
        verbose_name=_('Named URL'),
        blank=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('Parent')
    )
    order: int = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Order')
    )

    class Meta:
        """Meta options."""
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')
        ordering = ['order', 'name']
        unique_together = ['menu_name', 'parent', 'name']

    def __str__(self) -> str:
        """String representation."""
        return str(self.name)

    def clean(self) -> None:
        """Validate menu item data."""
        if self.parent and self.parent.pk == self.pk:
            raise ValidationError(_('An item cannot be its own parent'))
        if not self.url and not self.named_url:
            raise ValidationError(_('Either URL or Named URL must be provided'))
        if self.url and self.named_url:
            raise ValidationError(_('Cannot provide both URL and Named URL'))
        # Check for circular references
        parent = self.parent
        while parent:
            if parent.pk == self.pk:
                raise ValidationError(_('Circular reference detected'))
            parent = parent.parent

    def get_url(self) -> str:
        """Get the URL for this menu item."""
        if self.url:
            return self.url
        try:
            return reverse(self.named_url)
        except NoReverseMatch:
            return '#'

    def get_ancestors(self) -> list['MenuItem']:
        """Get all ancestors of this menu item."""
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

    def get_siblings(self) -> models.QuerySet:
        """Get all siblings of this menu item."""
        if self.parent:
            return MenuItem.objects.filter(parent=self.parent).exclude(pk=self.pk)
        return MenuItem.objects.filter(parent=None, menu_name=self.menu_name).exclude(pk=self.pk)
