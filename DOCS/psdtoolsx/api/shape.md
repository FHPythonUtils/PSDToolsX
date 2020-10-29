# shape

> Auto-generated documentation for [psdtoolsx.api.shape](../../../psdtoolsx/api/shape.py) module.

Shape module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / shape
    - [Ellipse](#ellipse)
    - [Invalidated](#invalidated)
        - [Invalidated().invalidated](#invalidatedinvalidated)
    - [Line](#line)
        - [Line().arrow_conc](#linearrow_conc)
        - [Line().arrow_end](#linearrow_end)
        - [Line().arrow_length](#linearrow_length)
        - [Line().arrow_start](#linearrow_start)
        - [Line().arrow_width](#linearrow_width)
        - [Line().line_end](#lineline_end)
        - [Line().line_start](#lineline_start)
        - [Line().line_weight](#lineline_weight)
    - [Origination](#origination)
        - [Origination().bbox](#originationbbox)
        - [Origination.create](#originationcreate)
        - [Origination().index](#originationindex)
        - [Origination().invalidated](#originationinvalidated)
        - [Origination().origin_type](#originationorigin_type)
        - [Origination().resolution](#originationresolution)
    - [Rectangle](#rectangle)
    - [RoundedRectangle](#roundedrectangle)
        - [RoundedRectangle().radii](#roundedrectangleradii)
    - [Stroke](#stroke)
        - [Stroke().blend_mode](#strokeblend_mode)
        - [Stroke().content](#strokecontent)
        - [Stroke().enabled](#strokeenabled)
        - [Stroke().fill_enabled](#strokefill_enabled)
        - [Stroke().line_alignment](#strokeline_alignment)
        - [Stroke().line_cap_type](#strokeline_cap_type)
        - [Stroke().line_dash_offset](#strokeline_dash_offset)
        - [Stroke().line_dash_set](#strokeline_dash_set)
        - [Stroke().line_join_type](#strokeline_join_type)
        - [Stroke().line_width](#strokeline_width)
        - [Stroke().miter_limit](#strokemiter_limit)
        - [Stroke().opacity](#strokeopacity)
        - [Stroke().scale_lock](#strokescale_lock)
        - [Stroke().stroke_adjust](#strokestroke_adjust)
    - [VectorMask](#vectormask)
        - [VectorMask().bbox](#vectormaskbbox)
        - [VectorMask().clipboard_record](#vectormaskclipboard_record)
        - [VectorMask().disabled](#vectormaskdisabled)
        - [VectorMask().initial_fill_rule](#vectormaskinitial_fill_rule)
        - [VectorMask().initial_fill_rule](#vectormaskinitial_fill_rule)
        - [VectorMask().inverted](#vectormaskinverted)
        - [VectorMask().not_linked](#vectormasknot_linked)
        - [VectorMask().paths](#vectormaskpaths)

In PSD/PSB, shapes are all represented as :pyclass `VectorMask` in each
layer, and optionally there might be :pyclass `Origination` object to control
live shape properties and :pyclass `Stroke` to specify how outline is
stylized.

## Ellipse

[[find in source code]](../../../psdtoolsx/api/shape.py#L359)

```python
class Ellipse(Origination):
```

Ellipse live shape.

#### See also

- [Origination](#origination)

## Invalidated

[[find in source code]](../../../psdtoolsx/api/shape.py#L337)

```python
class Invalidated(Origination):
```

Invalidated live shape.

This equals to a primitive shape that does not provide Live shape
properties. Use :pyclass `psdtoolsx.api.shape.VectorMask` to access
shape information instead of this origination object.

#### See also

- [Origination](#origination)

### Invalidated().invalidated

[[find in source code]](../../../psdtoolsx/api/shape.py#L346)

```python
@property
def invalidated():
```

## Line

[[find in source code]](../../../psdtoolsx/api/shape.py#L378)

```python
class Line(Origination):
```

Line live shape.

#### See also

- [Origination](#origination)

### Line().arrow_conc

[[find in source code]](../../../psdtoolsx/api/shape.py#L441)

```python
@property
def arrow_conc():
```

#### Returns

`int`

### Line().arrow_end

[[find in source code]](../../../psdtoolsx/api/shape.py#L416)

```python
@property
def arrow_end():
```

Line arrow end.

#### Returns

`bool`

### Line().arrow_length

[[find in source code]](../../../psdtoolsx/api/shape.py#L433)

```python
@property
def arrow_length():
```

Line arrow length.

#### Returns

`float`

### Line().arrow_start

[[find in source code]](../../../psdtoolsx/api/shape.py#L408)

```python
@property
def arrow_start():
```

Line arrow start.

#### Returns

`bool`

### Line().arrow_width

[[find in source code]](../../../psdtoolsx/api/shape.py#L425)

```python
@property
def arrow_width():
```

Line arrow width.

#### Returns

`float`

### Line().line_end

[[find in source code]](../../../psdtoolsx/api/shape.py#L381)

```python
@property
def line_end():
```

Line end.

#### Returns

:pyclass `psdtoolsx.psd.descriptor.Descriptor`

### Line().line_start

[[find in source code]](../../../psdtoolsx/api/shape.py#L390)

```python
@property
def line_start():
```

Line start.

#### Returns

:pyclass `psdtoolsx.psd.descriptor.Descriptor`

### Line().line_weight

[[find in source code]](../../../psdtoolsx/api/shape.py#L399)

```python
@property
def line_weight():
```

Line weight

#### Returns

`float`

## Origination

[[find in source code]](../../../psdtoolsx/api/shape.py#L256)

```python
class Origination(object):
    def __init__(data):
```

Vector origination.

Vector origination keeps live shape properties for some of the primitive
shapes.

### Origination().bbox

[[find in source code]](../../../psdtoolsx/api/shape.py#L297)

```python
@property
def bbox():
```

Bounding box of the live shape.

#### Returns

:pyclass `psdtoolsx.psd.descriptor.Descriptor`

### Origination.create

[[find in source code]](../../../psdtoolsx/api/shape.py#L264)

```python
@classmethod
def create(data):
```

### Origination().index

[[find in source code]](../../../psdtoolsx/api/shape.py#L314)

```python
@property
def index():
```

Origination item index.

#### Returns

`int`

### Origination().invalidated

[[find in source code]](../../../psdtoolsx/api/shape.py#L323)

```python
@property
def invalidated():
```

#### Returns

`bool`

### Origination().origin_type

[[find in source code]](../../../psdtoolsx/api/shape.py#L275)

```python
@property
def origin_type():
```

Type of the vector shape.

* 1: :pyclass `psdtoolsx.api.shape.Rectangle`
* 2: :pyclass `psdtoolsx.api.shape.RoundedRectangle`
* 4: :pyclass `psdtoolsx.api.shape.Line`
* 5: :pyclass `psdtoolsx.api.shape.Ellipse`

#### Returns

`int`

### Origination().resolution

[[find in source code]](../../../psdtoolsx/api/shape.py#L289)

```python
@property
def resolution():
```

Resolution.

#### Returns

`float`

## Rectangle

[[find in source code]](../../../psdtoolsx/api/shape.py#L354)

```python
class Rectangle(Origination):
```

Rectangle live shape.

#### See also

- [Origination](#origination)

## RoundedRectangle

[[find in source code]](../../../psdtoolsx/api/shape.py#L364)

```python
class RoundedRectangle(Origination):
```

Rounded rectangle live shape.

#### See also

- [Origination](#origination)

### RoundedRectangle().radii

[[find in source code]](../../../psdtoolsx/api/shape.py#L367)

```python
@property
def radii():
```

Corner radii of rounded rectangles.
The order is top-left, top-right, bottom-left, bottom-right.

#### Returns

:pyclass `psdtoolsx.psd.descriptor.Descriptor`

## Stroke

[[find in source code]](../../../psdtoolsx/api/shape.py#L139)

```python
class Stroke(object):
    def __init__(data):
```

Stroke contains decorative infromation for strokes.

This is a thin wrapper around
:pyclass `psdtoolsx.psd.descriptor.Descriptor` structure.
Check `_data` attribute to get the raw data.

### Stroke().blend_mode

[[find in source code]](../../../psdtoolsx/api/shape.py#L235)

```python
@property
def blend_mode():
```

Blend mode.

### Stroke().content

[[find in source code]](../../../psdtoolsx/api/shape.py#L245)

```python
@property
def content():
```

Fill effect.

### Stroke().enabled

[[find in source code]](../../../psdtoolsx/api/shape.py#L169)

```python
@property
def enabled():
```

If the stroke is enabled.

### Stroke().fill_enabled

[[find in source code]](../../../psdtoolsx/api/shape.py#L174)

```python
@property
def fill_enabled():
```

If the stroke fill is enabled.

### Stroke().line_alignment

[[find in source code]](../../../psdtoolsx/api/shape.py#L220)

```python
@property
def line_alignment():
```

Alignment, one of `inner`, `outer`, `center`.

### Stroke().line_cap_type

[[find in source code]](../../../psdtoolsx/api/shape.py#L208)

```python
@property
def line_cap_type():
```

Cap type, one of `butt`, `round`, `square`.

### Stroke().line_dash_offset

[[find in source code]](../../../psdtoolsx/api/shape.py#L194)

```python
@property
def line_dash_offset():
```

Line dash offset in float.

#### Returns

float

### Stroke().line_dash_set

[[find in source code]](../../../psdtoolsx/api/shape.py#L184)

```python
@property
def line_dash_set():
```

Line dash set in list of
:pyclass `psdtoolsx.decoder.actions.UnitFloat`.

#### Returns

list

### Stroke().line_join_type

[[find in source code]](../../../psdtoolsx/api/shape.py#L214)

```python
@property
def line_join_type():
```

Join type, one of `miter`, `round`, `bevel`.

### Stroke().line_width

[[find in source code]](../../../psdtoolsx/api/shape.py#L179)

```python
@property
def line_width():
```

Stroke width in float.

### Stroke().miter_limit

[[find in source code]](../../../psdtoolsx/api/shape.py#L203)

```python
@property
def miter_limit():
```

Miter limit in float.

### Stroke().opacity

[[find in source code]](../../../psdtoolsx/api/shape.py#L240)

```python
@property
def opacity():
```

Opacity value.

### Stroke().scale_lock

[[find in source code]](../../../psdtoolsx/api/shape.py#L226)

```python
@property
def scale_lock():
```

### Stroke().stroke_adjust

[[find in source code]](../../../psdtoolsx/api/shape.py#L230)

```python
@property
def stroke_adjust():
```

Stroke adjust

## VectorMask

[[find in source code]](../../../psdtoolsx/api/shape.py#L18)

```python
class VectorMask(object):
    def __init__(data):
```

Vector mask data.

Vector mask is a resolution-independent mask that consists of one or more
Path objects. In Photoshop, all the path objects are represented as
Bezier curves. Check :pyattribute `~psdtoolsx.api.shape.VectorMask.paths`
property for how to deal with path objects.

### VectorMask().bbox

[[find in source code]](../../../psdtoolsx/api/shape.py#L110)

```python
@property
def bbox():
```

Bounding box tuple (left, top, right, bottom) in relative coordinates,
where top-left corner is (0., 0.) and bottom-right corner is (1., 1.).

#### Returns

`tuple`

### VectorMask().clipboard_record

[[find in source code]](../../../psdtoolsx/api/shape.py#L101)

```python
@property
def clipboard_record():
```

Clipboard record containing bounding box information.

Depending on the Photoshop version, this field can be `None`.

### VectorMask().disabled

[[find in source code]](../../../psdtoolsx/api/shape.py#L54)

```python
@property
def disabled():
```

If the mask is disabled.

### VectorMask().initial_fill_rule

[[find in source code]](../../../psdtoolsx/api/shape.py#L85)

```python
@property
def initial_fill_rule():
```

Initial fill rule.

When 0, fill inside of the path. When 1, fill outside of the shape.

#### Returns

`int`

### VectorMask().initial_fill_rule

[[find in source code]](../../../psdtoolsx/api/shape.py#L96)

```python
@initial_fill_rule.setter
def initial_fill_rule(value):
```

### VectorMask().inverted

[[find in source code]](../../../psdtoolsx/api/shape.py#L44)

```python
@property
def inverted():
```

Invert the mask.

### VectorMask().not_linked

[[find in source code]](../../../psdtoolsx/api/shape.py#L49)

```python
@property
def not_linked():
```

If the knots are not linked.

### VectorMask().paths

[[find in source code]](../../../psdtoolsx/api/shape.py#L59)

```python
@property
def paths():
```

List of :pyclass `psdtoolsx.psd.vector.Subpath`. Subpath is a
list-like structure that contains one or more
:pyclass `psdtoolsx.psd.vector.Knot` items. Knot contains
relative coordinates of control points for a Bezier curve.
:pyattribute `~psdtoolsx.psd.vector.Subpath.index` indicates which
origination item the subpath belongs, and
:pyclass `psdtoolsx.psd.vector.Subpath.operation` indicates how
to combine multiple shape paths.

In PSD, path fill rule is even-odd.

Example

```python
for subpath in layer.vector_mask.paths:
    anchors = [(
        int(knot.anchor[1] * psd.width),
        int(knot.anchor[0] * psd.height),
    ) for knot in subpath]
```

#### Returns

List of Subpath.
