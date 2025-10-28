# Organized Core App Structure Guide

**Clean, scalable, and professional organization of blocks, mixins, and models**

---

## 🎯 Overview

The core app is now organized into separate, focused modules:

```
core/
├── models.py              ← Page models only (BasePage, HomePage)
├── mixins.py              ← Reusable mixins (SEOMixin)
├── blocks/                ← All blocks organized by type
│   ├── __init__.py       ← Exports all blocks
│   ├── hero_blocks.py    ← Hero/banner blocks
│   └── content_blocks.py ← Content blocks
├── admin.py
├── apps.py
├── tests.py
├── views.py
└── migrations/
```

---

## 📁 File Structure Details

### 1. `core/models.py` (110 lines)

**Purpose**: Contains only page models

**Contents**:
- `BasePage` - Abstract base class with hero + body StreamFields
- `HomePage` - Home page model

**Key Features**:
- Clean imports from blocks and mixins
- No block definitions (kept separate)
- Easy to read and maintain

**Example**:
```python
from core.blocks import BannerBlock, FAQBlock
from core.mixins import SEOMixin

class BasePage(SEOMixin, Page):
    hero = StreamField([...])
    body = StreamField([...])

class HomePage(BasePage):
    pass
```

---

### 2. `core/mixins.py` (60 lines)

**Purpose**: Reusable model mixins

**Contents**:
- `SEOMixin` - Extended SEO fields (meta description, og_image, twitter, canonical URL, no-index, no-follow)

**Key Features**:
- Abstract model (can be mixed into any page)
- Includes admin panels configuration
- Reusable across all page types

**Example**:
```python
class SEOMixin(models.Model):
    meta_description = models.CharField(max_length=160)
    og_image = models.ForeignKey(Image, ...)
    twitter_card_type = models.CharField(...)
    canonical_url = models.URLField(...)
    no_index = models.BooleanField(...)
    no_follow = models.BooleanField(...)
    
    class Meta:
        abstract = True
```

---

### 3. `core/blocks/__init__.py` (40 lines)

**Purpose**: Central export point for all blocks

**Contents**:
- Imports all blocks from submodules
- Re-exports them for easy access

**Key Features**:
- Single import point: `from core.blocks import BannerBlock`
- Easy to add new blocks
- Clear organization

**Example**:
```python
from .hero_blocks import BannerBlock, SliderBlock, VideoBlock, ParallaxBlock
from .content_blocks import ImageWithContentBlock, FAQBlock, AccordionBlock, GetInTouchBlock

__all__ = [
    'BannerBlock',
    'SliderBlock',
    'VideoBlock',
    'ParallaxBlock',
    'ImageWithContentBlock',
    'FAQBlock',
    'AccordionBlock',
    'GetInTouchBlock',
]
```

---

### 4. `core/blocks/hero_blocks.py` (180 lines)

**Purpose**: Hero/banner blocks for page headers

**Contents**:
- `BannerBlock` - Static banner with responsive images
- `SliderBlock` - Image carousel
- `VideoBlock` - Video banner with poster image
- `ParallaxBlock` - Parallax scrolling effect

**Key Features**:
- Responsive image support
- Customizable display options
- CTA button support
- Professional documentation

**Example**:
```python
class BannerBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock()
    height = blocks.ChoiceBlock(choices=[...])
    
    class Meta:
        icon = 'image'
        label = 'Banner'
        template = 'blocks/banner_block.html'
```

---

### 5. `core/blocks/content_blocks.py` (200 lines)

**Purpose**: Content blocks for page body sections

**Contents**:
- `ImageWithContentBlock` - Image with text and CTA
- `FAQBlock` - Frequently Asked Questions
- `AccordionBlock` - Expandable content sections
- `GetInTouchBlock` - Contact information and CTA

**Key Features**:
- Rich text support
- Flexible layouts
- Multiple configuration options
- Professional styling

**Example**:
```python
class ImageWithContentBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    description = blocks.RichTextBlock()
    image = ImageChooserBlock()
    image_position = blocks.ChoiceBlock(choices=[...])
    
    class Meta:
        icon = 'image'
        label = 'Image with Content'
        template = 'blocks/image_with_content_block.html'
```

---

## 🚀 How to Use

### Import Blocks

```python
# Option 1: Import from core.blocks (recommended)
from core.blocks import BannerBlock, FAQBlock, ImageWithContentBlock

# Option 2: Import from specific module
from core.blocks.hero_blocks import BannerBlock
from core.blocks.content_blocks import FAQBlock
```

### Import Mixins

```python
from core.mixins import SEOMixin
```

### Import Models

