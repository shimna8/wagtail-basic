# Advanced Wagtail Block Examples with Preview

This document shows advanced patterns for creating blocks with rich preview functionality.

---

## Example 1: Block with Custom Preview Value

```python
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class AdvancedImageBlock(blocks.StructBlock):
    """Block with computed preview values."""
    
    title = blocks.CharBlock(max_length=255)
    description = blocks.RichTextBlock()
    image = ImageChooserBlock()
    
    def get_preview_value(self, value):
        """
        Transform block value for preview template.
        Useful for computed properties or data enrichment.
        """
        preview_value = super().get_preview_value(value)
        
        # Add computed fields
        if value.get('description'):
            # Count words in description
            word_count = len(value['description'].split())
            preview_value['word_count'] = word_count
            preview_value['has_long_description'] = word_count > 50
        
        # Add image info
        if value.get('image'):
            preview_value['has_image'] = True
            preview_value['image_title'] = value['image'].title
        
        return preview_value
    
    class Meta:
        icon = 'image'
        label = 'Advanced Image Block'
        template = 'blocks/advanced_image_block.html'
        preview_template = 'blocks/previews/advanced_image_preview.html'
```

---

## Example 2: Nested Block with Preview

```python
class TestimonialBlock(blocks.StructBlock):
    """Testimonial with author info."""
    
    class AuthorBlock(blocks.StructBlock):
        name = blocks.CharBlock(max_length=100)
        title = blocks.CharBlock(max_length=100, required=False)
        image = ImageChooserBlock(required=False)
        
        class Meta:
            label = 'Author'
    
    quote = blocks.RichTextBlock()
    author = AuthorBlock()
    rating = blocks.IntegerBlock(min_value=1, max_value=5, default=5)
    
    class Meta:
        icon = 'openquote'
        label = 'Testimonial'
        template = 'blocks/testimonial_block.html'
        preview_template = 'blocks/previews/testimonial_preview.html'
```

---

## Example 3: Block with Conditional Fields

```python
class CTABlock(blocks.StructBlock):
    """Call-to-action with flexible link options."""
    
    heading = blocks.CharBlock(max_length=255)
    description = blocks.RichTextBlock()
    
    # Link options
    link_type = blocks.ChoiceBlock(
        choices=[
            ('internal', 'Internal Page'),
            ('external', 'External URL'),
            ('email', 'Email'),
            ('phone', 'Phone'),
        ],
        default='internal'
    )
    
    link_page = blocks.PageChooserBlock(required=False)
    link_url = blocks.URLBlock(required=False)
    link_email = blocks.EmailBlock(required=False)
    link_phone = blocks.CharBlock(required=False, max_length=20)
    
    button_text = blocks.CharBlock(max_length=50, default='Learn More')
    button_style = blocks.ChoiceBlock(
        choices=[
            ('primary', 'Primary'),
            ('secondary', 'Secondary'),
            ('outline', 'Outline'),
        ],
        default='primary'
    )
    
    def get_preview_value(self, value):
        """Add link preview info."""
        preview_value = super().get_preview_value(value)
        
        link_type = value.get('link_type', 'internal')
        preview_value['link_display'] = self._get_link_display(value, link_type)
        
        return preview_value
    
    def _get_link_display(self, value, link_type):
        """Get human-readable link display."""
        if link_type == 'internal' and value.get('link_page'):
            return f"→ {value['link_page'].title}"
        elif link_type == 'external' and value.get('link_url'):
            return f"🔗 {value['link_url']}"
        elif link_type == 'email' and value.get('link_email'):
            return f"✉️ {value['link_email']}"
        elif link_type == 'phone' and value.get('link_phone'):
            return f"📞 {value['link_phone']}"
        return "No link set"
    
    class Meta:
        icon = 'link'
        label = 'Call to Action'
        template = 'blocks/cta_block.html'
        preview_template = 'blocks/previews/cta_preview.html'
```

---

## Example 4: Block with List Items

```python
class FeaturesBlock(blocks.StructBlock):
    """Features list with icons."""
    
    class FeatureItem(blocks.StructBlock):
        icon = blocks.ChoiceBlock(
            choices=[
                ('star', '⭐ Star'),
                ('check', '✅ Check'),
                ('lightning', '⚡ Lightning'),
                ('heart', '❤️ Heart'),
            ]
        )
        title = blocks.CharBlock(max_length=100)
        description = blocks.RichTextBlock()
        
        class Meta:
            label = 'Feature'
    
    heading = blocks.CharBlock(max_length=255)
    features = blocks.ListBlock(
        FeatureItem(),
        min_num=1,
        max_num=6
    )
    
    def get_preview_value(self, value):
        """Add feature count to preview."""
        preview_value = super().get_preview_value(value)
        preview_value['feature_count'] = len(value.get('features', []))
        return preview_value
    
    class Meta:
        icon = 'list-ul'
        label = 'Features'
        template = 'blocks/features_block.html'
        preview_template = 'blocks/previews/features_preview.html'
```

