# Content Blocks - File Structure

**Complete file structure for content blocks system**

---

## 📁 Project Structure

```
voyah/
├── core/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                    ✅ UPDATED
│   │   ├── BannerBlock
│   │   ├── SliderBlock
│   │   ├── VideoBlock
│   │   ├── ParallaxBlock
│   │   ├── ImageWithContentBlock    ✅ NEW
│   │   ├── FAQBlock                 ✅ NEW
│   │   ├── AccordionBlock           ✅ NEW
│   │   ├── GetInTouchBlock          ✅ NEW
│   │   ├── SEOMixin
│   │   └── BasePage                 ✅ UPDATED
│   ├── tests.py
│   └── views.py
│
├── voyah/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── stage.py
│   │   └── production.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── blocks/                  ✅ NEW DIRECTORY
│   │   │   ├── banner_block.html
│   │   │   ├── slider_block.html
│   │   │   ├── video_block.html
│   │   │   ├── parallax_block.html
│   │   │   ├── image_with_content_block.html    ✅ NEW
│   │   │   ├── faq_block.html                   ✅ NEW
│   │   │   ├── accordion_block.html             ✅ NEW
│   │   │   └── get_in_touch_block.html          ✅ NEW
│   │   └── home/
│   │       └── home_page.html
│   ├── urls.py
│   └── wsgi.py
│
├── home/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── CONTENT_BLOCKS_GUIDE.md                      ✅ NEW
├── CONTENT_BLOCKS_IMPLEMENTATION.md             ✅ NEW
├── CONTENT_BLOCKS_QUICK_REFERENCE.md            ✅ NEW
├── CONTENT_BLOCKS_SUMMARY.md                    ✅ NEW
├── CONTENT_BLOCKS_FILE_STRUCTURE.md             ✅ NEW
├── CORE_MODELS_SETUP.md
├── HERO_BLOCKS_QUICK_REFERENCE.md
├── AUGMENT_SETUP_PROMPT.md
├── QUICK_SETUP_PROMPT.md
├── SETUP_STEPS_CHECKLIST.md
├── manage.py
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   ├── stage.txt
│   └── production.txt
└── README.md
```

---

## 📝 Files Modified

### 1. core/models.py
**Status**: ✅ Updated  
**Lines**: 820+ (was 598)  
**Changes**:
- Added ImageWithContentBlock (lines 456-502)
- Added FAQBlock (lines 505-545)
- Added AccordionBlock (lines 548-595)
- Added GetInTouchBlock (lines 598-666)
- Updated BasePage with body StreamField (lines 774-798)

**Key Additions**:
```python
# New content blocks
class ImageWithContentBlock(blocks.StructBlock):
    # Image with text content and optional CTA

class FAQBlock(blocks.StructBlock):
    # FAQ section with Q&A pairs

class AccordionBlock(blocks.StructBlock):
    # Collapsible content sections

class GetInTouchBlock(blocks.StructBlock):
    # Contact information and CTA

# Updated BasePage
class BasePage(SEOMixin, Page):
    hero = StreamField([...])  # Existing
    body = StreamField([       # NEW
        ('image_with_content', ImageWithContentBlock()),
        ('faq', FAQBlock()),
        ('accordion', AccordionBlock()),
        ('get_in_touch', GetInTouchBlock()),
    ])
```

---

## 📄 Files Created

### Templates (4 files)

#### 1. image_with_content_block.html
**Path**: `voyah/templates/blocks/`  
**Size**: ~150 lines  
**Features**:
- Responsive image left/right positioning
- Bootstrap 5 grid layout
- CTA button with hover effects
- Inline CSS styling
- Lazy loading for images

#### 2. faq_block.html
**Path**: `voyah/templates/blocks/`  
**Size**: ~120 lines  
**Features**:
- Collapsible FAQ items
- Bootstrap collapse integration
- Icon rotation animation
- Smooth transitions
- Inline CSS and JavaScript

#### 3. accordion_block.html
**Path**: `voyah/templates/blocks/`  
**Size**: ~130 lines  
**Features**:
- Expandable accordion items
- Single/multiple open modes
- Icon rotation animation
- Bootstrap collapse integration
- Inline CSS and JavaScript

#### 4. get_in_touch_block.html
**Path**: `voyah/templates/blocks/`  
**Size**: ~140 lines  
**Features**:
- Contact information display
- 4 background color options
- Contact icons
- Responsive design
- Inline CSS styling

### Documentation (5 files)

#### 1. CONTENT_BLOCKS_GUIDE.md
**Size**: 300+ lines  
**Purpose**: Complete user guide  
**Includes**:
- Overview of all blocks
- Detailed field descriptions
- Usage examples
- Best practices
- Customization guide
- Troubleshooting

#### 2. CONTENT_BLOCKS_IMPLEMENTATION.md
**Size**: 300+ lines  
**Purpose**: Implementation details  
**Includes**:
- What was created
- Block features
- How to use
- Model structure
- Next steps
- Customization examples

#### 3. CONTENT_BLOCKS_QUICK_REFERENCE.md
**Size**: 200+ lines  
**Purpose**: Quick lookup guide  
**Includes**:
- Block types overview
- When to use each block
- Recommended image sizes
- Block settings
- Pro tips
- Common issues

