from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from core.models import BasePage
from core.blocks.content_blocks import ContentImageBlock,ExploreModelsBlock,ModelCardsBlock,LargeBannerBlock,ContentPointsBlock,ExclusiveOfferBlock,NewsListSwiperBlock
# from core.blocks.content_blocks import ContentImageBlock
# from core.blocks import (
#     ContentImageBlock,
#     FAQBlock,
#     AccordionBlock,
#     GetInTouchBlock,
# )

class HomePage(BasePage):
    """
    Homepage - inherits SEO and flexible hero from BasePage.
    Can use any hero type: banner, slider, video, or parallax.
    """

    # Page content below the hero
    content = StreamField([        
        ('content_image_block', ContentImageBlock(group="Base Blocks")),
        ('explore_models_block', ExploreModelsBlock(group="Base Blocks")),
        ('model_cards_block', ModelCardsBlock(group="Base Blocks")),
        ('large_banner_block', LargeBannerBlock(group="Base Blocks")),
        ('content_points_block', ContentPointsBlock(group="Base Blocks")), 
        ('exclusive_offer_block', ExclusiveOfferBlock(group="Base Blocks")),
        ('news_list_swiper_block', NewsListSwiperBlock(group="Base Blocks")),        
    ], blank=True, use_json_field=True, help_text="Main page content")

    content_panels = BasePage.content_panels + [
        FieldPanel('content'),
    ]
    class Meta:
        verbose_name = "Home Page"
