"""
Core models for the Wagtail project.
Contains base page classes, mixins, and reusable StreamField blocks.
"""

from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock


# ============================================
# HERO/BANNER BLOCKS (Reusable Components)
# ============================================

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
        help_text="Or link to external URL (overrides page link)"
    )

    class Meta:
        icon = 'image'
        label = 'Static Banner'
        template = 'blocks/banner_block.html'


class SliderBlock(blocks.StructBlock):
    """
    Image slider/carousel with multiple slides.
    Each slide can have its own image, text, and CTA.
    """

    class SlideBlock(blocks.StructBlock):
        """Individual slide in the slider"""

        title = blocks.CharBlock(
            required=False,
            max_length=255,
            help_text="Slide title"
        )

        subtitle = blocks.CharBlock(
            required=False,
            max_length=255,
            help_text="Slide subtitle"
        )

        # Responsive images for each slide
        image = ImageChooserBlock(
            required=True,
            help_text="Desktop image (1920x600px)"
        )

        image_tablet = ImageChooserBlock(
            required=False,
            help_text="Tablet image (1024x600px) - Optional"
        )

        image_mobile = ImageChooserBlock(
            required=False,
            help_text="Mobile image (768x600px) - Optional"
        )

        # CTA for each slide
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
            help_text="Or external URL"
        )

        class Meta:
            icon = 'image'
            label = 'Slide'

    # List of slides
    slides = blocks.ListBlock(
        SlideBlock(),
        min_num=2,
        max_num=10,
        help_text="Add 2-10 slides"
    )

    # Slider Settings
    autoplay = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Auto-advance slides"
    )

    autoplay_speed = blocks.IntegerBlock(
        default=5000,
        min_value=1000,
        max_value=10000,
        help_text="Milliseconds between slides (1000 = 1 second)"
    )

    show_arrows = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Show previous/next arrows"
    )

    show_dots = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Show navigation dots"
    )

    # Display Options
    height = blocks.ChoiceBlock(
        choices=[
            ('small', 'Small (400px)'),
            ('medium', 'Medium (600px)'),
            ('large', 'Large (800px)'),
            ('full', 'Full Screen'),
        ],
        default='medium'
    )

    overlay_opacity = blocks.IntegerBlock(
        default=30,
        min_value=0,
        max_value=100,
        help_text="Dark overlay opacity (0-100)"
    )

    text_alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='center'
    )

    text_color = blocks.ChoiceBlock(
        choices=[
            ('white', 'White'),
            ('black', 'Black'),
        ],
        default='white'
    )

    class Meta:
        icon = 'image'
        label = 'Image Slider'
        template = 'blocks/slider_block.html'


class VideoBlock(blocks.StructBlock):
    """
    Video banner with YouTube/Vimeo embed support.
    Includes fallback poster image and overlay content.
    """

    # Video Source
    video_url = blocks.URLBlock(
        required=False,
        help_text="YouTube or Vimeo URL (e.g., https://www.youtube.com/watch?v=...)"
    )

    # Fallback/Poster Image
    poster_image = ImageChooserBlock(
        required=False,
        help_text="Fallback image shown while loading or if video fails (1920x1080px)"
    )

    # Overlay Content
    title = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Title overlaid on video"
    )

    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Subtitle overlaid on video"
    )

    # Video Settings
    autoplay = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Auto-play video on page load"
    )

    loop = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Loop video continuously"
    )

    muted = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text="Mute video (must be muted for autoplay to work)"
    )

    show_controls = blocks.BooleanBlock(
        required=False,
        default=False,
        help_text="Show video controls"
    )

    # Display Options
    height = blocks.ChoiceBlock(
        choices=[
            ('medium', 'Medium (600px)'),
            ('large', 'Large (800px)'),
            ('full', 'Full Screen'),
        ],
        default='large',
        help_text="Video banner height"
    )

    overlay_opacity = blocks.IntegerBlock(
        default=40,
        min_value=0,
        max_value=100,
        help_text="Dark overlay opacity (0-100)"
    )

    text_alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='center'
    )

    text_color = blocks.ChoiceBlock(
        choices=[
            ('white', 'White'),
            ('black', 'Black'),
        ],
        default='white'
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
        help_text="Or external URL"
    )

    class Meta:
        icon = 'media'
        label = 'Video Banner'
        template = 'blocks/video_block.html'


