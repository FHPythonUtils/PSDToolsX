# effects

> Auto-generated documentation for [psdtoolsx.composer.effects](../../../psdtoolsx/composer/effects.py) module.

Effects module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [composer](index.md#composer) / effects
    - [create_stroke_effect](#create_stroke_effect)
    - [create_stroke_mask](#create_stroke_mask)

## create_stroke_effect

[[find in source code]](../../../psdtoolsx/composer/effects.py#L15)

```python
def create_stroke_effect(alpha, setting, psd, mask_given=False):
```

## create_stroke_mask

[[find in source code]](../../../psdtoolsx/composer/effects.py#L33)

```python
def create_stroke_mask(alpha, setting):
```

Create a mask image for the given alpha image.

TODO: MaxFilter is square, but the desired region is circle.
