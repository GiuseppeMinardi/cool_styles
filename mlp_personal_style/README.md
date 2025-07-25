# MLP Personal Style

A simple matplotlib style package with direct style imports.

## Installation

You can install the package directly from source:

```bash
pip install .
```

Or if the package is published on PyPI:

```bash
pip install mlp_personal_style
```

## Usage

This package is designed to be simple and direct. It provides style paths that can be used directly with matplotlib's `plt.style.use()`.

### Basic Usage

```python
from matplotlib import pyplot as plt
from mlp_personal_style import light, dark

# Use light theme
plt.style.use(light.incredible_style)

# Create your plot
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Sample Plot with Light Style')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# Or use dark theme
plt.style.use(dark.incredible_style)

# Create another plot
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Sample Plot with Dark Style')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
```

### Available Styles

- **Light Styles**:
  - `light.incredible_style`: A clean, light-themed style with a carefully selected color palette.

- **Dark Styles**:
  - `dark.incredible_style`: A dark-themed style perfect for presentations or dark mode interfaces.

### Listing All Available Styles

You can access lists of all available styles:

```python
from mlp_personal_style import light, dark

# Get all light styles
print(light.available_styles)

# Get all dark styles
print(dark.available_styles)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.