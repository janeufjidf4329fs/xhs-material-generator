# Xiaohongshu Style Guide

This document outlines the style standards for the Xiaohongshu image generator, based on the `base_template.html` file.

## 1. Color Palette

The color scheme is designed to be soft, warm, and inviting.

| Color          | Hex/RGBA Code                     | Usage                                    |
|----------------|-----------------------------------|------------------------------------------|
| Gradient Start | `#FFC3A0`                         | Background gradient (top left)           |
| Gradient End   | `#FFAFBD`                         | Background gradient (bottom right)       |
| Container      | `rgba(255, 255, 255, 0.9)`        | Main content background (semi-transparent) |
| Title Text     | `#333333`                         | Main title text color                    |
| Content Text   | `#444444`                         | Body text color                          |
| Footer Text    | `#888888`                         | Footer text color                        |
| Borders        | `rgba(0, 0, 0, 0.05)`             | Separator lines                          |

## 2. Font Usage

The typography is designed for clarity and modern aesthetics.

- **Font Family**: `'Noto Sans SC', sans-serif` (imported from Google Fonts)

| Element      | Font Size | Font Weight | Notes                                      |
|--------------|-----------|-------------|--------------------------------------------|
| Title        | `80px`    | `700` (Bold)| For strong emphasis and visual hierarchy.  |
| Content      | `48px`    | `400` (Normal)| For optimal readability of the main text.  |
| Footer       | `36px`    | `400` (Normal)| For less prominent, secondary information. |

## 3. Spacing and Layout

Consistent spacing and a clear layout are crucial for a clean design.

- **Image Size**: `1242px` x `1660px`
- **Container Size**: `1100px` x `1520px`
- **Container Padding**: `80px` on all sides
- **Content Line Height**: `2.0` (or 200% of font size) for excellent readability.
- **Title Padding**: `60px` bottom padding.
- **Content Padding**: `60px` top and bottom padding.
- **Footer Padding**: `60px` top padding.

## 4. Component Style Guide

This section details the styles of the main UI components.

### Container (`.container`)

- **Background**: Semi-transparent white (`rgba(255, 255, 255, 0.9)`)
- **Border Radius**: `50px` for a soft, rounded look.
- **Shadow**: A subtle `box-shadow` (`0 10px 30px rgba(0, 0, 0, 0.1)`) to create depth.

### Title Area (`.title-area`)

- **Alignment**: Centered text.
- **Border**: A `3px` solid border on the bottom with a very low opacity (`rgba(0,0,0,0.05)`) to act as a subtle separator.

### Content Area (`.content-area`)

- **Layout**: Set to `flex-grow: 1` to fill the available vertical space.
- **Alignment**: Left-aligned text for a classic, readable format.

### Footer Area (`.footer-area`)

- **Alignment**: Centered text.
- **Border**: A `3px` solid border on the top with a very low opacity (`rgba(0,0,0,0.05)`) to separate it from the main content.
