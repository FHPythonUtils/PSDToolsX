# engine_data

> Auto-generated documentation for [psdtoolsx.psd.engine_data](../../../psdtoolsx/psd/engine_data.py) module.

EngineData structure.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / engine_data
    - [Bool](#bool)
        - [Bool.frombytes](#boolfrombytes)
        - [Bool.read](#boolread)
        - [Bool().write](#boolwrite)
    - [Dict](#dict)
        - [Dict.frombytes](#dictfrombytes)
        - [Dict().get](#dictget)
        - [Dict.read](#dictread)
        - [Dict().write](#dictwrite)
    - [EngineData](#enginedata)
    - [EngineData2](#enginedata2)
        - [EngineData2().write](#enginedata2write)
    - [EngineToken](#enginetoken)
    - [Float](#float)
        - [Float.frombytes](#floatfrombytes)
        - [Float.read](#floatread)
        - [Float().write](#floatwrite)
    - [Integer](#integer)
        - [Integer.frombytes](#integerfrombytes)
        - [Integer.read](#integerread)
        - [Integer().write](#integerwrite)
    - [List](#list)
        - [List.frombytes](#listfrombytes)
        - [List.read](#listread)
        - [List().write](#listwrite)
    - [Property](#property)
        - [Property.frombytes](#propertyfrombytes)
        - [Property.read](#propertyread)
        - [Property().write](#propertywrite)
    - [String](#string)
        - [String.frombytes](#stringfrombytes)
        - [String.read](#stringread)
        - [String().write](#stringwrite)
    - [Tag](#tag)
        - [Tag.read](#tagread)
        - [Tag().write](#tagwrite)
    - [Tokenizer](#tokenizer)
        - [Tokenizer().next](#tokenizernext)
    - [compile_re](#compile_re)

PSD file embeds text formatting data in its own markup language referred
EngineData. The format looks like the following

```python
<<
  /EngineDict
  <<
    /Editor
    <<
      /Text (Ë›Ë‡Make a change and save.)
    >>
  >>
  /Font
  <<
    /Name (Ë›Ë‡HelveticaNeue-Light)
    /FillColor
    <<
      /Type 1
      /Values [ 1.0 0.0 0.0 0.0 ]
    >>
    /StyleSheetSet [
    <<
      /Name (Ë›Ë‡Normal RGB)
    >>
    ]
  >>
>>
```

## Bool

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L326)

```python
register(EngineToken.BOOLEAN)
class Bool(BooleanElement):
```

Bool element.

#### See also

- [BooleanElement](base.md#booleanelement)

### Bool.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L335)

```python
@classmethod
def frombytes(data):
```

### Bool.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L331)

```python
@classmethod
def read(fp):
```

### Bool().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L339)

```python
def write(fp, indent=0):
```

## Dict

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L126)

```python
register(EngineToken.DICT_START)
class Dict(DictElement):
```

Dict-like element.

#### See also

- [DictElement](base.md#dictelement)

### Dict.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L135)

```python
@classmethod
def frombytes(data, **kwargs):
```

### Dict().get

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L216)

```python
def get(key, *args):
```

### Dict.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L131)

```python
@classmethod
def read(fp, **kwargs):
```

### Dict().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L157)

```python
def write(fp, indent=0, write_container=True):
```

## EngineData

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L221)

```python
class EngineData(Dict):
```

Dict-like element.

TYPE_TOOL_OBJECT_SETTING tagged block contains this object in its
descriptor.

#### See also

- [Dict](#dict)

## EngineData2

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L231)

```python
class EngineData2(Dict):
```

Dict-like element.

TEXT_ENGINE_DATA tagged block has this object.

#### See also

- [Dict](#dict)

### EngineData2().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L238)

```python
def write(fp, indent=None, write_container=False, **kwargs):
```

## EngineToken

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L53)

```python
class EngineToken(Enum):
```

#### Attributes

- `UNKNOWN_TAG` - Unknown tags: b'(hwid)', b'(fwid)', b'(aalt)': `compile_re('^\\([a-zA-Z0-9]*\\)$')`

## Float

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L362)

```python
register(EngineToken.NUMBER_WITH_DECIMAL)
class Float(NumericElement):
```

Float element.

#### See also

- [NumericElement](base.md#numericelement)

### Float.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L371)

```python
@classmethod
def frombytes(data):
```

### Float.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L367)

```python
@classmethod
def read(fp):
```

### Float().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L375)

```python
def write(fp):
```

## Integer

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L344)

```python
register(EngineToken.NUMBER)
class Integer(IntegerElement):
```

Integer element.

#### See also

- [IntegerElement](base.md#integerelement)

### Integer.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L353)

```python
@classmethod
def frombytes(data):
```

### Integer.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L349)

```python
@classmethod
def read(fp):
```

### Integer().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L357)

```python
def write(fp, indent=0):
```

## List

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L245)

```python
register(EngineToken.ARRAY_START)
class List(ListElement):
```

List-like element.

#### See also

- [ListElement](base.md#listelement)

### List.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L254)

```python
@classmethod
def frombytes(data):
```

### List.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L250)

```python
@classmethod
def read(fp):
```

### List().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L271)

```python
def write(fp, indent=None):
```

## Property

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L386)

```python
register(EngineToken.PROPERTY)
attr.s(repr=False, frozen=True, eq=False, order=False)
class Property(ValueElement):
```

Property element.

#### See also

- [ValueElement](base.md#valueelement)

### Property.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L395)

```python
@classmethod
def frombytes(data):
```

### Property.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L391)

```python
@classmethod
def read(fp):
```

### Property().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L399)

```python
def write(fp):
```

## String

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L301)

```python
register(EngineToken.STRING)
class String(ValueElement):
```

String element.

#### See also

- [ValueElement](base.md#valueelement)

### String.frombytes

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L311)

```python
@classmethod
def frombytes(data):
```

### String.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L307)

```python
@classmethod
def read(fp):
```

### String().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L318)

```python
def write(fp):
```

## Tag

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L405)

```python
register(EngineToken.UNKNOWN_TAG)
register(EngineToken.UNKNOWN_TAG2)
class Tag(ValueElement):
```

Tag element.

#### See also

- [ValueElement](base.md#valueelement)

### Tag.read

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L410)

```python
@classmethod
def read(fp):
```

### Tag().write

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L414)

```python
def write(fp):
```

## Tokenizer

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L69)

```python
class Tokenizer(object):
    def __init__(data):
```

Tokenize engine data.

Example

```python
tokenizer = Tokenizer(data)
for token, token_type in tokenizer:
    print('%s: %r' % (token_type.name, token))
```

### Tokenizer().next

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L93)

```python
def next():
```

## compile_re

[[find in source code]](../../../psdtoolsx/psd/engine_data.py#L49)

```python
def compile_re(pattern):
```
