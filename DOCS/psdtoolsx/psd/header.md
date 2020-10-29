# header

> Auto-generated documentation for [psdtoolsx.psd.header](../../../psdtoolsx/psd/header.py) module.

File header structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / header
    - [FileHeader](#fileheader)
        - [FileHeader.read](#fileheaderread)
        - [FileHeader().write](#fileheaderwrite)

## FileHeader

[[find in source code]](../../../psdtoolsx/psd/header.py#L16)

```python
attr.s(repr=True, slots=True)
class FileHeader(BaseElement):
```

Header section of the PSD file.

Example

```python
from psdtoolsx.psd.header import FileHeader
from psdtoolsx.constants import ColorMode

header = FileHeader(channels=2, height=359, width=400, depth=8,
                    color_mode=ColorMode.GRAYSCALE)
```

signature

Signature: always equal to ``b'8BPS'``.

version

Version number. PSD is 1, and PSB is 2.

channels

The number of channels in the image, including any user-defined alpha
channel.

height

The height of the image in pixels.

width

The width of the image in pixels.

depth

The number of bits per channel.

color_mode

The color mode of the file. See
:pyclass `psdtoolsx.constants.ColorMode`

#### See also

- [BaseElement](base.md#baseelement)

### FileHeader.read

[[find in source code]](../../../psdtoolsx/psd/header.py#L75)

```python
@classmethod
def read(fp):
```

### FileHeader().write

[[find in source code]](../../../psdtoolsx/psd/header.py#L79)

```python
def write(fp):
```
