# Content Blocks Quick Reference

**Quick lookup guide for content blocks**

---

## 📦 Block Types

### 1️⃣ Image with Content
**Icon**: 🖼️ Image  
**Use for**: Features, services, testimonials  
**Key fields**: Title, Description, Image, Position, Link

```
┌─────────────────────────────────┐
│ Title                           │
│ Description text with content   │
│ [Link Button]                   │
│                                 │
│ [Image]                         │
└─────────────────────────────────┘
```

---

### 2️⃣ FAQ
**Icon**: ❓ Help  
**Use for**: FAQ pages, support  
**Key fields**: Title, Description, Q&A pairs

```
┌─────────────────────────────────┐
│ FAQ Title                       │
│ ┌─────────────────────────────┐ │
│ │ + Question 1                │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ + Question 2                │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

### 3️⃣ Accordion
**Icon**: 📋 List  
**Use for**: Guides, process steps, terms  
**Key fields**: Title, Description, Items

```
┌─────────────────────────────────┐
│ Accordion Title                 │
│ ┌─────────────────────────────┐ │
│ │ ▶ Step 1                    │ │
│ └─────────────────────────────┘ │
│ ┌─────────────────────────────┐ │
│ │ ▶ Step 2                    │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

### 4️⃣ Get In Touch
**Icon**: ✉️ Mail  
**Use for**: Contact sections, CTAs  
**Key fields**: Title, Description, Contact info, CTA

```
┌─────────────────────────────────┐
│ Get In Touch                    │
│ Description text                │
│ ✉ email@example.com            │
│ ☎ +1 (555) 123-4567            │
│ 📍 123 Main St, City            │
│ [Contact Us Button]             │
└─────────────────────────────────┘
```

---

## 🎯 When to Use Each Block

| Block | Best For | Example |
|-------|----------|---------|
| Image + Content | Showcase features | "Why Choose Us" section |
| FAQ | Answer questions | Support page |
| Accordion | Detailed info | "How It Works" steps |
| Get In Touch | Call-to-action | Contact section |

---

## 📐 Recommended Image Sizes

| Block | Size | Aspect Ratio |
|-------|------|--------------|
| Image + Content | 600x400px | 3:2 |
| Image + Content | 800x600px | 4:3 |
| Image + Content | 1200x800px | 3:2 |

---

## ⚙️ Block Settings

### Image with Content
- **Image Position**: Left or Right
- **Link**: Optional CTA button
- **Rich Text**: Full formatting support

### FAQ
- **Items**: 1-20 Q&A pairs
- **Collapsible**: Auto-expand/collapse
- **Rich Text**: Full formatting in answers

### Accordion
- **Items**: 1-20 sections
- **Multiple Open**: Allow multiple expanded
- **Rich Text**: Full formatting in content

### Get In Touch
- **Contact Fields**: Email, Phone, Address
- **Background**: 4 color options
- **CTA**: Internal or external link

---

## 🚀 Quick Start

### Add a Block
1. Edit page → Body field
2. Click "Add"
3. Choose block type
4. Fill fields
5. Save

### Reorder Blocks
- Drag block by handle (≡)

### Duplicate Block
- Click duplicate icon

### Delete Block
- Click delete icon (×)

---

## 💡 Pro Tips

✅ **Keep titles short** (max 60 chars)  
✅ **Use rich text formatting** (bold, lists)  
✅ **Add alt text to images**  
✅ **Test on mobile**  
✅ **Limit items** (10-15 per block)  
✅ **Optimize images** (< 500KB)  

---

## 🎨 Styling

All blocks include:
- ✅ Responsive design
- ✅ Mobile-friendly
- ✅ Bootstrap 5
- ✅ Smooth animations
- ✅ Hover effects

---

## 📝 Field Types

| Type | Example | Notes |
|------|---------|-------|
| Text | "My Title" | Single line |
| Rich Text | "Bold **text**" | Formatting support |
| Image | Upload file | Recommended sizes |
| Link | Internal/External | Both supported |
| Email | user@example.com | Clickable mailto |
| Phone | +1 (555) 123-4567 | Clickable tel |
| Choice | Primary/Secondary | Dropdown select |

---

## 🔗 Links

### Internal Links
- Link to any page on site
- Auto-updates if page moves
- Recommended for navigation

### External Links
- Link to external websites
- Use full URL (https://...)
- Opens in new tab

---

## 🎨 Background Colors

**Get In Touch Block**:
- 🔵 Primary (Blue)
- ⚫ Secondary (Gray)
- ⚪ Light (Light Gray)
- ⬛ Dark (Dark Gray)

---

## 📱 Responsive Behavior

All blocks are mobile-responsive:
- **Desktop**: Full layout
- **Tablet**: Adjusted spacing
- **Mobile**: Stacked layout

---

## ✅ Checklist Before Publishing

- [ ] Title is clear and concise
- [ ] Content is well-formatted
- [ ] Images have alt text
- [ ] Links work correctly
- [ ] Tested on mobile
- [ ] No spelling errors
- [ ] Content is accurate
- [ ] CTA is clear

---

## 🆘 Common Issues

**Blocks not showing?**
- Run migrations
- Clear cache
- Restart server

**Styling looks wrong?**
- Check CSS is loading
- Verify Bootstrap 5
- Check browser cache

**Links not working?**
- Verify URL is correct
- Check page exists
- Test in new tab

---

## 📚 Full Documentation

See **CONTENT_BLOCKS_GUIDE.md** for:
- Detailed field descriptions
- Usage examples
- Best practices
- Customization guide
- Troubleshooting

---

## 🎓 Learn More

- **Wagtail Docs**: https://docs.wagtail.org/
- **Bootstrap 5**: https://getbootstrap.com/
- **Rich Text**: https://docs.wagtail.org/en/stable/topics/rich_text/

---

**Quick Reference v1.0**  
**Last Updated**: 2024-10-25  

