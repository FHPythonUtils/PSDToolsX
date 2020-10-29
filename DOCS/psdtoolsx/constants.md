# constants

> Auto-generated documentation for [psdtoolsx.constants](../../psdtoolsx/constants.py) module.

Various constants for psdtoolsx

- [Psdtoolsx](../README.md#psdtoolsx-index) / [Modules](../README.md#psdtoolsx-modules) / [psdtoolsx](index.md#psdtoolsx) / constants
    - [BlendMode](#blendmode)
    - [ChannelID](#channelid)
    - [Clipping](#clipping)
    - [ColorMode](#colormode)
        - [ColorMode.channels](#colormodechannels)
    - [ColorSpaceID](#colorspaceid)
    - [Compression](#compression)
    - [EffectOSType](#effectostype)
    - [GlobalLayerMaskKind](#globallayermaskkind)
    - [LinkedLayerType](#linkedlayertype)
    - [OSType](#ostype)
    - [PathResourceID](#pathresourceid)
    - [PlacedLayerType](#placedlayertype)
    - [PrintScaleStyle](#printscalestyle)
    - [Resource](#resource)
        - [Resource.is_path_info](#resourceis_path_info)
        - [Resource.is_plugin_resource](#resourceis_plugin_resource)
    - [SectionDivider](#sectiondivider)
    - [SheetColorType](#sheetcolortype)
    - [Tag](#tag)

## BlendMode

[[find in source code]](../../psdtoolsx/constants.py#L233)

```python
class BlendMode(bytes, Enum):
```

Blend modes.

## ChannelID

[[find in source code]](../../psdtoolsx/constants.py#L208)

```python
class ChannelID(IntEnum):
```

Channel types.

## Clipping

[[find in source code]](../../psdtoolsx/constants.py#L227)

```python
class Clipping(IntEnum):
```

Clipping.

## ColorMode

[[find in source code]](../../psdtoolsx/constants.py#L7)

```python
class ColorMode(IntEnum):
```

Color mode.

### ColorMode.channels

[[find in source code]](../../psdtoolsx/constants.py#L20)

```python
@staticmethod
def channels(value, alpha=False):
```

## ColorSpaceID

[[find in source code]](../../psdtoolsx/constants.py#L34)

```python
class ColorSpaceID(IntEnum):
```

Color space types.

## Compression

[[find in source code]](../../psdtoolsx/constants.py#L275)

```python
class Compression(IntEnum):
```

Compression modes.

Compression. 0 = Raw Data, 1 = RLE compressed, 2 = ZIP without prediction,
3 = ZIP with prediction.

## EffectOSType

[[find in source code]](../../psdtoolsx/constants.py#L429)

```python
class EffectOSType(bytes, Enum):
```

OS Type keys for Layer Effects.

## GlobalLayerMaskKind

[[find in source code]](../../psdtoolsx/constants.py#L267)

```python
class GlobalLayerMaskKind(IntEnum):
```

Global layer mask kind.

## LinkedLayerType

[[find in source code]](../../psdtoolsx/constants.py#L199)

```python
class LinkedLayerType(bytes, Enum):
```

Linked layer types.

## OSType

[[find in source code]](../../psdtoolsx/constants.py#L394)

```python
class OSType(bytes, Enum):
```

Descriptor OSTypes and reference OSTypes.

#### Attributes

- `REFERENCE` - OS types: `b'obj '`
- `PROPERTY` - Reference OS types: `b'prop'`

## PathResourceID

[[find in source code]](../../psdtoolsx/constants.py#L442)

```python
class PathResourceID(IntEnum):
```

## PlacedLayerType

[[find in source code]](../../psdtoolsx/constants.py#L454)

```python
class PlacedLayerType(IntEnum):
```

## PrintScaleStyle

[[find in source code]](../../psdtoolsx/constants.py#L387)

```python
class PrintScaleStyle(IntEnum):
```

Print scale style.

## Resource

[[find in source code]](../../psdtoolsx/constants.py#L45)

```python
class Resource(IntEnum):
```

Image resource keys.

Note the following is not defined for performance reasons.

* PATH_INFO_10 to PATH_INFO_989 corresponding to 2010 - 2989
* PLUGIN_RESOURCES_10 to PLUGIN_RESOURCES_989 corresponding to
   4010 - 4989

#### Attributes

- `PATH_INFO_990` - PATH_INFO 2010-2989 is not defined for performance reasons.: `2990`
- `PLUGIN_RESOURCE_4990` - PLUGIN_RESOURCE 4010-4989 is not defined for performance reasons.: `4990`

### Resource.is_path_info

[[find in source code]](../../psdtoolsx/constants.py#L187)

```python
@staticmethod
def is_path_info(value):
```

### Resource.is_plugin_resource

[[find in source code]](../../psdtoolsx/constants.py#L191)

```python
@staticmethod
def is_plugin_resource(value):
```

## SectionDivider

[[find in source code]](../../psdtoolsx/constants.py#L461)

```python
class SectionDivider(IntEnum):
```

## SheetColorType

[[find in source code]](../../psdtoolsx/constants.py#L468)

```python
class SheetColorType(IntEnum):
```

## Tag

[[find in source code]](../../psdtoolsx/constants.py#L288)

```python
class Tag(bytes, Enum):
```

Tagged blocks keys.

#### Attributes

- `PATT` - Unknown: `b'patt'`
