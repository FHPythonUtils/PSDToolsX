[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/PSDToolsX.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual|gh/FHPythonUtils/PSDToolsX)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/PSDToolsX.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/PSDToolsX.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/PSDToolsX.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/PSDToolsX.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/PSDToolsX.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/psdtoolsx.svg?style=for-the-badge)](https://pypi.org/project/psdtoolsx/)
[![PyPI Version](https://img.shields.io/pypi/v/psdtoolsx.svg?style=for-the-badge)](https://pypi.org/project/psdtoolsx/)

# PSDToolsX

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">



PSDToolsX is a Python package for working with Adobe
Photoshop PSD files as described in
[specification](https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/).

[![PyPI Version](https://img.shields.io/pypi/v/psd-tools.svg)](https://pypi.python.org/pypi/psd-tools)
![Test](https://github.com/psd-tools/psd-tools/workflows/Test/badge.svg)
[![Document Status](https://readthedocs.org/projects/psd-tools/badge/)](http://psd-tools.readthedocs.io/en/latest/)



## Changes from upstream

1. Use poetry
2. find and replace `psd_tools` with `psdtoolsx`


## Installation

Use `pip` to install the package:

    pip install psd-tools

::: {.note}
::: {.title}
Note
:::

In order to extract images from 32bit PSD files PIL/Pillow must be built
with LITTLECMS or LITTLECMS2 support.
:::

## Getting started

```python
from psdtoolsx import PSDImage

psd = PSDImage.open('example.psd')
psd.composite().save('example.png')

for layer in psd:
    print(layer)
    layer_image = layer.composite()
    layer_image.save('%s.png' % layer.name)
```

Check out the [documentation](https://psd-tools.readthedocs.io/) for
features and details.

## Contributing

See
[contributing](https://github.com/psd-tools/psd-tools/blob/master/docs/contributing.rst)
page.
