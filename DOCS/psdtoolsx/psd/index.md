# psd

> Auto-generated documentation for [psdtoolsx.psd](../../../psdtoolsx/psd/__init__.py) module.

Low-level API that translates binary data to Python structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / psd
    - [PSD](#psd)
        - [PSD.read](#psdread)
        - [PSD().write](#psdwrite)
    - Modules
        - [adjustments](adjustments.md#adjustments)
        - [base](base.md#base)
        - [color](color.md#color)
        - [color_mode_data](color_mode_data.md#color_mode_data)
        - [descriptor](descriptor.md#descriptor)
        - [effects_layer](effects_layer.md#effects_layer)
        - [engine_data](engine_data.md#engine_data)
        - [filter_effects](filter_effects.md#filter_effects)
        - [header](header.md#header)
        - [image_data](image_data.md#image_data)
        - [image_resources](image_resources.md#image_resources)
        - [layer_and_mask](layer_and_mask.md#layer_and_mask)
        - [linked_layer](linked_layer.md#linked_layer)
        - [patterns](patterns.md#patterns)
        - [tagged_blocks](tagged_blocks.md#tagged_blocks)
        - [vector](vector.md#vector)

All the data structure in this subpackage inherits from one of the object
defined in :py:mod:`psdtoolsx.psd.base` module.

## PSD

[[find in source code]](../../../psdtoolsx/psd/__init__.py#L21)

```python
attr.s(repr=False, slots=True)
class PSD(BaseElement):
```

Low-level PSD file structure that resembles the specification_.

.. _specification: https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/

Example

```python
from psdtoolsx.psd import PSD

with open(input_file, 'rb') as f:
    psd = PSD.read(f)

with open(output_file, 'wb') as f:
    psd.write(f)
```

header

See :pyclass `.FileHeader`.

color_mode_data

See :pyclass `.ColorModeData`.

image_resources

See :pyclass `.ImageResources`.

layer_and_mask_information

See :pyclass `.LayerAndMaskInformation`.

image_data

See :pyclass `.ImageData`.

### PSD.read

[[find in source code]](../../../psdtoolsx/psd/__init__.py#L64)

```python
@classmethod
def read(fp, encoding='macroman', **kwargs):
```

### PSD().write

[[find in source code]](../../../psdtoolsx/psd/__init__.py#L76)

```python
def write(fp, encoding='macroman', **kwargs):
```
