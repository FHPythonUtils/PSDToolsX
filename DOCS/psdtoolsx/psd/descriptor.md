# descriptor

> Auto-generated documentation for [psdtoolsx.psd.descriptor](../../../psdtoolsx/psd/descriptor.py) module.

Descriptor data structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / descriptor
    - [Alias](#alias)
    - [Bool](#bool)
        - [Bool.read](#boolread)
        - [Bool().write](#boolwrite)
    - [Class](#class)
        - [Class.read](#classread)
        - [Class().write](#classwrite)
    - [Class1](#class1)
    - [Class2](#class2)
    - [Class3](#class3)
    - [Descriptor](#descriptor)
        - [Descriptor.read](#descriptorread)
        - [Descriptor().write](#descriptorwrite)
    - [DescriptorBlock](#descriptorblock)
        - [DescriptorBlock.read](#descriptorblockread)
        - [DescriptorBlock().write](#descriptorblockwrite)
    - [DescriptorBlock2](#descriptorblock2)
        - [DescriptorBlock2.read](#descriptorblock2read)
        - [DescriptorBlock2().write](#descriptorblock2write)
    - [Double](#double)
        - [Double.read](#doubleread)
        - [Double().write](#doublewrite)
    - [Enumerated](#enumerated)
        - [Enumerated().get_name](#enumeratedget_name)
        - [Enumerated.read](#enumeratedread)
        - [Enumerated().write](#enumeratedwrite)
    - [EnumeratedReference](#enumeratedreference)
        - [EnumeratedReference.read](#enumeratedreferenceread)
        - [EnumeratedReference().write](#enumeratedreferencewrite)
    - [GlobalObject](#globalobject)
    - [Identifier](#identifier)
    - [Index](#index)
    - [Integer](#integer)
        - [Integer.read](#integerread)
        - [Integer().write](#integerwrite)
    - [LargeInteger](#largeinteger)
        - [LargeInteger.read](#largeintegerread)
        - [LargeInteger().write](#largeintegerwrite)
    - [List](#list)
        - [List.read](#listread)
        - [List().write](#listwrite)
    - [Name](#name)
        - [Name.read](#nameread)
        - [Name().write](#namewrite)
    - [ObjectArray](#objectarray)
        - [ObjectArray.read](#objectarrayread)
        - [ObjectArray().write](#objectarraywrite)
    - [Offset](#offset)
        - [Offset.read](#offsetread)
        - [Offset().write](#offsetwrite)
    - [Path](#path)
    - [Property](#property)
        - [Property.read](#propertyread)
        - [Property().write](#propertywrite)
    - [RawData](#rawdata)
        - [RawData.read](#rawdataread)
        - [RawData().write](#rawdatawrite)
    - [Reference](#reference)
    - [String](#string)
    - [UnitFloat](#unitfloat)
        - [UnitFloat.read](#unitfloatread)
        - [UnitFloat().write](#unitfloatwrite)
    - [UnitFloats](#unitfloats)
        - [UnitFloats.read](#unitfloatsread)
        - [UnitFloats().write](#unitfloatswrite)
    - [read_length_and_key](#read_length_and_key)
    - [write_length_and_key](#write_length_and_key)

Descriptors are basic data structure used throughout PSD files. Descriptor is
one kind of serialization protocol for data objects, and
enum classes in :py:mod:[terminology](../terminology.md#terminology) or bytes indicates what kind
of descriptor it is.

The class ID can be pre-defined enum if the tag is 4-byte length or plain
bytes if the length is arbitrary. They depend on the internal version of
Adobe Photoshop but the detail is unknown.

Pretty printing is the best approach to check the descriptor content

```python
from IPython.pretty import pprint
pprint(descriptor)
```

## Alias

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L656)

```python
register(OSType.ALIAS)
class Alias(RawData):
```

Alias structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.RawData`.

#### See also

- [RawData](#rawdata)

## Bool

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L494)

```python
register(OSType.BOOLEAN)
class Bool(BooleanElement):
```

Bool structure.

value

`bool` value

#### See also

- [BooleanElement](base.md#booleanelement)

### Bool.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L503)

```python
@classmethod
def read(fp):
```

### Bool().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L507)

```python
def write(fp):
```

## Class

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L375)

```python
attr.s(repr=False)
class Class(BaseElement):
```

Class structure.

name

`str` value

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

#### See also

- [BaseElement](base.md#baseelement)

### Class.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L390)

```python
@classmethod
def read(fp):
```

### Class().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L396)

```python
def write(fp):
```

## Class1

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L620)

```python
register(OSType.CLASS1)
class Class1(Class):
```

Class structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.Class`.

#### See also

- [Class](#class)

## Class2

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L629)

```python
register(OSType.CLASS2)
class Class2(Class):
```

Class structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.Class`.

#### See also

- [Class](#class)

## Class3

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L638)

```python
register(OSType.CLASS3)
class Class3(Class):
```

Class structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.Class`.

#### See also

- [Class](#class)

## Descriptor

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L136)

```python
register(OSType.DESCRIPTOR)
attr.s(repr=False)
class Descriptor(_DescriptorMixin):
```

Dict-like descriptor structure.

Key values can be 4-character `bytes` in
:pyclass `psdtoolsx.terminology.Key` or arbitrary length `bytes`.
Supports direct access by :pyclass `psdtoolsx.terminology.Key`.

Example

```python
from psdtoolsx.terminology import Key

descriptor[Key.Enabled]

for key in descriptor:
    print(descriptor[key])
```

name

`str`

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

### Descriptor.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L164)

```python
@classmethod
def read(fp):
```

### Descriptor().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L168)

```python
def write(fp):
```

## DescriptorBlock

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L736)

```python
attr.s(repr=False)
class DescriptorBlock(Descriptor):
```

Dict-like Descriptor-based structure that has `version` field. See
:pyclass `psdtoolsx.psd.descriptor.Descriptor`.

version

#### See also

- [Descriptor](#descriptor)

### DescriptorBlock.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L745)

```python
@classmethod
def read(fp, **kwargs):
```

### DescriptorBlock().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L750)

```python
def write(fp, padding=4, **kwargs):
```

## DescriptorBlock2

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L758)

```python
attr.s(repr=False)
class DescriptorBlock2(Descriptor):
```

Dict-like Descriptor-based structure that has `version` and
`data_version` fields. See
:pyclass `psdtoolsx.psd.descriptor.Descriptor`.

version
data_version

#### See also

- [Descriptor](#descriptor)

### DescriptorBlock2.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L770)

```python
@classmethod
def read(fp, **kwargs):
```

### DescriptorBlock2().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L777)

```python
def write(fp, padding=4, **kwargs):
```

## Double

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L357)

```python
register(OSType.DOUBLE)
class Double(NumericElement):
```

Double structure.

value

`float` value

#### See also

- [NumericElement](base.md#numericelement)

### Double.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L366)

```python
@classmethod
def read(fp):
```

### Double().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L370)

```python
def write(fp):
```

## Enumerated

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L549)

```python
register(OSType.ENUMERATED)
attr.s(repr=False)
class Enumerated(BaseElement):
```

Enum structure.

typeID

bytes in :pyclass `psdtoolsx.terminology.Type`

enum

bytes in :pyclass `psdtoolsx.terminology.Enum`

#### See also

- [BaseElement](base.md#baseelement)

### Enumerated().get_name

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L584)

```python
def get_name():
```

Get enum name.

### Enumerated.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L564)

```python
@classmethod
def read(fp):
```

### Enumerated().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L570)

```python
def write(fp):
```

## EnumeratedReference

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L416)

```python
register(OSType.ENUMERATED_REFERENCE)
attr.s(repr=False)
class EnumeratedReference(BaseElement):
```

Enumerated reference structure.

name

`str` value

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

typeID

bytes in :pyclass `psdtoolsx.terminology.Type`

enum

bytes in :pyclass `psdtoolsx.terminology.Enum`

#### See also

- [BaseElement](base.md#baseelement)

### EnumeratedReference.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L441)

```python
@classmethod
def read(fp):
```

### EnumeratedReference().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L449)

```python
def write(fp):
```

## GlobalObject

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L665)

```python
register(OSType.GLOBAL_OBJECT)
class GlobalObject(Descriptor):
```

Global object structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.Descriptor`.

#### See also

- [Descriptor](#descriptor)

## Identifier

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L683)

```python
register(OSType.IDENTIFIER)
class Identifier(Integer):
```

Identifier equivalent to
:pyclass `psdtoolsx.psd.descriptor.Integer`.

#### See also

- [Integer](#integer)

## Index

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L692)

```python
register(OSType.INDEX)
class Index(Integer):
```

Index equivalent to :pyclass `psdtoolsx.psd.descriptor.Integer`.

#### See also

- [Integer](#integer)

## Integer

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L530)

```python
register(OSType.INTEGER)
class Integer(IntegerElement):
```

Integer structure.

value

`int` value

#### See also

- [IntegerElement](base.md#integerelement)

### Integer.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L539)

```python
@classmethod
def read(fp):
```

### Integer().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L543)

```python
def write(fp):
```

## LargeInteger

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L512)

```python
register(OSType.LARGE_INTEGER)
class LargeInteger(IntegerElement):
```

LargeInteger structure.

value

`int` value

#### See also

- [IntegerElement](base.md#integerelement)

### LargeInteger.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L521)

```python
@classmethod
def read(fp):
```

### LargeInteger().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L525)

```python
def write(fp):
```

## List

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L208)

```python
register(OSType.LIST)
attr.s(repr=False)
class List(ListElement):
```

List structure.

Example

```python
for item in list_value:
    print(item)
```

#### See also

- [ListElement](base.md#listelement)

### List.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L218)

```python
@classmethod
def read(fp):
```

### List().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L229)

```python
def write(fp):
```

## Name

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L701)

```python
register(OSType.NAME)
attr.s(repr=False)
class Name(BaseElement):
```

Name structure (Undocumented).

name

str

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

value

str

#### See also

- [BaseElement](base.md#baseelement)

### Name.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L721)

```python
@classmethod
def read(fp):
```

### Name().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L728)

```python
def write(fp):
```

## ObjectArray

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L174)

```python
register(OSType.OBJECT_ARRAY)
attr.s(repr=False)
class ObjectArray(_DescriptorMixin):
```

Object array structure almost equivalent to
:pyclass `psdtoolsx.psd.descriptor.Descriptor`.

items_count

`int` value

name

`str` value

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

### ObjectArray.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L195)

```python
@classmethod
def read(fp):
```

### ObjectArray().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L200)

```python
def write(fp):
```

## Offset

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L459)

```python
register(OSType.OFFSET)
attr.s(repr=False)
class Offset(BaseElement):
```

Offset structure.

name

`str` value

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

value

`int` value

#### See also

- [BaseElement](base.md#baseelement)

### Offset.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L479)

```python
@classmethod
def read(fp):
```

### Offset().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L486)

```python
def write(fp):
```

## Path

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L674)

```python
register(OSType.PATH)
class Path(RawData):
```

Undocumented path structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.RawData`.

#### See also

- [RawData](#rawdata)

## Property

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L239)

```python
register(OSType.PROPERTY)
attr.s(repr=False)
class Property(BaseElement):
```

Property structure.

name

`str` value

classID

bytes in :pyclass `psdtoolsx.terminology.Klass`

keyID

bytes in :pyclass `psdtoolsx.terminology.Key`

#### See also

- [BaseElement](base.md#baseelement)

### Property.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L259)

```python
@classmethod
def read(fp):
```

### Property().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L266)

```python
def write(fp):
```

## RawData

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L596)

```python
register(OSType.RAW_DATA)
attr.s(repr=False)
class RawData(BaseElement):
```

RawData structure.

value

`bytes` value

#### See also

- [BaseElement](base.md#baseelement)

### RawData.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L606)

```python
@classmethod
def read(fp):
```

### RawData().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L610)

```python
def write(fp):
```

## Reference

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L647)

```python
register(OSType.REFERENCE)
class Reference(List):
```

Reference structure equivalent to
:pyclass `psdtoolsx.psd.descriptor.List`.

#### See also

- [List](#list)

## String

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L403)

```python
register(OSType.STRING)
class String(StringElement):
```

String structure.

value

`str` value

#### See also

- [StringElement](base.md#stringelement)

## UnitFloat

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L275)

```python
register(OSType.UNIT_FLOAT)
attr.s(slots=True, repr=False, eq=False, order=False)
class UnitFloat(NumericElement):
```

Unit float structure.

unit

unit of the value in :pyclass `Unit` or :pyclass `Enum`

value

`float` value

#### See also

- [NumericElement](base.md#numericelement)

### UnitFloat.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L290)

```python
@classmethod
def read(fp):
```

### UnitFloat().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L300)

```python
def write(fp):
```

## UnitFloats

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L313)

```python
register(OSType.UNIT_FLOATS)
attr.s(repr=False)
class UnitFloats(BaseElement):
```

Unit floats structure.

unit

unit of the value in :pyclass `Unit` or :pyclass `Enum`

values

List of `float` values

#### See also

- [BaseElement](base.md#baseelement)

### UnitFloats.read

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L328)

```python
@classmethod
def read(fp):
```

### UnitFloats().write

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L339)

```python
def write(fp):
```

## read_length_and_key

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L57)

```python
def read_length_and_key(fp):
```

Helper to read descriptor key.

## write_length_and_key

[[find in source code]](../../../psdtoolsx/psd/descriptor.py#L69)

```python
def write_length_and_key(fp, value):
```

Helper to write descriptor key.
