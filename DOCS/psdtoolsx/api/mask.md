# mask

> Auto-generated documentation for [psdtoolsx.api.mask](../../../psdtoolsx/api/mask.py) module.

Mask module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / mask
    - [Mask](#mask)
        - [Mask().background_color](#maskbackground_color)
        - [Mask().bbox](#maskbbox)
        - [Mask().bottom](#maskbottom)
        - [Mask().disabled](#maskdisabled)
        - [Mask().flags](#maskflags)
        - [Mask().height](#maskheight)
        - [Mask().left](#maskleft)
        - [Mask().parameters](#maskparameters)
        - [Mask().real_flags](#maskreal_flags)
        - [Mask().right](#maskright)
        - [Mask().size](#masksize)
        - [Mask().top](#masktop)
        - [Mask().topil](#masktopil)
        - [Mask().width](#maskwidth)

## Mask

[[find in source code]](../../../psdtoolsx/api/mask.py#L12)

```python
class Mask(object):
    def __init__(layer):
```

Mask data attached to a layer.

There are two distinct internal mask data: user mask and vector mask.
User mask refers any pixel-based mask whereas vector mask refers a mask
from a shape path. Internally, two masks are combined and referred
real mask.

### Mask().background_color

[[find in source code]](../../../psdtoolsx/api/mask.py#L25)

```python
@property
def background_color():
```

Background color.

### Mask().bbox

[[find in source code]](../../../psdtoolsx/api/mask.py#L32)

```python
@property
def bbox():
```

BBox

### Mask().bottom

[[find in source code]](../../../psdtoolsx/api/mask.py#L58)

```python
@property
def bottom():
```

Bottom coordinate.

### Mask().disabled

[[find in source code]](../../../psdtoolsx/api/mask.py#L80)

```python
@property
def disabled():
```

Disabled.

### Mask().flags

[[find in source code]](../../../psdtoolsx/api/mask.py#L85)

```python
@property
def flags():
```

Flags.

### Mask().height

[[find in source code]](../../../psdtoolsx/api/mask.py#L70)

```python
@property
def height():
```

Height.

### Mask().left

[[find in source code]](../../../psdtoolsx/api/mask.py#L37)

```python
@property
def left():
```

Left coordinate.

### Mask().parameters

[[find in source code]](../../../psdtoolsx/api/mask.py#L90)

```python
@property
def parameters():
```

Parameters.

### Mask().real_flags

[[find in source code]](../../../psdtoolsx/api/mask.py#L95)

```python
@property
def real_flags():
```

Real flag.

### Mask().right

[[find in source code]](../../../psdtoolsx/api/mask.py#L44)

```python
@property
def right():
```

Right coordinate.

### Mask().size

[[find in source code]](../../../psdtoolsx/api/mask.py#L75)

```python
@property
def size():
```

(Width, Height) tuple.

### Mask().top

[[find in source code]](../../../psdtoolsx/api/mask.py#L51)

```python
@property
def top():
```

Top coordinate.

### Mask().topil

[[find in source code]](../../../psdtoolsx/api/mask.py#L106)

```python
def topil(real=True, **kwargs):
```

Get PIL Image of the mask.

#### Arguments

- `real` - When True, returns pixel + vector mask combined.

#### Returns

PIL Image object, or None if the mask is empty.

### Mask().width

[[find in source code]](../../../psdtoolsx/api/mask.py#L65)

```python
@property
def width():
```

Width.
