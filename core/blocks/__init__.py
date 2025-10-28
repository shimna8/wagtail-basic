"""
Reusable StreamField blocks for Wagtail.

This package contains all custom blocks organized by category:
- hero_blocks: Banner, Slider, Video, Parallax
- content_blocks: Image with Content, FAQ, Accordion, Get In Touch
"""

# Hero Blocks
from .hero_blocks import (
    BannerBlock,
    SliderBlock,
    VideoBlock,
    ParallaxBlock,
)

# Content Blocks
from .content_blocks import (
    ImageWithContentBlock,
    FAQBlock,
    AccordionBlock,
    GetInTouchBlock,
)

__all__ = [
    # Hero Blocks
    'BannerBlock',
    'SliderBlock',
    'VideoBlock',
    'ParallaxBlock',
    # Content Blocks
    'ImageWithContentBlock',
    'FAQBlock',
    'AccordionBlock',
    'GetInTouchBlock',
]

