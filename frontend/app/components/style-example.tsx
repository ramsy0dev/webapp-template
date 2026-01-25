/**
 * Style Manager Usage Example Component
 * Demonstrates how to use the theme and style utilities
 */

import {
  getColor,
  getSpacing,
  getButtonStyles,
  getCardStyles,
  typographyPresets,
  getTransition,
} from "~/lib/styles";
import { spacing, borderRadius, shadows } from "~/lib/theme";

export function StyleExampleComponent() {
  // Color utilities
  const primaryColor = getColor("primary", 600);
  const errorColor = getColor("error", 500);
  const successColor = getColor("success", 500);

  // Spacing utilities
  const paddingMd = getSpacing(4);
  const marginLg = getSpacing(8);

  // Component style utilities
  const buttonStyle = getButtonStyles("primary", "md");
  const cardStyle = getCardStyles("lg");

  // Typography presets
  const heading = typographyPresets.h2;
  const body = typographyPresets.body;

  return (
    <div
      style={{
        padding: paddingMd,
        margin: marginLg,
        backgroundColor: getColor("neutral", 50),
        borderRadius: borderRadius.lg,
        transition: getTransition("base"),
      }}
    >
      {/* Heading using typography preset */}
      <h1
        style={{
          ...heading,
          color: primaryColor,
          marginBottom: spacing[4],
        }}
      >
        Style Manager Example
      </h1>

      {/* Card with preset styles */}
      <div
        style={{
          ...cardStyle,
          marginBottom: spacing[6],
          boxShadow: shadows.md,
        }}
      >
        {/* Body text using preset */}
        <p
          style={{
            ...body,
            color: getColor("neutral", 700),
            marginBottom: spacing[4],
          }}
        >
          This component demonstrates how to use the centralized style manager.
        </p>

        {/* Color showcase */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: spacing[4] }}>
          <div
            style={{
              padding: spacing[4],
              backgroundColor: primaryColor,
              color: "white",
              borderRadius: borderRadius.md,
              textAlign: "center",
            }}
          >
            Primary
          </div>
          <div
            style={{
              padding: spacing[4],
              backgroundColor: errorColor,
              color: "white",
              borderRadius: borderRadius.md,
              textAlign: "center",
            }}
          >
            Error
          </div>
          <div
            style={{
              padding: spacing[4],
              backgroundColor: successColor,
              color: "white",
              borderRadius: borderRadius.md,
              textAlign: "center",
            }}
          >
            Success
          </div>
        </div>
      </div>

      {/* Button using style generator */}
      <button
        style={{
          ...buttonStyle,
          width: "100%",
          borderRadius: borderRadius.md,
          border: "none",
          cursor: "pointer",
          fontWeight: 600,
        }}
      >
        Themed Button
      </button>
    </div>
  );
}

export default StyleExampleComponent;
