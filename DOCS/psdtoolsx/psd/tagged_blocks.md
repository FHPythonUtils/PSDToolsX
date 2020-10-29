# tagged_blocks

> Auto-generated documentation for [psdtoolsx.psd.tagged_blocks](../../../psdtoolsx/psd/tagged_blocks.py) module.

Tagged block data structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / tagged_blocks
    - [Annotation](#annotation)
        - [Annotation.read](#annotationread)
        - [Annotation().write](#annotationwrite)
    - [Annotations](#annotations)
        - [Annotations.read](#annotationsread)
        - [Annotations().write](#annotationswrite)
    - [Bytes](#bytes)
        - [Bytes.read](#bytesread)
        - [Bytes().write](#byteswrite)
    - [ChannelBlendingRestrictionsSetting](#channelblendingrestrictionssetting)
        - [ChannelBlendingRestrictionsSetting.read](#channelblendingrestrictionssettingread)
        - [ChannelBlendingRestrictionsSetting().write](#channelblendingrestrictionssettingwrite)
    - [FilterMask](#filtermask)
        - [FilterMask.read](#filtermaskread)
        - [FilterMask().write](#filtermaskwrite)
    - [MetadataSetting](#metadatasetting)
        - [MetadataSetting.read](#metadatasettingread)
        - [MetadataSetting().write](#metadatasettingwrite)
    - [MetadataSettings](#metadatasettings)
        - [MetadataSettings.read](#metadatasettingsread)
        - [MetadataSettings().write](#metadatasettingswrite)
    - [PixelSourceData2](#pixelsourcedata2)
        - [PixelSourceData2.read](#pixelsourcedata2read)
        - [PixelSourceData2().write](#pixelsourcedata2write)
    - [PlacedLayerData](#placedlayerdata)
        - [PlacedLayerData.read](#placedlayerdataread)
        - [PlacedLayerData().write](#placedlayerdatawrite)
    - [ProtectedSetting](#protectedsetting)
        - [ProtectedSetting().composite](#protectedsettingcomposite)
        - [ProtectedSetting().position](#protectedsettingposition)
        - [ProtectedSetting().transparency](#protectedsettingtransparency)
    - [ReferencePoint](#referencepoint)
        - [ReferencePoint.read](#referencepointread)
        - [ReferencePoint().write](#referencepointwrite)
    - [SectionDividerSetting](#sectiondividersetting)
        - [SectionDividerSetting.read](#sectiondividersettingread)
        - [SectionDividerSetting().write](#sectiondividersettingwrite)
    - [SheetColorSetting](#sheetcolorsetting)
        - [SheetColorSetting.read](#sheetcolorsettingread)
        - [SheetColorSetting().write](#sheetcolorsettingwrite)
    - [SmartObjectLayerData](#smartobjectlayerdata)
        - [SmartObjectLayerData.read](#smartobjectlayerdataread)
        - [SmartObjectLayerData().write](#smartobjectlayerdatawrite)
    - [TaggedBlock](#taggedblock)
        - [TaggedBlock.read](#taggedblockread)
        - [TaggedBlock().write](#taggedblockwrite)
    - [TaggedBlocks](#taggedblocks)
        - [TaggedBlocks().get_data](#taggedblocksget_data)
        - [TaggedBlocks.read](#taggedblocksread)
        - [TaggedBlocks().set_data](#taggedblocksset_data)
    - [TypeToolObjectSetting](#typetoolobjectsetting)
        - [TypeToolObjectSetting.read](#typetoolobjectsettingread)
        - [TypeToolObjectSetting().write](#typetoolobjectsettingwrite)
    - [UserMask](#usermask)
        - [UserMask.read](#usermaskread)
        - [UserMask().write](#usermaskwrite)

Support the following tagged blocks: ``Tag.PATTERN_DATA``,
    ``Tag.TYPE_TOOL_INFO``, ``Tag.LAYER``,
    ``Tag.ALPHA``

## Annotation

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L333)

```python
attr.s(repr=False, slots=True)
class Annotation(BaseElement):
```

Annotation structure.

kind
is_open

#### See also

- [BaseElement](base.md#baseelement)

### Annotation.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L357)

```python
@classmethod
def read(fp, **kwargs):
```

### Annotation().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L373)

```python
def write(fp, **kwargs):
```

## Annotations

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L295)

```python
register(Tag.ANNOTATIONS)
attr.s(repr=False, slots=True)
class Annotations(ListElement):
```

List of Annotation, see :py:class: `.Annotation`.

major_version
minor_version

#### See also

- [ListElement](base.md#listelement)

### Annotations.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L305)

```python
@classmethod
def read(fp, **kwargs):
```

### Annotations().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L320)

```python
def write(fp, **kwargs):
```

## Bytes

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L394)

```python
register(Tag.FOREIGN_EFFECT_ID)
register(Tag.LAYER_NAME_SOURCE_SETTING)
attr.s(repr=False, slots=True, eq=False, order=False)
class Bytes(ValueElement):
```

Bytes structure.

value

#### See also

- [ValueElement](base.md#valueelement)

### Bytes.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L402)

```python
@classmethod
def read(fp, **kwargs):
```

### Bytes().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L406)

```python
def write(fp, **kwargs):
```

## ChannelBlendingRestrictionsSetting

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L412)

```python
register(Tag.CHANNEL_BLENDING_RESTRICTIONS_SETTING)
attr.s(repr=False, slots=True)
class ChannelBlendingRestrictionsSetting(ListElement):
```

ChannelBlendingRestrictionsSetting structure.

List of restricted channel numbers (int).

#### See also

- [ListElement](base.md#listelement)

### ChannelBlendingRestrictionsSetting.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L419)

```python
@classmethod
def read(fp, **kwargs):
```

### ChannelBlendingRestrictionsSetting().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L426)

```python
def write(fp, **kwargs):
```

## FilterMask

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L432)

```python
register(Tag.FILTER_MASK)
attr.s(repr=False, slots=True)
class FilterMask(BaseElement):
```

FilterMask structure.

color
opacity

#### See also

- [BaseElement](base.md#baseelement)

### FilterMask.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L442)

```python
@classmethod
def read(fp, **kwargs):
```

### FilterMask().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L448)

```python
def write(fp, **kwargs):
```

## MetadataSetting

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L475)

```python
attr.s(repr=False, slots=True)
class MetadataSetting(BaseElement):
```

MetadataSetting structure.

#### See also

- [BaseElement](base.md#baseelement)

### MetadataSetting.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L487)

```python
@classmethod
def read(fp, **kwargs):
```

### MetadataSetting().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L504)

```python
def write(fp, **kwargs):
```

## MetadataSettings

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L455)

```python
register(Tag.METADATA_SETTING)
class MetadataSettings(ListElement):
```

MetadataSettings structure.

#### See also

- [ListElement](base.md#listelement)

### MetadataSettings.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L460)

```python
@classmethod
def read(fp, **kwargs):
```

### MetadataSettings().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L468)

```python
def write(fp, **kwargs):
```

## PixelSourceData2

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L522)

```python
register(Tag.PIXEL_SOURCE_DATA2)
attr.s(repr=False, slots=True)
class PixelSourceData2(ListElement):
```

PixelSourceData2 structure.

#### See also

- [ListElement](base.md#listelement)

### PixelSourceData2.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L527)

```python
@classmethod
def read(fp, **kwargs):
```

### PixelSourceData2().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L534)

```python
def write(fp, padding=4, **kwargs):
```

## PlacedLayerData

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L547)

```python
register(Tag.PLACED_LAYER1)
register(Tag.PLACED_LAYER2)
attr.s(repr=False, slots=True)
class PlacedLayerData(BaseElement):
```

PlacedLayerData structure.

#### See also

- [BaseElement](base.md#baseelement)

### PlacedLayerData.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L565)

```python
@classmethod
def read(fp, **kwargs):
```

### PlacedLayerData().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L577)

```python
def write(fp, padding=4, **kwargs):
```

## ProtectedSetting

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L591)

```python
register(Tag.PROTECTED_SETTING)
class ProtectedSetting(IntegerElement):
```

ProtectedSetting structure.

#### See also

- [IntegerElement](base.md#integerelement)

### ProtectedSetting().composite

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L600)

```python
@property
def composite():
```

### ProtectedSetting().position

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L604)

```python
@property
def position():
```

### ProtectedSetting().transparency

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L596)

```python
@property
def transparency():
```

## ReferencePoint

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L611)

```python
register(Tag.REFERENCE_POINT)
attr.s(repr=False, slots=True)
class ReferencePoint(ListElement):
```

ReferencePoint structure.

#### See also

- [ListElement](base.md#listelement)

### ReferencePoint.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L616)

```python
@classmethod
def read(fp, **kwargs):
```

### ReferencePoint().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L620)

```python
def write(fp, **kwargs):
```

## SectionDividerSetting

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L627)

```python
register(Tag.SECTION_DIVIDER_SETTING)
register(Tag.NESTED_SECTION_DIVIDER_SETTING)
attr.s(repr=False, slots=True)
class SectionDividerSetting(BaseElement):
```

SectionDividerSetting structure.

kind
blend_mode
sub_type

#### See also

- [BaseElement](base.md#baseelement)

### SectionDividerSetting.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L644)

```python
@classmethod
def read(fp, **kwargs):
```

### SectionDividerSetting().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L662)

```python
def write(fp, **kwargs):
```

## SheetColorSetting

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L675)

```python
register(Tag.SHEET_COLOR_SETTING)
attr.s(repr=False, slots=True, eq=False, order=False)
class SheetColorSetting(ValueElement):
```

SheetColorSetting value.

This setting represents color label in the layers panel in Photoshop UI.

value

#### See also

- [ValueElement](base.md#valueelement)

### SheetColorSetting.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L685)

```python
@classmethod
def read(fp, **kwargs):
```

### SheetColorSetting().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L689)

```python
def write(fp, **kwargs):
```

## SmartObjectLayerData

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L696)

```python
register(Tag.SMART_OBJECT_LAYER_DATA1)
register(Tag.SMART_OBJECT_LAYER_DATA2)
attr.s(repr=False, slots=True)
class SmartObjectLayerData(BaseElement):
```

VersionedDescriptorBlock structure.

kind
version
data

#### See also

- [BaseElement](base.md#baseelement)

### SmartObjectLayerData.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L708)

```python
@classmethod
def read(fp, **kwargs):
```

### SmartObjectLayerData().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L714)

```python
def write(fp, padding=4, **kwargs):
```

## TaggedBlock

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L192)

```python
attr.s(repr=False, slots=True)
class TaggedBlock(BaseElement):
```

Layer tagged block with extra info.

key

4-character code. See :pyclass `psdtoolsx.constants.Tag`

data

Data.

#### See also

- [BaseElement](base.md#baseelement)

### TaggedBlock.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L236)

```python
@classmethod
def read(fp, version=1, padding=1):
```

### TaggedBlock().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L271)

```python
def write(fp, version=1, padding=1):
```

## TaggedBlocks

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L102)

```python
attr.s(repr=False, slots=True)
class TaggedBlocks(DictElement):
```

Dict of tagged block items.

See :pyclass `psdtoolsx.constants.Tag` for available keys.

Example

```python
from psdtoolsx.constants import Tag

# Iterate over fields
for key in tagged_blocks:
    print(key)

# Get a field
value = tagged_blocks.get_data(Tag.TYPE_TOOL_OBJECT_SETTING)
```

#### See also

- [DictElement](base.md#dictelement)

### TaggedBlocks().get_data

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L120)

```python
def get_data(key, default=None):
```

Get data from the tagged blocks.

Shortcut for the following

```python
if key in tagged_blocks:
    value = tagged_blocks[key].data
```

### TaggedBlocks.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L152)

```python
@classmethod
def read(fp, version=1, padding=1, end_pos=None):
```

### TaggedBlocks().set_data

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L137)

```python
def set_data(key, *args, **kwargs):
```

Set data for the given key.

Shortut for the following

```python
key = getattr(Tag, key)
kls = TYPES.get(key)
self[key] = TaggedBlocks(key=key, data=kls(value))
```

## TypeToolObjectSetting

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L723)

```python
register(Tag.TYPE_TOOL_OBJECT_SETTING)
attr.s(repr=False, slots=True)
class TypeToolObjectSetting(BaseElement):
```

TypeToolObjectSetting structure.

version
transform

Tuple of affine transform parameters (xx, xy, yx, yy, tx, ty).

text_version
text_data
warp_version
warp
left
top
right
bottom

#### See also

- [BaseElement](base.md#baseelement)

### TypeToolObjectSetting.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L752)

```python
@classmethod
def read(fp, **kwargs):
```

### TypeToolObjectSetting().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L774)

```python
def write(fp, padding=4, **kwargs):
```

## UserMask

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L789)

```python
register(Tag.USER_MASK)
attr.s(repr=False, slots=True)
class UserMask(BaseElement):
```

UserMask structure.

color
opacity
flag

#### See also

- [BaseElement](base.md#baseelement)

### UserMask.read

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L801)

```python
@classmethod
def read(fp, **kwargs):
```

### UserMask().write

[[find in source code]](../../../psdtoolsx/psd/tagged_blocks.py#L807)

```python
def write(fp, **kwargs):
```
