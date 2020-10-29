# validators

> Auto-generated documentation for [psdtoolsx.validators](../../psdtoolsx/validators.py) module.

Validation functions for attr.

- [Psdtoolsx](../README.md#psdtoolsx-index) / [Modules](../README.md#psdtoolsx-modules) / [psdtoolsx](index.md#psdtoolsx) / validators
    - [range_](#range_)

## range_

[[find in source code]](../../psdtoolsx/validators.py#L30)

```python
def range_(minimum, maximum):
```

A validator that raises a exception `ValueError` if the initializer is called
with a value that does not belong in the [minimum, maximum] range. The
check is performed using ``minimum <= value and value <= maximum``
