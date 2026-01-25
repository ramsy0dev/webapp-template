/**
 * Style Management System Documentation
 */

# 🎨 Style Interface Manager

A comprehensive, centralized style management system for maintaining visual consistency across the entire webapp.

## Overview

The style manager provides:
- **Centralized theme configuration** - Single source of truth for all design tokens
- **Style utilities** - Helper functions for common styling patterns
- **Type safety** - Full TypeScript support for theme values
- **Consistency** - Ensures uniform styling across components
- **Scalability** - Easy to update and extend the entire design system

## Files

### `lib/theme.ts`
Defines the complete theme configuration with all design tokens:
- Colors (primary, secondary, semantic)
- Typography (fonts, sizes, weights)
- Spacing scale
- Border radius
- Shadows
- Breakpoints
- Transitions
- Component sizes
- Z-index stack

### `lib/styles.ts`
Utility functions and helpers for working with the theme:
- Color getters
- Style generators
- Responsive utilities
- Typography presets
- Contrast calculation

## Usage Examples

### Basic Color Usage

```typescript
import { getColor } from "~/lib/styles";

const primaryColor = getColor("primary", 600);        // #0284c7
const errorColor = getColor("error", 500);            // #ef4444
const successLight = getColor("success", 100);        // #dcfce7
```

### Component Style Generation

```typescript
import { getButtonStyles, getInputStyles, getCardStyles } from "~/lib/styles";

// Button styles
const buttonStyles = getButtonStyles("primary", "md");

// Input styles
const inputStyles = getInputStyles("lg");

// Card styles
const cardStyles = getCardStyles("md");
```

### Typography Presets

```typescript
import { typographyPresets } from "~/lib/styles";

// Use predefined typography styles
const heading1 = typographyPresets.h1;     // 48px, bold
const bodyText = typographyPresets.body;   // 16px, normal
const caption = typographyPresets.caption; // 12px, normal
```

### Responsive Design

```typescript
import { createResponsiveSpacing, createResponsiveFontSize } from "~/lib/styles";

// Responsive spacing
const spacing = createResponsiveSpacing(
  "4",      // mobile: 16px
  "6",      // tablet: 24px
  "8"       // desktop: 32px
);

// Responsive font size
const fontSize = createResponsiveFontSize(
  "lg",     // mobile
  "xl",     // tablet
  "2xl"     // desktop
);
```

### Working with Transitions

```typescript
import { getTransition } from "~/lib/styles";

// Get a transition value
const transition = getTransition("base"); // all 200ms cubic-bezier(...)
```

### Spacing System

```typescript
import { spacing } from "~/lib/theme";

// Available spacing values (in pixels)
spacing[0]   // 0px
spacing[1]   // 4px
spacing[2]   // 8px
spacing[4]   // 16px
spacing[8]   // 32px
spacing[16]  // 64px
spacing[32]  // 128px
```

### Z-Index Management

```typescript
import { zIndex } from "~/lib/theme";

// Organized z-index stack
zIndex.base           // 0
zIndex.dropdown       // 1000
zIndex.sticky         // 1020
zIndex.fixed          // 1030
zIndex.modalBackdrop  // 1040
zIndex.modal          // 1050
zIndex.popover        // 1060
zIndex.tooltip        // 1070
```

## Color Palette

### Primary
Used for main actions and primary elements:
- 50: #f0f9ff (lightest)
- 500: #0ea5e9 (main)
- 600: #0284c7 (hover)
- 900: #0c3d66 (darkest)

### Secondary
Used for secondary actions:
- 500: #8b5cf6
- 600: #7c3aed
- 700: #6d28d9

