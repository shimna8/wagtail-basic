# Hero Blocks - Quick Reference Card

## 🎯 Overview

Your Wagtail project now has a flexible hero system with 4 block types that editors can choose from.

---

## 📦 Available Hero Blocks

### 1. BannerBlock - Static Banner
**Best for**: Simple hero sections with one image

**Fields**:
- Title, Subtitle
- Images: Desktop, Tablet, Mobile
- Height: Small/Medium/Large/Full
- Overlay: 0-100%
- Text: Alignment (L/C/R), Color (W/B)
- CTA: Text, Link (internal/external)

**Use case**: Homepage, About page, simple landing pages

---

### 2. SliderBlock - Image Carousel
**Best for**: Showcasing multiple products, features, or messages

**Fields**:
- Slides (2-10):
  - Each slide: Title, Subtitle, Images (D/T/M), CTA
- Autoplay: On/Off, Speed (1000-10000ms)
- Navigation: Arrows (Y/N), Dots (Y/N)
- Height, Overlay, Text alignment

**Use case**: Product pages, portfolio, featured content

---

### 3. VideoBlock - Video Banner
**Best for**: Engaging video backgrounds

**Fields**:
- Video URL (YouTube/Vimeo)
- Poster Image (fallback)
- Title, Subtitle, CTA
- Video: Autoplay, Loop, Muted, Controls
- Height, Overlay, Text alignment

**Use case**: Landing pages, promotional pages, brand pages

---

### 4. ParallaxBlock - Parallax Scrolling
**Best for**: Modern, engaging visual effects

**Fields**:
- Background Image (large, 2400x1200px)
- Title, Subtitle, CTA
- Parallax Speed: Slow/Medium/Fast
- Height, Overlay, Text alignment

**Use case**: Modern landing pages, creative portfolios

---

## 🎨 Common Settings

All blocks share these settings:

| Setting | Options | Default |
|---------|---------|---------|
| Height | Small (400px), Medium (600px), Large (800px), Full Screen | Medium |
| Overlay Opacity | 0-100% | 30% |
| Text Alignment | Left, Center, Right | Center |
| Text Color | White, Black | White |

---

## 📱 Responsive Images

### Recommended Sizes:

| Device | Size | Aspect Ratio |
|--------|------|--------------|
| Desktop | 1920x600px | 16:5 |
| Tablet | 1024x600px | 16:9 (approx) |
| Mobile | 768x600px | 4:3 (approx) |

### Fallback Behavior:
- If mobile image not provided → uses desktop image
- If tablet image not provided → uses desktop image

---

## 🔧 How to Use

### In Wagtail Admin:

1. **Edit any page** (e.g., HomePage)
2. **Find "Hero" field** in Content tab
3. **Click "Add"** and choose block type:
   - Banner
   - Slider
   - Video
   - Parallax
4. **Fill in fields**
5. **Save and publish**

### In Code:

```python
# Create a new page type
from core.models import BasePage

class MyPage(BasePage):
    # Add your custom fields
    intro = models.TextField()
    
    content_panels = BasePage.content_panels + [
        FieldPanel('intro'),
    ]
```

That's it! The page automatically gets hero functionality.

---

## 🎓 Best Practices

### Image Optimization
✅ Use WebP format when possible
✅ Compress images before upload
✅ Use appropriate dimensions
✅ Add descriptive alt text

### Content Guidelines
✅ Keep titles short (max 60 chars)
✅ Keep subtitles concise (max 100 chars)
✅ Use clear CTA text ("Learn More", "Get Started", etc.)
✅ Test on mobile devices

### Performance
✅ Limit slider to 5-7 slides max
✅ Use poster images for videos
✅ Enable lazy loading for below-fold content
✅ Optimize video file sizes

### Accessibility
✅ Ensure text contrast is readable
✅ Provide alt text for images
✅ Make CTAs keyboard accessible
✅ Test with screen readers

---

## 🚀 Quick Start Checklist

- [ ] Core app created and added to INSTALLED_APPS
- [ ] Migrations run successfully
- [ ] Create block templates (banner_block.html, etc.)
- [ ] Add CSS styles for hero sections
- [ ] Add JavaScript for slider/video/parallax
- [ ] Update base template to render hero
- [ ] Test in Wagtail admin
- [ ] Upload test images
- [ ] Create a test page with each hero type
- [ ] Test on mobile, tablet, desktop
- [ ] Optimize images and performance

---

## 📝 Template Structure

### Minimal Template Example:

```django
{# templates/home/home_page.html #}
{% extends "base.html" %}
{% load wagtailcore_tags %}

{% block hero %}
    {% if page.has_hero %}
        {% for block in page.hero %}
            {% include_block block %}
        {% endfor %}
    {% endif %}
{% endblock %}

{% block content %}
    <div class="container">
        {% for block in page.body %}
            {% include_block block %}
        {% endfor %}
    </div>
{% endblock %}
```

---

## 🎯 Common Use Cases

### Homepage
**Recommended**: BannerBlock or SliderBlock
**Why**: Clear, impactful first impression

### Product Page
**Recommended**: SliderBlock
**Why**: Show multiple product images

### About Page
**Recommended**: VideoBlock or BannerBlock
**Why**: Tell your story visually

### Landing Page
**Recommended**: ParallaxBlock or VideoBlock
**Why**: Engaging, modern feel

### Blog Post
**Recommended**: BannerBlock or none
**Why**: Simple, focused on content

---

## 🔍 Troubleshooting

### Hero not showing?
- Check `page.has_hero()` returns True
- Verify template includes hero block
- Check CSS is loaded

### Images not responsive?
- Verify all image sizes uploaded
- Check `<picture>` element in template
- Test media queries in CSS

### Slider not working?
- Check JavaScript is loaded
- Verify slider.js is included
- Check browser console for errors

### Video not playing?
- Verify video URL is correct
- Check autoplay requires muted=True
- Test with poster image fallback

---

## 📚 Related Documentation

- **CORE_MODELS_SETUP.md** - Complete setup guide
- **Wagtail Docs** - https://docs.wagtail.org/
- **StreamField Guide** - https://docs.wagtail.org/en/stable/topics/streamfield.html

---

## 💡 Tips & Tricks

### Tip 1: Reuse Blocks
You can use the same blocks in other StreamFields:

```python
from core.models import BannerBlock

body = StreamField([
    ('banner', BannerBlock()),  # Reuse in body!
    ('paragraph', blocks.RichTextBlock()),
])
```

### Tip 2: Customize Blocks
Extend blocks for specific needs:

```python
class CustomBannerBlock(BannerBlock):
    # Add extra fields
    badge_text = blocks.CharBlock(required=False)
```

### Tip 3: Conditional Display
Show different heroes based on conditions:

```python
def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    if request.user.is_authenticated:
        context['show_special_hero'] = True
    return context
```

### Tip 4: Analytics
Track hero interactions:

```html
<a href="{{ cta_url }}" 
   onclick="gtag('event', 'hero_cta_click', {'hero_type': '{{ hero_type }}'})">
    {{ cta_text }}
</a>
```

---

## ✅ Success Criteria

Your hero system is working when:

✅ Editors can choose hero type in admin
✅ All 4 hero types render correctly
✅ Responsive images work on all devices
✅ Slider autoplay and navigation work
✅ Video embeds play correctly
✅ Parallax effect is smooth
✅ CTAs link to correct pages
✅ SEO fields are populated
✅ Page loads quickly (<3 seconds)
✅ Accessible to screen readers

---

**Created**: 2024-10-25  
**Version**: 1.0  
**Wagtail**: 6.3+  
**Django**: 5.1+  

