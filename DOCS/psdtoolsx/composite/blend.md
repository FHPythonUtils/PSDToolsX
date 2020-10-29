# blend

> Auto-generated documentation for [psdtoolsx.composite.blend](../../../psdtoolsx/composite/blend.py) module.

Blend mode implementations.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [composite](index.md#composite) / blend
    - [color](#color)
    - [color_burn](#color_burn)
    - [color_dodge](#color_dodge)
    - [darken](#darken)
    - [darker_color](#darker_color)
    - [difference](#difference)
    - [dissolve](#dissolve)
    - [divide](#divide)
    - [exclusion](#exclusion)
    - [hard_light](#hard_light)
    - [hard_mix](#hard_mix)
    - [hue](#hue)
    - [lighten](#lighten)
    - [lighter_color](#lighter_color)
    - [linear_burn](#linear_burn)
    - [linear_dodge](#linear_dodge)
    - [linear_light](#linear_light)
    - [luminosity](#luminosity)
    - [multiply](#multiply)
    - [non_separable](#non_separable)
    - [normal](#normal)
    - [overlay](#overlay)
    - [pin_light](#pin_light)
    - [saturation](#saturation)
    - [screen](#screen)
    - [soft_light](#soft_light)
    - [subtract](#subtract)
    - [vivid_light](#vivid_light)

## color

[[find in source code]](../../../psdtoolsx/composite/blend.py#L216)

```python
@non_separable()
def color(Cb, Cs):
```

## color_burn

[[find in source code]](../../../psdtoolsx/composite/blend.py#L47)

```python
def color_burn(Cb, Cs, s=1.0):
```

## color_dodge

[[find in source code]](../../../psdtoolsx/composite/blend.py#L38)

```python
def color_dodge(Cb, Cs, s=1.0):
```

## darken

[[find in source code]](../../../psdtoolsx/composite/blend.py#L30)

```python
def darken(Cb, Cs):
```

## darker_color

[[find in source code]](../../../psdtoolsx/composite/blend.py#L226)

```python
@non_separable()
def darker_color(Cb, Cs):
```

## difference

[[find in source code]](../../../psdtoolsx/composite/blend.py#L134)

```python
def difference(Cb, Cs):
```

## dissolve

[[find in source code]](../../../psdtoolsx/composite/blend.py#L242)

```python
def dissolve(Cb, Cs):
```

## divide

[[find in source code]](../../../psdtoolsx/composite/blend.py#L160)

```python
def divide(Cb, Cs):
```

Looks at the color information in each channel and divides the blend color
from the base color.

## exclusion

[[find in source code]](../../../psdtoolsx/composite/blend.py#L138)

```python
def exclusion(Cb, Cs):
```

## hard_light

[[find in source code]](../../../psdtoolsx/composite/blend.py#L63)

```python
def hard_light(Cb, Cs):
```

## hard_mix

[[find in source code]](../../../psdtoolsx/composite/blend.py#L146)

```python
def hard_mix(Cb, Cs):
```

Adds the red, green and blue channel values of the blend color to the RGB
values of the base color. If the resulting sum for a channel is 255 or
greater, it receives a value of 255; if less than 255, a value of 0.
Therefore, all blended pixels have red, green, and blue channel values of
either 0 or 255. This changes all pixels to primary additive colors (red,
green, or blue), white, or black.

## hue

[[find in source code]](../../../psdtoolsx/composite/blend.py#L206)

```python
@non_separable()
def hue(Cb, Cs):
```

## lighten

[[find in source code]](../../../psdtoolsx/composite/blend.py#L34)

```python
def lighten(Cb, Cs):
```

## lighter_color

[[find in source code]](../../../psdtoolsx/composite/blend.py#L234)

```python
@non_separable()
def lighter_color(Cb, Cs):
```

## linear_burn

[[find in source code]](../../../psdtoolsx/composite/blend.py#L59)

```python
def linear_burn(Cb, Cs):
```

## linear_dodge

[[find in source code]](../../../psdtoolsx/composite/blend.py#L55)

```python
def linear_dodge(Cb, Cs):
```

## linear_light

[[find in source code]](../../../psdtoolsx/composite/blend.py#L105)

```python
def linear_light(Cb, Cs):
```

Burns or dodges the colors by decreasing or increasing the brightness,
depending on the blend color. If the blend color (light source) is lighter
than 50% gray, the image is lightened by increasing the brightness. If the
blend color is darker than 50% gray, the image is darkened by decreasing
the brightness.

## luminosity

[[find in source code]](../../../psdtoolsx/composite/blend.py#L221)

```python
@non_separable('s')
def luminosity(Cb, Cs):
```

## multiply

[[find in source code]](../../../psdtoolsx/composite/blend.py#L18)

```python
def multiply(Cb, Cs):
```

## non_separable

[[find in source code]](../../../psdtoolsx/composite/blend.py#L174)

```python
def non_separable(k='s'):
```

Wrap non-separable blending function for CMYK handling.

.. note: This implementation is still inaccurate.

## normal

[[find in source code]](../../../psdtoolsx/composite/blend.py#L14)

```python
def normal(Cb, Cs):
```

## overlay

[[find in source code]](../../../psdtoolsx/composite/blend.py#L26)

```python
def overlay(Cb, Cs):
```

## pin_light

[[find in source code]](../../../psdtoolsx/composite/blend.py#L119)

```python
def pin_light(Cb, Cs):
```

Replaces the colors, depending on the blend color. If the blend color
(light source) is lighter than 50% gray, pixels darker than the blend color
are replaced, and pixels lighter than the blend color do not change. If the
blend color is darker than 50% gray, pixels lighter than the blend color
are replaced, and pixels darker than the blend color do not change. This is
useful for adding special effects to an image.

## saturation

[[find in source code]](../../../psdtoolsx/composite/blend.py#L211)

```python
@non_separable()
def saturation(Cb, Cs):
```

## screen

[[find in source code]](../../../psdtoolsx/composite/blend.py#L22)

```python
def screen(Cb, Cs):
```

## soft_light

[[find in source code]](../../../psdtoolsx/composite/blend.py#L70)

```python
def soft_light(Cb, Cs):
```

## subtract

[[find in source code]](../../../psdtoolsx/composite/blend.py#L142)

```python
def subtract(Cb, Cs):
```

## vivid_light

[[find in source code]](../../../psdtoolsx/composite/blend.py#L86)

```python
def vivid_light(Cb, Cs):
```

Burns or dodges the colors by increasing or decreasing the contrast,
depending on the blend color. If the blend color (light source) is lighter
than 50% gray, the image is lightened by decreasing the contrast. If the
blend color is darker than 50% gray, the image is darkened by increasing
the contrast.
