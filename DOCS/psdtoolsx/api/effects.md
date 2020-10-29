# effects

> Auto-generated documentation for [psdtoolsx.api.effects](../../../psdtoolsx/api/effects.py) module.

Effects module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / effects
    - [BevelEmboss](#bevelemboss)
        - [BevelEmboss().altitude](#bevelembossaltitude)
        - [BevelEmboss().anti_aliased](#bevelembossanti_aliased)
        - [BevelEmboss().bevel_style](#bevelembossbevel_style)
        - [BevelEmboss().bevel_type](#bevelembossbevel_type)
        - [BevelEmboss().contour](#bevelembosscontour)
        - [BevelEmboss().depth](#bevelembossdepth)
        - [BevelEmboss().direction](#bevelembossdirection)
        - [BevelEmboss().highlight_color](#bevelembosshighlight_color)
        - [BevelEmboss().highlight_mode](#bevelembosshighlight_mode)
        - [BevelEmboss().highlight_opacity](#bevelembosshighlight_opacity)
        - [BevelEmboss().shadow_color](#bevelembossshadow_color)
        - [BevelEmboss().shadow_mode](#bevelembossshadow_mode)
        - [BevelEmboss().shadow_opacity](#bevelembossshadow_opacity)
        - [BevelEmboss().size](#bevelembosssize)
        - [BevelEmboss().soften](#bevelembosssoften)
        - [BevelEmboss().use_shape](#bevelembossuse_shape)
        - [BevelEmboss().use_texture](#bevelembossuse_texture)
    - [ColorOverlay](#coloroverlay)
    - [DropShadow](#dropshadow)
        - [DropShadow().layer_knocks_out](#dropshadowlayer_knocks_out)
    - [Effects](#effects)
        - [Effects().enabled](#effectsenabled)
        - [Effects().find](#effectsfind)
        - [Effects().items](#effectsitems)
        - [Effects().scale](#effectsscale)
    - [GradientOverlay](#gradientoverlay)
        - [GradientOverlay().angle](#gradientoverlayangle)
        - [GradientOverlay().dithered](#gradientoverlaydithered)
        - [GradientOverlay().offset](#gradientoverlayoffset)
        - [GradientOverlay().reversed](#gradientoverlayreversed)
        - [GradientOverlay().type](#gradientoverlaytype)
    - [InnerGlow](#innerglow)
        - [InnerGlow().glow_source](#innerglowglow_source)
    - [InnerShadow](#innershadow)
    - [OuterGlow](#outerglow)
        - [OuterGlow().spread](#outerglowspread)
    - [PatternOverlay](#patternoverlay)
        - [PatternOverlay().phase](#patternoverlayphase)
    - [Satin](#satin)
        - [Satin().angle](#satinangle)
        - [Satin().anti_aliased](#satinanti_aliased)
        - [Satin().contour](#satincontour)
        - [Satin().distance](#satindistance)
        - [Satin().inverted](#satininverted)
        - [Satin().size](#satinsize)
    - [Stroke](#stroke)
        - [Stroke().fill_type](#strokefill_type)
        - [Stroke().overprint](#strokeoverprint)
        - [Stroke().position](#strokeposition)
        - [Stroke().size](#strokesize)

## BevelEmboss

[[find in source code]](../../../psdtoolsx/api/effects.py#L347)

```python
register(Klass.BevelEmboss.value)
class BevelEmboss(_Effect, _AngleMixin):
```

### BevelEmboss().altitude

[[find in source code]](../../../psdtoolsx/api/effects.py#L391)

```python
@property
def altitude():
```

Altitude value.

### BevelEmboss().anti_aliased

[[find in source code]](../../../psdtoolsx/api/effects.py#L416)

```python
@property
def anti_aliased():
```

Anti-aliased.

### BevelEmboss().bevel_style

[[find in source code]](../../../psdtoolsx/api/effects.py#L383)

```python
@property
def bevel_style():
```

Bevel style, one of `OuterBevel`, `InnerBevel`, `Emboss`,
`PillowEmboss`, or `StrokeEmboss`.

### BevelEmboss().bevel_type

[[find in source code]](../../../psdtoolsx/api/effects.py#L378)

```python
@property
def bevel_type():
```

Bevel type, one of `SoftMatte`, `HardLight`, `SoftLight`.

### BevelEmboss().contour

[[find in source code]](../../../psdtoolsx/api/effects.py#L411)

```python
@property
def contour():
```

Contour configuration.

### BevelEmboss().depth

[[find in source code]](../../../psdtoolsx/api/effects.py#L396)

```python
@property
def depth():
```

Depth value.

### BevelEmboss().direction

[[find in source code]](../../../psdtoolsx/api/effects.py#L406)

```python
@property
def direction():
```

Direction, either `StampIn` or `StampOut`.

### BevelEmboss().highlight_color

[[find in source code]](../../../psdtoolsx/api/effects.py#L353)

```python
@property
def highlight_color():
```

Highlight color value.

### BevelEmboss().highlight_mode

[[find in source code]](../../../psdtoolsx/api/effects.py#L348)

```python
@property
def highlight_mode():
```

Highlight blending mode.

### BevelEmboss().highlight_opacity

[[find in source code]](../../../psdtoolsx/api/effects.py#L358)

```python
@property
def highlight_opacity():
```

Highlight opacity value.

### BevelEmboss().shadow_color

[[find in source code]](../../../psdtoolsx/api/effects.py#L368)

```python
@property
def shadow_color():
```

Shadow color value.

### BevelEmboss().shadow_mode

[[find in source code]](../../../psdtoolsx/api/effects.py#L363)

```python
@property
def shadow_mode():
```

Shadow blending mode.

### BevelEmboss().shadow_opacity

[[find in source code]](../../../psdtoolsx/api/effects.py#L373)

```python
@property
def shadow_opacity():
```

Shadow opacity value.

### BevelEmboss().size

[[find in source code]](../../../psdtoolsx/api/effects.py#L401)

```python
@property
def size():
```

Size value in pixel.

### BevelEmboss().soften

[[find in source code]](../../../psdtoolsx/api/effects.py#L421)

```python
@property
def soften():
```

Soften value.

### BevelEmboss().use_shape

[[find in source code]](../../../psdtoolsx/api/effects.py#L426)

```python
@property
def use_shape():
```

Using shape.

### BevelEmboss().use_texture

[[find in source code]](../../../psdtoolsx/api/effects.py#L431)

```python
@property
def use_texture():
```

Using texture.

## ColorOverlay

[[find in source code]](../../../psdtoolsx/api/effects.py#L278)

```python
register(Klass.SolidFill.value)
class ColorOverlay(_OverlayEffect, _ColorMixin):
```

## DropShadow

[[find in source code]](../../../psdtoolsx/api/effects.py#L250)

```python
register(Klass.DropShadow.value)
class DropShadow(_ShadowEffect):
```

### DropShadow().layer_knocks_out

[[find in source code]](../../../psdtoolsx/api/effects.py#L251)

```python
@property
def layer_knocks_out():
```

Layers are knocking out.

## Effects

[[find in source code]](../../../psdtoolsx/api/effects.py#L17)

```python
class Effects(object):
    def __init__(layer):
```

List-like effects.

### Effects().enabled

[[find in source code]](../../../psdtoolsx/api/effects.py#L52)

```python
@property
def enabled():
```

Whether if all the effects are enabled.

#### Returns

Type: *bool*

### Effects().find

[[find in source code]](../../../psdtoolsx/api/effects.py#L64)

```python
def find(name):
```

Iterate effect items by name.

### Effects().items

[[find in source code]](../../../psdtoolsx/api/effects.py#L60)

```python
@property
def items():
```

### Effects().scale

[[find in source code]](../../../psdtoolsx/api/effects.py#L47)

```python
@property
def scale():
```

Scale value.

## GradientOverlay

[[find in source code]](../../../psdtoolsx/api/effects.py#L283)

```python
register(b'GrFl')
class GradientOverlay(_OverlayEffect, _AlignScaleMixin, _GradientMixin):
```

### GradientOverlay().angle

[[find in source code]](../../../psdtoolsx/api/effects.py#L284)

```python
@property
def angle():
```

Angle value.

### GradientOverlay().dithered

[[find in source code]](../../../psdtoolsx/api/effects.py#L302)

```python
@property
def dithered():
```

Dither flag.

### GradientOverlay().offset

[[find in source code]](../../../psdtoolsx/api/effects.py#L307)

```python
@property
def offset():
```

Offset value.

### GradientOverlay().reversed

[[find in source code]](../../../psdtoolsx/api/effects.py#L297)

```python
@property
def reversed():
```

Reverse flag.

### GradientOverlay().type

[[find in source code]](../../../psdtoolsx/api/effects.py#L289)

```python
@property
def type():
```

Gradient type, one of `linear`, `radial`, [GradientOverlay().angle](#gradientoverlayangle), `reflected`, or
`diamond`.

## InnerGlow

[[find in source code]](../../../psdtoolsx/api/effects.py#L270)

```python
register(Klass.InnerGlow.value)
class InnerGlow(_GlowEffect):
```

### InnerGlow().glow_source

[[find in source code]](../../../psdtoolsx/api/effects.py#L271)

```python
@property
def glow_source():
```

Elements source.

## InnerShadow

[[find in source code]](../../../psdtoolsx/api/effects.py#L258)

```python
register(Klass.InnerShadow.value)
class InnerShadow(_ShadowEffect):
```

## OuterGlow

[[find in source code]](../../../psdtoolsx/api/effects.py#L263)

```python
register(Klass.OuterGlow.value)
class OuterGlow(_GlowEffect):
```

### OuterGlow().spread

[[find in source code]](../../../psdtoolsx/api/effects.py#L264)

```python
@property
def spread():
```

## PatternOverlay

[[find in source code]](../../../psdtoolsx/api/effects.py#L314)

```python
register(b'patternFill')
class PatternOverlay(_OverlayEffect, _AlignScaleMixin, _PatternMixin):
```

### PatternOverlay().phase

[[find in source code]](../../../psdtoolsx/api/effects.py#L315)

```python
@property
def phase():
```

Phase value in Point.

## Satin

[[find in source code]](../../../psdtoolsx/api/effects.py#L438)

```python
register(Klass.ChromeFX.value)
class Satin(_Effect, _ColorMixin):
```

Satin effect

### Satin().angle

[[find in source code]](../../../psdtoolsx/api/effects.py#L451)

```python
@property
def angle():
```

Angle value.

### Satin().anti_aliased

[[find in source code]](../../../psdtoolsx/api/effects.py#L441)

```python
@property
def anti_aliased():
```

Anti-aliased.

### Satin().contour

[[find in source code]](../../../psdtoolsx/api/effects.py#L466)

```python
@property
def contour():
```

Contour configuration.

### Satin().distance

[[find in source code]](../../../psdtoolsx/api/effects.py#L456)

```python
@property
def distance():
```

Distance value.

### Satin().inverted

[[find in source code]](../../../psdtoolsx/api/effects.py#L446)

```python
@property
def inverted():
```

Inverted.

### Satin().size

[[find in source code]](../../../psdtoolsx/api/effects.py#L461)

```python
@property
def size():
```

Size value in pixel.

## Stroke

[[find in source code]](../../../psdtoolsx/api/effects.py#L322)

```python
register(Klass.FrameFX.value)
class Stroke(_Effect, _ColorMixin, _PatternMixin, _GradientMixin):
```

### Stroke().fill_type

[[find in source code]](../../../psdtoolsx/api/effects.py#L330)

```python
@property
def fill_type():
```

Fill type, SolidColor, Gradient, or Pattern.

### Stroke().overprint

[[find in source code]](../../../psdtoolsx/api/effects.py#L340)

```python
@property
def overprint():
```

Overprint flag.

### Stroke().position

[[find in source code]](../../../psdtoolsx/api/effects.py#L323)

```python
@property
def position():
```

Position of the stroke, InsetFrame, OutsetFrame, or CenteredFrame.

### Stroke().size

[[find in source code]](../../../psdtoolsx/api/effects.py#L335)

```python
@property
def size():
```

Size value.
