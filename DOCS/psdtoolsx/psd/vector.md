# vector

> Auto-generated documentation for [psdtoolsx.psd.vector](../../../psdtoolsx/psd/vector.py) module.

Vector mask, path, and stroke structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / vector
    - [ClipboardRecord](#clipboardrecord)
        - [ClipboardRecord.read](#clipboardrecordread)
        - [ClipboardRecord().write](#clipboardrecordwrite)
    - [ClosedKnotLinked](#closedknotlinked)
    - [ClosedKnotUnlinked](#closedknotunlinked)
    - [ClosedPath](#closedpath)
        - [ClosedPath().is_closed](#closedpathis_closed)
    - [InitialFillRule](#initialfillrule)
        - [InitialFillRule.read](#initialfillruleread)
        - [InitialFillRule().write](#initialfillrulewrite)
    - [Knot](#knot)
        - [Knot.read](#knotread)
        - [Knot().write](#knotwrite)
    - [OpenKnotLinked](#openknotlinked)
    - [OpenKnotUnlinked](#openknotunlinked)
    - [OpenPath](#openpath)
        - [OpenPath().is_closed](#openpathis_closed)
    - [Path](#path)
        - [Path.read](#pathread)
        - [Path().write](#pathwrite)
    - [PathFillRule](#pathfillrule)
        - [PathFillRule.read](#pathfillruleread)
        - [PathFillRule().write](#pathfillrulewrite)
    - [Subpath](#subpath)
        - [Subpath().is_closed](#subpathis_closed)
        - [Subpath.read](#subpathread)
        - [Subpath().write](#subpathwrite)
    - [VectorMaskSetting](#vectormasksetting)
        - [VectorMaskSetting().disable](#vectormasksettingdisable)
        - [VectorMaskSetting().invert](#vectormasksettinginvert)
        - [VectorMaskSetting().not_link](#vectormasksettingnot_link)
        - [VectorMaskSetting.read](#vectormasksettingread)
        - [VectorMaskSetting().write](#vectormasksettingwrite)
    - [VectorStrokeContentSetting](#vectorstrokecontentsetting)
        - [VectorStrokeContentSetting.read](#vectorstrokecontentsettingread)
        - [VectorStrokeContentSetting().write](#vectorstrokecontentsettingwrite)
    - [decode_fixed_point](#decode_fixed_point)
    - [encode_fixed_point](#encode_fixed_point)

## ClipboardRecord

[[find in source code]](../../../psdtoolsx/psd/vector.py#L206)

```python
register(PathResourceID.CLIPBOARD)
attr.s(repr=False, slots=True)
class ClipboardRecord(BaseElement):
```

Clipboard record.

top

Top position in `int`

left

Left position in `int`

bottom

Bottom position in `int`

right

Right position in `int`

resolution

Resolution in `int`

#### See also

- [BaseElement](base.md#baseelement)

### ClipboardRecord.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L236)

```python
@classmethod
def read(fp):
```

### ClipboardRecord().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L240)

```python
def write(fp):
```

## ClosedKnotLinked

[[find in source code]](../../../psdtoolsx/psd/vector.py#L169)

```python
register(PathResourceID.CLOSED_KNOT_LINKED)
class ClosedKnotLinked(Knot):
```

#### See also

- [Knot](#knot)

## ClosedKnotUnlinked

[[find in source code]](../../../psdtoolsx/psd/vector.py#L174)

```python
register(PathResourceID.CLOSED_KNOT_UNLINKED)
class ClosedKnotUnlinked(Knot):
```

#### See also

- [Knot](#knot)

## ClosedPath

[[find in source code]](../../../psdtoolsx/psd/vector.py#L157)

```python
register(PathResourceID.CLOSED_LENGTH)
class ClosedPath(Subpath):
```

#### See also

- [Subpath](#subpath)

### ClosedPath().is_closed

[[find in source code]](../../../psdtoolsx/psd/vector.py#L158)

```python
def is_closed():
```

## InitialFillRule

[[find in source code]](../../../psdtoolsx/psd/vector.py#L246)

```python
register(PathResourceID.INITIAL_FILL)
attr.s(repr=False, slots=True)
class InitialFillRule(ValueElement):
```

Initial fill rule record.

rule

A value of 1 means that the fill starts with all pixels. The value
will be either 0 or 1.

#### See also

- [ValueElement](base.md#valueelement)

### InitialFillRule.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L257)

```python
@classmethod
def read(fp):
```

### InitialFillRule().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L261)

```python
def write(fp):
```

## Knot

[[find in source code]](../../../psdtoolsx/psd/vector.py#L123)

```python
attr.s(repr=False, slots=True)
class Knot(BaseElement):
```

Knot element consisting of 3 control points for Bezier curves.

preceding

(y, x) tuple of preceding control point in relative coordinates.

anchor

(y, x) tuple of anchor point in relative coordinates.

leaving

(y, x) tuple of leaving control point in relative coordinates.

#### See also

- [BaseElement](base.md#baseelement)

### Knot.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L144)

```python
@classmethod
def read(fp):
```

### Knot().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L151)

```python
def write(fp):
```

## OpenKnotLinked

[[find in source code]](../../../psdtoolsx/psd/vector.py#L179)

```python
register(PathResourceID.OPEN_KNOT_LINKED)
class OpenKnotLinked(Knot):
```

#### See also

- [Knot](#knot)

## OpenKnotUnlinked

[[find in source code]](../../../psdtoolsx/psd/vector.py#L184)

```python
register(PathResourceID.OPEN_KNOT_UNLINKED)
class OpenKnotUnlinked(Knot):
```

#### See also

- [Knot](#knot)

## OpenPath

[[find in source code]](../../../psdtoolsx/psd/vector.py#L163)

```python
register(PathResourceID.OPEN_LENGTH)
class OpenPath(Subpath):
```

#### See also

- [Subpath](#subpath)

### OpenPath().is_closed

[[find in source code]](../../../psdtoolsx/psd/vector.py#L164)

```python
def is_closed():
```

## Path

[[find in source code]](../../../psdtoolsx/psd/vector.py#L29)

```python
attr.s(repr=False, slots=True)
class Path(ListElement):
```

List-like Path structure. Elements are either PathFillRule,
InitialFillRule, ClipboardRecord, ClosedPath, or OpenPath.

#### See also

- [ListElement](base.md#listelement)

### Path.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L35)

```python
@classmethod
def read(fp):
```

### Path().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L44)

```python
def write(fp, padding=4):
```

## PathFillRule

[[find in source code]](../../../psdtoolsx/psd/vector.py#L190)

```python
register(PathResourceID.PATH_FILL)
attr.s(repr=False, slots=True)
class PathFillRule(BaseElement):
```

Path fill rule record, empty.

#### See also

- [BaseElement](base.md#baseelement)

### PathFillRule.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L195)

```python
@classmethod
def read(fp):
```

### PathFillRule().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L200)

```python
def write(fp):
```

## Subpath

[[find in source code]](../../../psdtoolsx/psd/vector.py#L54)

```python
attr.s(repr=False, slots=True)
class Subpath(ListElement):
```

Subpath element. This is a list of Knot objects.

#### Notes

There are undocumented data associated with this structure.

operation

`int` value indicating how multiple subpath should be combined:

1: Or (union), 2: Not-Or, 3: And (intersect), 0: Xor (exclude)

The first path element is applied to the background surface.
Intersection does not have strokes.

index

`int` index that specifies corresponding origination object.

#### Attributes

- `operation` - Undocumented data that seem to contain path operation info.: `attr.ib(default=1, type=int)`

#### See also

- [ListElement](base.md#listelement)

### Subpath().is_closed

[[find in source code]](../../../psdtoolsx/psd/vector.py#L110)

```python
def is_closed():
```

Returns whether if the path is closed or not.

#### Returns

`bool`.

### Subpath.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L81)

```python
@classmethod
def read(fp):
```

### Subpath().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L100)

```python
def write(fp):
```

## VectorMaskSetting

[[find in source code]](../../../psdtoolsx/psd/vector.py#L266)

```python
attr.s(repr=False, slots=True)
class VectorMaskSetting(BaseElement):
```

VectorMaskSetting structure.

version
path

List of :pyclass `psdtoolsx.psd.vector.Subpath` objects.

#### See also

- [BaseElement](base.md#baseelement)

### VectorMaskSetting().disable

[[find in source code]](../../../psdtoolsx/psd/vector.py#L301)

```python
@property
def disable():
```

Flag to indicate that the vector mask is disabled.

### VectorMaskSetting().invert

[[find in source code]](../../../psdtoolsx/psd/vector.py#L291)

```python
@property
def invert():
```

Flag to indicate that the vector mask is inverted.

### VectorMaskSetting().not_link

[[find in source code]](../../../psdtoolsx/psd/vector.py#L296)

```python
@property
def not_link():
```

Flag to indicate that the vector mask is not linked.

### VectorMaskSetting.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L279)

```python
@classmethod
def read(fp, **kwargs):
```

### VectorMaskSetting().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L286)

```python
def write(fp, **kwargs):
```

## VectorStrokeContentSetting

[[find in source code]](../../../psdtoolsx/psd/vector.py#L308)

```python
attr.s(repr=False, slots=True)
class VectorStrokeContentSetting(Descriptor):
```

Dict-like Descriptor-based structure. See
:pyclass `psdtoolsx.psd.descriptor.Descriptor`.

key
version

#### See also

- [Descriptor](descriptor.md#descriptor)

### VectorStrokeContentSetting.read

[[find in source code]](../../../psdtoolsx/psd/vector.py#L319)

```python
@classmethod
def read(fp, **kwargs):
```

### VectorStrokeContentSetting().write

[[find in source code]](../../../psdtoolsx/psd/vector.py#L324)

```python
def write(fp, padding=4, **kwargs):
```

## decode_fixed_point

[[find in source code]](../../../psdtoolsx/psd/vector.py#L20)

```python
def decode_fixed_point(numbers):
```

## encode_fixed_point

[[find in source code]](../../../psdtoolsx/psd/vector.py#L24)

```python
def encode_fixed_point(numbers):
```
