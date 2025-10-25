# Core Models Setup - Complete Documentation

## ✅ What Was Created

### 1. Core App Structure
```
core/
├── __init__.py
├── admin.py
├── apps.py
├── models.py          # ⭐ Main file with all blocks and base models
├── migrations/
├── tests.py
└── views.py
```

### 2. Models and Blocks Created

#### **Hero/Banner Blocks** (StreamField Components)

1. **BannerBlock** - Static banner with responsive images
   - Desktop, tablet, and mobile image support
   - Configurable height (small, medium, large, full)
   - Overlay opacity control
   - Text alignment and color options
   - Call-to-action button with internal/external links

2. **SliderBlock** - Image carousel/slider
   - Multiple slides (2-10 slides)
   - Each slide has responsive images (desktop, tablet, mobile)
   - Individual title, subtitle, and CTA per slide
   - Autoplay settings (on/off, speed)
   - Navigation arrows and dots (show/hide)
   - Configurable height and overlay

3. **VideoBlock** - Video banner
   - YouTube/Vimeo embed support
   - Poster/fallback image
   - Video controls (autoplay, loop, muted, controls)
   - Overlay content (title, subtitle, CTA)
   - Configurable height and overlay

4. **ParallaxBlock** - Parallax scrolling banner
   - Large background image for parallax effect
   - Parallax speed control (slow, medium, fast)
   - Title, subtitle, and CTA
   - Configurable height and overlay

#### **SEOMixin** - Extended SEO Fields

Adds to Wagtail's built-in SEO fields:
- **og_image** - Social media sharing image
- **twitter_card_type** - Twitter card type selection
- **canonical_url** - Custom canonical URL
- **no_index** - Prevent search engine indexing
- **no_follow** - Prevent following links

**Note**: Wagtail's Page model already includes `seo_title` and `search_description`, so we don't duplicate those.

#### **BasePage** - Abstract Base Page Class

- Inherits from SEOMixin and Wagtail's Page
- Includes flexible `hero` StreamField (max 1 block)
- Editors can choose: Banner, Slider, Video, Parallax, or none
- Helper methods:
  - `has_hero()` - Check if hero exists
  - `get_hero_type()` - Get hero type name
  - `get_hero_data()` - Get hero block data

---

## 📁 File Structure

### Updated Files

1. **`core/models.py`** (609 lines)
   - All hero blocks
   - SEOMixin
   - BasePage

2. **`mywagtailproject/settings/base.py`**
   - Added `'core'` to INSTALLED_APPS

3. **`home/models.py`**
   - Updated HomePage to inherit from BasePage
   - Added body StreamField for page content

4. **Migrations Created**
   - `home/migrations/0003_alter_homepage_options_homepage_body_and_more.py`

---

## 🎨 Features by Block Type

### BannerBlock Features
✅ Responsive images (desktop, tablet, mobile)
✅ Height options (400px, 600px, 800px, full screen)
✅ Overlay opacity (0-100%)
✅ Text alignment (left, center, right)
✅ Text color (white, black)
✅ Title and subtitle
✅ CTA button (internal page or external URL)

### SliderBlock Features
✅ 2-10 slides
✅ Each slide has responsive images
✅ Individual content per slide
✅ Autoplay with configurable speed
✅ Navigation arrows (show/hide)
✅ Navigation dots (show/hide)
✅ All banner features per slide

### VideoBlock Features
✅ YouTube/Vimeo embed
✅ Poster/fallback image
✅ Autoplay, loop, muted options
✅ Show/hide controls
✅ Overlay content
✅ CTA button

### ParallaxBlock Features
✅ Parallax scrolling effect
✅ Speed control (slow, medium, fast)
✅ Large background image
✅ Overlay content
✅ CTA button

---

## 🚀 Usage Examples

### Example 1: HomePage with Banner

```python
# home/models.py
from core.models import BasePage

class HomePage(BasePage):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ], blank=True, use_json_field=True)
    
    content_panels = BasePage.content_panels + [
        FieldPanel('body'),
    ]
```

### Example 2: Product Page with Slider

```python
# products/models.py
from core.models import BasePage

class ProductPage(BasePage):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()
    
    content_panels = BasePage.content_panels + [
        FieldPanel('price'),
        FieldPanel('description'),
    ]
```

### Example 3: About Page with Video

```python
# about/models.py
from core.models import BasePage

class AboutPage(BasePage):
    intro = models.TextField()
    team_members = StreamField([...])
    
    content_panels = BasePage.content_panels + [
        FieldPanel('intro'),
        FieldPanel('team_members'),
    ]
```

### Example 4: Landing Page with Parallax

```python
# landing/models.py
from core.models import BasePage

class LandingPage(BasePage):
    features = StreamField([...])
    testimonials = StreamField([...])
    
    content_panels = BasePage.content_panels + [
        FieldPanel('features'),
        FieldPanel('testimonials'),
    ]
```

