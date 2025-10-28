"""
Hero/Banner blocks for page headers.

Includes:
- BannerBlock: Static banner with responsive images
- SliderBlock: Image carousel
- VideoBlock: Video banner with poster image
- ParallaxBlock: Parallax scrolling effect
"""

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


class BannerBlock(blocks.StructBlock):
    """
    Static banner with single image and responsive support.
    Perfect for simple hero sections with one image.
    """
    title = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Override page title (leave blank to use page title)"
    )

    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Subtitle or tagline"
    )

    # Responsive Images
    image = ImageChooserBlock(
        required=False,
        help_text="Desktop image (1920x600px recommended)"
    )

    image_tablet = ImageChooserBlock(
        required=False,
        help_text="Tablet image (1024x600px recommended) - Optional"
    )

    image_mobile = ImageChooserBlock(
        required=False,
        help_text="Mobile image (768x600px recommended) - Falls back to desktop if not provided"
    )

    # Display Options
    height = blocks.ChoiceBlock(
        choices=[
            ('small', 'Small (400px)'),
            ('medium', 'Medium (600px)'),
            ('large', 'Large (800px)'),
            ('full', 'Full Screen'),
        ],
        default='medium',
        help_text="Banner height on desktop"
    )

    overlay_opacity = blocks.IntegerBlock(
        default=30,
        min_value=0,
        max_value=100,
        help_text="Dark overlay opacity (0-100) - Helps text readability"
    )

    text_alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='center',
        help_text="Text alignment in banner"
    )

    text_color = blocks.ChoiceBlock(
        choices=[
            ('white', 'White'),
            ('black', 'Black'),
        ],
        default='white',
        help_text="Text color"
    )

    # Call to Action
    cta_text = blocks.CharBlock(
        required=False,
        max_length=50,
        help_text="Button text"
    )

    cta_link = blocks.PageChooserBlock(
        required=False,
        help_text="Link to internal page"
    )

    cta_external = blocks.URLBlock(
        required=False,
        help_text="External URL (overrides internal link)"
    )

    class Meta:
        icon = 'image'
        label = 'Banner'
        template = 'blocks/banner_block.html'


class SliderBlock(blocks.StructBlock):
    """
    Image carousel/slider with multiple slides.
    Perfect for showcasing multiple images.
    """
    class SlideBlock(blocks.StructBlock):
        image = ImageChooserBlock()
        title = blocks.CharBlock(required=False, max_length=255)
        description = blocks.RichTextBlock(required=False)
        link_page = blocks.PageChooserBlock(required=False)
        link_external = blocks.URLBlock(required=False)

        class Meta:
            icon = 'image'
            label = 'Slide'

    slides = blocks.ListBlock(SlideBlock(), min_num=2, max_num=10)
    autoplay = blocks.BooleanBlock(required=False, default=True)
    autoplay_speed = blocks.IntegerBlock(default=5000, help_text="Milliseconds")
    show_arrows = blocks.BooleanBlock(required=False, default=True)
    show_dots = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        icon = 'image'
        label = 'Slider'
        template = 'blocks/slider_block.html'


class VideoBlock(blocks.StructBlock):
    """
    Video banner with poster image fallback.
    Supports YouTube, Vimeo, and self-hosted videos.
    """
    video_url = blocks.URLBlock(help_text="YouTube, Vimeo, or video file URL")
    poster_image = ImageChooserBlock(help_text="Fallback image (1920x600px)")
    autoplay = blocks.BooleanBlock(required=False, default=True)
    loop = blocks.BooleanBlock(required=False, default=True)
    muted = blocks.BooleanBlock(required=False, default=True)
    show_controls = blocks.BooleanBlock(required=False, default=True)

    class Meta:
        icon = 'media'
        label = 'Video'
        template = 'blocks/video_block.html'


class ParallaxBlock(blocks.StructBlock):
    """
    Parallax scrolling effect with background image.
    Creates depth effect as user scrolls.
    """
    image = ImageChooserBlock(help_text="Large background image (1920x800px)")
    title = blocks.CharBlock(required=False, max_length=255)
    subtitle = blocks.CharBlock(required=False, max_length=255)
    speed = blocks.IntegerBlock(
        default=50,
        min_value=0,
        max_value=100,
        help_text="Parallax speed (0-100)"
    )
    height = blocks.ChoiceBlock(
        choices=[
            ('small', 'Small (400px)'),
            ('medium', 'Medium (600px)'),
            ('large', 'Large (800px)'),
        ],
        default='medium'
    )

    class Meta:
        icon = 'image'
        label = 'Parallax'
        template = 'blocks/parallax_block.html'