---

## Example 5: Preview Template with Conditional Display

```html
{# blocks/previews/cta_preview.html #}
<div class="block-preview cta-preview">
    <div class="preview-header">
        <span class="preview-icon">🎯</span>
        <span class="preview-label">Call to Action</span>
    </div>
    
    <div class="preview-content">
        {% if value.heading %}
            <div class="preview-title">{{ value.heading }}</div>
        {% else %}
            <div class="preview-title preview-empty">No heading</div>
        {% endif %}
        
        <div class="preview-meta">
            <span class="preview-badge">
                Button: {{ value.button_text|default:"Learn More" }}
            </span>
            
            <span class="preview-badge">
                Style: {{ value.button_style|default:"primary" }}
            </span>
            
            {% if value.link_display %}
                <span class="preview-badge preview-link">
                    {{ value.link_display }}
                </span>
            {% else %}
                <span class="preview-badge preview-missing">
                    No link configured
                </span>
            {% endif %}
        </div>
        
        {% if value.description %}
            <div class="preview-description">
                {{ value.description|truncatewords:15|striptags }}
            </div>
        {% endif %}
    </div>
</div>

<style>
.block-preview.cta-preview {
    background: linear-gradient(135deg, #fff5e6 0%, #ffe6cc 100%);
    border: 2px solid #ff9800;
    border-radius: 8px;
    padding: 16px;
}

.preview-badge.preview-link {
    background-color: #e8f5e9;
    color: #2e7d32;
}

.preview-badge.preview-missing {
    background-color: #ffebee;
    color: #c62828;
}
</style>
```

---

## Example 6: Block with Media Gallery

```python
class GalleryBlock(blocks.StructBlock):
    """Image gallery with captions."""
    
    class GalleryItem(blocks.StructBlock):
        image = ImageChooserBlock()
        caption = blocks.CharBlock(max_length=255, required=False)
        
        class Meta:
            label = 'Gallery Item'
    
    title = blocks.CharBlock(max_length=255)
    images = blocks.ListBlock(
        GalleryItem(),
        min_num=1,
        max_num=12
    )
    columns = blocks.IntegerBlock(
        min_value=1,
        max_value=4,
        default=3
    )
    
    def get_preview_value(self, value):
        """Add gallery stats to preview."""
        preview_value = super().get_preview_value(value)
        images = value.get('images', [])
        preview_value['image_count'] = len(images)
        preview_value['first_image'] = images[0] if images else None
        return preview_value
    
    class Meta:
        icon = 'image'
        label = 'Image Gallery'
        template = 'blocks/gallery_block.html'
        preview_template = 'blocks/previews/gallery_preview.html'
```

---

## Example 7: Block with Form Styling

```python
class FormBlock(blocks.StructBlock):
    """Contact form block."""
    
    title = blocks.CharBlock(max_length=255)
    description = blocks.RichTextBlock()
    form_id = blocks.ChoiceBlock(
        choices=[
            ('contact', 'Contact Form'),
            ('newsletter', 'Newsletter Signup'),
            ('demo', 'Demo Request'),
        ]
    )
    
    class Meta:
        icon = 'form'
        label = 'Form'
        template = 'blocks/form_block.html'
        preview_template = 'blocks/previews/form_preview.html'
        form_classname = 'struct-block form-block-form'
```

---

## Best Practices Summary

### ✅ DO:
1. Use `get_preview_value()` for computed properties
2. Show field status (filled/empty) in preview
3. Truncate long content in preview
4. Use color coding for different block types
5. Make previews responsive
6. Test preview on mobile

### ❌ DON'T:
1. Make preview templates too complex
2. Show all data in preview
3. Use hardcoded colors
4. Forget to handle missing fields
5. Make preview slower than necessary
6. Use deprecated Wagtail APIs

---

## Testing Checklist

- [ ] Block appears in block chooser
- [ ] Preview displays correctly
- [ ] Preview updates when fields change
- [ ] All fields are editable
- [ ] Frontend template renders correctly
- [ ] Block works on mobile
- [ ] Help text is clear
- [ ] Icon is appropriate
- [ ] No console errors
- [ ] Performance is acceptable

