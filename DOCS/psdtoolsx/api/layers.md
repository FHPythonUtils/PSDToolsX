# layers

> Auto-generated documentation for [psdtoolsx.api.layers](../../../psdtoolsx/api/layers.py) module.

Layer module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / layers
    - [AdjustmentLayer](#adjustmentlayer)
        - [AdjustmentLayer().compose](#adjustmentlayercompose)
    - [Artboard](#artboard)
        - [Artboard().bbox](#artboardbbox)
        - [Artboard().bottom](#artboardbottom)
        - [Artboard().compose](#artboardcompose)
        - [Artboard().left](#artboardleft)
        - [Artboard().right](#artboardright)
        - [Artboard().top](#artboardtop)
    - [FillLayer](#filllayer)
        - [FillLayer().bottom](#filllayerbottom)
        - [FillLayer().left](#filllayerleft)
        - [FillLayer().right](#filllayerright)
        - [FillLayer().top](#filllayertop)
    - [Group](#group)
        - [Group().blend_mode](#groupblend_mode)
        - [Group().blend_mode](#groupblend_mode)
        - [Group().composite](#groupcomposite)
        - [Group.extract_bbox](#groupextract_bbox)
    - [GroupMixin](#groupmixin)
        - [GroupMixin().bbox](#groupmixinbbox)
        - [GroupMixin().bottom](#groupmixinbottom)
        - [GroupMixin().compose](#groupmixincompose)
        - [GroupMixin().descendants](#groupmixindescendants)
        - [GroupMixin().left](#groupmixinleft)
        - [GroupMixin().right](#groupmixinright)
        - [GroupMixin().top](#groupmixintop)
    - [Layer](#layer)
        - [Layer().bbox](#layerbbox)
        - [Layer().blend_mode](#layerblend_mode)
        - [Layer().blend_mode](#layerblend_mode)
        - [Layer().bottom](#layerbottom)
        - [Layer().clip_layers](#layerclip_layers)
        - [Layer().compose](#layercompose)
        - [Layer().composite](#layercomposite)
        - [Layer().effects](#layereffects)
        - [Layer().has_clip_layers](#layerhas_clip_layers)
        - [Layer().has_effects](#layerhas_effects)
        - [Layer().has_mask](#layerhas_mask)
        - [Layer().has_origination](#layerhas_origination)
        - [Layer().has_pixels](#layerhas_pixels)
        - [Layer().has_stroke](#layerhas_stroke)
        - [Layer().has_vector_mask](#layerhas_vector_mask)
        - [Layer().height](#layerheight)
        - [Layer().is_group](#layeris_group)
        - [Layer().is_visible](#layeris_visible)
        - [Layer().kind](#layerkind)
        - [Layer().layer_id](#layerlayer_id)
        - [Layer().left](#layerleft)
        - [Layer().left](#layerleft)
        - [Layer().mask](#layermask)
        - [Layer().name](#layername)
        - [Layer().name](#layername)
        - [Layer().numpy](#layernumpy)
        - [Layer().offset](#layeroffset)
        - [Layer().offset](#layeroffset)
        - [Layer().opacity](#layeropacity)
        - [Layer().opacity](#layeropacity)
        - [Layer().origination](#layerorigination)
        - [Layer().parent](#layerparent)
        - [Layer().right](#layerright)
        - [Layer().size](#layersize)
        - [Layer().stroke](#layerstroke)
        - [Layer().tagged_blocks](#layertagged_blocks)
        - [Layer().top](#layertop)
        - [Layer().top](#layertop)
        - [Layer().topil](#layertopil)
        - [Layer().vector_mask](#layervector_mask)
        - [Layer().visible](#layervisible)
        - [Layer().visible](#layervisible)
        - [Layer().width](#layerwidth)
    - [PixelLayer](#pixellayer)
    - [ShapeLayer](#shapelayer)
        - [ShapeLayer().bbox](#shapelayerbbox)
        - [ShapeLayer().bottom](#shapelayerbottom)
        - [ShapeLayer().left](#shapelayerleft)
        - [ShapeLayer().right](#shapelayerright)
        - [ShapeLayer().top](#shapelayertop)
    - [SmartObjectLayer](#smartobjectlayer)
        - [SmartObjectLayer().smart_object](#smartobjectlayersmart_object)
    - [TypeLayer](#typelayer)
        - [TypeLayer().document_resources](#typelayerdocument_resources)
        - [TypeLayer().engine_dict](#typelayerengine_dict)
        - [TypeLayer().resource_dict](#typelayerresource_dict)
        - [TypeLayer().text](#typelayertext)
        - [TypeLayer().transform](#typelayertransform)
        - [TypeLayer().warp](#typelayerwarp)

## AdjustmentLayer

[[find in source code]](../../../psdtoolsx/api/layers.py#L921)

```python
class AdjustmentLayer(Layer):
    def __init__(*args):
```

Layer that applies specified image adjustment effect.

#### See also

- [Layer](#layer)

### AdjustmentLayer().compose

[[find in source code]](../../../psdtoolsx/api/layers.py#L929)

```python
def compose(**kwargs):
```

Adjustment layer is never composed.

#### Returns

None

## Artboard

[[find in source code]](../../../psdtoolsx/api/layers.py#L681)

```python
class Artboard(Group):
```

Artboard is a special kind of group that has a pre-defined viewbox.

Example

```python
artboard = psd[1]
image = artboard.compose()
```

#### See also

- [Group](#group)

### Artboard().bbox

[[find in source code]](../../../psdtoolsx/api/layers.py#L717)

```python
@property
def bbox():
```

(left, top, right, bottom) tuple.

### Artboard().bottom

[[find in source code]](../../../psdtoolsx/api/layers.py#L713)

```python
@property
def bottom():
```

### Artboard().compose

[[find in source code]](../../../psdtoolsx/api/layers.py#L737)

```python
def compose(bbox=None, **kwargs):
```

Compose the artboard.

See :py:func:`~psdtoolsx.compose` for available extra arguments.

#### Arguments

- `bbox` - Viewport tuple (left, top, right, bottom).

#### Returns

:pyclass `PIL.Image`, or `None` if there is no pixel.

### Artboard().left

[[find in source code]](../../../psdtoolsx/api/layers.py#L701)

```python
@property
def left():
```

### Artboard().right

[[find in source code]](../../../psdtoolsx/api/layers.py#L709)

```python
@property
def right():
```

### Artboard().top

[[find in source code]](../../../psdtoolsx/api/layers.py#L705)

```python
@property
def top():
```

## FillLayer

[[find in source code]](../../../psdtoolsx/api/layers.py#L938)

```python
class FillLayer(Layer):
    def __init__(*args):
```

Layer that fills the canvas region.

#### See also

- [Layer](#layer)

### FillLayer().bottom

[[find in source code]](../../../psdtoolsx/api/layers.py#L958)

```python
@property
def bottom():
```

### FillLayer().left

[[find in source code]](../../../psdtoolsx/api/layers.py#L946)

```python
@property
def left():
```

### FillLayer().right

[[find in source code]](../../../psdtoolsx/api/layers.py#L954)

```python
@property
def right():
```

### FillLayer().top

[[find in source code]](../../../psdtoolsx/api/layers.py#L950)

```python
@property
def top():
```

## Group

[[find in source code]](../../../psdtoolsx/api/layers.py#L586)

```python
class Group(GroupMixin, Layer):
    def __init__(*args):
```

Group of layers.

Example

```python
group = psd[1]
for layer in group:
    if layer.kind == 'pixel':
        print(layer.name)
```

#### See also

- [GroupMixin](#groupmixin)
- [Layer](#layer)

### Group().blend_mode

[[find in source code]](../../../psdtoolsx/api/layers.py#L634)

```python
@property
def blend_mode():
```

### Group().blend_mode

[[find in source code]](../../../psdtoolsx/api/layers.py#L641)

```python
@blend_mode.setter
def blend_mode(value):
```

### Group().composite

[[find in source code]](../../../psdtoolsx/api/layers.py#L652)

```python
def composite(
    viewport=None,
    force=False,
    color=1.0,
    alpha=0.0,
    layer_filter=None,
):
```

Composite layer and masks (mask, vector mask, and clipping layers).

#### Arguments

- `viewport` - Viewport bounding box specified by (x1, y1, x2, y2)
    tuple. Default is the layer's bbox.
- `force` - Boolean flag to force vector drawing.
- `color` - Backdrop color specified by scalar or tuple of scalar.
    The color value should be in [0.0, 1.0]. For example, (1., 0., 0.)
    specifies red in RGB color mode.
- `alpha` - Backdrop alpha in [0.0, 1.0].
- `layer_filter` - Callable that takes a layer as argument and
    returns whether if the layer is composited. Default is
    :py:func:`~psdtoolsx.api.layers.PixelLayer.is_visible`.

#### Returns

:pyclass `PIL.Image`.

### Group.extract_bbox

[[find in source code]](../../../psdtoolsx/api/layers.py#L597)

```python
@staticmethod
def extract_bbox(layers, include_invisible=False):
```

Returns a bounding box for ``layers`` or (0, 0, 0, 0) if the layers
have no bounding box.

#### Arguments

- `include_invisible` - include invisible layers in calculation.

#### Returns

tuple of four int

## GroupMixin

[[find in source code]](../../../psdtoolsx/api/layers.py#L497)

```python
class GroupMixin(object):
```

### GroupMixin().bbox

[[find in source code]](../../../psdtoolsx/api/layers.py#L514)

```python
@property
def bbox():
```

(left, top, right, bottom) tuple.

### GroupMixin().bottom

[[find in source code]](../../../psdtoolsx/api/layers.py#L510)

```python
@property
def bottom():
```

### GroupMixin().compose

[[find in source code]](../../../psdtoolsx/api/layers.py#L536)

```python
@deprecated
def compose(
    force=False,
    bbox=None,
    layer_filter=None,
    context=None,
    color=None,
):
```

Compose layer and masks (mask, vector mask, and clipping layers).

#### Returns

PIL Image object, or None if the layer has no pixels.

#### See also

- [deprecated](index.md#deprecated)

### GroupMixin().descendants

[[find in source code]](../../../psdtoolsx/api/layers.py#L560)

```python
def descendants(include_clip=True):
```

Return a generator to iterate over all descendant layers.

Example

```python
# Iterate over all layers
for layer in psd.descendants():
    print(layer)

# Iterate over all layers in reverse order
for layer in reversed(list(psd.descendants())):
    print(layer)
```

#### Arguments

- `include_clip` - include clipping layers.

### GroupMixin().left

[[find in source code]](../../../psdtoolsx/api/layers.py#L498)

```python
@property
def left():
```

### GroupMixin().right

[[find in source code]](../../../psdtoolsx/api/layers.py#L506)

```python
@property
def right():
```

### GroupMixin().top

[[find in source code]](../../../psdtoolsx/api/layers.py#L502)

```python
@property
def top():
```

## Layer

[[find in source code]](../../../psdtoolsx/api/layers.py#L18)

```python
class Layer(object):
    def __init__(psd, record, channels, parent):
```

### Layer().bbox

[[find in source code]](../../../psdtoolsx/api/layers.py#L223)

```python
@property
def bbox():
```

(left, top, right, bottom) tuple.

### Layer().blend_mode

[[find in source code]](../../../psdtoolsx/api/layers.py#L116)

```python
@property
def blend_mode():
```

Blend mode of this layer. Writable.

Example

```python
from psdtoolsx.constants import BlendMode
if layer.blend_mode == BlendMode.NORMAL:
    layer.blend_mode = BlendMode.SCREEN
```

#### Returns

:pyclass `psdtoolsx.constants.BlendMode`.

### Layer().blend_mode

[[find in source code]](../../../psdtoolsx/api/layers.py#L131)

```python
@blend_mode.setter
def blend_mode(value):
```

### Layer().bottom

[[find in source code]](../../../psdtoolsx/api/layers.py#L174)

```python
@property
def bottom():
```

Bottom coordinate.

#### Returns

int

### Layer().clip_layers

[[find in source code]](../../../psdtoolsx/api/layers.py#L428)

```python
@property
def clip_layers():
```

Clip layers associated with this layer.

To compose clipping layers

```python
from psdtoolsx import compose
clip_mask = compose(layer.clip_layers)
```

#### Returns

list of layers

### Layer().compose

[[find in source code]](../../../psdtoolsx/api/layers.py#L362)

```python
@deprecated
def compose(force=False, bbox=None, layer_filter=None):
```

Deprecated, use :py:func:`~psdtoolsx.api.layers.PixelLayer.composite`.

Compose layer and masks (mask, vector mask, and clipping layers).

Note that the resulting image size is not necessarily equal to the
layer size due to different mask dimensions. The offset of the
composed image is stored at `.info['offset']` attribute of `PIL.Image`.

#### Arguments

- `bbox` - Viewport bounding box specified by (x1, y1, x2, y2) tuple.

#### Returns

:pyclass `PIL.Image`, or `None` if the layer has no pixel.

#### See also

- [deprecated](index.md#deprecated)

### Layer().composite

[[find in source code]](../../../psdtoolsx/api/layers.py#L394)

```python
def composite(
    viewport=None,
    force=False,
    color=1.0,
    alpha=0.0,
    layer_filter=None,
):
```

Composite layer and masks (mask, vector mask, and clipping layers).

#### Arguments

- `viewport` - Viewport bounding box specified by (x1, y1, x2, y2)
    tuple. Default is the layer's bbox.
- `force` - Boolean flag to force vector drawing.
- `color` - Backdrop color specified by scalar or tuple of scalar.
    The color value should be in [0.0, 1.0]. For example, (1., 0., 0.)
    specifies red in RGB color mode.
- `alpha` - Backdrop alpha in [0.0, 1.0].
- `layer_filter` - Callable that takes a layer as argument and
    returns whether if the layer is composited. Default is
    :py:func:`~psdtoolsx.api.layers.PixelLayer.is_visible`.

#### Returns

:pyclass `PIL.Image`.

### Layer().effects

[[find in source code]](../../../psdtoolsx/api/layers.py#L456)

```python
@property
def effects():
```

Layer effects.

#### Returns

:pyclass `psdtoolsx.api.effects.Effects`

### Layer().has_clip_layers

[[find in source code]](../../../psdtoolsx/api/layers.py#L420)

```python
def has_clip_layers():
```

Returns True if the layer has associated clipping.

#### Returns

`bool`

### Layer().has_effects

[[find in source code]](../../../psdtoolsx/api/layers.py#L442)

```python
def has_effects():
```

Returns True if the layer has effects.

#### Returns

`bool`

### Layer().has_mask

[[find in source code]](../../../psdtoolsx/api/layers.py#L240)

```python
def has_mask():
```

Returns True if the layer has a mask.

#### Returns

`bool`

### Layer().has_origination

[[find in source code]](../../../psdtoolsx/api/layers.py#L286)

```python
def has_origination():
```

Returns True if the layer has live shape properties.

#### Returns

`bool`

### Layer().has_pixels

[[find in source code]](../../../psdtoolsx/api/layers.py#L228)

```python
def has_pixels():
```

Returns True if the layer has associated pixels. When this is True,
[Layer().topil](#layertopil) method returns :pyclass `PIL.Image`.

#### Returns

`bool`

### Layer().has_stroke

[[find in source code]](../../../psdtoolsx/api/layers.py#L323)

```python
def has_stroke():
```

Returns True if the shape has a stroke.

### Layer().has_vector_mask

[[find in source code]](../../../psdtoolsx/api/layers.py#L259)

```python
def has_vector_mask():
```

Returns True if the layer has a vector mask.

#### Returns

`bool`

### Layer().height

[[find in source code]](../../../psdtoolsx/api/layers.py#L192)

```python
@property
def height():
```

Height of the layer.

#### Returns

int

### Layer().is_group

[[find in source code]](../../../psdtoolsx/api/layers.py#L108)

```python
def is_group():
```

Return True if the layer is a group.

#### Returns

`bool`

### Layer().is_visible

[[find in source code]](../../../psdtoolsx/api/layers.py#L81)

```python
def is_visible():
```

Layer visibility. Takes group visibility in account.

#### Returns

`bool`

### Layer().kind

[[find in source code]](../../../psdtoolsx/api/layers.py#L49)

```python
@property
def kind():
```

Kind of this layer, such as group, pixel, shape, type, smartobject,
or psdimage. Class name without `layer` suffix.

#### Returns

`str`

### Layer().layer_id

[[find in source code]](../../../psdtoolsx/api/layers.py#L59)

```python
@property
def layer_id():
```

Layer ID.

#### Returns

int layer id. if the layer is not assigned an id, -1.

### Layer().left

[[find in source code]](../../../psdtoolsx/api/layers.py#L135)

```python
@property
def left():
```

Left coordinate. Writable.

#### Returns

int

### Layer().left

[[find in source code]](../../../psdtoolsx/api/layers.py#L144)

```python
@left.setter
def left(value):
```

### Layer().mask

[[find in source code]](../../../psdtoolsx/api/layers.py#L248)

```python
@property
def mask():
```

Returns mask associated with this layer.

#### Returns

:pyclass `psdtoolsx.api.mask.Mask` or `None`

### Layer().name

[[find in source code]](../../../psdtoolsx/api/layers.py#L26)

```python
@property
def name():
```

Layer name. Writable.

#### Returns

`str`

### Layer().name

[[find in source code]](../../../psdtoolsx/api/layers.py#L37)

```python
@name.setter
def name(value):
```

### Layer().numpy

[[find in source code]](../../../psdtoolsx/api/layers.py#L383)

```python
def numpy(channel=None, real_mask=True):
```

Get NumPy array of the layer.

#### Arguments

- `channel` - Which channel to return, can be 'color',
    'shape', 'alpha', or 'mask'. Default is 'color+alpha'.

#### Returns

:pyclass `numpy.ndarray` or None if there is no pixel.

### Layer().offset

[[find in source code]](../../../psdtoolsx/api/layers.py#L201)

```python
@property
def offset():
```

(left, top) tuple. Writable.

#### Returns

`tuple`

### Layer().offset

[[find in source code]](../../../psdtoolsx/api/layers.py#L210)

```python
@offset.setter
def offset(value):
```

### Layer().opacity

[[find in source code]](../../../psdtoolsx/api/layers.py#L89)

```python
@property
def opacity():
```

Opacity of this layer in [0, 255] range. Writable.

#### Returns

int

### Layer().opacity

[[find in source code]](../../../psdtoolsx/api/layers.py#L98)

```python
@opacity.setter
def opacity(value):
```

### Layer().origination

[[find in source code]](../../../psdtoolsx/api/layers.py#L296)

```python
@property
def origination():
```

Property for a list of live shapes or a line.

Some of the vector masks have associated live shape properties, that
are Photoshop feature to handle primitive shapes such as a rectangle,
an ellipse, or a line. Vector masks without live shape properties are
plain path objects.

See :py:mod:[shape](shape.md#shape).

#### Returns

List of :pyclass `psdtoolsx.api.shape.Invalidated`,
    :pyclass `psdtoolsx.api.shape.Rectangle`,
    :pyclass `psdtoolsx.api.shape.RoundedRectangle`,
    :pyclass `psdtoolsx.api.shape.Ellipse`, or
    :pyclass `psdtoolsx.api.shape.Line`.

### Layer().parent

[[find in source code]](../../../psdtoolsx/api/layers.py#L103)

```python
@property
def parent():
```

Parent of this layer.

### Layer().right

[[find in source code]](../../../psdtoolsx/api/layers.py#L165)

```python
@property
def right():
```

Right coordinate.

#### Returns

int

### Layer().size

[[find in source code]](../../../psdtoolsx/api/layers.py#L214)

```python
@property
def size():
```

(width, height) tuple.

#### Returns

`tuple`

### Layer().stroke

[[find in source code]](../../../psdtoolsx/api/layers.py#L327)

```python
@property
def stroke():
```

Property for strokes.

### Layer().tagged_blocks

[[find in source code]](../../../psdtoolsx/api/layers.py#L467)

```python
@property
def tagged_blocks():
```

Layer tagged blocks that is a dict-like container of settings.

See :py:class:[Tag](../constants.md#tag) for available
keys.

#### Returns

:pyclass `psdtoolsx.psd.tagged_blocks.TaggedBlocks` or
    `None`.

Example

```python
from psdtoolsx.constants import Tag
metadata = layer.tagged_blocks.get_data(Tag.METADATA_SETTING)
```

### Layer().top

[[find in source code]](../../../psdtoolsx/api/layers.py#L150)

```python
@property
def top():
```

Top coordinate. Writable.

#### Returns

int

### Layer().top

[[find in source code]](../../../psdtoolsx/api/layers.py#L159)

```python
@top.setter
def top(value):
```

### Layer().topil

[[find in source code]](../../../psdtoolsx/api/layers.py#L337)

```python
def topil(channel=None, apply_icc=False):
```

Get PIL Image of the layer.

#### Arguments

- `channel` - Which channel to return; e.g., 0 for 'R' channel in RGB
    image. See :pyclass `psdtoolsx.constants.ChannelID`. When `None`,
    the method returns all the channels supported by PIL modes.
- `apply_icc` - Whether to apply ICC profile conversion to sRGB.

#### Returns

:pyclass `PIL.Image`, or `None` if the layer has no pixels.

Example

```python
from psdtoolsx.constants import ChannelID

image = layer.topil()
red = layer.topil(ChannelID.CHANNEL_0)
alpha = layer.topil(ChannelID.TRANSPARENCY_MASK)
```

#### Notes

Not all of the PSD image modes are supported in
    :pyclass `PIL.Image`. For example, 'CMYK' mode cannot include
    alpha channel in PIL. In this case, topil drops alpha channel.

### Layer().vector_mask

[[find in source code]](../../../psdtoolsx/api/layers.py#L270)

```python
@property
def vector_mask():
```

Returns vector mask associated with this layer.

#### Returns

:pyclass `psdtoolsx.api.shape.VectorMask` or `None`

### Layer().visible

[[find in source code]](../../../psdtoolsx/api/layers.py#L68)

```python
@property
def visible():
```

Layer visibility. Doesn't take group visibility in account. Writable.

#### Returns

`bool`

### Layer().visible

[[find in source code]](../../../psdtoolsx/api/layers.py#L77)

```python
@visible.setter
def visible(value):
```

### Layer().width

[[find in source code]](../../../psdtoolsx/api/layers.py#L183)

```python
@property
def width():
```

Width of the layer.

#### Returns

int

## PixelLayer

[[find in source code]](../../../psdtoolsx/api/layers.py#L750)

```python
class PixelLayer(Layer):
```

Layer that has rasterized image in pixels.

Example

```python
assert layer.kind == 'pixel':
image = layer.topil()
image.save('layer.png')

composed_image = layer.compose()
composed_image.save('composed-layer.png')
```

#### See also

- [Layer](#layer)

## ShapeLayer

[[find in source code]](../../../psdtoolsx/api/layers.py#L867)

```python
class ShapeLayer(Layer):
```

Layer that has drawing in vector mask.

#### See also

- [Layer](#layer)

### ShapeLayer().bbox

[[find in source code]](../../../psdtoolsx/api/layers.py#L887)

```python
@property
def bbox():
```

(left, top, right, bottom) tuple.

### ShapeLayer().bottom

[[find in source code]](../../../psdtoolsx/api/layers.py#L883)

```python
@property
def bottom():
```

### ShapeLayer().left

[[find in source code]](../../../psdtoolsx/api/layers.py#L871)

```python
@property
def left():
```

### ShapeLayer().right

[[find in source code]](../../../psdtoolsx/api/layers.py#L879)

```python
@property
def right():
```

### ShapeLayer().top

[[find in source code]](../../../psdtoolsx/api/layers.py#L875)

```python
@property
def top():
```

## SmartObjectLayer

[[find in source code]](../../../psdtoolsx/api/layers.py#L766)

```python
class SmartObjectLayer(Layer):
```

Layer that inserts external data.

Use :pyattribute `~psdtoolsx.api.layers.SmartObjectLayer.smart_object`
attribute to get the external data. See
:pyclass `psdtoolsx.api.smart_object.SmartObject`.

Example

```python
import io
if layer.smart_object.filetype == 'jpg':
    image = Image.open(io.BytesIO(layer.smart_object.data))
```

#### See also

- [Layer](#layer)

### SmartObjectLayer().smart_object

[[find in source code]](../../../psdtoolsx/api/layers.py#L780)

```python
@property
def smart_object():
```

Associated smart object.

#### Returns

:pyclass `psdtoolsx.api.smart_object.SmartObject`.

## TypeLayer

[[find in source code]](../../../psdtoolsx/api/layers.py#L792)

```python
class TypeLayer(Layer):
    def __init__(*args):
```

Layer that has text and styling information for fonts or paragraphs.

Text is accessible at :pyattribute `~psdtoolsx.api.layers.TypeLayer.text`
property. Styling information for paragraphs is in
:pyattribute `~psdtoolsx.api.layers.TypeLayer.engine_dict`.
Document styling information such as font list is is
:pyattribute `~psdtoolsx.api.layers.TypeLayer.resource_dict`.

Currently, textual information is read-only.

Example

```python
if layer.kind == 'type':
    print(layer.text)
    print(layer.engine_dict['StyleRun'])

    # Extract font for each substring in the text.
    text = layer.engine_dict['Editor']['Text'].value
    fontset = layer.resource_dict['FontSet']
    runlength = layer.engine_dict['StyleRun']['RunLengthArray']
    rundata = layer.engine_dict['StyleRun']['RunArray']
    index = 0
    for length, style in zip(runlength, rundata):
        substring = text[index:index + length]
        stylesheet = style['StyleSheet']['StyleSheetData']
        font = fontset[stylesheet['Font']]
        print('%r gets %s' % (substring, font))
        index += length
```

#### See also

- [Layer](#layer)

### TypeLayer().document_resources

[[find in source code]](../../../psdtoolsx/api/layers.py#L856)

```python
@property
def document_resources():
```

Resource set relevant to the document.

### TypeLayer().engine_dict

[[find in source code]](../../../psdtoolsx/api/layers.py#L846)

```python
@property
def engine_dict():
```

Styling information dict.

### TypeLayer().resource_dict

[[find in source code]](../../../psdtoolsx/api/layers.py#L851)

```python
@property
def resource_dict():
```

Resource set.

### TypeLayer().text

[[find in source code]](../../../psdtoolsx/api/layers.py#L827)

```python
@property
def text():
```

Text in the layer. Read-only.

#### Notes

New-line character in Photoshop is `'\\r'`.

### TypeLayer().transform

[[find in source code]](../../../psdtoolsx/api/layers.py#L836)

```python
@property
def transform():
```

Matrix (xx, xy, yx, yy, tx, ty) applies affine transformation.

### TypeLayer().warp

[[find in source code]](../../../psdtoolsx/api/layers.py#L861)

```python
@property
def warp():
```

Warp configuration.
