# blend

> Auto-generated documentation for [psdtoolsx.composer.blend](../../../psdtoolsx/composer/blend.py) module.

Blending module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [composer](index.md#composer) / blend
    - [blend](#blend)
    - [hls_to_rgb](#hls_to_rgb)
    - [rgb_to_hls](#rgb_to_hls)

Check Blending_ section of W3C recommendation for blending mode definitions.

.. _Blending: https://www.w3.org/TR/compositing/#blending

## blend

[[find in source code]](../../../psdtoolsx/composer/blend.py#L20)

```python
def blend(backdrop, image, offset, mode=None):
```

## hls_to_rgb

[[find in source code]](../../../psdtoolsx/composer/blend.py#L313)

```python
def hls_to_rgb(h, l, s):
```

HSL to RGB conversion.

See colorsys module.

## rgb_to_hls

[[find in source code]](../../../psdtoolsx/composer/blend.py#L279)

```python
def rgb_to_hls(rgb):
```

RGB to HSL conversion.

See colorsys module.
