# compression

> Auto-generated documentation for [psdtoolsx.compression](../../../psdtoolsx/compression/__init__.py) module.

Image compression utils.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / compression
    - [compress](#compress)
    - [decode_prediction](#decode_prediction)
    - [decode_rle](#decode_rle)
    - [decompress](#decompress)
    - [encode_prediction](#encode_prediction)
    - [encode_rle](#encode_rle)
    - Modules
        - [rle](rle.md#rle)

## compress

[[find in source code]](../../../psdtoolsx/compression/__init__.py#L18)

```python
def compress(data, compression, width, height, depth, version=1):
```

Compress raw data.

#### Arguments

- `data` - raw data bytes to write.
- `compression` - compression type, see :pyclass `.Compression`.
- `width` - width.
- `height` - height.
- `depth` - bit depth of the pixel.
- `version` - psd file version.

#### Returns

compressed data bytes.

## decode_prediction

[[find in source code]](../../../psdtoolsx/compression/__init__.py#L117)

```python
def decode_prediction(data, w, h, depth):
```

## decode_rle

[[find in source code]](../../../psdtoolsx/compression/__init__.py#L90)

```python
def decode_rle(data, width, height, depth, version):
```

## decompress

[[find in source code]](../../../psdtoolsx/compression/__init__.py#L42)

```python
def decompress(data, compression, width, height, depth, version=1):
```

Decompress raw data.

#### Arguments

- `data` - compressed data bytes.
- `compression` - compression type,
        see :pyclass `psdtoolsx.constants.Compression`.
- `width` - width.
- `height` - height.
- `depth` - bit depth of the pixel.
- `version` - psd file version.

#### Returns

decompressed data bytes.

## encode_prediction

[[find in source code]](../../../psdtoolsx/compression/__init__.py#L99)

```python
def encode_prediction(data, w, h, depth):
```

## encode_rle

[[find in source code]](../../../psdtoolsx/compression/__init__.py#L75)

```python
def encode_rle(data, width, height, depth, version):
```
