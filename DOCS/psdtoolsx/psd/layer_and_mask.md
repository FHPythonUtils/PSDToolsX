# layer_and_mask

> Auto-generated documentation for [psdtoolsx.psd.layer_and_mask](../../../psdtoolsx/psd/layer_and_mask.py) module.

Layer and mask data structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / layer_and_mask
    - [ChannelData](#channeldata)
        - [ChannelData().get_data](#channeldataget_data)
        - [ChannelData.read](#channeldataread)
        - [ChannelData().set_data](#channeldataset_data)
        - [ChannelData().write](#channeldatawrite)
    - [ChannelDataList](#channeldatalist)
        - [ChannelDataList.read](#channeldatalistread)
    - [ChannelImageData](#channelimagedata)
        - [ChannelImageData.read](#channelimagedataread)
        - [ChannelImageData().write](#channelimagedatawrite)
    - [ChannelInfo](#channelinfo)
        - [ChannelInfo.read](#channelinforead)
        - [ChannelInfo().write](#channelinfowrite)
    - [GlobalLayerMaskInfo](#globallayermaskinfo)
        - [GlobalLayerMaskInfo.read](#globallayermaskinforead)
        - [GlobalLayerMaskInfo().write](#globallayermaskinfowrite)
    - [LayerAndMaskInformation](#layerandmaskinformation)
        - [LayerAndMaskInformation.read](#layerandmaskinformationread)
        - [LayerAndMaskInformation().write](#layerandmaskinformationwrite)
    - [LayerBlendingRanges](#layerblendingranges)
        - [LayerBlendingRanges.read](#layerblendingrangesread)
        - [LayerBlendingRanges().write](#layerblendingrangeswrite)
    - [LayerFlags](#layerflags)
        - [LayerFlags.read](#layerflagsread)
        - [LayerFlags().write](#layerflagswrite)
    - [LayerInfo](#layerinfo)
        - [LayerInfo.read](#layerinforead)
        - [LayerInfo().write](#layerinfowrite)
    - [LayerInfoBlock](#layerinfoblock)
        - [LayerInfoBlock.read](#layerinfoblockread)
        - [LayerInfoBlock().write](#layerinfoblockwrite)
    - [LayerRecord](#layerrecord)
        - [LayerRecord().channel_sizes](#layerrecordchannel_sizes)
        - [LayerRecord().height](#layerrecordheight)
        - [LayerRecord.read](#layerrecordread)
        - [LayerRecord().width](#layerrecordwidth)
        - [LayerRecord().write](#layerrecordwrite)
    - [LayerRecords](#layerrecords)
        - [LayerRecords.read](#layerrecordsread)
    - [MaskData](#maskdata)
        - [MaskData().height](#maskdataheight)
        - [MaskData.read](#maskdataread)
        - [MaskData().real_height](#maskdatareal_height)
        - [MaskData().real_width](#maskdatareal_width)
        - [MaskData().width](#maskdatawidth)
        - [MaskData().write](#maskdatawrite)
    - [MaskFlags](#maskflags)
        - [MaskFlags.read](#maskflagsread)
        - [MaskFlags().write](#maskflagswrite)
    - [MaskParameters](#maskparameters)
        - [MaskParameters.read](#maskparametersread)
        - [MaskParameters().write](#maskparameterswrite)

## ChannelData

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L836)

```python
attr.s(repr=False, slots=True)
class ChannelData(BaseElement):
```

Channel data.

compression

Compression type. See :pyclass `psdtoolsx.constants.Compression`.

data

Data.

#### See also

- [BaseElement](base.md#baseelement)

### ChannelData().get_data

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L867)

```python
def get_data(width, height, depth, version=1):
```

Get decompressed channel data.

#### Arguments

- `width` - width.
- `height` - height.
- `depth` - bit depth of the pixel.
- `version` - psd file version.

#### Returns

Type: *bytes*

### ChannelData.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L855)

```python
@classmethod
def read(fp, length=0, **kwargs):
```

### ChannelData().set_data

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L880)

```python
def set_data(data, width, height, depth, version=1):
```

Set raw channel data and compress to store.

#### Arguments

- `data` - raw data bytes to write.
- `compression` - compression type,
    see :pyclass `psdtoolsx.constants.Compression`.
- `width` - width.
- `height` - height.
- `depth` - bit depth of the pixel.
- `version` - psd file version.

### ChannelData().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L861)

```python
def write(fp, **kwargs):
```

## ChannelDataList

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L815)

```python
class ChannelDataList(ListElement):
```

List of channel image data, corresponding to each color or alpha.

See :pyclass `.ChannelData`.

#### See also

- [ListElement](base.md#listelement)

### ChannelDataList.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L822)

```python
@classmethod
def read(fp, channel_info, **kwargs):
```

## ChannelImageData

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L778)

```python
class ChannelImageData(ListElement):
```

List of channel data list.

This size of this list corresponds to the size of
:py:class:[LayerRecords](#layerrecords). Each item corresponds to the channels of each
layer.

See :pyclass `.ChannelDataList`.

#### See also

- [ListElement](base.md#listelement)

### ChannelImageData.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L789)

```python
@classmethod
def read(fp, layer_records=None):
```

### ChannelImageData().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L800)

```python
def write(fp, **kwargs):
```

## ChannelInfo

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L196)

```python
attr.s(repr=False, slots=True)
class ChannelInfo(BaseElement):
```

Channel information.

id

Channel ID: 0 = red, 1 = green, etc.; -1 = transparency mask; -2 =
user supplied layer mask, -3 real user supplied layer mask (when both
a user mask and a vector mask are present). See
:pyclass `psdtoolsx.constants.ChannelID`.

length

Length of the corresponding channel data.

#### See also

- [BaseElement](base.md#baseelement)

### ChannelInfo.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L218)

```python
@classmethod
def read(fp, version=1):
```

### ChannelInfo().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L222)

```python
def write(fp, version=1):
```

## GlobalLayerMaskInfo

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L904)

```python
attr.s(repr=False, slots=True)
class GlobalLayerMaskInfo(BaseElement):
```

Global mask information.

overlay_color

Overlay color space (undocumented) and color components.

opacity

Opacity. 0 = transparent, 100 = opaque.

kind

Kind.
0 = Color selected--i.e. inverted;
1 = Color protected;
128 = use value stored per layer. This value is preferred. The others
are for backward compatibility with beta versions.

#### See also

- [BaseElement](base.md#baseelement)

### GlobalLayerMaskInfo.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L932)

```python
@classmethod
def read(fp):
```

### GlobalLayerMaskInfo().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L956)

```python
def write(fp):
```

## LayerAndMaskInformation

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L26)

```python
attr.s(repr=False, slots=True)
class LayerAndMaskInformation(BaseElement):
```

Layer and mask information section.

layer_info

See :pyclass `.LayerInfo`.

global_layer_mask_info

See :pyclass `.GlobalLayerMaskInfo`.

tagged_blocks

See :pyclass `.TaggedBlocks`.

#### See also

- [BaseElement](base.md#baseelement)

### LayerAndMaskInformation.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L46)

```python
@classmethod
def read(fp, encoding='macroman', version=1):
```

### LayerAndMaskInformation().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L80)

```python
def write(fp, encoding='macroman', version=1, padding=4):
```

## LayerBlendingRanges

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L270)

```python
attr.s(repr=False, slots=True)
class LayerBlendingRanges(BaseElement):
```

Layer blending ranges.

All ranges contain 2 black values followed by 2 white values.

composite_ranges

List of composite gray blend source and destination ranges.

channel_ranges

List of channel source and destination ranges.

#### See also

- [BaseElement](base.md#baseelement)

### LayerBlendingRanges.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L294)

```python
@classmethod
def read(fp):
```

### LayerBlendingRanges().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L315)

```python
def write(fp):
```

## LayerFlags

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L227)

```python
attr.s(repr=False, slots=True)
class LayerFlags(BaseElement):
```

Layer flags.

Note there are undocumented flags. Maybe photoshop version.

transparency_protected
visible
pixel_data_irrelevant

#### See also

- [BaseElement](base.md#baseelement)

### LayerFlags.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L246)

```python
@classmethod
def read(fp):
```

### LayerFlags().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L260)

```python
def write(fp):
```

## LayerInfo

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L101)

```python
attr.s(repr=False, slots=True)
class LayerInfo(BaseElement):
```

High-level organization of the layer information.

layer_count

Layer count. If it is a negative number, its absolute value is the
number of layers and the first alpha channel contains the transparency
data for the merged result.

layer_records

Information about each layer. See :pyclass `.LayerRecords`.

channel_image_data

Channel image data. See :pyclass `.ChannelImageData`.

#### See also

- [BaseElement](base.md#baseelement)

### LayerInfo.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L123)

```python
@classmethod
def read(fp, encoding='macroman', version=1):
```

### LayerInfo().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L145)

```python
def write(fp, encoding='macroman', version=1, padding=4):
```

## LayerInfoBlock

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L183)

```python
register(Tag.LAYER_16)
register(Tag.LAYER_32)
attr.s(repr=False)
class LayerInfoBlock(LayerInfo):
```

#### See also

- [LayerInfo](#layerinfo)

### LayerInfoBlock.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L187)

```python
@classmethod
def read(fp, encoding='macroman', version=1, **kwargs):
```

### LayerInfoBlock().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L191)

```python
def write(fp, encoding='macroman', version=1, padding=4, **kwargs):
```

## LayerRecord

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L344)

```python
attr.s(repr=False, slots=True)
class LayerRecord(BaseElement):
```

Layer record.

top

Top position.

left

Left position.

bottom

Bottom position.

right

Right position.

channel_info

List of :pyclass `.ChannelInfo`.

signature

Blend mode signature ``b'8BIM'``.

blend_mode

Blend mode key. See :pyclass `psdtoolsx.constants.BlendMode`.

opacity

Opacity, 0 = transparent, 255 = opaque.

clipping

Clipping, 0 = base, 1 = non-base. See
:pyclass `psdtoolsx.constants.Clipping`.

flags

See :pyclass `.LayerFlags`.

mask_data

:pyclass `.MaskData` or None.

blending_ranges

See :pyclass `psdtoolsx.constants.LayerBlendingRanges`.

name

Layer name.

tagged_blocks

See :pyclass `.TaggedBlocks`.

#### See also

- [BaseElement](base.md#baseelement)

### LayerRecord().channel_sizes

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L507)

```python
@property
def channel_sizes():
```

List of channel sizes: [(width, height)].

### LayerRecord().height

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L502)

```python
@property
def height():
```

Height of the layer.

### LayerRecord.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L428)

```python
@classmethod
def read(fp, encoding='macroman', version=1):
```

### LayerRecord().width

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L497)

```python
@property
def width():
```

Width of the layer.

### LayerRecord().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L461)

```python
def write(fp, encoding='macroman', version=1):
```

## LayerRecords

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L330)

```python
class LayerRecords(ListElement):
```

List of layer records. See :pyclass `.LayerRecord`.

#### See also

- [ListElement](base.md#listelement)

### LayerRecords.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L335)

```python
@classmethod
def read(fp, layer_count, encoding='macroman', version=1):
```

## MaskData

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L576)

```python
attr.s(repr=False, slots=True)
class MaskData(BaseElement):
```

Mask data.

Real user mask is a final composite mask of vector and pixel masks.

top

Top position.

left

Left position.

bottom

Bottom position.

right

Right position.

background_color

Default color. 0 or 255.

flags

See :pyclass `.MaskFlags`.

parameters

:pyclass `.MaskParameters` or None.

real_flags

Real user mask flags. See :pyclass `.MaskFlags`.

real_background_color

Real user mask background. 0 or 255.

real_top

Top position of real user mask.

real_left

Left position of real user mask.

real_bottom

Bottom position of real user mask.

real_right

Right position of real user mask.

#### See also

- [BaseElement](base.md#baseelement)

### MaskData().height

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L718)

```python
@property
def height():
```

Height of the mask.

### MaskData.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L648)

```python
@classmethod
def read(fp):
```

### MaskData().real_height

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L728)

```python
@property
def real_height():
```

Height of real user mask.

### MaskData().real_width

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L723)

```python
@property
def real_width():
```

Width of real user mask.

### MaskData().width

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L713)

```python
@property
def width():
```

Width of the mask.

### MaskData().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L686)

```python
def write(fp):
```

## MaskFlags

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L525)

```python
attr.s(repr=False, slots=True)
class MaskFlags(BaseElement):
```

Mask flags.

pos_relative_to_layer

Position relative to layer.

mask_disabled

Layer mask disabled.

invert_mask

Invert layer mask when blending (Obsolete).

user_mask_from_render

The user mask actually came from rendering other data.

parameters_applied

The user and/or vector masks have parameters applied to them.

#### See also

- [BaseElement](base.md#baseelement)

### MaskFlags.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L558)

```python
@classmethod
def read(fp):
```

### MaskFlags().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L567)

```python
def write(fp):
```

## MaskParameters

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L735)

```python
attr.s(repr=False, slots=True)
class MaskParameters(BaseElement):
```

Mask parameters.

user_mask_density
user_mask_feather
vector_mask_density
vector_mask_feather

#### See also

- [BaseElement](base.md#baseelement)

### MaskParameters.read

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L749)

```python
@classmethod
def read(fp):
```

### MaskParameters().write

[[find in source code]](../../../psdtoolsx/psd/layer_and_mask.py#L759)

```python
def write(fp):
```
