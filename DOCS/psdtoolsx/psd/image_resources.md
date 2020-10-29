# image_resources

> Auto-generated documentation for [psdtoolsx.psd.image_resources](../../../psdtoolsx/psd/image_resources.py) module.

Image resources section structure. Image resources are used to store non-pixel
data associated with images, such as pen tool paths or slices.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / image_resources
    - [AlphaIdentifiers](#alphaidentifiers)
        - [AlphaIdentifiers.read](#alphaidentifiersread)
        - [AlphaIdentifiers().write](#alphaidentifierswrite)
    - [AlphaNamesPascal](#alphanamespascal)
        - [AlphaNamesPascal.read](#alphanamespascalread)
        - [AlphaNamesPascal().write](#alphanamespascalwrite)
    - [AlphaNamesUnicode](#alphanamesunicode)
        - [AlphaNamesUnicode.read](#alphanamesunicoderead)
        - [AlphaNamesUnicode().write](#alphanamesunicodewrite)
    - [Byte](#byte)
        - [Byte.read](#byteread)
        - [Byte().write](#bytewrite)
    - [GridGuidesInfo](#gridguidesinfo)
        - [GridGuidesInfo.read](#gridguidesinforead)
        - [GridGuidesInfo().write](#gridguidesinfowrite)
    - [HalftoneScreen](#halftonescreen)
        - [HalftoneScreen.read](#halftonescreenread)
        - [HalftoneScreen().write](#halftonescreenwrite)
    - [HalftoneScreens](#halftonescreens)
        - [HalftoneScreens.read](#halftonescreensread)
        - [HalftoneScreens().write](#halftonescreenswrite)
    - [ImageResource](#imageresource)
        - [ImageResource.read](#imageresourceread)
        - [ImageResource().write](#imageresourcewrite)
    - [ImageResources](#imageresources)
        - [ImageResources().get_data](#imageresourcesget_data)
        - [ImageResources.new](#imageresourcesnew)
        - [ImageResources.read](#imageresourcesread)
        - [ImageResources().write](#imageresourceswrite)
    - [Integer](#integer)
        - [Integer.read](#integerread)
        - [Integer().write](#integerwrite)
    - [LayerGroupEnabledIDs](#layergroupenabledids)
        - [LayerGroupEnabledIDs.read](#layergroupenabledidsread)
        - [LayerGroupEnabledIDs().write](#layergroupenabledidswrite)
    - [LayerGroupInfo](#layergroupinfo)
        - [LayerGroupInfo.read](#layergroupinforead)
        - [LayerGroupInfo().write](#layergroupinfowrite)
    - [LayerSelectionIDs](#layerselectionids)
        - [LayerSelectionIDs.read](#layerselectionidsread)
        - [LayerSelectionIDs().write](#layerselectionidswrite)
    - [PascalString](#pascalstring)
        - [PascalString.read](#pascalstringread)
        - [PascalString().write](#pascalstringwrite)
    - [PixelAspectRatio](#pixelaspectratio)
        - [PixelAspectRatio.read](#pixelaspectratioread)
        - [PixelAspectRatio().write](#pixelaspectratiowrite)
    - [PrintFlags](#printflags)
        - [PrintFlags.read](#printflagsread)
        - [PrintFlags().write](#printflagswrite)
    - [PrintFlagsInfo](#printflagsinfo)
        - [PrintFlagsInfo.read](#printflagsinforead)
        - [PrintFlagsInfo().write](#printflagsinfowrite)
    - [PrintScale](#printscale)
        - [PrintScale.read](#printscaleread)
        - [PrintScale().write](#printscalewrite)
    - [ResoulutionInfo](#resoulutioninfo)
        - [ResoulutionInfo.read](#resoulutioninforead)
        - [ResoulutionInfo().write](#resoulutioninfowrite)
    - [ShortInteger](#shortinteger)
        - [ShortInteger.read](#shortintegerread)
        - [ShortInteger().write](#shortintegerwrite)
    - [SliceV6](#slicev6)
        - [SliceV6.read](#slicev6read)
        - [SliceV6().write](#slicev6write)
    - [Slices](#slices)
        - [Slices.read](#slicesread)
        - [Slices().write](#sliceswrite)
    - [SlicesV6](#slicesv6)
        - [SlicesV6.read](#slicesv6read)
        - [SlicesV6().write](#slicesv6write)
    - [ThumbnailResource](#thumbnailresource)
        - [ThumbnailResource.read](#thumbnailresourceread)
        - [ThumbnailResource().topil](#thumbnailresourcetopil)
        - [ThumbnailResource().write](#thumbnailresourcewrite)
    - [ThumbnailResourceV4](#thumbnailresourcev4)
    - [TransferFunction](#transferfunction)
        - [TransferFunction.read](#transferfunctionread)
        - [TransferFunction().write](#transferfunctionwrite)
    - [TransferFunctions](#transferfunctions)
        - [TransferFunctions.read](#transferfunctionsread)
        - [TransferFunctions().write](#transferfunctionswrite)
    - [URLItem](#urlitem)
        - [URLItem.read](#urlitemread)
        - [URLItem().write](#urlitemwrite)
    - [URLList](#urllist)
        - [URLList.read](#urllistread)
        - [URLList().write](#urllistwrite)
    - [VersionInfo](#versioninfo)
        - [VersionInfo.read](#versioninforead)
        - [VersionInfo().write](#versioninfowrite)

See :pyclass `psdtoolsx.constants.Resource` to check available
resource names.

Example

```python
from psdtoolsx.constants import Resource

version_info = psd.image_resources.get_data(Resource.VERSION_INFO)
```

The following resources are plain bytes

```python
Resource.OBSOLETE1: 1000
Resource.MAC_PRINT_MANAGER_INFO: 1001
Resource.MAC_PAGE_FORMAT_INFO: 1002
Resource.OBSOLETE2: 1003
Resource.DISPLAY_INFO_OBSOLETE: 1007
Resource.BORDER_INFO: 1009
Resource.DUOTONE_IMAGE_INFO: 1018
Resource.EFFECTIVE_BW: 1019
Resource.OBSOLETE3: 1020
Resource.EPS_OPTIONS: 1021
Resource.QUICK_MASK_INFO: 1022
Resource.OBSOLETE4: 1023
Resource.WORKING_PATH: 1025
Resource.OBSOLETE5: 1027
Resource.IPTC_NAA: 1028
Resource.IMAGE_MODE_RAW: 1029
Resource.JPEG_QUALITY: 1030
Resource.URL: 1035
Resource.COLOR_SAMPLERS_RESOURCE_OBSOLETE: 1038
Resource.ICC_PROFILE: 1039
Resource.SPOT_HALFTONE: 1043
Resource.JUMP_TO_XPEP: 1052
Resource.EXIF_DATA_1: 1058
Resource.EXIF_DATA_3: 1059
Resource.XMP_METADATA: 1060
Resource.CAPTION_DIGEST: 1061
Resource.ALTERNATE_DUOTONE_COLORS: 1066
Resource.ALTERNATE_SPOT_COLORS: 1067
Resource.HDR_TONING_INFO: 1070
Resource.PRINT_INFO_CS2: 1071
Resource.COLOR_SAMPLERS_RESOURCE: 1073
Resource.DISPLAY_INFO: 1077
Resource.MAC_NSPRINTINFO: 1084
Resource.WINDOWS_DEVMODE: 1085
Resource.PATH_INFO_N: 2000-2999
Resource.PLUGIN_RESOURCES_N: 4000-4999
Resource.IMAGE_READY_VARIABLES: 7000
Resource.IMAGE_READY_DATA_SETS: 7001
Resource.IMAGE_READY_DEFAULT_SELECTED_STATE: 7002
Resource.IMAGE_READY_7_ROLLOVER_EXPANDED_STATE: 7003
Resource.IMAGE_READY_ROLLOVER_EXPANDED_STATE: 7004
Resource.IMAGE_READY_SAVE_LAYER_SETTINGS: 7005
Resource.IMAGE_READY_VERSION: 7006
Resource.LIGHTROOM_WORKFLOW: 8000
```

## AlphaIdentifiers

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L279)

```python
register(Resource.ALPHA_IDENTIFIERS)
class AlphaIdentifiers(ListElement):
```

List of alpha identifiers.

#### See also

- [ListElement](base.md#listelement)

### AlphaIdentifiers.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L284)

```python
@classmethod
def read(fp, **kwargs):
```

### AlphaIdentifiers().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L291)

```python
def write(fp, **kwargs):
```

## AlphaNamesPascal

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L296)

```python
register(Resource.ALPHA_NAMES_PASCAL)
class AlphaNamesPascal(ListElement):
```

List of alpha names.

#### See also

- [ListElement](base.md#listelement)

### AlphaNamesPascal.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L301)

```python
@classmethod
def read(fp, **kwargs):
```

### AlphaNamesPascal().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L308)

```python
def write(fp, **kwargs):
```

## AlphaNamesUnicode

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L313)

```python
register(Resource.ALPHA_NAMES_UNICODE)
class AlphaNamesUnicode(ListElement):
```

List of alpha names.

#### See also

- [ListElement](base.md#listelement)

### AlphaNamesUnicode.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L318)

```python
@classmethod
def read(fp, **kwargs):
```

### AlphaNamesUnicode().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L325)

```python
def write(fp, **kwargs):
```

## Byte

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L333)

```python
register(Resource.ICC_UNTAGGED_PROFILE)
register(Resource.COPYRIGHT_FLAG)
register(Resource.EFFECTS_VISIBLE)
register(Resource.WATERMARK)
class Byte(ByteElement):
```

Byte element.

#### See also

- [ByteElement](base.md#byteelement)

### Byte.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L338)

```python
@classmethod
def read(fp, **kwargs):
```

### Byte().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L342)

```python
def write(fp, **kwargs):
```

## GridGuidesInfo

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L348)

```python
register(Resource.GRID_AND_GUIDES_INFO)
attr.s(repr=False, slots=True)
class GridGuidesInfo(BaseElement):
```

Grid and guides info structure.

.. py:attribute: version

#### See also

- [BaseElement](base.md#baseelement)

### GridGuidesInfo.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L359)

```python
@classmethod
def read(fp, **kwargs):
```

### GridGuidesInfo().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L367)

```python
def write(fp, **kwargs):
```

## HalftoneScreen

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L396)

```python
attr.s(repr=False, slots=True)
class HalftoneScreen(BaseElement):
```

Halftone screen.

freq
unit
angle
shape
use_accurate
use_printer

#### See also

- [BaseElement](base.md#baseelement)

### HalftoneScreen.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L414)

```python
@classmethod
def read(fp, **kwargs):
```

### HalftoneScreen().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L422)

```python
def write(fp, **kwargs):
```

## HalftoneScreens

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L379)

```python
register(Resource.COLOR_HALFTONING_INFO)
register(Resource.DUOTONE_HALFTONING_INFO)
register(Resource.GRAYSCALE_HALFTONING_INFO)
class HalftoneScreens(ListElement):
```

Halftone screens.

#### See also

- [ListElement](base.md#listelement)

### HalftoneScreens.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L384)

```python
@classmethod
def read(fp, **kwargs):
```

### HalftoneScreens().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L391)

```python
def write(fp, **kwargs):
```

## ImageResource

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L207)

```python
attr.s(repr=False, slots=True)
class ImageResource(BaseElement):
```

Image resource block.

signature

Binary signature, always ``b'8BIM'``.

key

Unique identifier for the resource. See
:pyclass `psdtoolsx.constants.Resource`.

name
data

The resource data.

#### See also

- [BaseElement](base.md#baseelement)

### ImageResource.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L235)

```python
@classmethod
def read(fp, encoding='macroman'):
```

### ImageResource().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L263)

```python
def write(fp, encoding='macroman'):
```

## ImageResources

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L112)

```python
attr.s(repr=False, slots=True)
class ImageResources(DictElement):
```

Image resources section of the PSD file. Dict of
:pyclass `.ImageResource`.

#### See also

- [DictElement](base.md#dictelement)

### ImageResources().get_data

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L118)

```python
def get_data(key, default=None):
```

Get data from the image resources.

Shortcut for the following

```python
if key in image_resources:
    value = tagged_blocks[key].data
```

### ImageResources.new

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L135)

```python
@classmethod
def new(**kwargs):
```

Create a new default image resouces.

#### Returns

ImageResources

### ImageResources.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L156)

```python
@classmethod
def read(fp, encoding='macroman'):
```

### ImageResources().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L171)

```python
def write(fp, encoding='macroman'):
```

## Integer

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L435)

```python
register(Resource.GLOBAL_ALTITUDE)
register(Resource.GLOBAL_ANGLE)
register(Resource.IDS_SEED_NUMBER)
class Integer(IntegerElement):
```

Integer element.

#### See also

- [IntegerElement](base.md#integerelement)

### Integer.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L440)

```python
@classmethod
def read(fp, **kwargs):
```

### Integer().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L444)

```python
def write(fp, **kwargs):
```

## LayerGroupEnabledIDs

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L449)

```python
register(Resource.LAYER_GROUPS_ENABLED_ID)
class LayerGroupEnabledIDs(ListElement):
```

Layer group enabled ids.

#### See also

- [ListElement](base.md#listelement)

### LayerGroupEnabledIDs.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L454)

```python
@classmethod
def read(fp, **kwargs):
```

### LayerGroupEnabledIDs().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L461)

```python
def write(fp, **kwargs):
```

## LayerGroupInfo

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L466)

```python
register(Resource.LAYER_GROUP_INFO)
class LayerGroupInfo(ListElement):
```

Layer group info list.

#### See also

- [ListElement](base.md#listelement)

### LayerGroupInfo.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L471)

```python
@classmethod
def read(fp, **kwargs):
```

### LayerGroupInfo().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L478)

```python
def write(fp, **kwargs):
```

## LayerSelectionIDs

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L483)

```python
register(Resource.LAYER_SELECTION_IDS)
class LayerSelectionIDs(ListElement):
```

Layer selection ids.

#### See also

- [ListElement](base.md#listelement)

### LayerSelectionIDs.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L488)

```python
@classmethod
def read(fp, **kwargs):
```

### LayerSelectionIDs().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L493)

```python
def write(fp, **kwargs):
```

## PascalString

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L517)

```python
register(Resource.CAPTION_PASCAL)
register(Resource.CLIPPING_PATH_NAME)
class PascalString(ValueElement):
```

Pascal string element.

#### See also

- [ValueElement](base.md#valueelement)

### PascalString.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L522)

```python
@classmethod
def read(fp, **kwargs):
```

### PascalString().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L526)

```python
def write(fp, **kwargs):
```

## PixelAspectRatio

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L532)

```python
register(Resource.PIXEL_ASPECT_RATIO)
attr.s(repr=False, slots=True)
class PixelAspectRatio(NumericElement):
```

Pixel aspect ratio.

.. py:attribute: version

#### See also

- [NumericElement](base.md#numericelement)

### PixelAspectRatio.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L540)

```python
@classmethod
def read(fp, **kwargs):
```

### PixelAspectRatio().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L545)

```python
def write(fp, **kwargs):
```

## PrintFlags

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L551)

```python
register(Resource.PRINT_FLAGS)
attr.s(repr=False, slots=True)
class PrintFlags(BaseElement):
```

Print flags.

.. py:attribute: labels
.. py:attribute: crop_marks
.. py:attribute: colorbars
.. py:attribute: registration_marks
.. py:attribute: negative
.. py:attribute: flip
.. py:attribute: interpolate
.. py:attribute: caption
.. py:attribute: print_flags

#### See also

- [BaseElement](base.md#baseelement)

### PrintFlags.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L575)

```python
@classmethod
def read(fp, **kwargs):
```

### PrintFlags().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L582)

```python
def write(fp, **kwargs):
```

## PrintFlagsInfo

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L591)

```python
register(Resource.PRINT_FLAGS_INFO)
attr.s(repr=False, slots=True)
class PrintFlagsInfo(BaseElement):
```

Print flags info structure.

version
center_crop
bleed_width_value
bleed_width_scale

#### See also

- [BaseElement](base.md#baseelement)

### PrintFlagsInfo.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L605)

```python
@classmethod
def read(fp, **kwargs):
```

### PrintFlagsInfo().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L609)

```python
def write(fp, **kwargs):
```

## PrintScale

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L615)

```python
register(Resource.PRINT_SCALE)
attr.s(repr=False, slots=True)
class PrintScale(BaseElement):
```

Print scale structure.

style
x
y
scale

#### See also

- [BaseElement](base.md#baseelement)

### PrintScale.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L633)

```python
@classmethod
def read(fp, **kwargs):
```

### PrintScale().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L637)

```python
def write(fp, **kwargs):
```

## ResoulutionInfo

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L645)

```python
register(Resource.RESOLUTION_INFO)
attr.s(repr=False, slots=True)
class ResoulutionInfo(BaseElement):
```

Resoulution info structure.

horizontal
horizontal_unit
width_unit
vertical
vertical_unit
height_unit

#### See also

- [BaseElement](base.md#baseelement)

### ResoulutionInfo.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L663)

```python
@classmethod
def read(fp, **kwargs):
```

### ResoulutionInfo().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L667)

```python
def write(fp, **kwargs):
```

## ShortInteger

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L502)

```python
register(Resource.INDEXED_COLOR_TABLE_COUNT)
register(Resource.LAYER_STATE_INFO)
register(Resource.TRANSPARENCY_INDEX)
class ShortInteger(ShortIntegerElement):
```

Short integer element.

#### See also

- [ShortIntegerElement](base.md#shortintegerelement)

### ShortInteger.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L507)

```python
@classmethod
def read(fp, **kwargs):
```

### ShortInteger().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L511)

```python
def write(fp, **kwargs):
```

## SliceV6

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L727)

```python
attr.s(repr=False)
class SliceV6(BaseElement):
```

Slice element for version 6.

slice_id
group_id
origin
associated_id
name
slice_type
bbox
url
target
message
alt_tag
cell_is_html
cell_text
horizontal
vertical
alpha
red
green
blue
data

#### See also

- [BaseElement](base.md#baseelement)

### SliceV6.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L773)

```python
@classmethod
def read(fp):
```

### SliceV6().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L810)

```python
def write(fp):
```

## Slices

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L673)

```python
register(Resource.SLICES)
attr.s(repr=False, slots=True)
class Slices(BaseElement):
```

Slices resource.

version
data

#### See also

- [BaseElement](base.md#baseelement)

### Slices.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L683)

```python
@classmethod
def read(fp, **kwargs):
```

### Slices().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L691)

```python
def write(fp, **kwargs):
```

## SlicesV6

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L698)

```python
attr.s(repr=False, slots=True)
class SlicesV6(BaseElement):
```

Slices resource version 6.

bbox
name
items

#### See also

- [BaseElement](base.md#baseelement)

### SlicesV6.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L710)

```python
@classmethod
def read(fp):
```

### SlicesV6().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L718)

```python
def write(fp, **kwargs):
```

## ThumbnailResource

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L841)

```python
register(Resource.THUMBNAIL_RESOURCE)
attr.s(repr=False)
class ThumbnailResource(BaseElement):
```

Thumbnail resource structure.

fmt
width
height
row
total_size
size
bits
planes
data

#### See also

- [BaseElement](base.md#baseelement)

### ThumbnailResource.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L866)

```python
@classmethod
def read(fp, **kwargs):
```

### ThumbnailResource().topil

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L882)

```python
def topil():
```

Get PIL Image.

#### Returns

PIL Image object.

### ThumbnailResource().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L874)

```python
def write(fp, **kwargs):
```

## ThumbnailResourceV4

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L902)

```python
register(Resource.THUMBNAIL_RESOURCE_PS4)
class ThumbnailResourceV4(ThumbnailResource):
```

#### See also

- [ThumbnailResource](#thumbnailresource)

## TransferFunction

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L926)

```python
attr.s(repr=False)
class TransferFunction(BaseElement):
```

Transfer function

#### See also

- [BaseElement](base.md#baseelement)

### TransferFunction.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L933)

```python
@classmethod
def read(fp, **kwargs):
```

### TransferFunction().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L939)

```python
def write(fp, **kwargs):
```

## TransferFunctions

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L909)

```python
register(Resource.COLOR_TRANSFER_FUNCTION)
register(Resource.DUOTONE_TRANSFER_FUNCTION)
register(Resource.GRAYSCALE_TRANSFER_FUNCTION)
class TransferFunctions(ListElement):
```

Transfer functions.

#### See also

- [ListElement](base.md#listelement)

### TransferFunctions.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L914)

```python
@classmethod
def read(fp, **kwargs):
```

### TransferFunctions().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L921)

```python
def write(fp, **kwargs):
```

## URLItem

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L966)

```python
attr.s(repr=False)
class URLItem(BaseElement):
```

URL item.

number
id
name

#### See also

- [BaseElement](base.md#baseelement)

### URLItem.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L978)

```python
@classmethod
def read(fp):
```

### URLItem().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L984)

```python
def write(fp):
```

## URLList

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L946)

```python
register(Resource.URL_LIST)
class URLList(ListElement):
```

URL list structure.

#### See also

- [ListElement](base.md#listelement)

### URLList.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L951)

```python
@classmethod
def read(fp, **kwargs):
```

### URLList().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L959)

```python
def write(fp, **kwargs):
```

## VersionInfo

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L992)

```python
register(Resource.VERSION_INFO)
attr.s(repr=False)
class VersionInfo(BaseElement):
```

Version info structure.

version
has_composite
writer
reader
file_version

#### See also

- [BaseElement](base.md#baseelement)

### VersionInfo.read

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L1008)

```python
@classmethod
def read(fp, **kwargs):
```

### VersionInfo().write

[[find in source code]](../../../psdtoolsx/psd/image_resources.py#L1016)

```python
def write(fp, **kwargs):
```