```python
from core.models import BasePage, HomePage
```

### Create New Page Type

```python
from core.models import BasePage

class ServicePage(BasePage):
    """Service page with hero and flexible content blocks."""
    
    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Pages"
```

---

## 📊 Statistics

| File | Lines | Purpose |
|------|-------|---------|
| `models.py` | 110 | Page models |
| `mixins.py` | 60 | Reusable mixins |
| `blocks/__init__.py` | 40 | Block exports |
| `blocks/hero_blocks.py` | 180 | Hero blocks |
| `blocks/content_blocks.py` | 200 | Content blocks |
| **Total** | **590** | **All organized** |

---

## 🎯 Benefits

✅ **Clean Separation** - Each file has a single responsibility  
✅ **Easy to Find** - Know exactly where to look for blocks  
✅ **Scalable** - Add new blocks without cluttering models.py  
✅ **Maintainable** - Easy to modify individual blocks  
✅ **Professional** - Industry-standard organization  
✅ **Testable** - Easy to test individual blocks  
✅ **Reusable** - Mixins can be used in any model  

---

## 🔧 Adding New Blocks

### Step 1: Create Block in Appropriate File

If it's a hero block, add to `core/blocks/hero_blocks.py`:

```python
class MyHeroBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    # ... more fields
    
    class Meta:
        icon = 'image'
        label = 'My Hero Block'
        template = 'blocks/my_hero_block.html'
```

If it's a content block, add to `core/blocks/content_blocks.py`:

```python
class MyContentBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    # ... more fields
    
    class Meta:
        icon = 'document'
        label = 'My Content Block'
        template = 'blocks/my_content_block.html'
```

### Step 2: Export from `core/blocks/__init__.py`

```python
from .hero_blocks import MyHeroBlock
# or
from .content_blocks import MyContentBlock

__all__ = [
    # ... existing blocks
    'MyHeroBlock',  # or 'MyContentBlock'
]
```

### Step 3: Add to BasePage StreamField

```python
# In core/models.py
hero = StreamField([
    # ... existing blocks
    ('my_hero', MyHeroBlock()),
])
# or
body = StreamField([
    # ... existing blocks
    ('my_content', MyContentBlock()),
])
```

### Step 4: Create Template

Create `templates/blocks/my_hero_block.html` or `templates/blocks/my_content_block.html`

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🎓 Best Practices

### 1. Keep Blocks Focused
Each block should do one thing well. Don't create mega-blocks.

### 2. Use Descriptive Names
- `ImageWithContentBlock` ✅
- `Block1` ❌

### 3. Add Help Text
Help editors understand what each field does:

```python
title = blocks.CharBlock(
    help_text="Section title (max 60 characters)"
)
```

### 4. Set Reasonable Limits
Use `min_num` and `max_num` for ListBlocks:

```python
items = blocks.ListBlock(ItemBlock(), min_num=1, max_num=20)
```

### 5. Document Your Blocks
Add docstrings explaining what the block does:

```python
class MyBlock(blocks.StructBlock):
    """
    My custom block.
    
    Perfect for: Use cases
    Features: What it does
    """
```

---

## 📚 File Organization Summary

```
core/
├── models.py
│   └── Contains: BasePage, HomePage
│       Purpose: Page models only
│       Size: ~110 lines
│
├── mixins.py
│   └── Contains: SEOMixin
│       Purpose: Reusable model mixins
│       Size: ~60 lines
│
└── blocks/
    ├── __init__.py
    │   └── Contains: Block exports
    │       Purpose: Central import point
    │       Size: ~40 lines
    │
    ├── hero_blocks.py
    │   └── Contains: BannerBlock, SliderBlock, VideoBlock, ParallaxBlock
    │       Purpose: Hero/banner blocks
    │       Size: ~180 lines
    │
    └── content_blocks.py
        └── Contains: ImageWithContentBlock, FAQBlock, AccordionBlock, GetInTouchBlock
            Purpose: Content blocks
            Size: ~200 lines
```

---

## ✅ Verification

To verify the structure is working:

```bash
# Test imports
python manage.py shell -c "
from core.blocks import BannerBlock, FAQBlock
from core.mixins import SEOMixin
from core.models import BasePage, HomePage
print('✅ All imports successful!')
"
```

---

## 🎉 You're All Set!

Your core app is now organized, clean, and professional. 

**Next Steps**:
1. Run migrations: `python manage.py migrate`
2. Test in admin: `python manage.py runserver`
3. Create new page types as needed
4. Add new blocks following the pattern

---

**Created**: 2024-10-25  
**Version**: 1.0  
**Status**: ✅ Complete & Organized  

