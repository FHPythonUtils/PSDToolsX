# filter_effects

> Auto-generated documentation for [psdtoolsx.psd.filter_effects](../../../psdtoolsx/psd/filter_effects.py) module.

Filter effects structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / filter_effects
    - [FilterEffect](#filtereffect)
        - [FilterEffect.read](#filtereffectread)
        - [FilterEffect().write](#filtereffectwrite)
    - [FilterEffectChannel](#filtereffectchannel)
        - [FilterEffectChannel.read](#filtereffectchannelread)
        - [FilterEffectChannel().write](#filtereffectchannelwrite)
    - [FilterEffectExtra](#filtereffectextra)
        - [FilterEffectExtra.read](#filtereffectextraread)
        - [FilterEffectExtra().write](#filtereffectextrawrite)
    - [FilterEffects](#filtereffects)
        - [FilterEffects.read](#filtereffectsread)
        - [FilterEffects().write](#filtereffectswrite)

## FilterEffect

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L53)

```python
attr.s(repr=False, slots=True)
class FilterEffect(BaseElement):
```

FilterEffect structure.

uuid
version
rectangle
depth
max_channels
channels

List of :py:class:[FilterEffectChannel](#filtereffectchannel).

extra

See :py:class:[FilterEffectExtra](#filtereffectextra).

#### See also

- [BaseElement](base.md#baseelement)

### FilterEffect.read

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L78)

```python
@classmethod
def read(fp, **kwargs):
```

### FilterEffect().write

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L100)

```python
def write(fp, **kwargs):
```

## FilterEffectChannel

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L124)

```python
attr.s(repr=False, slots=True)
class FilterEffectChannel(BaseElement):
```

FilterEffectChannel structure.

is_written
compression
data

#### See also

- [BaseElement](base.md#baseelement)

### FilterEffectChannel.read

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L136)

```python
@classmethod
def read(fp, **kwargs):
```

### FilterEffectChannel().write

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L149)

```python
def write(fp, **kwargs):
```

## FilterEffectExtra

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L166)

```python
attr.s(repr=False, slots=True)
class FilterEffectExtra(BaseElement):
```

FilterEffectExtra structure.

is_written
rectangle
compression
data

#### See also

- [BaseElement](base.md#baseelement)

### FilterEffectExtra.read

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L180)

```python
@classmethod
def read(fp):
```

### FilterEffectExtra().write

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L195)

```python
def write(fp):
```

## FilterEffects

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L25)

```python
attr.s(repr=False, slots=True)
class FilterEffects(ListElement):
```

List-like FilterEffects structure. See :py:class:[FilterEffect](#filtereffect).

version

#### See also

- [ListElement](base.md#listelement)

### FilterEffects.read

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L33)

```python
@classmethod
def read(fp, **kwargs):
```

### FilterEffects().write

[[find in source code]](../../../psdtoolsx/psd/filter_effects.py#L43)

```python
def write(fp, **kwargs):
```
