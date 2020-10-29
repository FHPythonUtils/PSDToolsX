# composite

> Auto-generated documentation for [psdtoolsx.composite](../../../psdtoolsx/composite/__init__.py) module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / composite
    - [Compositor](#compositor)
        - [Compositor().alpha](#compositoralpha)
        - [Compositor().apply](#compositorapply)
        - [Compositor().color](#compositorcolor)
        - [Compositor().finish](#compositorfinish)
        - [Compositor().height](#compositorheight)
        - [Compositor().shape](#compositorshape)
        - [Compositor().viewport](#compositorviewport)
        - [Compositor().width](#compositorwidth)
    - [composite](#composite)
    - [composite_pil](#composite_pil)
    - [has_fill](#has_fill)
    - [paste](#paste)
    - Modules
        - [blend](blend.md#blend)
        - [effects](effects.md#effects)
        - [vector](vector.md#vector)

## Compositor

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L130)

```python
class Compositor(object):
    def __init__(
        viewport,
        color=1.0,
        alpha=0.0,
        isolated=False,
        layer_filter=None,
        force=False,
    ):
```

Composite context.

Example

```python
compositor = Compositor(group.bbox)
for layer in group:
    compositor.apply(layer)
color, shape, alpha = compositor.finish()
```

### Compositor().alpha

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L273)

```python
@property
def alpha():
```

### Compositor().apply

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L179)

```python
def apply(layer):
```

### Compositor().color

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L262)

```python
@property
def color():
```

### Compositor().finish

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L247)

```python
def finish():
```

### Compositor().height

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L258)

```python
@property
def height():
```

### Compositor().shape

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L269)

```python
@property
def shape():
```

### Compositor().viewport

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L250)

```python
@property
def viewport():
```

### Compositor().width

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L254)

```python
@property
def width():
```

## composite

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L63)

```python
def composite(
    group,
    color=1.0,
    alpha=0.0,
    viewport=None,
    layer_filter=None,
    force=False,
    as_layer=False,
):
```

Composite the given group of layers.

## composite_pil

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L17)

```python
def composite_pil(
    layer,
    color,
    alpha,
    viewport,
    layer_filter,
    force,
    as_layer=False,
):
```

## has_fill

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L497)

```python
def has_fill(layer):
```

## paste

[[find in source code]](../../../psdtoolsx/composite/__init__.py#L107)

```python
def paste(viewport, bbox, values, background=None):
```

Change to the specified viewport.
