# image_data

> Auto-generated documentation for [psdtoolsx.psd.image_data](../../../psdtoolsx/psd/image_data.py) module.

Image data section structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / image_data
    - [ImageData](#imagedata)
        - [ImageData().get_data](#imagedataget_data)
        - [ImageData.new](#imagedatanew)
        - [ImageData.read](#imagedataread)
        - [ImageData().set_data](#imagedataset_data)
        - [ImageData().write](#imagedatawrite)

:pyclass `ImageData` corresponds to the last section of the PSD/PSB file
where a composited image is stored. When the file does not contain layers,
this is the only place pixels are saved.

## ImageData

[[find in source code]](../../../psdtoolsx/psd/image_data.py#L23)

```python
attr.s(repr=False, slots=True)
class ImageData(BaseElement):
```

Merged channel image data.

compression

See :pyclass `psdtoolsx.constants.Compression`.

data

`bytes` as compressed in the `compression` flag.

#### See also

- [BaseElement](base.md#baseelement)

### ImageData().get_data

[[find in source code]](../../../psdtoolsx/psd/image_data.py#L57)

```python
def get_data(header, split=True):
```

Get decompressed data.

#### Arguments

- `header` - See :pyclass `psdtoolsx.psd.header.FileHeader`.

#### Returns

`list` of bytes corresponding each channel.

### ImageData.new

[[find in source code]](../../../psdtoolsx/psd/image_data.py#L90)

```python
@classmethod
def new(header, color=0, compression=Compression.RAW):
```

Create a new image data object.

#### Arguments

- `header` - FileHeader.
- `compression` - compression type.
- `color` - default color. int or iterable for channel length.

### ImageData.read

[[find in source code]](../../../psdtoolsx/psd/image_data.py#L42)

```python
@classmethod
def read(fp):
```

### ImageData().set_data

[[find in source code]](../../../psdtoolsx/psd/image_data.py#L74)

```python
def set_data(data, header):
```

Set raw data and compress.

#### Arguments

- `data` - list of raw data bytes corresponding channels.
- `compression` - compression type,
    see :pyclass `psdtoolsx.constants.Compression`.
- `header` - See :pyclass `psdtoolsx.psd.header.FileHeader`.

#### Returns

length of compressed data.

### ImageData().write

[[find in source code]](../../../psdtoolsx/psd/image_data.py#L50)

```python
def write(fp):
```
