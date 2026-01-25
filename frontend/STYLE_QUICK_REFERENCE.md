/**
 * Style Manager Quick Reference
 */

# 🎨 Style Manager - Quick Reference

Fast lookup for the most common style manager operations.

## Import Statements

```typescript
// Get theme values
import { colors, spacing, typography, borderRadius, shadows, componentSizes, zIndex } from "~/lib/theme";

// Get utility functions
import { 
  getColor, 
  getSpacing, 
  getButtonStyles,
  getInputStyles,
  getCardStyles,
  getAlertStyles,
  typographyPresets,
  getTransition,
  getContrastColor
} from "~/lib/styles";
```

## Common Usage Patterns

### Colors

```typescript
// Get a color
const primaryColor = getColor("primary", 600);           // #0284c7
const errorColor = getColor("error", 500);               // #ef4444

// Available variants: primary, secondary, success, error, warning, info

// Available shades: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900
```

### Spacing

```typescript
// Get a spacing value
const padding = spacing[4];     // 16px
const margin = spacing[8];      // 32px

// Available: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 24, 28, 32...
```

### Button Styles

```typescript
// Generate button styles
const primaryMd = getButtonStyles("primary", "md");
const secondaryLg = getButtonStyles("secondary", "lg");
const errorSm = getButtonStyles("error", "sm");

// Sizes: sm, md, lg
// Variants: primary, secondary, success, error, warning, info
```

### Input Styles

```typescript
// Generate input field styles
const inputMd = getInputStyles("md");
const inputLg = getInputStyles("lg");

// Sizes: sm, md, lg
```

### Card Styles

```typescript
// Generate card container styles
const cardMd = getCardStyles("md");
const cardLg = getCardStyles("lg");

// Sizes: sm, md, lg
```

### Alert Styles

```typescript
// Generate alert styles
const successAlert = getAlertStyles("success");
const errorAlert = getAlertStyles("error");
const warningAlert = getAlertStyles("warning");
const infoAlert = getAlertStyles("info");

// Variants: primary, secondary, success, error, warning, info
```

### Typography

```typescript
// Use preset typography
const heading1 = typographyPresets.h1;     // 48px, bold
const heading2 = typographyPresets.h2;     // 36px, bold
const bodyText = typographyPresets.body;   // 16px, normal
const caption = typographyPresets.caption; // 12px, normal

// Available: h1, h2, h3, h4, h5, h6, body, small, caption
```

### Transitions

```typescript
// Get a transition value
const transition = getTransition("base");   // all 200ms cubic-bezier(...)
const transitionFast = getTransition("fast");
const transitionSlow = getTransition("slow");

// Duration options: fast (150ms), base (200ms), slow (300ms), slower (500ms)
```

### Border Radius

```typescript
// Get border radius
const roundedMd = borderRadius.md;    // 6px
const roundedLg = borderRadius.lg;    // 8px
const roundedFull = borderRadius.full; // 9999px

// Available: none, sm, base, md, lg, xl, 2xl, 3xl, full
```

### Shadows

```typescript
// Get shadow value
const shadowBase = shadows.base;
const shadowMd = shadows.md;
const shadowLg = shadows.lg;

// Available: none, sm, base, md, lg, xl, 2xl, inner
```

### Z-Index

```typescript
// Get z-index values
const modal = zIndex.modal;           // 1050
const dropdown = zIndex.dropdown;     // 1000
const tooltip = zIndex.tooltip;       // 1070

// Available: hide, auto, base, dropdown, sticky, fixed, modalBackdrop, modal, popover, tooltip
```

## Component Examples

### Button Component

```typescript
<button style={getButtonStyles("primary", "md")}>
  Click me
</button>
```

### Input Component

```typescript
<input style={getInputStyles("lg")} placeholder="Enter text" />
```

### Card Component

```typescript
<div style={getCardStyles("md")}>
  Content here
</div>
```

### Alert Component

```typescript
const alertStyles = getAlertStyles("success");
<div style={{ 
  backgroundColor: alertStyles.bg, 
  borderColor: alertStyles.border,
  color: alertStyles.text 
}}>
  Success message
</div>
```

### Responsive Section

