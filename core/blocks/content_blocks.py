"""
Content blocks for page body sections.

Includes:
- ImageWithContentBlock: Image with text and CTA (with preview)
- FAQBlock: Frequently Asked Questions
- AccordionBlock: Expandable content sections
- GetInTouchBlock: Contact information and CTA
"""

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageWithContentBlock(blocks.StructBlock):
    """
    Image with text content and optional link.
    Perfect for features, services, testimonials.

    Features:
    - Live preview in block chooser
    - Flexible image positioning (left/right)
    - Optional CTA button with internal/external links
    - Rich text description support
    - Form collapsing for cleaner UI
    """
    title = blocks.CharBlock(
        max_length=255,
        help_text="Section title"
    )

    description = blocks.RichTextBlock(
        help_text="Content text with formatting support"
    )

    image = ImageChooserBlock(
        help_text="Image (recommended: 600x400px)"
    )

    image_position = blocks.ChoiceBlock(
        choices=[('left', 'Image on Left'), ('right', 'Image on Right')],
        default='left'
    )

    link_text = blocks.CharBlock(
        required=False,
        max_length=50,
        help_text="Button text"
    )

    link_page = blocks.PageChooserBlock(required=False)
    link_external = blocks.URLBlock(required=False)

    class Meta:
        icon = 'image'
        label = 'Image with Content'
        template = 'blocks/image_with_content_block.html'
        preview_template = 'blocks/previews/image_with_content_preview.html'
        help_text = 'Add an image with accompanying text content and optional call-to-action button'
        form_classname = 'struct-block image-with-content-block-form'


class FAQBlock(blocks.StructBlock):
    """
    FAQ section with Q&A pairs.
    Perfect for FAQ pages and support sections.
    """
    class FAQItemBlock(blocks.StructBlock):
        question = blocks.CharBlock(max_length=255)
        answer = blocks.RichTextBlock()

        class Meta:
            label = 'FAQ Item'

    title = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Section title"
    )

    description = blocks.RichTextBlock(
        required=False,
        help_text="Section description"
    )

    faqs = blocks.ListBlock(
        FAQItemBlock(),
        min_num=1,
        max_num=20,
        help_text="Add 1-20 FAQ items"
    )

    class Meta:
        icon = 'help'
        label = 'FAQ Section'
        template = 'blocks/faq_block.html'


class AccordionBlock(blocks.StructBlock):
    """
    Accordion/Collapsible section.
    Perfect for guides, process steps, terms.
    """
    class AccordionItemBlock(blocks.StructBlock):
        heading = blocks.CharBlock(max_length=255)
        description = blocks.RichTextBlock()

        class Meta:
            label = 'Accordion Item'

    title = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Section title"
    )

    description = blocks.RichTextBlock(
        required=False,
        help_text="Section description"
    )

    items = blocks.ListBlock(
        AccordionItemBlock(),
        min_num=1,
        max_num=20,
        help_text="Add 1-20 accordion items"
    )

    allow_multiple_open = blocks.BooleanBlock(
        required=False,
        default=False,
        help_text="Allow multiple items to be open at once"
    )

    class Meta:
        icon = 'list-ul'
        label = 'Accordion Section'
        template = 'blocks/accordion_block.html'


class GetInTouchBlock(blocks.StructBlock):
    """
    Get in Touch / Contact CTA section.
    Perfect for contact sections and CTAs.
    """
    title = blocks.CharBlock(
        max_length=255,
        default="Get In Touch",
        help_text="Section title"
    )

    description = blocks.RichTextBlock(
        help_text="Section description"
    )

    email = blocks.EmailBlock(
        required=False,
        help_text="Contact email"
    )

    phone = blocks.CharBlock(
        required=False,
        max_length=20,
        help_text="Contact phone number"
    )

    address = blocks.CharBlock(
        required=False,
        max_length=255,
        help_text="Contact address"
    )

    cta_text = blocks.CharBlock(
        max_length=50,
        default="Contact Us",
        help_text="Button text"
    )

    cta_link = blocks.PageChooserBlock(required=False)
    cta_external = blocks.URLBlock(required=False)

    background_color = blocks.ChoiceBlock(
        choices=[
            ('primary', 'Primary Color'),
            ('secondary', 'Secondary Color'),
            ('light', 'Light Gray'),
            ('dark', 'Dark Gray'),
        ],
        default='primary',
        help_text="Background color"
    )

    class Meta:
        icon = 'mail'
        label = 'Get In Touch'
        template = 'blocks/get_in_touch_block.html'

