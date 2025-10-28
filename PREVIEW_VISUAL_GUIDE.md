# Wagtail Block Preview - Visual Guide

## 🎨 Preview in Action

### Block Chooser View
```
┌─────────────────────────────────────────────────────────────┐
│ Add a block                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🖼️  Image with Content                                    │
│      Add an image with accompanying text content and       │
│      optional call-to-action button                        │
│                                                             │
│  ❓  FAQ Section                                           │
│      Frequently Asked Questions section                    │
│                                                             │
│  📋 Accordion Section                                      │
│      Expandable/Collapsible content sections               │
│                                                             │
│  ✉️  Get In Touch                                          │
│      Contact information and CTA section                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Block Editor with Preview

### Empty Block
```
┌─────────────────────────────────────────────────────────────┐
│ Image with Content Block                                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Title *                                                     │
│ [_________________________________]                        │
│                                                             │
│ Description *                                               │
│ [_________________________________]                        │
│ [_________________________________]                        │
│                                                             │
│ Image *                                                     │
│ [Choose an image]                                           │
│                                                             │
│ Image Position                                              │
│ (•) Image on Left  ( ) Image on Right                      │
│                                                             │
│ Link Text                                                   │
│ [_________________________________]                        │
│                                                             │
│ Link Page                                                   │
│ [Choose a page]                                             │
│                                                             │
│ Link External                                               │
│ [_________________________________]                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ PREVIEW:                                                    │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 🖼️ Image with Content                                  │ │
│ ├─────────────────────────────────────────────────────────┤ │
│ │ No title                                                │ │
│ │                                                         │ │
│ │ ❌ No image                                             │ │
│ │                                                         │ │
│ │ No description                                          │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

### Filled Block
```
┌─────────────────────────────────────────────────────────────┐
│ Image with Content Block                                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Title *                                                     │
│ [Our Amazing Features_____________________________________]│
│                                                             │
│ Description *                                               │
│ [Discover what makes us different. Our platform offers...] │
│ [cutting-edge technology and exceptional support...]       │
│                                                             │
│ Image *                                                     │
│ [✓ feature-image.jpg (600x400)]                            │
│                                                             │
│ Image Position                                              │
│ (•) Image on Left  ( ) Image on Right                      │
│                                                             │
│ Link Text                                                   │
│ [Learn More_____________________________________________]  │
│                                                             │
│ Link Page                                                   │
│ [✓ Services Page]                                           │
│                                                             │
│ Link External                                               │
│ [_________________________________]                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ PREVIEW:                                                    │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 🖼️ Image with Content                                  │ │
│ ├─────────────────────────────────────────────────────────┤ │
│ │ Our Amazing Features                                    │ │
│ │                                                         │ │
│ │ 📷 Image  ⬅️ Image Left  🔗 CTA: Learn More            │ │
│ │                                                         │ │
│ │ Discover what makes us different. Our platform...      │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Preview States

### State 1: All Fields Empty
```
┌─────────────────────────────────────────┐
│ 🖼️ Image with Content                   │
├─────────────────────────────────────────┤
│ No title                                │
│                                         │
│ ❌ No image                             │
│                                         │
│ No description                          │
└─────────────────────────────────────────┘
```

### State 2: Title Only
```
┌─────────────────────────────────────────┐
│ 🖼️ Image with Content                   │
├─────────────────────────────────────────┤
│ Our Amazing Features                    │
│                                         │
│ ❌ No image                             │
│                                         │
│ No description                          │
└─────────────────────────────────────────┘
```

### State 3: Title + Image
```
┌─────────────────────────────────────────┐
│ 🖼️ Image with Content                   │
├─────────────────────────────────────────┤
│ Our Amazing Features                    │
│                                         │
│ 📷 Image  ⬅️ Image Left                 │
│                                         │
│ No description                          │
└─────────────────────────────────────────┘
```

### State 4: Title + Image + Description
```
┌─────────────────────────────────────────┐
│ 🖼️ Image with Content                   │
├─────────────────────────────────────────┤
│ Our Amazing Features                    │
│                                         │
│ 📷 Image  ⬅️ Image Left                 │
│                                         │
│ Discover what makes us different...     │
└─────────────────────────────────────────┘
```

### State 5: Complete Block
```
┌─────────────────────────────────────────┐
│ 🖼️ Image with Content                   │
├─────────────────────────────────────────┤
│ Our Amazing Features                    │
│                                         │
│ 📷 Image  ⬅️ Image Left  🔗 CTA: Learn  │
│                                         │
│ Discover what makes us different...     │
└─────────────────────────────────────────┘
```

---

## 🎨 Color Scheme

### Preview Container
- **Background:** Linear gradient (light blue to darker blue)
- **Border:** 2px solid #007bff (Wagtail blue)
- **Border Radius:** 8px
- **Padding:** 16px

### Header
- **Icon:** 🖼️ (emoji)
- **Label:** "Image with Content" (uppercase, letter-spaced)
- **Color:** #007bff (Wagtail blue)
- **Font Size:** 14px
- **Font Weight:** 600

### Content
- **Background:** White
- **Border Radius:** 6px
- **Padding:** 12px

### Title
- **Font Size:** 16px
- **Font Weight:** 600
- **Color:** #333 (dark gray)
- **Empty State:** #999 (light gray, italic)

### Badges
- **Filled Fields:** 
  - Background: #e7f3ff (light blue)
  - Color: #0056b3 (dark blue)
- **Missing Fields:**
  - Background: #ffe7e7 (light red)
  - Color: #b30000 (dark red)
- **Padding:** 4px 8px
- **Border Radius:** 4px
- **Font Size:** 12px

### Description
- **Font Size:** 13px
- **Color:** #666 (medium gray)
- **Max Height:** 60px
- **Truncation:** 2 lines max
- **Empty State:** #999 (light gray, italic)

---

## 📱 Responsive Behavior

### Desktop (> 600px)
```
┌─────────────────────────────────────────┐
│ 🖼️ Image with Content                   │
├─────────────────────────────────────────┤
│ Our Amazing Features                    │
│                                         │
│ 📷 Image  ⬅️ Image Left  🔗 CTA: Learn  │
│                                         │
│ Discover what makes us different...     │
└─────────────────────────────────────────┘
```

### Mobile (< 600px)
```
┌──────────────────────────┐
│ 🖼️ Image with Content    │
├──────────────────────────┤
│ Our Amazing Features     │
│                          │
│ 📷 Image  ⬅️ Image Left  │
│ 🔗 CTA: Learn            │
│                          │
│ Discover what makes...   │
└──────────────────────────┘
```

---

## 🔄 Preview Update Flow

### User Action → Preview Update

```
1. User types title
   ↓
   Preview updates: "Our Amazing Features"

