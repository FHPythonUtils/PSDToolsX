# color_mode_data

> Auto-generated documentation for [psdtoolsx.psd.color_mode_data](../../../psdtoolsx/psd/color_mode_data.py) module.

Color mode data structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / color_mode_data
    - [ColorModeData](#colormodedata)
        - [ColorModeData().interleave](#colormodedatainterleave)
        - [ColorModeData.read](#colormodedataread)
        - [ColorModeData().write](#colormodedatawrite)

## ColorModeData

[[find in source code]](../../../psdtoolsx/psd/color_mode_data.py#L17)

```python
attr.s(repr=False, slots=True)
class ColorModeData(ValueElement):
```

Color mode data section of the PSD file.

For indexed color images the data is the color table for the image in a
non-interleaved order.

Duotone images also have this data, but the data format is undocumented.

#### See also

- [ValueElement](base.md#valueelement)

### ColorModeData().interleave

[[find in source code]](../../../psdtoolsx/psd/color_mode_data.py#L42)

```python
def interleave():
```

Returns interleaved color table in bytes.

### ColorModeData.read

[[find in source code]](../../../psdtoolsx/psd/color_mode_data.py#L28)

```python
@classmethod
def read(fp):
```

### ColorModeData().write

[[find in source code]](../../../psdtoolsx/psd/color_mode_data.py#L35)

```python
def write(fp):
```
