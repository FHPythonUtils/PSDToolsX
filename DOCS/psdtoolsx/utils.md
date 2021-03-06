# utils

> Auto-generated documentation for [psdtoolsx.utils](../../psdtoolsx/utils.py) module.

Various utility functions for low-level binary processing.

- [Psdtoolsx](../README.md#psdtoolsx-index) / [Modules](../README.md#psdtoolsx-modules) / [psdtoolsx](index.md#psdtoolsx) / utils
    - [be_array_from_bytes](#be_array_from_bytes)
    - [be_array_to_bytes](#be_array_to_bytes)
    - [decode_fixed_point_32bit](#decode_fixed_point_32bit)
    - [fix_byteorder](#fix_byteorder)
    - [is_readable](#is_readable)
    - [new_registry](#new_registry)
    - [pack](#pack)
    - [pad](#pad)
    - [read_be_array](#read_be_array)
    - [read_fmt](#read_fmt)
    - [read_length_block](#read_length_block)
    - [read_padding](#read_padding)
    - [read_pascal_string](#read_pascal_string)
    - [read_unicode_string](#read_unicode_string)
    - [reserve_position](#reserve_position)
    - [trimmed_repr](#trimmed_repr)
    - [unpack](#unpack)
    - [write_be_array](#write_be_array)
    - [write_bytes](#write_bytes)
    - [write_fmt](#write_fmt)
    - [write_length_block](#write_length_block)
    - [write_padding](#write_padding)
    - [write_pascal_string](#write_pascal_string)
    - [write_position](#write_position)
    - [write_unicode_string](#write_unicode_string)

## be_array_from_bytes

[[find in source code]](../../psdtoolsx/utils.py#L255)

```python
def be_array_from_bytes(fmt, data):
```

Reads an array from bytestring with big-endian data.

## be_array_to_bytes

[[find in source code]](../../psdtoolsx/utils.py#L263)

```python
def be_array_to_bytes(arr):
```

Writes an array to bytestring with big-endian data.

## decode_fixed_point_32bit

[[find in source code]](../../psdtoolsx/utils.py#L284)

```python
def decode_fixed_point_32bit(data):
```

Decodes ``data`` as an unsigned 4-byte fixed-point number.

## fix_byteorder

[[find in source code]](../../psdtoolsx/utils.py#L245)

```python
def fix_byteorder(arr):
```

Fixes the byte order of the array (assuming it was read
from a Big Endian data).

## is_readable

[[find in source code]](../../psdtoolsx/utils.py#L166)

```python
def is_readable(fp, size=1):
```

Check if the file-like object is readable.

#### Arguments

- `fp` - file-like object
- `size` - byte size

#### Returns

bool

## new_registry

[[find in source code]](../../psdtoolsx/utils.py#L293)

```python
def new_registry(attribute=None):
```

Returns an empty dict and a @register decorator.

## pack

[[find in source code]](../../psdtoolsx/utils.py#L18)

```python
def pack(fmt, *args):
```

## pad

[[find in source code]](../../psdtoolsx/utils.py#L179)

```python
def pad(number, divisor):
```

## read_be_array

[[find in source code]](../../psdtoolsx/utils.py#L226)

```python
def read_be_array(fmt, count, fp):
```

Reads an array from a file with big-endian data.

## read_fmt

[[find in source code]](../../psdtoolsx/utils.py#L28)

```python
def read_fmt(fmt, fp):
```

Reads data from ``fp`` according to ``fmt``.

## read_length_block

[[find in source code]](../../psdtoolsx/utils.py#L69)

```python
def read_length_block(fp, fmt='I', padding=1):
```

Read a block of data with a length marker at the beginning.

#### Arguments

- `fp` - file-like
- `fmt` - format of the length marker

#### Returns

bytes object

## read_padding

[[find in source code]](../../psdtoolsx/utils.py#L138)

```python
def read_padding(fp, size, divisor=2):
```

Read padding bytes for the given byte size.

#### Arguments

- `fp` - file-like object
- `divisor` - divisor of the byte alignment

#### Returns

read byte size

## read_pascal_string

[[find in source code]](../../psdtoolsx/utils.py#L185)

```python
def read_pascal_string(fp, encoding='macroman', padding=2):
```

Reads pascal string (length + bytes).

#### Arguments

- `fp` - file-like object
- `encoding` - string encoding
- `padding` - padding size

#### Returns

str

## read_unicode_string

[[find in source code]](../../psdtoolsx/utils.py#L211)

```python
def read_unicode_string(fp, padding=1):
```

## reserve_position

[[find in source code]](../../psdtoolsx/utils.py#L106)

```python
def reserve_position(fp, fmt='I'):
```

Reserves the current position for write.

Use with [write_position](#write_position).

#### Arguments

- `fp` - file-like object
- `fmt` - format of the reserved position

#### Returns

the position

## trimmed_repr

[[find in source code]](../../psdtoolsx/utils.py#L274)

```python
def trimmed_repr(data, trim_length=16):
```

## unpack

[[find in source code]](../../psdtoolsx/utils.py#L23)

```python
def unpack(fmt, data):
```

## write_be_array

[[find in source code]](../../psdtoolsx/utils.py#L238)

```python
def write_be_array(fp, arr):
```

Writes an array to a file with big-endian data.

## write_bytes

[[find in source code]](../../psdtoolsx/utils.py#L55)

```python
def write_bytes(fp, data):
```

Write bytes to the file object and returns bytes written.

#### Returns

written byte size

## write_fmt

[[find in source code]](../../psdtoolsx/utils.py#L44)

```python
def write_fmt(fp, fmt, *args):
```

Writes data to ``fp`` according to ``fmt``.

## write_length_block

[[find in source code]](../../psdtoolsx/utils.py#L84)

```python
def write_length_block(fp, writer, fmt='I', padding=1, **kwargs):
```

Writes a block of data with a length marker at the beginning.

Example

```python
with io.BytesIO() as fp:
    write_length_block(fp, lambda f: f.write(b'  '))
```

#### Arguments

- `fp` - file-like
- `writer` - function object that takes file-like object as an argument
- `fmt` - format of the length marker
- `padding` - divisor for padding not included in length marker

#### Returns

written byte size

## write_padding

[[find in source code]](../../psdtoolsx/utils.py#L152)

```python
def write_padding(fp, size, divisor=2):
```

Writes padding bytes given the currently written size.

#### Arguments

- `fp` - file-like object
- `divisor` - divisor of the byte alignment

#### Returns

written byte size

## write_pascal_string

[[find in source code]](../../psdtoolsx/utils.py#L203)

```python
def write_pascal_string(fp, value, encoding='macroman', padding=2):
```

## write_position

[[find in source code]](../../psdtoolsx/utils.py#L121)

```python
def write_position(fp, position, value, fmt='I'):
```

Writes a value to the specified position.

#### Arguments

- `fp` - file-like object
- `position` - position of the value marker
- `value` - value to write
- `fmt` - format of the value

#### Returns

written byte size

## write_unicode_string

[[find in source code]](../../psdtoolsx/utils.py#L218)

```python
def write_unicode_string(fp, value, padding=1):
```
