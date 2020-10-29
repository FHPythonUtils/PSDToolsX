# adjustments

> Auto-generated documentation for [psdtoolsx.api.adjustments](../../../psdtoolsx/api/adjustments.py) module.

Adjustment and fill layers.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / adjustments
    - [BlackAndWhite](#blackandwhite)
        - [BlackAndWhite().blue](#blackandwhiteblue)
        - [BlackAndWhite().cyan](#blackandwhitecyan)
        - [BlackAndWhite().green](#blackandwhitegreen)
        - [BlackAndWhite().magenta](#blackandwhitemagenta)
        - [BlackAndWhite().preset_file_name](#blackandwhitepreset_file_name)
        - [BlackAndWhite().preset_kind](#blackandwhitepreset_kind)
        - [BlackAndWhite().red](#blackandwhitered)
        - [BlackAndWhite().tint_color](#blackandwhitetint_color)
        - [BlackAndWhite().use_tint](#blackandwhiteuse_tint)
        - [BlackAndWhite().yellow](#blackandwhiteyellow)
    - [BrightnessContrast](#brightnesscontrast)
        - [BrightnessContrast().automatic](#brightnesscontrastautomatic)
        - [BrightnessContrast().brightness](#brightnesscontrastbrightness)
        - [BrightnessContrast().contrast](#brightnesscontrastcontrast)
        - [BrightnessContrast().lab](#brightnesscontrastlab)
        - [BrightnessContrast().mean](#brightnesscontrastmean)
        - [BrightnessContrast().use_legacy](#brightnesscontrastuse_legacy)
        - [BrightnessContrast().vrsn](#brightnesscontrastvrsn)
    - [ChannelMixer](#channelmixer)
        - [ChannelMixer().data](#channelmixerdata)
        - [ChannelMixer().monochrome](#channelmixermonochrome)
    - [ColorBalance](#colorbalance)
        - [ColorBalance().highlights](#colorbalancehighlights)
        - [ColorBalance().luminosity](#colorbalanceluminosity)
        - [ColorBalance().midtones](#colorbalancemidtones)
        - [ColorBalance().shadows](#colorbalanceshadows)
    - [ColorLookup](#colorlookup)
    - [Curves](#curves)
        - [Curves().data](#curvesdata)
        - [Curves().extra](#curvesextra)
    - [Exposure](#exposure)
        - [Exposure().exposure](#exposureexposure)
        - [Exposure().gamma](#exposuregamma)
        - [Exposure().offset](#exposureoffset)
    - [GradientFill](#gradientfill)
        - [GradientFill().angle](#gradientfillangle)
        - [GradientFill().data](#gradientfilldata)
        - [GradientFill().gradient_kind](#gradientfillgradient_kind)
    - [GradientMap](#gradientmap)
        - [GradientMap().color_model](#gradientmapcolor_model)
        - [GradientMap().color_stops](#gradientmapcolor_stops)
        - [GradientMap().dithered](#gradientmapdithered)
        - [GradientMap().expansion](#gradientmapexpansion)
        - [GradientMap().gradient_name](#gradientmapgradient_name)
        - [GradientMap().interpolation](#gradientmapinterpolation)
        - [GradientMap().length](#gradientmaplength)
        - [GradientMap().max_color](#gradientmapmax_color)
        - [GradientMap().min_color](#gradientmapmin_color)
        - [GradientMap().mode](#gradientmapmode)
        - [GradientMap().random_seed](#gradientmaprandom_seed)
        - [GradientMap().reversed](#gradientmapreversed)
        - [GradientMap().roughness](#gradientmaproughness)
        - [GradientMap().show_transparency](#gradientmapshow_transparency)
        - [GradientMap().transparency_stops](#gradientmaptransparency_stops)
        - [GradientMap().use_vector_color](#gradientmapuse_vector_color)
    - [HueSaturation](#huesaturation)
        - [HueSaturation().colorization](#huesaturationcolorization)
        - [HueSaturation().data](#huesaturationdata)
        - [HueSaturation().enable_colorization](#huesaturationenable_colorization)
        - [HueSaturation().master](#huesaturationmaster)
    - [Invert](#invert)
    - [Levels](#levels)
        - [Levels().data](#levelsdata)
        - [Levels().master](#levelsmaster)
    - [PatternFill](#patternfill)
        - [PatternFill().data](#patternfilldata)
    - [PhotoFilter](#photofilter)
        - [PhotoFilter().color_components](#photofiltercolor_components)
        - [PhotoFilter().color_space](#photofiltercolor_space)
        - [PhotoFilter().density](#photofilterdensity)
        - [PhotoFilter().luminosity](#photofilterluminosity)
        - [PhotoFilter().xyz](#photofilterxyz)
    - [Posterize](#posterize)
        - [Posterize().posterize](#posterizeposterize)
    - [SelectiveColor](#selectivecolor)
        - [SelectiveColor().data](#selectivecolordata)
        - [SelectiveColor().method](#selectivecolormethod)
    - [SolidColorFill](#solidcolorfill)
        - [SolidColorFill().data](#solidcolorfilldata)
    - [Threshold](#threshold)
        - [Threshold().threshold](#thresholdthreshold)
    - [Vibrance](#vibrance)
        - [Vibrance().saturation](#vibrancesaturation)
        - [Vibrance().vibrance](#vibrancevibrance)

Example

```python
if layer.kind == 'brightnesscontrast':
    print(layer.brightness)

if layer.kind == 'gradientfill':
    print(layer.gradient_kind)
```

## BlackAndWhite

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L281)

```python
register(Tag.BLACK_AND_WHITE)
class BlackAndWhite(AdjustmentLayer):
```

Black and white adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### BlackAndWhite().blue

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L300)

```python
@property
def blue():
```

### BlackAndWhite().cyan

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L296)

```python
@property
def cyan():
```

### BlackAndWhite().green

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L292)

```python
@property
def green():
```

### BlackAndWhite().magenta

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L304)

```python
@property
def magenta():
```

### BlackAndWhite().preset_file_name

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L320)

```python
@property
def preset_file_name():
```

### BlackAndWhite().preset_kind

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L316)

```python
@property
def preset_kind():
```

### BlackAndWhite().red

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L284)

```python
@property
def red():
```

### BlackAndWhite().tint_color

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L312)

```python
@property
def tint_color():
```

### BlackAndWhite().use_tint

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L308)

```python
@property
def use_tint():
```

### BlackAndWhite().yellow

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L288)

```python
@property
def yellow():
```

## BrightnessContrast

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L72)

```python
register(Tag.CONTENT_GENERATOR_EXTRA_DATA)
class BrightnessContrast(AdjustmentLayer):
```

Brightness and contrast adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### BrightnessContrast().automatic

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L100)

```python
@property
def automatic():
```

### BrightnessContrast().brightness

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L76)

```python
@property
def brightness():
```

### BrightnessContrast().contrast

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L80)

```python
@property
def contrast():
```

### BrightnessContrast().lab

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L88)

```python
@property
def lab():
```

### BrightnessContrast().mean

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L84)

```python
@property
def mean():
```

### BrightnessContrast().use_legacy

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L92)

```python
@property
def use_legacy():
```

### BrightnessContrast().vrsn

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L96)

```python
@property
def vrsn():
```

## ChannelMixer

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L356)

```python
register(Tag.CHANNEL_MIXER)
class ChannelMixer(AdjustmentLayer):
```

Channel mixer adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### ChannelMixer().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L363)

```python
@property
def data():
```

### ChannelMixer().monochrome

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L359)

```python
@property
def monochrome():
```

## ColorBalance

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L244)

```python
register(Tag.COLOR_BALANCE)
class ColorBalance(AdjustmentLayer):
```

Color balance adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### ColorBalance().highlights

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L263)

```python
@property
def highlights():
```

Highlights.

#### Returns

`tuple`

### ColorBalance().luminosity

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L271)

```python
@property
def luminosity():
```

Luminosity.

#### Returns

`int`

### ColorBalance().midtones

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L255)

```python
@property
def midtones():
```

Mid-tones.

#### Returns

`tuple`

### ColorBalance().shadows

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L247)

```python
@property
def shadows():
```

Shadows.

#### Returns

`tuple`

## ColorLookup

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L369)

```python
register(Tag.COLOR_LOOKUP)
class ColorLookup(AdjustmentLayer):
```

Color lookup adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

## Curves

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L106)

```python
register(Tag.CURVES)
class Curves(AdjustmentLayer):
```

Curves adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### Curves().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L111)

```python
@property
def data():
```

Raw data.

#### Returns

:pyclass `psdtoolsx.psd.adjustments.Curves`

### Curves().extra

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L120)

```python
@property
def extra():
```

## Exposure

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L126)

```python
register(Tag.EXPOSURE)
class Exposure(AdjustmentLayer):
```

Exposure adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### Exposure().exposure

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L131)

```python
@property
def exposure():
```

Exposure.

#### Returns

`float`

### Exposure().gamma

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L147)

```python
@property
def gamma():
```

Gamma.

#### Returns

`float`

### Exposure().offset

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L139)

```python
@property
def offset():
```

Offset.

#### Returns

`float`

## GradientFill

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L45)

```python
register(Tag.GRADIENT_FILL_SETTING)
class GradientFill(FillLayer):
```

Gradient fill.

#### See also

- [FillLayer](layers.md#filllayer)

### GradientFill().angle

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L48)

```python
@property
def angle():
```

### GradientFill().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L65)

```python
@property
def data():
```

Gradient in Descriptor(GRADIENT).

### GradientFill().gradient_kind

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L52)

```python
@property
def gradient_kind():
```

Kind of the gradient, one of the following:

- `Linear`
- `Radial`
- `Angle`
- `Reflected`
- `Diamond`

## GradientMap

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L420)

```python
register(Tag.GRADIENT_MAP)
class GradientMap(AdjustmentLayer):
```

Gradient map adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### GradientMap().color_model

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L476)

```python
@property
def color_model():
```

### GradientMap().color_stops

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L435)

```python
@property
def color_stops():
```

### GradientMap().dithered

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L427)

```python
@property
def dithered():
```

### GradientMap().expansion

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L443)

```python
@property
def expansion():
```

### GradientMap().gradient_name

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L431)

```python
@property
def gradient_name():
```

### GradientMap().interpolation

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L447)

```python
@property
def interpolation():
```

Interpolation between 0.0 and 1.0.

### GradientMap().length

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L452)

```python
@property
def length():
```

### GradientMap().max_color

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L484)

```python
@property
def max_color():
```

### GradientMap().min_color

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L480)

```python
@property
def min_color():
```

### GradientMap().mode

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L456)

```python
@property
def mode():
```

### GradientMap().random_seed

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L460)

```python
@property
def random_seed():
```

### GradientMap().reversed

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L423)

```python
@property
def reversed():
```

### GradientMap().roughness

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L472)

```python
@property
def roughness():
```

### GradientMap().show_transparency

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L464)

```python
@property
def show_transparency():
```

### GradientMap().transparency_stops

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L439)

```python
@property
def transparency_stops():
```

### GradientMap().use_vector_color

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L468)

```python
@property
def use_vector_color():
```

## HueSaturation

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L202)

```python
register(Tag.HUE_SATURATION)
class HueSaturation(AdjustmentLayer):
```

Hue/Saturation adjustment.

HueSaturation contains a list of data.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### HueSaturation().colorization

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L226)

```python
@property
def colorization():
```

Colorization.

#### Returns

`tuple`

### HueSaturation().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L209)

```python
@property
def data():
```

List of Hue/Saturation records.

#### Returns

`list`

### HueSaturation().enable_colorization

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L218)

```python
@property
def enable_colorization():
```

Enable colorization.

#### Returns

`int`

### HueSaturation().master

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L234)

```python
@property
def master():
```

Master record.

#### Returns

`tuple`

## Invert

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L375)

```python
register(Tag.INVERT)
class Invert(AdjustmentLayer):
```

Invert adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

## Levels

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L157)

```python
register(Tag.LEVELS)
class Levels(AdjustmentLayer):
```

Levels adjustment.

Levels contain a list of
:pyclass `psdtoolsx.psd.adjustments.LevelRecord`.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### Levels().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L165)

```python
@property
def data():
```

List of level records. The first record is the master.

#### Returns

:pyclass `psdtoolsx.psd.adjustments.Levels`.

### Levels().master

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L174)

```python
@property
def master():
```

Master record.

## PatternFill

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L35)

```python
register(Tag.PATTERN_FILL_SETTING)
class PatternFill(FillLayer):
```

Pattern fill.

#### See also

- [FillLayer](layers.md#filllayer)

### PatternFill().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L38)

```python
@property
def data():
```

Pattern in Descriptor(PATTERN).

## PhotoFilter

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L327)

```python
register(Tag.PHOTO_FILTER)
class PhotoFilter(AdjustmentLayer):
```

Photo filter adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### PhotoFilter().color_components

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L342)

```python
@property
def color_components():
```

### PhotoFilter().color_space

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L338)

```python
@property
def color_space():
```

### PhotoFilter().density

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L346)

```python
@property
def density():
```

### PhotoFilter().luminosity

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L350)

```python
@property
def luminosity():
```

### PhotoFilter().xyz

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L330)

```python
@property
def xyz():
```

xyz.

#### Returns

`bool`

## Posterize

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L381)

```python
register(Tag.POSTERIZE)
class Posterize(AdjustmentLayer):
```

Posterize adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### Posterize().posterize

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L384)

```python
@property
def posterize():
```

Posterize value.

#### Returns

`int`

## SelectiveColor

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L407)

```python
register(Tag.SELECTIVE_COLOR)
class SelectiveColor(AdjustmentLayer):
```

Selective color adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### SelectiveColor().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L414)

```python
@property
def data():
```

### SelectiveColor().method

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L410)

```python
@property
def method():
```

## SolidColorFill

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L25)

```python
register(Tag.SOLID_COLOR_SHEET_SETTING)
class SolidColorFill(FillLayer):
```

Solid color fill.

#### See also

- [FillLayer](layers.md#filllayer)

### SolidColorFill().data

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L28)

```python
@property
def data():
```

Color in Descriptor(RGB).

## Threshold

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L394)

```python
register(Tag.THRESHOLD)
class Threshold(AdjustmentLayer):
```

Threshold adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### Threshold().threshold

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L397)

```python
@property
def threshold():
```

Threshold value.

#### Returns

`int`

## Vibrance

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L181)

```python
register(Tag.VIBRANCE)
class Vibrance(AdjustmentLayer):
```

Vibrance adjustment.

#### See also

- [AdjustmentLayer](layers.md#adjustmentlayer)

### Vibrance().saturation

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L192)

```python
@property
def saturation():
```

Saturation.

#### Returns

`int`

### Vibrance().vibrance

[[find in source code]](../../../psdtoolsx/api/adjustments.py#L184)

```python
@property
def vibrance():
```

Vibrance.

#### Returns

`int`
