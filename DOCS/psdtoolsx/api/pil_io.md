# pil_io

> Auto-generated documentation for [psdtoolsx.api.pil_io](../../../psdtoolsx/api/pil_io.py) module.

PIL IO module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / pil_io
    - [convert_image_data_to_pil](#convert_image_data_to_pil)
    - [convert_layer_to_pil](#convert_layer_to_pil)
    - [convert_pattern_to_pil](#convert_pattern_to_pil)
    - [convert_thumbnail_to_pil](#convert_thumbnail_to_pil)
    - [get_color_mode](#get_color_mode)
    - [get_pil_channels](#get_pil_channels)
    - [get_pil_mode](#get_pil_mode)

## convert_image_data_to_pil

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L52)

```python
def convert_image_data_to_pil(psd, channel, apply_icc):
```

Convert ImageData to PIL Image.

## convert_layer_to_pil

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L98)

```python
def convert_layer_to_pil(layer, channel, apply_icc):
```

Convert Layer to PIL Image.

## convert_pattern_to_pil

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L132)

```python
def convert_pattern_to_pil(pattern):
```

Convert Pattern to PIL Image.

## convert_thumbnail_to_pil

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L155)

```python
def convert_thumbnail_to_pil(thumbnail, mode='RGB'):
```

Convert thumbnail resource.

## get_color_mode

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L14)

```python
def get_color_mode(mode):
```

Convert PIL mode to ColorMode.

## get_pil_channels

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L36)

```python
def get_pil_channels(pil_mode):
```

Get the number of channels for PIL modes.

## get_pil_mode

[[find in source code]](../../../psdtoolsx/api/pil_io.py#L22)

```python
def get_pil_mode(color_mode, alpha=False):
```

Get PIL mode from ColorMode.