2. User selects image
   ↓
   Preview updates: "📷 Image" badge appears

3. User changes image position
   ↓
   Preview updates: "⬅️ Image Left" or "➡️ Image Right"

4. User enters description
   ↓
   Preview updates: Description preview appears

5. User enters CTA text
   ↓
   Preview updates: "🔗 CTA: Learn More" badge appears
```

---

## 🎯 Badge Meanings

| Badge | Meaning | Color |
|-------|---------|-------|
| 📷 Image | Image is selected | Blue |
| ❌ No image | No image selected | Red |
| ⬅️ Image Left | Image positioned on left | Blue |
| ➡️ Image Right | Image positioned on right | Blue |
| 🔗 CTA: [text] | CTA button text | Blue |
| No title | Title field is empty | Gray |
| No description | Description field is empty | Gray |

---

## 🖼️ Frontend Rendering

### Desktop Layout (Image Left)
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  ┌──────────────┐  ┌──────────────────────────┐   │
│  │              │  │ Our Amazing Features     │   │
│  │   IMAGE      │  │                          │   │
│  │   600x400    │  │ Discover what makes us   │   │
│  │              │  │ different. Our platform  │   │
│  │              │  │ offers cutting-edge...   │   │
│  │              │  │                          │   │
│  │              │  │ [Learn More]             │   │
│  └──────────────┘  └──────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Desktop Layout (Image Right)
```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  ┌──────────────────────────┐  ┌──────────────┐   │
│  │ Our Amazing Features     │  │              │   │
│  │                          │  │   IMAGE      │   │
│  │ Discover what makes us   │  │   600x400    │   │
│  │ different. Our platform  │  │              │   │
│  │ offers cutting-edge...   │  │              │   │
│  │                          │  │              │   │
│  │ [Learn More]             │  └──────────────┘   │
│  └──────────────────────────┘                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Mobile Layout
```
┌──────────────────────────┐
│                          │
│  ┌────────────────────┐  │
│  │                    │  │
│  │   IMAGE 600x400    │  │
│  │                    │  │
│  └────────────────────┘  │
│                          │
│  Our Amazing Features    │
│                          │
│  Discover what makes us  │
│  different. Our platform │
│  offers cutting-edge...  │
│                          │
│  [Learn More]            │
│                          │
└──────────────────────────┘
```

---

## ✨ Key Visual Features

### 1. Gradient Background
Creates visual separation from the form

### 2. Color-Coded Badges
- Blue = Complete/Available
- Red = Missing/Required

### 3. Emoji Icons
- 🖼️ = Image block
- 📷 = Image present
- ❌ = Missing field
- ⬅️/➡️ = Position
- 🔗 = Link/CTA

### 4. Truncated Text
- Description limited to 2 lines
- Long text shows "..."
- Prevents preview from being too large

### 5. Responsive Design
- Adapts to screen size
- Mobile-friendly
- Maintains readability

---

## 🎓 Design Principles

1. **Clear Hierarchy:** Header > Content > Meta
2. **Visual Feedback:** Status badges show field state
3. **Responsive:** Works on all screen sizes
4. **Accessible:** Good contrast, readable fonts
5. **Consistent:** Matches Wagtail admin style
6. **Informative:** Shows what's filled/missing
7. **Compact:** Doesn't take too much space
8. **Professional:** Clean, modern appearance

---

**Last Updated:** October 25, 2025  
**Wagtail Version:** 6.3.5+

