# Wagtail Block Preview - Quick Reference

## 1. Basic Block with Preview (5 minutes)

### Step 1: Create Block Class
```python
# core/blocks/content_blocks.py
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class MyBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    image = ImageChooserBlock()
    
    class Meta:
        icon = 'image'
        label = 'My Block'
        template = 'blocks/my_block.html'
        preview_template = 'blocks/previews/my_block_preview.html'  # ← ADD THIS
```

### Step 2: Create Preview Template
```html
{# voyah/templates/blocks/previews/my_block_preview.html #}
<div class="block-preview">
    <div class="preview-header">
        <span class="preview-icon">🎨</span>
        <span class="preview-label">My Block</span>
    </div>
    <div class="preview-content">
        {% if value.title %}
            <div class="preview-title">{{ value.title }}</div>
        {% else %}
            <div class="preview-title preview-empty">No title</div>
        {% endif %}
    </div>
</div>

<style>
.block-preview {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border: 2px solid #007bff;
    border-radius: 8px;
    padding: 16px;
}
.preview-title {
    font-size: 16px;
    font-weight: 600;
    color: #333;
}
.preview-title.preview-empty {
    color: #999;
    font-style: italic;
}
</style>
```

### Step 3: Use in Model
```python
# home/models.py
from core.blocks import MyBlock

class HomePage(BasePage):
    body = StreamField([
        ('my_block', MyBlock()),
    ])
```

---

## 2. Preview Template Patterns

### Pattern 1: Simple Title + Status
```html
<div class="block-preview">
    <div class="preview-title">{{ value.title|default:"No title" }}</div>
    <div class="preview-meta">
        {% if value.image %}
            <span class="badge">📷 Image</span>
        {% else %}
            <span class="badge missing">No image</span>
        {% endif %}
    </div>
</div>
```

### Pattern 2: Title + Description + Badges
```html
<div class="block-preview">
    <div class="preview-title">{{ value.title }}</div>
    <div class="preview-description">
        {{ value.description|truncatewords:20|striptags }}
    </div>
    <div class="preview-meta">
        <span class="badge">{{ value.type }}</span>
        <span class="badge">{{ value.count }} items</span>
    </div>
</div>
```

### Pattern 3: Icon + Title + Status
```html
<div class="block-preview">
    <div class="preview-header">
        <span class="icon">{{ value.icon }}</span>
        <span class="title">{{ value.title }}</span>
    </div>
    <div class="preview-status">
        {% if value.is_complete %}
            <span class="status complete">✅ Complete</span>
        {% else %}
            <span class="status incomplete">⚠️ Incomplete</span>
        {% endif %}
    </div>
</div>
```

---

## 3. Common Meta Options

```python
class Meta:
    # Display
    icon = 'image'                    # Wagtail icon name
    label = 'My Block'                # Display name
    help_text = 'Block description'   # Help text in chooser
    
    # Templates
    template = 'blocks/my_block.html'                    # Frontend
    preview_template = 'blocks/previews/my_block_preview.html'  # Admin
    
    # Styling
    form_classname = 'struct-block my-block-form'  # CSS class for form
```

---

## 4. Wagtail Icon Names

```
Common icons:
- image, images
- link, document
- media, video, music
- list-ul, list-ol
- help, info, warning
- mail, phone
- star, heart, check
- code, pilcrow
- table, grid
- user, users
- settings, cog
```

Full list: https://wagtail.io/features/

---

## 5. Preview CSS Classes

```css
/* Container */
.block-preview { }

/* Header */
.preview-header { }
.preview-icon { }
.preview-label { }

/* Content */
.preview-content { }
.preview-title { }
.preview-title.preview-empty { }
.preview-description { }

/* Meta */
.preview-meta { }
.preview-badge { }
.preview-badge.preview-missing { }
```

---

## 6. Conditional Display in Preview

```html
{% if value.title %}
    <div class="preview-title">{{ value.title }}</div>
{% else %}
    <div class="preview-title preview-empty">No title</div>
{% endif %}

{% if value.image %}
    <span class="badge">📷 Image</span>
{% else %}
    <span class="badge missing">No image</span>
{% endif %}

{% if value.items %}
    <span class="badge">{{ value.items|length }} items</span>
{% endif %}
```

