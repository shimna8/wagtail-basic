# Content Blocks Guide

**Version**: 1.0  
**Created**: 2024-10-25  
**Wagtail**: 6.3+  
**Django**: 5.1+  

---

## 🎯 Overview

Your Wagtail project now has a flexible content block system with 4 reusable blocks that editors can mix and match to build pages.

---

## 📦 Available Content Blocks

### 1. Image with Content Block

**Purpose**: Display an image alongside text content with optional CTA button.

**Best for**:
- Feature sections
- Service descriptions
- Product highlights
- Team member profiles
- Case studies

**Fields**:
- **Title** (required) - Section heading
- **Description** (required) - Rich text content with formatting
- **Image** (required) - Image file (recommended: 600x400px)
- **Image Position** - Left or Right (default: Left)
- **Link Text** (optional) - CTA button text
- **Link Page** (optional) - Internal page link
- **Link External** (optional) - External URL

**Example Use Cases**:
```
Title: "Why Choose Us"
Description: "We provide world-class service..."
Image: Company photo
Position: Left
Link: "Learn More" → Services page
```

---

### 2. FAQ Block

**Purpose**: Display frequently asked questions in an organized format.

**Best for**:
- FAQ pages
- Product pages
- Support sections
- Help documentation
- Common questions

**Fields**:
- **Title** (optional) - Section heading
- **Description** (optional) - Intro text
- **FAQs** (required) - List of Q&A pairs (1-20 items)
  - Question (required)
  - Answer (required, rich text)

**Example Use Cases**:
```
Title: "Frequently Asked Questions"
Description: "Find answers to common questions"
FAQs:
  - Q: "How do I get started?"
    A: "Simply sign up and..."
  - Q: "What's the pricing?"
    A: "We offer flexible plans..."
```

---

### 3. Accordion Block

**Purpose**: Display collapsible content sections.

**Best for**:
- Detailed information
- Terms and conditions
- Feature lists
- Process steps
- Expandable content

**Fields**:
- **Title** (optional) - Section heading
- **Description** (optional) - Intro text
- **Items** (required) - List of accordion items (1-20)
  - Heading (required)
  - Description (required, rich text)
- **Allow Multiple Open** (optional) - Allow multiple items open at once

**Example Use Cases**:
```
Title: "How It Works"
Items:
  - Heading: "Step 1: Sign Up"
    Description: "Create your account..."
  - Heading: "Step 2: Configure"
    Description: "Set up your preferences..."
  - Heading: "Step 3: Launch"
    Description: "Go live with your..."
```

---

### 4. Get In Touch Block

**Purpose**: Display contact information and call-to-action.

**Best for**:
- Contact sections
- Footer CTAs
- Landing pages
- Service pages
- Support pages

**Fields**:
- **Title** (required) - Section heading (default: "Get In Touch")
- **Description** (required) - Section text
- **Email** (optional) - Contact email
- **Phone** (optional) - Contact phone
- **Address** (optional) - Physical address
- **CTA Text** (required) - Button text (default: "Contact Us")
- **CTA Link** (optional) - Internal page link
- **CTA External** (optional) - External URL
- **Background Color** - Primary/Secondary/Light/Dark

**Example Use Cases**:
```
Title: "Get In Touch"
Description: "Have questions? We'd love to hear from you!"
Email: contact@example.com
Phone: +1 (555) 123-4567
Address: 123 Main St, City, State
CTA: "Contact Us" → Contact page
Background: Primary Color
```

---

## 🎨 How to Use in Wagtail Admin

### Adding Content Blocks

1. **Edit any page** (e.g., HomePage)
2. **Find "Body" field** in Content tab
3. **Click "Add"** and choose block type:
   - Image with Content
   - FAQ Section
   - Accordion Section
   - Get In Touch
4. **Fill in the fields**
5. **Save and publish**

### Reordering Blocks

- Drag blocks up/down to reorder
- Click the drag handle (≡) on each block

### Duplicating Blocks

- Click the duplicate icon to copy a block
- Useful for similar sections

### Deleting Blocks

- Click the delete icon (×) to remove a block

---

## 📐 Recommended Image Sizes

