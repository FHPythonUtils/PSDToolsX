# vector

> Auto-generated documentation for [psdtoolsx.composer.vector](../../../psdtoolsx/composer/vector.py) module.

Vector module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [composer](index.md#composer) / vector
    - [draw_gradient_fill](#draw_gradient_fill)
    - [draw_pattern_fill](#draw_pattern_fill)
    - [draw_solid_color_fill](#draw_solid_color_fill)
    - [draw_stroke](#draw_stroke)
    - [draw_vector_mask](#draw_vector_mask)

## draw_gradient_fill

[[find in source code]](../../../psdtoolsx/composer/vector.py#L203)

```python
def draw_gradient_fill(size, setting):
```

Create a gradient fill image.

#### Arguments

- `size` - (width, height) tuple.
- `setting` - Descriptor containing pattern fill.

## draw_pattern_fill

[[find in source code]](../../../psdtoolsx/composer/vector.py#L171)

```python
def draw_pattern_fill(size, psd, setting):
```

Create a pattern fill image.

#### Arguments

- `size` - (width, height) tuple.
- `psd` - :pyclass `PSDImage`.
- `setting` - Descriptor containing pattern fill.

## draw_solid_color_fill

[[find in source code]](../../../psdtoolsx/composer/vector.py#L158)

```python
def draw_solid_color_fill(size, setting):
```

## draw_stroke

[[find in source code]](../../../psdtoolsx/composer/vector.py#L49)

```python
def draw_stroke(backdrop, layer, vector_mask=None):
```

## draw_vector_mask

[[find in source code]](../../../psdtoolsx/composer/vector.py#L20)

```python
def draw_vector_mask(layer, bbox=None):
```