---

## 7. Truncating Content

```html
{# Truncate to 20 words #}
{{ value.description|truncatewords:20 }}

{# Remove HTML tags #}
{{ value.description|striptags }}

{# Combine both #}
{{ value.description|truncatewords:20|striptags }}

{# Truncate to 100 characters #}
{{ value.description|truncatechars:100 }}
```

---

## 8. Custom Preview Value (Advanced)

```python
class MyBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    items = blocks.ListBlock(blocks.CharBlock())
    
    def get_preview_value(self, value):
        """Add computed fields to preview."""
        preview_value = super().get_preview_value(value)
        
        # Add computed fields
        preview_value['item_count'] = len(value.get('items', []))
        preview_value['is_empty'] = preview_value['item_count'] == 0
        
        return preview_value
    
    class Meta:
        preview_template = 'blocks/previews/my_block_preview.html'
```

Then use in template:
```html
<span class="badge">{{ value.item_count }} items</span>
{% if value.is_empty %}
    <span class="badge missing">Empty</span>
{% endif %}
```

---

## 9. Responsive Preview CSS

```css
.block-preview {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border: 2px solid #007bff;
    border-radius: 8px;
    padding: 16px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.preview-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 10px;
}

.preview-badge {
    display: inline-block;
    background-color: #e7f3ff;
    color: #0056b3;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 500;
    white-space: nowrap;
}

.preview-badge.preview-missing {
    background-color: #ffe7e7;
    color: #b30000;
}

/* Mobile */
@media (max-width: 600px) {
    .block-preview {
        padding: 12px;
    }
    .preview-badge {
        font-size: 11px;
        padding: 3px 6px;
    }
}
```

---

## 10. File Structure

```
voyah/
└── templates/
    └── blocks/
        ├── my_block.html                    (Frontend)
        └── previews/
            └── my_block_preview.html        (Admin preview)

core/
└── blocks/
    └── content_blocks.py                    (Block definition)

home/
└── models.py                                (StreamField usage)
```

---

## 11. Testing Checklist

- [ ] Block appears in block chooser
- [ ] Preview displays in editor
- [ ] Preview updates when fields change
- [ ] All fields are editable
- [ ] Frontend renders correctly
- [ ] No console errors
- [ ] Mobile responsive
- [ ] Help text is clear

---

## 12. Troubleshooting

| Issue | Solution |
|-------|----------|
| Preview not showing | Check `preview_template` path |
| Preview looks broken | Check CSS syntax |
| Block not in chooser | Restart Django server |
| Fields not editable | Check block field definitions |
| Frontend broken | Check `template` path |

---

## 13. Resources

- Wagtail Docs: https://docs.wagtail.io/
- StreamField: https://docs.wagtail.io/en/stable/topics/streamfield.html
- Block Types: https://docs.wagtail.io/en/stable/topics/streamfield.html#built-in-block-types
- Admin Customization: https://docs.wagtail.io/en/stable/advanced_topics/customisation/admin_templates.html

---

## 14. Copy-Paste Template

```python
# Block class
class MyBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255)
    
    class Meta:
        icon = 'image'
        label = 'My Block'
        template = 'blocks/my_block.html'
        preview_template = 'blocks/previews/my_block_preview.html'
```

```html
{# Preview template #}
<div class="block-preview">
    <div class="preview-header">
        <span class="preview-icon">🎨</span>
        <span class="preview-label">My Block</span>
    </div>
    <div class="preview-content">
        <div class="preview-title">{{ value.title|default:"No title" }}</div>
    </div>
</div>

<style>
.block-preview {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border: 2px solid #007bff;
    border-radius: 8px;
    padding: 16px;
}
.preview-title {
    font-size: 16px;
    font-weight: 600;
    color: #333;
}
</style>
```

---

**Last Updated:** October 2025  
**Wagtail Version:** 6.0+  
**Django Version:** 5.0+