```typescript
<div style={{
  padding: spacing[4],    // 16px on all screens
  gap: spacing[6],        // 24px gap
  backgroundColor: getColor("primary", 50)
}}>
  Content
</div>
```

## Full Component Example

```typescript
import { getColor, getButtonStyles, getCardStyles, typographyPresets, spacing, borderRadius } from "~/lib/styles";

export function MyComponent() {
  return (
    <div style={getCardStyles("lg")}>
      <h2 style={typographyPresets.h2}>
        Title
      </h2>
      
      <p style={{
        ...typographyPresets.body,
        color: getColor("neutral", 700),
        marginBottom: spacing[4]
      }}>
        Description
      </p>
      
      <button style={{
        ...getButtonStyles("primary", "md"),
        borderRadius: borderRadius.md,
        border: "none",
        cursor: "pointer"
      }}>
        Click me
      </button>
    </div>
  );
}
```

## Color Reference

### Primary
- 500: #0ea5e9 (main)
- 600: #0284c7 (darker/hover)
- 700: #0369a1 (darkest)

### Error
- 500: #ef4444
- 700: #b91c1c

### Success
- 500: #22c55e
- 700: #15803d

### Warning
- 500: #eab308
- 700: #b45309

### Info
- 500: #0ea5e9
- 700: #0369a1

### Neutral (Grayscale)
- 50: #f9fafb (lightest)
- 200: #e5e7eb (light)
- 500: #6b7280 (medium)
- 700: #374151 (dark)
- 900: #111827 (darkest)

## Size Reference

### Spacing Scale
```
1 = 4px    |   6 = 24px   |  12 = 48px  |  24 = 96px
2 = 8px    |   7 = 28px   |  14 = 56px  |  28 = 112px
3 = 12px   |   8 = 32px   |  16 = 64px  |  32 = 128px
4 = 16px   |   9 = 36px   |  20 = 80px  |  36 = 144px
5 = 20px   |  10 = 40px   |  24 = 96px  |  40 = 160px
```

### Font Sizes
```
xs = 12px   |  lg = 18px    |  3xl = 30px
sm = 14px   |  xl = 20px    |  4xl = 36px
base = 16px |  2xl = 24px   |  5xl = 48px
```

### Border Radius
```
sm = 2px     |  lg = 8px      |  3xl = 24px
base = 4px   |  xl = 12px     |  full = 9999px
md = 6px     |  2xl = 16px
```

## Tips & Tricks

### 1. Use Spread Operator for Styles
```typescript
<div style={{ ...getCardStyles("lg"), marginBottom: spacing[4] }}>
  Content
</div>
```

### 2. Combine Multiple Utilities
```typescript
const containerStyle = {
  ...getCardStyles("md"),
  backgroundColor: getColor("primary", 50),
  padding: spacing[6]
};
```

### 3. Create Reusable Style Objects
```typescript
const buttonPrimaryMd = getButtonStyles("primary", "md");
const buttonPrimarySm = getButtonStyles("primary", "sm");

// Use in multiple places
<button style={buttonPrimaryMd}>Save</button>
<button style={buttonPrimarySm}>Cancel</button>
```

### 4. Mix Theme Values with Tailwind
```typescript
<div className="p-4 rounded-lg" style={{ backgroundColor: getColor("primary", 100) }}>
  Content
</div>
```

### 5. Create Semantic Color Variables
```typescript
const primaryColor = getColor("primary", 600);
const primaryHover = getColor("primary", 700);
const primaryLight = getColor("primary", 100);

// Use consistently throughout component
```

## Customization Quick Start

### Change Primary Color
Edit `lib/theme.ts`:
```typescript
primary: {
  500: "#YOUR_COLOR",
  600: "#YOUR_DARKER_SHADE",
  // ... update all shades
}
```

### Adjust Spacing
Edit `lib/theme.ts`:
```typescript
export const spacing = {
  4: "16px",  // Change existing value
  13: "52px", // Add new value
}
```

### Update Button Sizes
Edit `lib/theme.ts`:
```typescript
componentSizes.button.md = {
  padding: "10px 20px",  // Change padding
  fontSize: "16px",
  height: "44px"         // Change height
}
```

---

**Need more details?** See [STYLE_MANAGER.md](./STYLE_MANAGER.md) for comprehensive documentation.
