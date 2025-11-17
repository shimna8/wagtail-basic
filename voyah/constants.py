from django.utils.translation import gettext_lazy as _

ITEMS_PER_PAGE = 10
DEFAULT_MAXIMUM_ITEMS_PER_BLOCK = 0

PAGE_TARGETS = [                                 
        # 'info_page.InformationPage', 
    ]

IMAGE_ALIGNMENT_CHOICES = [
    ('right', _('Right'),),        
    ('left', _('Left'),),
]

BG_CHOICES = [
    ('transparent', _('Transparent Background'),),
    ('solid-blue', _('Solid Blue Background'),),   
    ('solid-gray', _('Solid Grey Background'),),      
    ('gradient', _('Gradient Background'),),
    ('pattern', _('Pattern Background'),),
]