# color

> Auto-generated documentation for [psdtoolsx.psd.color](../../../psdtoolsx/psd/color.py) module.

Color structure and conversion methods.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [psd](index.md#psd) / color
    - [Color](#color)
        - [Color.read](#colorread)
        - [Color().write](#colorwrite)

## Color

[[find in source code]](../../../psdtoolsx/psd/color.py#L16)

```python
attr.s(repr=False, slots=True)
class Color(BaseElement):
```

Color structure.

id

See :pyclass `psdtoolsx.constants.ColorSpaceID`.

values

List of `int` values.

#### See also

- [BaseElement](base.md#baseelement)

### Color.read

[[find in source code]](../../../psdtoolsx/psd/color.py#L31)

```python
@classmethod
def read(fp, **kwargs):
```

### Color().write

[[find in source code]](../../../psdtoolsx/psd/color.py#L44)

```python
def write(fp, **kwargs):
```
