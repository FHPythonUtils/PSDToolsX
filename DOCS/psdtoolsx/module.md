# \_\_main\_\_

> Auto-generated documentation for [psdtoolsx.__main__](../../psdtoolsx/__main__.py) module.

- [Psdtoolsx](../README.md#psdtoolsx-index) / [Modules](../README.md#psdtoolsx-modules) / [psdtoolsx](index.md#psdtoolsx) / \_\_main\_\_
    - [main](#main)

## main

[[find in source code]](../../psdtoolsx/__main__.py#L17)

```python
def main(argv=None):
```

psd-tools command line utility.

Usage:
    psd-tools export <input_file> <output_file> [options]
    psd-tools show <input_file> [options]
    psd-tools debug <input_file> [options]
    psd-tools -h | --help
    psd-tools --version

Options:
    -v --verbose                Be more verbose.

#### Examples

psd-tools show example.psd  # Show the file content
psd-tools export example.psd example.png  # Export as PNG
psd-tools export example.psd[0] example-0.png  # Export layer as PNG