---

## 📋 Admin Panel Organization

When editing a page in Wagtail admin, you'll see:

### Content Tab
- **Hero** - Choose one: Banner, Slider, Video, Parallax, or none
- **Body** (or other content fields specific to page type)

### Promote Tab
- **SEO Title** (Wagtail built-in)
- **Search Description** (Wagtail built-in)
- **Social Media**
  - Social media image
  - Twitter card type
- **Advanced SEO**
  - Canonical URL
  - No index
  - No follow

### Settings Tab
- Standard Wagtail settings (slug, publish date, etc.)

---

## 🎯 Next Steps

### 1. Create Block Templates

You need to create templates for each block type:

```
mywagtailproject/templates/blocks/
├── banner_block.html
├── slider_block.html
├── video_block.html
└── parallax_block.html
```

### 2. Update Base Template

Update your base template to render the hero section:

```django
{# mywagtailproject/templates/base.html #}
{% block hero %}
    {% if page.has_hero %}
        {% for block in page.hero %}
            {% include_block block %}
        {% endfor %}
    {% endif %}
{% endblock %}
```

### 3. Add CSS Styles

Create CSS for hero sections:

```
mywagtailproject/static/css/
├── hero.css          # Hero/banner styles
└── slider.css        # Slider-specific styles
```

### 4. Add JavaScript

For slider and video functionality:

```
mywagtailproject/static/js/
├── slider.js         # Slider functionality
├── video-hero.js     # Video embed handling
└── parallax.js       # Parallax effect
```

### 5. Create More Page Types

Create additional page types that inherit from BasePage:

```bash
# Example: Create a blog app
python manage.py startapp blog

# In blog/models.py
from core.models import BasePage

class BlogIndexPage(BasePage):
    intro = RichTextField(blank=True)
    # ... more fields

class BlogPage(BasePage):
    date = models.DateField("Post date")
    body = RichTextField()
    # ... more fields
```

---

## 🔧 Customization Tips

### Adding New Hero Types

To add a new hero type (e.g., SplitScreenBlock):

1. Create the block in `core/models.py`:
```python
class SplitScreenBlock(blocks.StructBlock):
    # ... fields
    class Meta:
        icon = 'image'
        label = 'Split Screen'
        template = 'blocks/split_screen_block.html'
```

2. Add to BasePage hero field:
```python
hero = StreamField([
    ('banner', BannerBlock()),
    ('slider', SliderBlock()),
    ('video', VideoBlock()),
    ('parallax', ParallaxBlock()),
    ('split_screen', SplitScreenBlock()),  # NEW
], ...)
```

3. Create template and run migrations

### Modifying Existing Blocks

To add fields to existing blocks, edit the block class in `core/models.py` and run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Page-Specific Mixins

Create additional mixins for specific functionality:

```python
# core/models.py

class ContactFormMixin(models.Model):
    """Add contact form fields to any page"""
    show_contact_form = models.BooleanField(default=False)
    form_title = models.CharField(max_length=255, blank=True)
    
    class Meta:
        abstract = True

# Usage
class ContactPage(ContactFormMixin, BasePage):
    pass
```

---

## ✅ Verification Checklist

- [x] Core app created
- [x] Core app added to INSTALLED_APPS
- [x] All blocks defined (Banner, Slider, Video, Parallax)
- [x] SEOMixin created
- [x] BasePage created
- [x] HomePage updated to use BasePage
- [x] Migrations created and applied
- [ ] Block templates created
- [ ] CSS styles added
- [ ] JavaScript functionality added
- [ ] Base template updated

---

## 📊 Summary Statistics

**Files Created**: 1 app (core)
**Models Created**: 1 abstract model (BasePage), 1 mixin (SEOMixin)
**Blocks Created**: 4 hero blocks (Banner, Slider, Video, Parallax)
**Fields Added to HomePage**: 7 fields (hero, body, og_image, twitter_card_type, canonical_url, no_index, no_follow)
**Lines of Code**: ~600 lines in core/models.py

---

## 🎓 Best Practices Followed

✅ **Separation of Concerns** - Core app for reusable components
✅ **DRY Principle** - Single BasePage for all pages
✅ **Flexibility** - StreamField allows choosing hero type
✅ **Responsive Design** - Mobile, tablet, desktop images
✅ **SEO Optimization** - Extended SEO fields
✅ **User-Friendly** - Clear help text and labels
✅ **Extensible** - Easy to add new blocks or mixins
✅ **Abstract Models** - Proper use of abstract base classes

---

**Created**: 2024-10-25
**Django Version**: 5.1+
**Wagtail Version**: 6.3+
**Python Version**: 3.10+

