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
from django.utils.translation import gettext_lazy as _
from voyah.constants import *
from django.apps import apps
from django import forms

from django.core.exceptions import ValidationError

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



# ------------ home page ----------------

class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    link_type = blocks.ChoiceBlock(
        choices = [
            ('internal', _('Internal Page')),
            ('external', _('External URL')),
        ],
        default='internal',
        help_text=_("Select the type of link"),
    )
    internal_page = blocks.PageChooserBlock(
        required=False, 
        help_text=_("Select an internal page"),
        target_model = PAGE_TARGETS
    )
    external_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter an external URL"),
    )
    tab_key = blocks.CharBlock(required=False, help_text=_("Add the tab key"))

    def clean(self, value):
        """
        Custom validation to ensure that only one type of link (internal or external) is provided,
        and that the appropriate fields are filled based on the selected link type.
        """
        cleaned_data = super().clean(value)
        link_type = cleaned_data.get('link_type')
        internal_page = cleaned_data.get('internal_page')
        external_url = cleaned_data.get('external_url')

        # Validation logic based on link type
        if link_type == 'internal' and not internal_page:
            raise ValidationError(_('An internal page must be selected when "Internal Page" is chosen.'))
        elif link_type == 'external' and not external_url:
            raise ValidationError(_('A URL must be provided when "External URL" is chosen.'))

        # Prevent both internal and external links from being filled
        if link_type == 'internal' and external_url:
            raise ValidationError(_('An external URL should not be provided when linking to an internal page.'))
        if link_type == 'external' and internal_page:
            raise ValidationError(_('An internal page should not be provided when linking to an external URL.'))

        return cleaned_data
    
    class Meta:
        label = _("Link Information")
        icon = 'link'
        
class InternalLinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    internal_page = blocks.PageChooserBlock(
        required=False, 
        help_text=_("Select an internal page"),
        target_model = PAGE_TARGETS
    )
    tab_key = blocks.CharBlock(required=False, help_text=_("Add the tab key"))
    
    class Meta:
        label = _("Link Information")
        icon = 'link'
        
class DynamicModelChoiceBlock(blocks.FieldBlock):
    
    # Generic dropdown block to select a model instance dynamically.
    
    def __init__(self, model_name, filter_locale=None, **kwargs):
        self.model_name = model_name
        self.filter_locale = filter_locale
        self.field = forms.ChoiceField(choices=[], required=kwargs.get("required", True))
        super().__init__(**kwargs)

    def get_form_state(self, value):
        model = apps.get_model(self.model_name)
        qs = model.objects.live().order_by("title") if hasattr(model.objects, "live") else model.objects.all()

        # # Apply locale filter if specified
        # if self.filter_locale:
        #     try:
        #         locale_obj = Locale.objects.get(language_code=self.filter_locale)
        #         if hasattr(qs, "filter"):
        #             qs = qs.filter(locale=locale_obj)
        #     except Locale.DoesNotExist:
        #         pass

        # Populate choices
        self.field.choices = [("", "---------")] + [
            (str(o.pk), getattr(o, "title", str(o))) for o in qs
        ]
        return super().get_form_state(str(value.pk) if hasattr(value, "pk") else value)

    def to_python(self, value):
        if not value:
            return None
        model = apps.get_model(self.model_name)
        return model.objects.filter(pk=value).first()

    def get_prep_value(self, value):
        if not value:
            return ""
        return str(value.pk) if hasattr(value, "pk") else str(value)

    def value_for_form(self, value):
        return str(value.pk) if hasattr(value, "pk") else (str(value) if value else "")

    def value_from_form(self, value):
        if not value:
            return None
        model = apps.get_model(self.model_name)
        return model.objects.filter(pk=int(value)).first()

# class NewsChooserBlock(DynamicModelChoiceBlock):
#     def __init__(self, **kwargs):
#         # super().__init__(model_name="blog.NewsPage", filter_locale="en", **kwargs)
#         pass

class ContentImageBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    image = ImageChooserBlock(required=False,label=_("Image"),help_text=_("Please upload an image"))
    image_alignment = blocks.ChoiceBlock(max_length=20, choices=IMAGE_ALIGNMENT_CHOICES,  null=True, blank=True, default="left", help_text=_("Image Alignment"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
        
    class Meta:
        icon = "doc-full"
        label = _("Content Image Block")
        

class ExploreModelsBlock(blocks.StructBlock):
    main_heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    image = ImageChooserBlock(required=False,label=_("Image"),help_text=_("Please upload an image"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
        
    class Meta:
        icon = "doc-full"
        label = _("Explore Models Block")


class ModelsListSliderBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    image = ImageChooserBlock(required=False,label=_("Image"),help_text=_("Please upload an image"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
        
    class Meta:
        icon = "doc-full"
        label = _("Models List Slider Block")
    
       
class ModelCardsBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
    points = blocks.ListBlock(ModelsListSliderBlock(), label=_("Add Model Cards"), help_text=_("Add models cards to this section"))
    
    class Meta:
        icon = "doc-full"
        label = _("Model Cards Block")  
        

class LargeBannerBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add your sub heading"))
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    image = ImageChooserBlock(required=False,label=_("Image"),help_text=_("Please upload an image"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
        
    class Meta:
        icon = "doc-full"
        label = _("Large Banner Block")   
        
class PointDataBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    
    class Meta:
        icon = "doc-full"
        label = _("Point Data Block")  
        
        
class ContentPointsBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    image = ImageChooserBlock(required=False,label=_("Image"),help_text=_("Please upload an image"))
    points = blocks.ListBlock(PointDataBlock(), label=_("Add Points"), help_text=_("Add points to this section"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
        
    class Meta:
        icon = "doc-full"
        label = _("Content Points Block")
        

class ExclusiveOfferBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=False,label=_("Heading"),features=[])
    description = blocks.RichTextBlock(required=False, help_text=_("Add additional text"))
    links = blocks.ListBlock(LinkBlock(),min_num=0,max_num=2,help_text=_("Add button/link information to this section"),label=_("Add link details"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
     
    class Meta:
        icon = "doc-full"
        label = _("Exclusive Offer Block")
    
    
class NewsListSwiperBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Background"))
    view_more_page = blocks.ListBlock(LinkBlock(),min_num=0,help_text=_("Add button/link information to this section"),label= _("Add link details"))
    
    # class ChoosePageListBlock(blocks.StructBlock): 
    #     news = blocks.ListBlock(NewsChooserBlock(),label=_("Choose the news to display.")) 
    
    class ListAllBlock(blocks.StructBlock): 
        max_items = blocks.IntegerBlock(default= DEFAULT_MAXIMUM_ITEMS_PER_BLOCK, help_text=_("Maximum number of items to display (set to zero for full list of items)."))
        order_by = blocks.ChoiceBlock( 
            choices=[ 
                ('title', 'Title'),
                ('date', 'Date'), 
                ('path', 'Sort Order'),
            ], 
            default='date', 
            help_text=_("Select how to sort the items")
        )
     # StreamBlock for listing options (only one can be selected) 
    listing_options = blocks.StreamBlock([ 
        # ('choose_news', ChoosePageListBlock()),
        ('list_all_news', ListAllBlock())
    ],
    max_num= 1,
    required=True,
    default_value=[ 
        { 
            'type': 'list_all', 
            'value': { 
                'items_per_page': ITEMS_PER_PAGE, 
                'order_by': 'date' 
                } 
        } 
    ], label= _("List the news"))
    
    class Meta:
        icon = "sliders"
        label = _("News Swiper Block")





