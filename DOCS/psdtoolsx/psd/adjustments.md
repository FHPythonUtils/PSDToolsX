# adjustments

> Auto-generated documentation for [psdtoolsx.psd.adjustments](../../../psdtoolsx/psd/adjustments.py) module.

Adjustment layer structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / adjustments
    - [BrightnessContrast](#brightnesscontrast)
        - [BrightnessContrast.read](#brightnesscontrastread)
        - [BrightnessContrast().write](#brightnesscontrastwrite)
    - [ChannelMixer](#channelmixer)
        - [ChannelMixer.read](#channelmixerread)
        - [ChannelMixer().write](#channelmixerwrite)
    - [ColorBalance](#colorbalance)
        - [ColorBalance.read](#colorbalanceread)
        - [ColorBalance().write](#colorbalancewrite)
    - [ColorLookup](#colorlookup)
        - [ColorLookup.read](#colorlookupread)
        - [ColorLookup().write](#colorlookupwrite)
    - [ColorStop](#colorstop)
        - [ColorStop.read](#colorstopread)
        - [ColorStop().write](#colorstopwrite)
    - [Curves](#curves)
        - [Curves.read](#curvesread)
        - [Curves().write](#curveswrite)
    - [CurvesExtraItem](#curvesextraitem)
        - [CurvesExtraItem.read](#curvesextraitemread)
        - [CurvesExtraItem().write](#curvesextraitemwrite)
    - [CurvesExtraMarker](#curvesextramarker)
        - [CurvesExtraMarker.read](#curvesextramarkerread)
        - [CurvesExtraMarker().write](#curvesextramarkerwrite)
    - [Exposure](#exposure)
        - [Exposure.read](#exposureread)
        - [Exposure().write](#exposurewrite)
    - [GradientMap](#gradientmap)
        - [GradientMap.read](#gradientmapread)
        - [GradientMap().write](#gradientmapwrite)
    - [HueSaturation](#huesaturation)
        - [HueSaturation.read](#huesaturationread)
        - [HueSaturation().write](#huesaturationwrite)
    - [LevelRecord](#levelrecord)
        - [LevelRecord.read](#levelrecordread)
        - [LevelRecord().write](#levelrecordwrite)
    - [Levels](#levels)
        - [Levels.read](#levelsread)
        - [Levels().write](#levelswrite)
    - [PhotoFilter](#photofilter)
        - [PhotoFilter.read](#photofilterread)
        - [PhotoFilter().write](#photofilterwrite)
    - [SelectiveColor](#selectivecolor)
        - [SelectiveColor.read](#selectivecolorread)
        - [SelectiveColor().write](#selectivecolorwrite)
    - [TransparencyStop](#transparencystop)
        - [TransparencyStop.read](#transparencystopread)
        - [TransparencyStop().write](#transparencystopwrite)

## BrightnessContrast

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L40)

```python
register(Tag.BRIGHTNESS_AND_CONTRAST)
attr.s(repr=False, slots=True)
class BrightnessContrast(BaseElement):
```

BrightnessContrast structure.

brightness
contrast
mean
lab_only

#### See also

- [BaseElement](base.md#baseelement)

### BrightnessContrast.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L54)

```python
@classmethod
def read(fp, **kwargs):
```

### BrightnessContrast().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L58)

```python
def write(fp, **kwargs):
```

## ChannelMixer

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L121)

```python
register(Tag.CHANNEL_MIXER)
attr.s(repr=False, slots=True)
class ChannelMixer(BaseElement):
```

ChannelMixer structure.

version
monochrome
data

#### See also

- [BaseElement](base.md#baseelement)

### ChannelMixer.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L134)

```python
@classmethod
def read(fp, **kwargs):
```

### ChannelMixer().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L141)

```python
def write(fp, **kwargs):
```

## ColorBalance

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L64)

```python
register(Tag.COLOR_BALANCE)
attr.s(repr=False, slots=True)
class ColorBalance(BaseElement):
```

ColorBalance structure.

shadows
midtones
highlights
luminosity

#### See also

- [BaseElement](base.md#baseelement)

### ColorBalance.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L78)

```python
@classmethod
def read(fp, **kwargs):
```

### ColorBalance().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L86)

```python
def write(fp, **kwargs):
```

## ColorLookup

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L96)

```python
register(Tag.COLOR_LOOKUP)
class ColorLookup(DescriptorBlock2):
```

Dict-like Descriptor-based structure. See
:pyclass `psdtoolsx.psd.descriptor.Descriptor`.

version
data_version

#### See also

- [DescriptorBlock2](descriptor.md#descriptorblock2)

### ColorLookup.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L105)

```python
@classmethod
def read(fp, **kwargs):
```

### ColorLookup().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L112)

```python
def write(fp, padding=4, **kwargs):
```

## ColorStop

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L359)

```python
attr.s(repr=False, slots=True)
class ColorStop(BaseElement):
```

ColorStop of GradientMap.

location
midpoint
mode
color

#### See also

- [BaseElement](base.md#baseelement)

### ColorStop.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L373)

```python
@classmethod
def read(fp):
```

### ColorStop().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L379)

```python
def write(fp):
```

## Curves

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L150)

```python
register(Tag.CURVES)
attr.s(repr=False, slots=True)
class Curves(BaseElement):
```

Curves structure.

is_map
version
count
data
extra

#### See also

- [BaseElement](base.md#baseelement)

### Curves.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L166)

```python
@classmethod
def read(fp, **kwargs):
```

### Curves().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L199)

```python
def write(fp, **kwargs):
```

## CurvesExtraItem

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L242)

```python
attr.s(repr=False, slots=True)
class CurvesExtraItem(BaseElement):
```

Curves extra item.

channel_id
points

#### See also

- [BaseElement](base.md#baseelement)

### CurvesExtraItem.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L252)

```python
@classmethod
def read(fp, is_map=False, **kwargs):
```

### CurvesExtraItem().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L262)

```python
def write(fp, **kwargs):
```

## CurvesExtraMarker

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L218)

```python
attr.s(repr=False, slots=True)
class CurvesExtraMarker(ListElement):
```

Curves extra marker structure.

version

#### See also

- [ListElement](base.md#listelement)

### CurvesExtraMarker.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L226)

```python
@classmethod
def read(fp, **kwargs):
```

### CurvesExtraMarker().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L235)

```python
def write(fp, **kwargs):
```

## Exposure

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L408)

```python
register(Tag.EXPOSURE)
attr.s(repr=False, slots=True)
class Exposure(BaseElement):
```

Exposure structure.

version
exposure
offset
gamma

#### See also

- [BaseElement](base.md#baseelement)

### Exposure.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L422)

```python
@classmethod
def read(fp, **kwargs):
```

### Exposure().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L426)

```python
def write(fp, padding=4, **kwargs):
```

## GradientMap

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L274)

```python
register(Tag.GRADIENT_MAP)
attr.s(repr=False, slots=True)
class GradientMap(BaseElement):
```

GradientMap structure.

version
is_reversed
is_dithered
name
color_stops
transparency_stops
expansion
interpolation
length
mode
random_seed
show_transparency
use_vector_color
roughness
color_model
minimum_color
maximum_color

#### See also

- [BaseElement](base.md#baseelement)

### GradientMap.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L314)

```python
@classmethod
def read(fp, **kwargs):
```

### GradientMap().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L337)

```python
def write(fp, **kwargs):
```

## HueSaturation

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L435)

```python
register(Tag.HUE_SATURATION_V4)
register(Tag.HUE_SATURATION)
attr.s(repr=False, slots=True)
class HueSaturation(BaseElement):
```

HueSaturation structure.

version
enable
colorization
master
items

#### See also

- [BaseElement](base.md#baseelement)

### HueSaturation.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L451)

```python
@classmethod
def read(fp, **kwargs):
```

### HueSaturation().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L464)

```python
def write(fp, **kwargs):
```

## LevelRecord

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L527)

```python
attr.s(repr=False, slots=True)
class LevelRecord(BaseElement):
```

Level record.

input_floor

Input floor (0...253).

input_ceiling

Input ceiling (2...255).

output_floor

Output floor (0...255). Matched to input floor.

output_ceiling

Output ceiling (0...255).

gamma

Gamma. Short integer from 10...999 representing 0.1...9.99. Applied
to all image data.

#### See also

- [BaseElement](base.md#baseelement)

### LevelRecord.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L558)

```python
@classmethod
def read(fp):
```

### LevelRecord().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L562)

```python
def write(fp):
```

## Levels

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L477)

```python
register(Tag.LEVELS)
attr.s(repr=False, slots=True)
class Levels(ListElement):
```

List of level records. See :py:class:
`~psdtoolsx.psd.adjustments.LevelRecord`.

version

Version.

extra_version

Version of the extra field.

#### See also

- [ListElement](base.md#listelement)

### Levels.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L493)

```python
@classmethod
def read(fp, **kwargs):
```

### Levels().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L511)

```python
def write(fp, **kwargs):
```

## PhotoFilter

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L568)

```python
register(Tag.PHOTO_FILTER)
attr.s(repr=False, slots=True)
class PhotoFilter(BaseElement):
```

PhotoFilter structure.

version
xyz
color_space
color_components
density
luminosity

#### See also

- [BaseElement](base.md#baseelement)

### PhotoFilter.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L586)

```python
@classmethod
def read(fp, **kwargs):
```

### PhotoFilter().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L603)

```python
def write(fp, **kwargs):
```

## SelectiveColor

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L618)

```python
register(Tag.SELECTIVE_COLOR)
attr.s(repr=False, slots=True)
class SelectiveColor(BaseElement):
```

SelectiveColor structure.

version
method
data

#### See also

- [BaseElement](base.md#baseelement)

### SelectiveColor.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L630)

```python
@classmethod
def read(fp, **kwargs):
```

### SelectiveColor().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L636)

```python
def write(fp, **kwargs):
```

## TransparencyStop

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L386)

```python
attr.s(repr=False, slots=True)
class TransparencyStop(BaseElement):
```

TransparencyStop of GradientMap.

location
midpoint
opacity

#### See also

- [BaseElement](base.md#baseelement)

### TransparencyStop.read

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L398)

```python
@classmethod
def read(fp):
```

### TransparencyStop().write

[[find in source code]](../../../psdtoolsx/psd/adjustments.py#L402)

```python
def write(fp):
```