### Semantic Colors
- **Success**: Green (#22c55e)
- **Error**: Red (#ef4444)
- **Warning**: Amber (#eab308)
- **Info**: Blue (#0ea5e9)

### Neutral
Full grayscale from 50 (lightest) to 900 (darkest):
- 50: #f9fafb
- 500: #6b7280
- 900: #111827

## Typography System

### Font Families
```typescript
typography.fontFamily.sans  // Inter (default)
typography.fontFamily.mono  // JetBrains Mono (code)
```

### Font Sizes
```typescript
typography.fontSize.xs     // 12px
typography.fontSize.sm     // 14px
typography.fontSize.base   // 16px
typography.fontSize.lg     // 18px
typography.fontSize.xl     // 20px
typography.fontSize["2xl"] // 24px
typography.fontSize["3xl"] // 30px
typography.fontSize["4xl"] // 36px
typography.fontSize["5xl"] // 48px
```

### Font Weights
```typescript
typography.fontWeight.light       // 300
typography.fontWeight.normal      // 400
typography.fontWeight.medium      // 500
typography.fontWeight.semibold    // 600
typography.fontWeight.bold        // 700
typography.fontWeight.extrabold   // 800
```

## Responsive Breakpoints

```typescript
breakpoints.xs   // 320px
breakpoints.sm   // 640px
breakpoints.md   // 768px
breakpoints.lg   // 1024px
breakpoints.xl   // 1280px
breakpoints["2xl"] // 1536px
```

## Component Sizes

### Button Sizes
```typescript
componentSizes.button.sm  // { padding: "6px 12px", fontSize: "14px", height: "32px" }
componentSizes.button.md  // { padding: "8px 16px", fontSize: "16px", height: "40px" }
componentSizes.button.lg  // { padding: "12px 24px", fontSize: "18px", height: "48px" }
```

### Input Sizes
```typescript
componentSizes.input.sm   // sm: { padding: "6px 12px", fontSize: "14px", height: "32px" }
componentSizes.input.md   // md: { padding: "8px 12px", fontSize: "16px", height: "40px" }
componentSizes.input.lg   // lg: { padding: "12px 16px", fontSize: "18px", height: "48px" }
```

### Card Sizes
```typescript
componentSizes.card.sm    // { padding: "12px", borderRadius: "6px" }
componentSizes.card.md    // { padding: "16px", borderRadius: "8px" }
componentSizes.card.lg    // { padding: "24px", borderRadius: "12px" }
```

## Shadows

```typescript
shadows.none        // none
shadows.sm          // light shadow
shadows.base        // standard shadow
shadows.md          // medium shadow
shadows.lg          // large shadow
shadows.xl          // extra large shadow
shadows["2xl"]      // very large shadow
shadows.inner       // inset shadow
```

## Transitions

### Duration
```typescript
transitions.fast      // 150ms
transitions.base      // 200ms
transitions.slow      // 300ms
transitions.slower    // 500ms
```

### Timing Functions
```typescript
transitions.timing.linear       // linear
transitions.timing.ease         // cubic-bezier(0.4, 0, 0.2, 1)
transitions.timing.easeIn       // cubic-bezier(0.4, 0, 1, 1)
transitions.timing.easeOut      // cubic-bezier(0, 0, 0.2, 1)
transitions.timing.easeInOut    // cubic-bezier(0.4, 0, 0.2, 1)
```

## Utility Functions

### `getColor(variant, shade)`
Get a color from the palette:
```typescript
getColor("primary", 600)  // Returns hex color
getColor("error", 500)
```

### `getButtonStyles(variant, size)`
Generate complete button styles:
```typescript
const styles = getButtonStyles("primary", "md");
// Returns: { backgroundColor, color, padding, fontSize, height, transition }
```

### `getInputStyles(size)`
Generate input field styles:
```typescript
const styles = getInputStyles("lg");
```

### `getCardStyles(size)`
Generate card container styles:
```typescript
const styles = getCardStyles("md");
```

### `getAlertStyles(type)`
Generate alert box styles:
```typescript
const styles = getAlertStyles("success");
// Returns: { bg, border, text, icon colors }
```

### `getContrastColor(hexColor)`
Determine if text should be light or dark on a background:
```typescript
getContrastColor("#0284c7")  // Returns "light" or "dark"
```

## Best Practices

### 1. Use Theme Values Consistently
```typescript
// ✅ Good
import { getColor, getSpacing } from "~/lib/styles";
const backgroundColor = getColor("primary", 100);
const padding = getSpacing(4);

// ❌ Avoid
const backgroundColor = "#e0f2fe";  // Magic value
const padding = "16px";              // Hard-coded
```

### 2. Leverage TypeScript for Type Safety
```typescript
// ✅ Good - TypeScript knows all valid options
import { colors, spacing } from "~/lib/theme";
type Color = keyof typeof colors;
type Space = keyof typeof spacing;

// Use with type checking
const myColor: Color = "primary";  // ✅ Valid
const invalid: Color = "invalid";  // ❌ TypeScript error
```

### 3. Use Component Size Utilities
```typescript
// ✅ Good - Consistent sizing
import { componentSizes } from "~/lib/theme";
const buttonSize = componentSizes.button.md;

// ❌ Avoid - Inconsistent sizing
const buttonSize = { padding: "8px 16px", height: "40px" };
```

### 4. Create Semantic Aliases
```typescript
// Create semantic names for colors in your context
const primaryColor = getColor("primary", 600);
const primaryLight = getColor("primary", 100);
const primaryDark = getColor("primary", 700);

const successColor = getColor("success", 500);
const errorColor = getColor("error", 500);
```

### 5. Use Responsive Utilities
```typescript
// ✅ Good - Responsive design
const spacing = createResponsiveSpacing(
  "2",  // mobile
  "4",  // tablet
  "6"   // desktop
);

// ❌ Avoid - Hard-coded values
const padding = { mobile: "8px", tablet: "16px", desktop: "24px" };
```

## Customizing the Theme

### Changing Colors
Edit `lib/theme.ts` and update the color values:
```typescript
export const colors = {
  primary: {
    500: "#YOUR_CUSTOM_COLOR",
    600: "#YOUR_CUSTOM_SHADE",
    // ... other shades
  },
  // ... other colors
};
```

### Adding New Colors
```typescript
export const colors = {
  // ... existing colors
  custom: {
    50: "#f0f4ff",
    500: "#3366ff",
    900: "#001a4d",
  },
};
```

### Adjusting Spacing Scale
```typescript
export const spacing = {
  // Modify existing values
  4: "12px",  // was "16px"
  // Add new values
  13: "52px",
};
```

### Updating Component Sizes
```typescript
export const componentSizes = {
  button: {
    md: {
      padding: "10px 20px",  // adjusted
      fontSize: "16px",
      height: "44px",        // adjusted
    },
  },
};
```

## Integration with Tailwind CSS

The theme works alongside Tailwind CSS:
- **Theme values** are used for precise control
- **Tailwind utilities** are used for rapid styling

```typescript
// Using theme for specific cases
import { getColor } from "~/lib/styles";

<div style={{ backgroundColor: getColor("primary", 600) }}>
  {/* Use Tailwind for common cases */}
  <button className="px-4 py-2 bg-primary-600 hover:bg-primary-700">
    Click me
  </button>
</div>
```

## Export Summary

### `lib/theme.ts` exports:
- `colors` - Complete color palette
- `typography` - Font system
- `spacing` - Spacing scale
- `borderRadius` - Border radius values
- `shadows` - Shadow definitions
- `breakpoints` - Responsive breakpoints
- `transitions` - Animation settings
- `componentSizes` - Component sizing
- `zIndex` - Z-index stack
- `theme` - Complete theme object
- `ThemeConfig` - TypeScript interface

### `lib/styles.ts` exports:
- `getColor()` - Get color values
- `getSpacing()` - Get spacing values
- `getBorderRadius()` - Get border radius
- `getShadow()` - Get shadow values
- `getTransition()` - Get transition values
- `getZIndex()` - Get z-index
- `getButtonStyles()` - Button styling
- `getInputStyles()` - Input styling
- `getCardStyles()` - Card styling
- `getAlertStyles()` - Alert styling
- `createResponsiveSpacing()` - Responsive helpers
- `createResponsiveFontSize()` - Font size helpers
- `getContrastColor()` - Color contrast
- `typographyPresets` - Typography presets
- Type exports for `ColorVariant`, `SizeVariant`

## Next Steps

1. **Import and use** the theme in your components
2. **Customize** colors and values to match your brand
3. **Create custom utilities** based on the pattern
4. **Document** any additional design tokens specific to your app
5. **Update** the theme when design requirements change

---

This system ensures that all styling is consistent, maintainable, and easy to update across the entire application!
