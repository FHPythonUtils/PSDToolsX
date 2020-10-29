# effects_layer

> Auto-generated documentation for [psdtoolsx.psd.effects_layer](../../../psdtoolsx/psd/effects_layer.py) module.

Effects layer structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / effects_layer
    - [BevelInfo](#bevelinfo)
        - [BevelInfo.read](#bevelinforead)
        - [BevelInfo().write](#bevelinfowrite)
    - [CommonStateInfo](#commonstateinfo)
        - [CommonStateInfo.read](#commonstateinforead)
        - [CommonStateInfo().write](#commonstateinfowrite)
    - [EffectsLayer](#effectslayer)
        - [EffectsLayer.read](#effectslayerread)
        - [EffectsLayer().write](#effectslayerwrite)
    - [InnerGlowInfo](#innerglowinfo)
        - [InnerGlowInfo.read](#innerglowinforead)
        - [InnerGlowInfo().write](#innerglowinfowrite)
    - [OuterGlowInfo](#outerglowinfo)
        - [OuterGlowInfo.read](#outerglowinforead)
        - [OuterGlowInfo().write](#outerglowinfowrite)
    - [ShadowInfo](#shadowinfo)
        - [ShadowInfo.read](#shadowinforead)
        - [ShadowInfo().write](#shadowinfowrite)
    - [SolidFillInfo](#solidfillinfo)
        - [SolidFillInfo.read](#solidfillinforead)
        - [SolidFillInfo().write](#solidfillinfowrite)

Note the structures in this module is obsolete and object-based layer effects
are stored in tagged blocks.

## BevelInfo

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L224)

```python
attr.s(repr=False, slots=True)
class BevelInfo(BaseElement):
```

Effects layer bevel info.

version
angle
depth
blur
highlight_blend_mode
shadow_blend_mode
highlight_color
shadow_color
highlight_opacity
shadow_opacity
enabled
use_global_angle
direction
real_hightlight_color
real_shadow_color

#### See also

- [BaseElement](base.md#baseelement)

### BevelInfo.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L269)

```python
@classmethod
def read(fp):
```

### BevelInfo().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L292)

```python
def write(fp):
```

## CommonStateInfo

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L23)

```python
attr.s(repr=False, slots=True)
class CommonStateInfo(BaseElement):
```

Effects layer common state info.

version
visible

#### See also

- [BaseElement](base.md#baseelement)

### CommonStateInfo.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L33)

```python
@classmethod
def read(fp):
```

### CommonStateInfo().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L37)

```python
def write(fp):
```

## EffectsLayer

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L357)

```python
attr.s(repr=False, slots=True)
class EffectsLayer(DictElement):
```

Dict-like EffectsLayer structure. See
:py:class:[EffectOSType](../constants.md#effectostype) for available keys.

version

#### See also

- [DictElement](base.md#dictelement)

### EffectsLayer.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L376)

```python
@classmethod
def read(fp, **kwargs):
```

### EffectsLayer().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L388)

```python
def write(fp, **kwargs):
```

## InnerGlowInfo

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L173)

```python
attr.s(repr=False, slots=True)
class InnerGlowInfo(BaseElement, _GlowInfo):
```

Effects layer inner glow info.

version
blur
intensity
color
blend_mode
enabled
opacity
invert
native_color

#### See also

- [BaseElement](base.md#baseelement)

### InnerGlowInfo.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L201)

```python
@classmethod
def read(fp):
```

### InnerGlowInfo().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L215)

```python
def write(fp):
```

## OuterGlowInfo

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L126)

```python
attr.s(repr=False, slots=True)
class OuterGlowInfo(BaseElement, _GlowInfo):
```

Effects layer outer glow info.

version
blur
intensity
color
blend_mode
enabled
opacity
native_color

#### See also

- [BaseElement](base.md#baseelement)

### OuterGlowInfo.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L152)

```python
@classmethod
def read(fp):
```

### OuterGlowInfo().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L165)

```python
def write(fp):
```

## ShadowInfo

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L42)

```python
attr.s(repr=False, slots=True)
class ShadowInfo(BaseElement):
```

Effects layer shadow info.

version
blur
intensity
angle
distance
color
blend_mode
enabled
use_global_angle
opacity
native_color

#### See also

- [BaseElement](base.md#baseelement)

### ShadowInfo.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L74)

```python
@classmethod
def read(fp):
```

### ShadowInfo().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L89)

```python
def write(fp):
```

## SolidFillInfo

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L314)

```python
attr.s(repr=False, slots=True)
class SolidFillInfo(BaseElement):
```

Effects layer inner glow info.

version
blend_mode
color
opacity
enabled
native_color

#### See also

- [BaseElement](base.md#baseelement)

### SolidFillInfo.read

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L336)

```python
@classmethod
def read(fp):
```

### SolidFillInfo().write

[[find in source code]](../../../psdtoolsx/psd/effects_layer.py#L346)

```python
def write(fp):
```
