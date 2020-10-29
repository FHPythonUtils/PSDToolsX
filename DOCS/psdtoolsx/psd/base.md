# base

> Auto-generated documentation for [psdtoolsx.psd.base](../../../psdtoolsx/psd/base.py) module.

Base data structures intended for inheritance.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / base
    - [BaseElement](#baseelement)
        - [BaseElement.frombytes](#baseelementfrombytes)
        - [BaseElement.read](#baseelementread)
        - [BaseElement().tobytes](#baseelementtobytes)
        - [BaseElement().validate](#baseelementvalidate)
        - [BaseElement().write](#baseelementwrite)
    - [BooleanElement](#booleanelement)
        - [BooleanElement.read](#booleanelementread)
        - [BooleanElement().write](#booleanelementwrite)
    - [ByteElement](#byteelement)
        - [ByteElement.read](#byteelementread)
        - [ByteElement().write](#byteelementwrite)
    - [DictElement](#dictelement)
        - [DictElement().clear](#dictelementclear)
        - [DictElement().copy](#dictelementcopy)
        - [DictElement.fromkeys](#dictelementfromkeys)
        - [DictElement().get](#dictelementget)
        - [DictElement().items](#dictelementitems)
        - [DictElement().keys](#dictelementkeys)
        - [DictElement().pop](#dictelementpop)
        - [DictElement().popitem](#dictelementpopitem)
        - [DictElement.read](#dictelementread)
        - [DictElement().setdefault](#dictelementsetdefault)
        - [DictElement().update](#dictelementupdate)
        - [DictElement().values](#dictelementvalues)
        - [DictElement().write](#dictelementwrite)
    - [EmptyElement](#emptyelement)
        - [EmptyElement.read](#emptyelementread)
        - [EmptyElement().write](#emptyelementwrite)
    - [IntegerElement](#integerelement)
        - [IntegerElement.read](#integerelementread)
        - [IntegerElement().write](#integerelementwrite)
    - [ListElement](#listelement)
        - [ListElement().append](#listelementappend)
        - [ListElement().count](#listelementcount)
        - [ListElement().extend](#listelementextend)
        - [ListElement().index](#listelementindex)
        - [ListElement().insert](#listelementinsert)
        - [ListElement().pop](#listelementpop)
        - [ListElement().remove](#listelementremove)
        - [ListElement().reverse](#listelementreverse)
        - [ListElement().sort](#listelementsort)
        - [ListElement().write](#listelementwrite)
    - [NumericElement](#numericelement)
        - [NumericElement.read](#numericelementread)
        - [NumericElement().write](#numericelementwrite)
    - [ShortIntegerElement](#shortintegerelement)
        - [ShortIntegerElement.read](#shortintegerelementread)
        - [ShortIntegerElement().write](#shortintegerelementwrite)
    - [StringElement](#stringelement)
        - [StringElement.read](#stringelementread)
        - [StringElement().write](#stringelementwrite)
    - [ValueElement](#valueelement)

All the data objects in this subpackage inherit from the base classes here.
That means, all the data structures in the :py:mod:[psd](index.md#psd) subpackage
implements the methods of :pyclass `psdtoolsx.psd.BaseElement` for
serialization and decoding.

Objects that inherit from the :pyclass `psdtoolsx.psd.BaseElement` typically
gets attrs_ decoration to have data fields.

.. _attrs: https://www.attrs.org/en/stable/index.html

## BaseElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L32)

```python
class BaseElement(object):
```

Base element of various PSD file structs. All the data objects in
:py:mod:[psd](index.md#psd) subpackage inherit from this class.

read(cls, fp)

Read the element from a file-like object.

write(self, fp)

Write the element to a file-like object.

frombytes(self, data, *args, **kwargs)

Read the element from bytes.

tobytes(self, *args, **kwargs)

Write the element to bytes.

validate(self)

Validate the attribute.

### BaseElement.frombytes

[[find in source code]](../../../psdtoolsx/psd/base.py#L65)

```python
@classmethod
def frombytes(data, *args, **kwargs):
```

### BaseElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L58)

```python
@classmethod
def read(fp):
```

### BaseElement().tobytes

[[find in source code]](../../../psdtoolsx/psd/base.py#L70)

```python
def tobytes(*args, **kwargs):
```

### BaseElement().validate

[[find in source code]](../../../psdtoolsx/psd/base.py#L75)

```python
def validate():
```

### BaseElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L62)

```python
def write(fp):
```

## BooleanElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L388)

```python
attr.s(repr=False, eq=False, order=False)
class BooleanElement(IntegerElement):
```

Single bool value element that has a `value` attribute.

Use with `@attr.s(repr=False)` decorator.

#### See also

- [IntegerElement](#integerelement)

### BooleanElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L396)

```python
@classmethod
def read(fp, **kwargs):
```

### BooleanElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L404)

```python
def write(fp, **kwargs):
```

## ByteElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L368)

```python
attr.s(repr=False, eq=False, order=False)
class ByteElement(IntegerElement):
```

Single 1-byte integer element that has a `value` attribute.

Use with `@attr.s(repr=False)` decorator.

#### See also

- [IntegerElement](#integerelement)

### ByteElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L375)

```python
@classmethod
def read(fp, **kwargs):
```

### ByteElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L383)

```python
def write(fp, **kwargs):
```

## DictElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L506)

```python
attr.s(repr=False)
class DictElement(BaseElement):
```

Dict-like element that has `items` OrderedDict.

#### See also

- [BaseElement](#baseelement)

### DictElement().clear

[[find in source code]](../../../psdtoolsx/psd/base.py#L512)

```python
def clear():
```

### DictElement().copy

[[find in source code]](../../../psdtoolsx/psd/base.py#L515)

```python
def copy():
```

### DictElement.fromkeys

[[find in source code]](../../../psdtoolsx/psd/base.py#L518)

```python
@classmethod
def fromkeys(seq, *args):
```

### DictElement().get

[[find in source code]](../../../psdtoolsx/psd/base.py#L522)

```python
def get(key, *args):
```

### DictElement().items

[[find in source code]](../../../psdtoolsx/psd/base.py#L526)

```python
def items():
```

### DictElement().keys

[[find in source code]](../../../psdtoolsx/psd/base.py#L529)

```python
def keys():
```

### DictElement().pop

[[find in source code]](../../../psdtoolsx/psd/base.py#L532)

```python
def pop(key, *args):
```

### DictElement().popitem

[[find in source code]](../../../psdtoolsx/psd/base.py#L536)

```python
def popitem():
```

### DictElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L596)

```python
@classmethod
def read(fp, *args, **kwargs):
```

### DictElement().setdefault

[[find in source code]](../../../psdtoolsx/psd/base.py#L539)

```python
def setdefault(key, *args):
```

### DictElement().update

[[find in source code]](../../../psdtoolsx/psd/base.py#L543)

```python
def update(*args):
```

### DictElement().values

[[find in source code]](../../../psdtoolsx/psd/base.py#L546)

```python
def values():
```

### DictElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L600)

```python
def write(fp, *args, **kwargs):
```

## EmptyElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L129)

```python
attr.s(slots=True)
class EmptyElement(BaseElement):
```

Empty element that does not have a value.

#### See also

- [BaseElement](#baseelement)

### EmptyElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L134)

```python
@classmethod
def read(fp, *args, **kwargs):
```

### EmptyElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L138)

```python
def write(fp, *args, **kwargs):
```

## IntegerElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L286)

```python
attr.s(repr=False, eq=False, order=False)
class IntegerElement(NumericElement):
```

Single integer value element that has a `value` attribute.

Use with `@attr.s(repr=False)` decorator.

#### See also

- [NumericElement](#numericelement)

### IntegerElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L339)

```python
@classmethod
def read(fp, **kwargs):
```

### IntegerElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L343)

```python
def write(fp, **kwargs):
```

## ListElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L428)

```python
attr.s(repr=False)
class ListElement(BaseElement):
```

List-like element that has `items` list.

#### See also

- [BaseElement](#baseelement)

### ListElement().append

[[find in source code]](../../../psdtoolsx/psd/base.py#L434)

```python
def append(x):
```

### ListElement().count

[[find in source code]](../../../psdtoolsx/psd/base.py#L452)

```python
def count(x):
```

### ListElement().extend

[[find in source code]](../../../psdtoolsx/psd/base.py#L437)

```python
def extend(L):
```

### ListElement().index

[[find in source code]](../../../psdtoolsx/psd/base.py#L449)

```python
def index(x):
```

### ListElement().insert

[[find in source code]](../../../psdtoolsx/psd/base.py#L440)

```python
def insert(i, x):
```

### ListElement().pop

[[find in source code]](../../../psdtoolsx/psd/base.py#L446)

```python
def pop(*args):
```

### ListElement().remove

[[find in source code]](../../../psdtoolsx/psd/base.py#L443)

```python
def remove(x):
```

### ListElement().reverse

[[find in source code]](../../../psdtoolsx/psd/base.py#L458)

```python
def reverse():
```

### ListElement().sort

[[find in source code]](../../../psdtoolsx/psd/base.py#L455)

```python
def sort(*args, **kwargs):
```

### ListElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L495)

```python
def write(fp, *args, **kwargs):
```

## NumericElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L211)

```python
attr.s(repr=False, eq=False, order=False)
class NumericElement(ValueElement):
```

Single value element that has a numeric `value` attribute.

#### See also

- [ValueElement](#valueelement)

### NumericElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L277)

```python
@classmethod
def read(fp, **kwargs):
```

### NumericElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L281)

```python
def write(fp, **kwargs):
```

## ShortIntegerElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L348)

```python
attr.s(repr=False, eq=False, order=False)
class ShortIntegerElement(IntegerElement):
```

Single short integer element that has a `value` attribute.

Use with `@attr.s(repr=False)` decorator.

#### See also

- [IntegerElement](#integerelement)

### ShortIntegerElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L355)

```python
@classmethod
def read(fp, **kwargs):
```

### ShortIntegerElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L363)

```python
def write(fp, **kwargs):
```

## StringElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L409)

```python
attr.s(repr=False, slots=True, eq=False, order=False)
class StringElement(ValueElement):
```

Single unicode string.

value

`str` value

#### See also

- [ValueElement](#valueelement)

### StringElement.read

[[find in source code]](../../../psdtoolsx/psd/base.py#L419)

```python
@classmethod
def read(fp, padding=1, **kwargs):
```

### StringElement().write

[[find in source code]](../../../psdtoolsx/psd/base.py#L423)

```python
def write(fp, padding=1, **kwargs):
```

## ValueElement

[[find in source code]](../../../psdtoolsx/psd/base.py#L143)

```python
attr.s(repr=False, eq=False, order=False)
class ValueElement(BaseElement):
```

Single value wrapper that has a `value` attribute.

Pretty printing shows the internal value by default. Inherit with
`@attr.s(repr=False)` decorator to keep this behavior.

value

Internal value.

#### See also

- [BaseElement](#baseelement)