| Block | Recommended Size | Aspect Ratio |
|-------|------------------|--------------|
| Image with Content | 600x400px | 3:2 |
| Image with Content | 800x600px | 4:3 |
| Image with Content | 1200x800px | 3:2 |

---

## 🎯 Best Practices

### Content Guidelines

✅ **Keep titles concise** (max 60 characters)
✅ **Use clear, descriptive text**
✅ **Break up long content** with multiple blocks
✅ **Use rich text formatting** (bold, italic, lists)
✅ **Add descriptive alt text** to images
✅ **Test on mobile devices**

### Image Optimization

✅ **Compress images** before upload
✅ **Use appropriate dimensions**
✅ **Use WebP format** when possible
✅ **Optimize file size** (< 500KB per image)
✅ **Provide alt text** for accessibility

### Accessibility

✅ **Use semantic HTML** in rich text
✅ **Provide alt text** for all images
✅ **Ensure color contrast** is readable
✅ **Make links descriptive** (not "click here")
✅ **Test with screen readers**

### Performance

✅ **Limit FAQ items** to 10-15 per section
✅ **Limit accordion items** to 10-15 per section
✅ **Optimize images** for web
✅ **Use lazy loading** for images
✅ **Minimize rich text** complexity

---

## 🔧 Customization

### Adding New Blocks

To add a new content block:

1. **Create a new StructBlock** in `core/models.py`:
```python
class MyCustomBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    content = blocks.RichTextBlock()
    
    class Meta:
        icon = 'icon-name'
        label = 'My Custom Block'
        template = 'blocks/my_custom_block.html'
```

2. **Add to BasePage body StreamField**:
```python
body = StreamField([
    # ... existing blocks
    ('my_custom', MyCustomBlock()),
])
```

3. **Create template** in `templates/blocks/my_custom_block.html`

4. **Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📝 Template Structure

### Block Template Example

```django
{# templates/blocks/image_with_content_block.html #}
<section class="image-with-content">
    <div class="container">
        <div class="row">
            {% if block.value.image_position == 'left' %}
                <div class="col-md-6">
                    <img src="{{ block.value.image.url }}" 
                         alt="{{ block.value.image.alt }}"
                         class="img-fluid">
                </div>
                <div class="col-md-6">
                    <h2>{{ block.value.title }}</h2>
                    {{ block.value.description|safe }}
                    {% if block.value.link_text %}
                        <a href="{{ block.value.link_page.url }}" 
                           class="btn btn-primary">
                            {{ block.value.link_text }}
                        </a>
                    {% endif %}
                </div>
            {% else %}
                {# Right position #}
            {% endif %}
        </div>
    </div>
</section>
```

---

## 🚀 Common Workflows

### Create a Service Page

1. Add hero banner
2. Add "Image with Content" block (service description)
3. Add FAQ block (common questions)
4. Add "Get In Touch" block (CTA)

### Create a Help/Support Page

1. Add hero banner
2. Add FAQ block (common issues)
3. Add Accordion block (detailed guides)
4. Add "Get In Touch" block (contact support)

### Create a Features Page

1. Add hero banner
2. Add multiple "Image with Content" blocks (each feature)
3. Add FAQ block (feature questions)
4. Add "Get In Touch" block (CTA)

---

## ✅ Verification Checklist

- [ ] All 4 content blocks appear in admin
- [ ] Can add blocks to page body
- [ ] Can reorder blocks
- [ ] Can duplicate blocks
- [ ] Can delete blocks
- [ ] Rich text formatting works
- [ ] Image upload works
- [ ] Links work (internal and external)
- [ ] Blocks render on frontend
- [ ] Responsive on mobile

---

## 🎓 Next Steps

1. **Create block templates** for frontend rendering
2. **Add CSS styles** for each block
3. **Add JavaScript** for interactive features (accordion expand/collapse)
4. **Test in Wagtail admin** with sample content
5. **Create example pages** using all blocks

---

## 📚 Related Documentation

- **CORE_MODELS_SETUP.md** - Core models overview
- **HERO_BLOCKS_QUICK_REFERENCE.md** - Hero blocks guide
- **Wagtail Docs** - https://docs.wagtail.org/

---

**Created**: 2024-10-25  
**Version**: 1.0  

