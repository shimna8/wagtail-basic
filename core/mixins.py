"""
Reusable mixins for Wagtail pages.

Includes:
- SEOMixin: Extended SEO fields (og_image, twitter, canonical URL, etc.)
"""

from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.models import Image


class SEOMixin(models.Model):
    """
    Extended SEO fields for pages.
    
    Provides:
    - Meta description
    - OG image (Open Graph)
    - Twitter card type
    - Canonical URL
    - No-index/no-follow options
    """
    
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="Meta description for search engines (max 160 characters)"
    )
    
    og_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image for social media sharing (1200x630px recommended)"
    )
    
    twitter_card_type = models.CharField(
        max_length=20,
        choices=[
            ('summary', 'Summary'),
            ('summary_large_image', 'Summary with Large Image'),
            ('player', 'Player'),
        ],
        default='summary_large_image',
        help_text="Twitter card type"
    )
    
    canonical_url = models.URLField(
        blank=True,
        help_text="Canonical URL (leave blank to use page URL)"
    )
    
    no_index = models.BooleanField(
        default=False,
        help_text="Prevent search engines from indexing this page"
    )
    
    no_follow = models.BooleanField(
        default=False,
        help_text="Prevent search engines from following links on this page"
    )
    
    class Meta:
        abstract = True
    
    seo_panels = [
        MultiFieldPanel([
            FieldPanel('meta_description'),
            FieldPanel('og_image'),
            FieldPanel('twitter_card_type'),
            FieldPanel('canonical_url'),
            FieldPanel('no_index'),
            FieldPanel('no_follow'),
        ], heading='SEO Settings')
    ]

