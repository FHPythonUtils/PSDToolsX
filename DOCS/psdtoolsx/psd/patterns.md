# patterns

> Auto-generated documentation for [psdtoolsx.psd.patterns](../../../psdtoolsx/psd/patterns.py) module.

Patterns structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / patterns
    - [Pattern](#pattern)
        - [Pattern.read](#patternread)
        - [Pattern().write](#patternwrite)
    - [Patterns](#patterns)
        - [Patterns.read](#patternsread)
        - [Patterns().write](#patternswrite)
    - [VirtualMemoryArray](#virtualmemoryarray)
        - [VirtualMemoryArray().get_data](#virtualmemoryarrayget_data)
        - [VirtualMemoryArray.read](#virtualmemoryarrayread)
        - [VirtualMemoryArray().set_data](#virtualmemoryarrayset_data)
        - [VirtualMemoryArray().write](#virtualmemoryarraywrite)
    - [VirtualMemoryArrayList](#virtualmemoryarraylist)
        - [VirtualMemoryArrayList.read](#virtualmemoryarraylistread)
        - [VirtualMemoryArrayList().write](#virtualmemoryarraylistwrite)

## Pattern

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L54)

```python
attr.s(repr=False, slots=True)
class Pattern(BaseElement):
```

Pattern structure.

version
image_mode

See :pyclass `ColorMode`

point

Size in tuple.

name

`str` name of the pattern.

pattern_id

ID of this pattern.

color_table

Color table if the mode is INDEXED.

data

See :py:class:[VirtualMemoryArrayList](#virtualmemoryarraylist)

#### See also

- [BaseElement](base.md#baseelement)

### Pattern.read

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L93)

```python
@classmethod
def read(fp, **kwargs):
```

### Pattern().write

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L111)

```python
def write(fp, **kwargs):
```

## Patterns

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L29)

```python
class Patterns(ListElement):
```

List of Pattern structure. See
:pyclass `psdtoolsx.psd.patterns.Pattern`.

#### See also

- [ListElement](base.md#listelement)

### Patterns.read

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L35)

```python
@classmethod
def read(fp, **kwargs):
```

### Patterns().write

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L44)

```python
def write(fp, **kwargs):
```

## VirtualMemoryArray

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L172)

```python
attr.s(repr=False, slots=True)
class VirtualMemoryArray(BaseElement):
```

VirtualMemoryArrayList structure, corresponding to each channel.

is_written
depth
rectangle
pixel_depth
compression
data

#### See also

- [BaseElement](base.md#baseelement)

### VirtualMemoryArray().get_data

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L229)

```python
def get_data():
```

Get decompressed bytes.

### VirtualMemoryArray.read

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L194)

```python
@classmethod
def read(fp, **kwargs):
```

### VirtualMemoryArray().set_data

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L238)

```python
def set_data(size, data, depth, compression=0):
```

Set bytes.

### VirtualMemoryArray().write

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L210)

```python
def write(fp, **kwargs):
```

## VirtualMemoryArrayList

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L127)

```python
attr.s(repr=False, slots=True)
class VirtualMemoryArrayList(BaseElement):
```

VirtualMemoryArrayList structure. Container of channels.

version
rectangle

Tuple of `int`

channels

List of :py:class:[VirtualMemoryArray](#virtualmemoryarray)

#### See also

- [BaseElement](base.md#baseelement)

### VirtualMemoryArrayList.read

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L144)

```python
@classmethod
def read(fp, **kwargs):
```

### VirtualMemoryArrayList().write

[[find in source code]](../../../psdtoolsx/psd/patterns.py#L159)

```python
def write(fp, **kwargs):
```