class ParallaxBlock(blocks.StructBlock):
    """
    Parallax scrolling banner with depth effect.
    Creates an engaging visual experience as users scroll.
    """

    title = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Banner title"
    )

    subtitle = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Banner subtitle"
    )

    # Background Image (should be large for parallax effect)
    background_image = ImageChooserBlock(
        required=True,
        help_text="Large background image (2400x1200px recommended for best parallax effect)"
    )

    # Parallax Settings
    parallax_speed = blocks.ChoiceBlock(
        choices=[
            ('slow', 'Slow (0.3x)'),
            ('medium', 'Medium (0.5x)'),
            ('fast', 'Fast (0.7x)'),
        ],
        default='medium',
        help_text="Parallax scroll speed"
    )

    # Display Options
    height = blocks.ChoiceBlock(
        choices=[
            ('medium', 'Medium (600px)'),
            ('large', 'Large (800px)'),
            ('full', 'Full Screen'),
        ],
        default='large'
    )

    overlay_opacity = blocks.IntegerBlock(
        default=30,
        min_value=0,
        max_value=100,
        help_text="Dark overlay opacity (0-100)"
    )

    text_alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right'),
        ],
        default='center'
    )

    text_color = blocks.ChoiceBlock(
        choices=[
            ('white', 'White'),
            ('black', 'Black'),
        ],
        default='white'
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
        help_text="Or external URL"
    )

    class Meta:
        icon = 'image'
        label = 'Parallax Banner'
        template = 'blocks/parallax_block.html'


# ============================================
# SEO MIXIN
# ============================================

class SEOMixin(models.Model):
    """
    Extended SEO fields for meta tags, Open Graph, and Twitter Cards.
    Wagtail's Page model already includes seo_title and search_description,
    so we only add additional SEO fields here.
    """

    # Open Graph / Social Media
    og_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Social media image",
        help_text="Image for social media sharing (1200x630px recommended)"
    )

    # Twitter Card
    twitter_card_type = models.CharField(
        "Twitter card type",
        max_length=20,
        choices=[
            ('summary', 'Summary'),
            ('summary_large_image', 'Summary Large Image'),
        ],
        default='summary_large_image',
        blank=True,
        help_text="Type of Twitter card to use"
    )

    # Canonical URL
    canonical_url = models.URLField(
        "Canonical URL",
        blank=True,
        help_text="Override canonical URL (leave blank to use page URL)"
    )

    # Robots Meta Tags
    no_index = models.BooleanField(
        "No index",
        default=False,
        help_text="Prevent search engines from indexing this page"
    )

    no_follow = models.BooleanField(
        "No follow",
        default=False,
        help_text="Prevent search engines from following links on this page"
    )

    class Meta:
        abstract = True

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('og_image'),
            FieldPanel('twitter_card_type'),
        ], heading="Social Media"),

        MultiFieldPanel([
            FieldPanel('canonical_url'),
            FieldPanel('no_index'),
            FieldPanel('no_follow'),
        ], heading="Advanced SEO"),
    ]

    def get_meta_title(self):
        """Return SEO title or fall back to page title"""
        return self.seo_title or self.title

    def get_meta_description(self):
        """Return search description"""
        return self.search_description

    def get_meta_image(self):
        """Return OG image for social sharing"""
        return self.og_image

    def get_robots_tag(self):
        """Generate robots meta tag content"""
        tags = []
        if self.no_index:
            tags.append('noindex')
        if self.no_follow:
            tags.append('nofollow')
        return ', '.join(tags) if tags else None


# ============================================
# BASE PAGE WITH FLEXIBLE HERO
# ============================================

class BasePage(SEOMixin, Page):
    """
    Base page class that all content pages should inherit from.
    Includes SEO functionality and flexible hero section.

    Editors can choose from:
    - Static Banner (single image with text)
    - Image Slider (carousel with multiple slides)
    - Video Banner (YouTube/Vimeo background)
    - Parallax Banner (parallax scrolling effect)
    - Or no hero at all
    """

    # Flexible hero section - editors choose one type
    hero = StreamField([
        ('banner', BannerBlock()),
        ('slider', SliderBlock()),
        ('video', VideoBlock()),
        ('parallax', ParallaxBlock()),
    ], blank=True, null=True, max_num=1, use_json_field=True,
       help_text="Choose one hero type for the top of the page (optional)")

    class Meta:
        abstract = True

    content_panels = Page.content_panels + [
        FieldPanel('hero'),
    ]

    promote_panels = (
        Page.promote_panels +
        SEOMixin.promote_panels
    )

    def has_hero(self):
        """Check if page has a hero section"""
        return bool(self.hero)

    def get_hero_type(self):
        """Get the type of hero being used (banner, slider, video, parallax)"""
        if self.hero:
            return self.hero[0].block_type
        return None

    def get_hero_data(self):
        """Get the hero block data"""
        if self.hero:
            return self.hero[0]
        return None
