# Wagtail Block Preview Guide

## Overview

This guide demonstrates how to create Wagtail StreamField blocks with live preview functionality in the admin interface. The `ImageWithContentBlock` is used as a complete example.

---

## 1. Block Class with Preview Support

### File: `core/blocks/content_blocks.py`

```python
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
```

### Key Meta Options:

- **`icon`**: Wagtail icon name (used in block chooser)
- **`label`**: Display name in block chooser
- **`template`**: Frontend rendering template
- **`preview_template`**: Admin preview template (NEW in Wagtail 6+)
- **`help_text`**: Description shown in block chooser
- **`form_classname`**: CSS class for form styling

---

## 2. Preview Template

### File: `voyah/templates/blocks/previews/image_with_content_preview.html`

The preview template is rendered in the block chooser and editor. It shows:
- Block icon and label
- Title preview
- Image status badge
- Image position indicator
- CTA button text
- Description preview (truncated)

**Features:**
- Responsive design
- Visual badges for missing fields
- Truncated description (2 lines max)
- Color-coded status indicators
- Mobile-friendly styling

---

## 3. Frontend Template

### File: `voyah/templates/blocks/image_with_content_block.html`

The frontend template renders the block on the website:
- Responsive grid layout (Bootstrap 5)
- Image positioning (left/right)
- Rich text description
- Optional CTA button
- Internal/external link support
- Lazy loading for images
- Custom styling

---

## 4. Using the Block in Models

### File: `home/models.py`

```python
from wagtail.fields import StreamField
from core.blocks import ImageWithContentBlock

class HomePage(BasePage):
    body = StreamField([
        ('image_with_content', ImageWithContentBlock()),
        # ... other blocks
    ], blank=True, use_json_field=True)
```

---

## 5. Advanced: Custom Preview Value

For more complex previews, you can override the `get_preview_value()` method:

```python
class ImageWithContentBlock(blocks.StructBlock):
    # ... fields ...
    
    def get_preview_value(self, value):
        """
        Customize the value passed to preview template.
        Useful for computed properties or data transformation.
        """
        preview_value = super().get_preview_value(value)
        
        # Add computed fields
        if value.get('description'):
            preview_value['description_length'] = len(value['description'])
        
        return preview_value
```

---

## 6. Admin Interface Features

### Block Chooser
When adding a new block, users see:
- Block icon (🖼️)
- Block label ("Image with Content")
- Help text
- Preview of the block

### Block Editor
When editing a block, users see:
- Form fields for all block properties
- Live preview (if preview_template is set)
- Collapsible form sections (if form_classname is set)
- Field help text

### Preview Display
The preview shows:
- Title (or "No title" if empty)
- Image status (📷 Image or ❌ No image)
- Image position (⬅️ Image Left or ➡️ Image Right)
- CTA button text (if set)
- Description preview (first 20 words, truncated to 2 lines)

---

## 7. Styling the Preview

The preview template includes inline CSS for:
- Gradient background
- Color-coded badges
- Responsive layout
- Mobile adjustments

You can customize by:
1. Modifying the inline `<style>` in the preview template
2. Adding CSS classes to your admin stylesheet
3. Using Wagtail's admin CSS customization

---

## 8. Best Practices

### ✅ DO:
- Use meaningful icons from Wagtail's icon set
- Provide clear help text for each field
- Show field status in preview (filled/empty)
- Truncate long content in preview
- Make preview responsive
- Use color coding for status

### ❌ DON'T:
- Use deprecated `StreamFieldPanel`
- Make preview templates too complex
- Show all data in preview (keep it concise)
- Use hardcoded colors (use CSS variables)
- Forget to test on mobile

---

## 9. Wagtail Icon Reference

Common icons for blocks:
- `image` - Image blocks
- `link` - Link blocks
- `document` - Document blocks
- `media` - Media blocks
- `help` - FAQ/Help blocks
- `list-ul` - List/Accordion blocks
- `mail` - Contact/Email blocks
- `pilcrow` - Text blocks
- `code` - Code blocks

Full list: https://wagtail.io/features/

---

## 10. Testing the Block

### In Admin:
1. Go to Pages > Edit HomePage
2. Click "Add block" in the body section
3. Select "Image with Content"
4. Fill in the fields
5. See the preview update in real-time
6. Save and publish

### On Frontend:
1. Visit the published page
2. Verify the block renders correctly
3. Test image positioning
4. Test CTA button links
5. Test on mobile devices

---

## 11. Troubleshooting

### Preview not showing?
- Check `preview_template` path is correct
- Verify template file exists
- Check Django template loader settings

### Preview looks broken?
- Check CSS syntax in preview template
- Verify template variables match block fields
- Check browser console for errors

### Block not appearing in chooser?
- Verify block is imported in `__init__.py`
- Check StreamField includes the block
- Restart Django development server

---

## 12. File Structure

```
voyah/
├── templates/
│   └── blocks/
│       ├── image_with_content_block.html      (Frontend)
│       └── previews/
│           └── image_with_content_preview.html (Admin preview)
│
core/
├── blocks/
│   ├── __init__.py
│   ├── content_blocks.py                      (Block definition)
│   └── hero_blocks.py
│
home/
└── models.py                                  (StreamField usage)
```

---

## 13. Next Steps

1. **Create more blocks** with preview templates
2. **Customize preview styling** to match your brand
3. **Add computed fields** to preview using `get_preview_value()`
4. **Create block templates** for different page types
5. **Test thoroughly** in admin and on frontend

---

## References

- Wagtail Documentation: https://docs.wagtail.io/
- StreamField: https://docs.wagtail.io/en/stable/topics/streamfield.html
- Block Types: https://docs.wagtail.io/en/stable/topics/streamfield.html#built-in-block-types
- Admin Customization: https://docs.wagtail.io/en/stable/advanced_topics/customisation/admin_templates.html

