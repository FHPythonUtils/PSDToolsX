# linked_layer

> Auto-generated documentation for [psdtoolsx.psd.linked_layer](../../../psdtoolsx/psd/linked_layer.py) module.

Linked layer structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / linked_layer
    - [LinkedLayer](#linkedlayer)
        - [LinkedLayer.read](#linkedlayerread)
        - [LinkedLayer().write](#linkedlayerwrite)
    - [LinkedLayers](#linkedlayers)
        - [LinkedLayers.read](#linkedlayersread)
        - [LinkedLayers().write](#linkedlayerswrite)

## LinkedLayer

[[find in source code]](../../../psdtoolsx/psd/linked_layer.py#L46)

```python
attr.s(repr=False, slots=True)
class LinkedLayer(BaseElement):
```

LinkedLayer structure.

kind
version
uuid
filename
filetype
creator
filesize
open_file
linked_file
timestamp
data
child_id
mod_time
lock_state

#### See also

- [BaseElement](base.md#baseelement)

### LinkedLayer.read

[[find in source code]](../../../psdtoolsx/psd/linked_layer.py#L82)

```python
@classmethod
def read(fp, **kwargs):
```

### LinkedLayer().write

[[find in source code]](../../../psdtoolsx/psd/linked_layer.py#L132)

```python
def write(fp, padding=1, **kwargs):
```

## LinkedLayers

[[find in source code]](../../../psdtoolsx/psd/linked_layer.py#L22)

```python
class LinkedLayers(ListElement):
```

List of LinkedLayer structure. See :pyclass `.LinkedLayer`.

#### See also

- [ListElement](base.md#listelement)

### LinkedLayers.read

[[find in source code]](../../../psdtoolsx/psd/linked_layer.py#L27)

```python
@classmethod
def read(fp, **kwargs):
```

### LinkedLayers().write

[[find in source code]](../../../psdtoolsx/psd/linked_layer.py#L36)

```python
def write(fp, **kwargs):
```
