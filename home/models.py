from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from core.models import BasePage


class HomePage(BasePage):
    """
    Homepage - inherits SEO and flexible hero from BasePage.
    Can use any hero type: banner, slider, video, or parallax.
    """

    # Page content below the hero
    body = StreamField([
        ('heading', blocks.CharBlock(
            form_classname="title",
            help_text="Section heading"
        )),
        ('paragraph', blocks.RichTextBlock(
            help_text="Paragraph text with formatting"
        )),
        ('image', ImageChooserBlock(
            help_text="Full-width image"
        )),
        ('html', blocks.RawHTMLBlock(
            help_text="Raw HTML content (use with caution)"
        )),
    ], blank=True, use_json_field=True, help_text="Main page content")

    content_panels = BasePage.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"
