"""
Core models for the Wagtail project.

This module contains:
- Base page classes (BasePage)
- Page models (HomePage)

Blocks are organized in separate modules:
- core.blocks.hero_blocks: BannerBlock, SliderBlock, VideoBlock, ParallaxBlock
- core.blocks.content_blocks: ImageWithContentBlock, FAQBlock, AccordionBlock, GetInTouchBlock

Mixins are in:
- core.mixins: SEOMixin
"""

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

# Import blocks from separate modules
from core.blocks import (
    BannerBlock,
    SliderBlock,
    VideoBlock,
    ParallaxBlock,
    ImageWithContentBlock,
    FAQBlock,
    AccordionBlock,
    GetInTouchBlock,
)

# Import mixins
from core.mixins import SEOMixin


# ============================================
# BASE PAGE CLASS
# ============================================

class BasePage(SEOMixin, Page):
    """
    Abstract base page class with hero and body sections.
    
    All pages should inherit from this class to get:
    - Hero section (banner, slider, video, or parallax)
    - Body section (flexible content blocks)
    - SEO fields (meta description, og_image, etc.)
    
    Usage:
        class MyPage(BasePage):
            pass
    """
    
    # Flexible hero section - editors choose one type
    hero = StreamField(
        [
            ('banner', BannerBlock()),
            ('slider', SliderBlock()),
            ('video', VideoBlock()),
            ('parallax', ParallaxBlock()),
        ],
        blank=True,
        null=True,
        max_num=1,
        use_json_field=True,
        help_text="Choose a hero section type (optional)"
    )

    # Flexible body content - editors can mix and match blocks
    # body = StreamField(
    #     [
    #         ('image_with_content', ImageWithContentBlock()),
    #         ('faq', FAQBlock()),
    #         ('accordion', AccordionBlock()),
    #         ('get_in_touch', GetInTouchBlock()),
    #     ],
    #     blank=True,
    #     use_json_field=True,
    #     help_text="Add content blocks to build your page"
    # )

    class Meta:
        abstract = True

    content_panels = Page.content_panels + [
        FieldPanel('hero'),
        # FieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + SEOMixin.seo_panels

