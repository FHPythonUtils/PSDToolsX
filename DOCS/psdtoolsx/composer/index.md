# composer

> Auto-generated documentation for [psdtoolsx.composer](../../../psdtoolsx/composer/__init__.py) module.

Composer API.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / composer
    - [apply_effect](#apply_effect)
    - [apply_mask](#apply_mask)
    - [apply_opacity](#apply_opacity)
    - [compose](#compose)
    - [compose_layer](#compose_layer)
    - [create_fill](#create_fill)
    - [intersect](#intersect)
    - [union](#union)
    - Modules
        - [blend](blend.md#blend)
        - [effects](effects.md#effects)
        - [vector](vector.md#vector)

Composer takes responsibility of rendering layers as an image.

## apply_effect

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L312)

```python
def apply_effect(layer, backdrop, base_image):
```

Apply effect to the image.

..note: Correct effect order is the following. All the effects are first
    applied to the original image then blended together.

* dropshadow
* outerglow
* (original)
* patternoverlay
* gradientoverlay
* coloroverlay
* innershadow
* innerglow
* bevelemboss
* satin
* stroke

## apply_mask

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L269)

```python
def apply_mask(layer, image, bbox=None):
```

Apply raster mask to the image.

This might change the size and offset of the image. Resulting offset wrt
the psd viewport is kept in `image.info['offset']` field.

#### Arguments

- `layer` - `~psdtoolsx.api.layers.Layer`
- `image` - PIL.Image

#### Returns

PIL.Image

## apply_opacity

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L399)

```python
def apply_opacity(image, opacity):
```

## compose

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L48)

```python
@deprecated
def compose(
    layers,
    force=False,
    bbox=None,
    layer_filter=None,
    context=None,
    color=None,
):
```

Compose layers to a single :pyclass `PIL.Image`.
If the layers do not have visible pixels, the function returns `None`.

Example

```python
image = compose([layer1, layer2])
```

In order to skip some layers, pass `layer_filter` function which
should take `layer` as an argument and return `True` to keep the layer
or return `False` to skip

```python
image = compose(
    layers,
    layer_filter=lambda x: x.is_visible() and x.kind == 'type'
)
```

By default, visible layers are composed.

#### Notes

This function is experimental and does not guarantee
    Photoshop-quality rendering.

Currently the following are ignored:

- Adjustments layers
- Layer effects
- Blending modes: dissolve and darker/lighter color becomes normal

Shape drawing is inaccurate if the PSD file is not saved with
maximum compatibility.

Some of the blending modes do not reproduce photoshop blending.

#### Arguments

- `layers` - a layer, or an iterable of layers.
- `bbox` - (left, top, bottom, right) tuple that specifies a region to
    compose. By default, all the visible area is composed. The origin
    is at the top-left corner of the PSD document.
- `context` - `PIL.Image` object for the backdrop rendering context. Must
    be used with the correct `bbox` size.
- `layer_filter` - a callable that takes a layer and returns `bool`.
- `color` - background color in `int` or `tuple`.
- `kwargs` - arguments passed to underling `topil()` call.

#### Returns

:pyclass `PIL.Image` or `None`.

#### See also

- [deprecated](../api/index.md#deprecated)

## compose_layer

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L168)

```python
def compose_layer(layer, force=False):
```

Compose a single layer with pixels.

## create_fill

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L238)

```python
def create_fill(layer):
```

## intersect

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L36)

```python
def intersect(*bboxes):
```

## union

[[find in source code]](../../../psdtoolsx/composer/__init__.py#L24)

```python
def union(*bboxes):
```