#### 4. CONTENT_BLOCKS_SUMMARY.md
**Size**: 200+ lines  
**Purpose**: Complete overview  
**Includes**:
- What was built
- Key features
- How to use
- Model structure
- Next steps
- Common use cases

#### 5. CONTENT_BLOCKS_FILE_STRUCTURE.md
**Size**: 200+ lines  
**Purpose**: This file  
**Includes**:
- Project structure
- Files modified
- Files created
- File descriptions
- Quick reference

---

## 📊 Statistics

### Files Modified
- **core/models.py**: 1 file

### Files Created
- **Templates**: 4 files
- **Documentation**: 5 files
- **Total New Files**: 9 files

### Lines of Code
- **Models**: 222 lines (new blocks)
- **Templates**: 540 lines (all templates)
- **Documentation**: 1,200+ lines

### Total Project Size
- **Models**: 820+ lines
- **Templates**: 540+ lines
- **Documentation**: 1,200+ lines
- **Total**: 2,560+ lines

---

## 🎯 Block Model Structure

### ImageWithContentBlock
```
├── title (CharBlock)
├── description (RichTextBlock)
├── image (ImageChooserBlock)
├── image_position (ChoiceBlock: left/right)
├── link_text (CharBlock, optional)
├── link_page (PageChooserBlock, optional)
└── link_external (URLBlock, optional)
```

### FAQBlock
```
├── title (CharBlock, optional)
├── description (RichTextBlock, optional)
└── faqs (ListBlock, 1-20 items)
    ├── question (CharBlock)
    └── answer (RichTextBlock)
```

### AccordionBlock
```
├── title (CharBlock, optional)
├── description (RichTextBlock, optional)
├── items (ListBlock, 1-20 items)
│   ├── heading (CharBlock)
│   └── description (RichTextBlock)
└── allow_multiple_open (BooleanBlock)
```

### GetInTouchBlock
```
├── title (CharBlock)
├── description (RichTextBlock)
├── email (EmailBlock, optional)
├── phone (CharBlock, optional)
├── address (CharBlock, optional)
├── cta_text (CharBlock)
├── cta_link (PageChooserBlock, optional)
├── cta_external (URLBlock, optional)
└── background_color (ChoiceBlock)
```

---

## 🔗 Template Relationships

```
BasePage
├── hero StreamField
│   ├── BannerBlock → banner_block.html
│   ├── SliderBlock → slider_block.html
│   ├── VideoBlock → video_block.html
│   └── ParallaxBlock → parallax_block.html
│
└── body StreamField
    ├── ImageWithContentBlock → image_with_content_block.html
    ├── FAQBlock → faq_block.html
    ├── AccordionBlock → accordion_block.html
    └── GetInTouchBlock → get_in_touch_block.html
```

---

## 📋 File Checklist

### Models
- [x] ImageWithContentBlock created
- [x] FAQBlock created
- [x] AccordionBlock created
- [x] GetInTouchBlock created
- [x] BasePage updated with body StreamField

### Templates
- [x] image_with_content_block.html created
- [x] faq_block.html created
- [x] accordion_block.html created
- [x] get_in_touch_block.html created
- [x] All templates include CSS
- [x] All templates include JavaScript
- [x] All templates responsive

### Documentation
- [x] CONTENT_BLOCKS_GUIDE.md created
- [x] CONTENT_BLOCKS_IMPLEMENTATION.md created
- [x] CONTENT_BLOCKS_QUICK_REFERENCE.md created
- [x] CONTENT_BLOCKS_SUMMARY.md created
- [x] CONTENT_BLOCKS_FILE_STRUCTURE.md created

---

## 🚀 Next Steps

### 1. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Test Blocks
- Create test page
- Add each block type
- Verify rendering

### 3. Customize
- Update CSS colors
- Adjust spacing
- Add animations

### 4. Deploy
- Push to repository
- Deploy to staging
- Test on production

---

## 📚 Documentation Map

| File | Purpose | Audience |
|------|---------|----------|
| CONTENT_BLOCKS_GUIDE.md | Complete guide | Editors & Developers |
| CONTENT_BLOCKS_IMPLEMENTATION.md | Implementation details | Developers |
| CONTENT_BLOCKS_QUICK_REFERENCE.md | Quick lookup | Editors |
| CONTENT_BLOCKS_SUMMARY.md | Overview | Everyone |
| CONTENT_BLOCKS_FILE_STRUCTURE.md | File structure | Developers |

---

## 🎓 Related Documentation

- **CORE_MODELS_SETUP.md** - Core models overview
- **HERO_BLOCKS_QUICK_REFERENCE.md** - Hero blocks guide
- **AUGMENT_SETUP_PROMPT.md** - Complete setup prompt
- **QUICK_SETUP_PROMPT.md** - Quick setup guide

---

## ✅ Verification

All files have been created and verified:
- ✅ Models import successfully
- ✅ Templates exist and are valid
- ✅ Documentation is complete
- ✅ File structure is organized
- ✅ All links are correct

---

**Created**: 2024-10-25  
**Version**: 1.0  
**Status**: ✅ Complete  

