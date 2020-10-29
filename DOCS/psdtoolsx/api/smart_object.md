# smart_object

> Auto-generated documentation for [psdtoolsx.api.smart_object](../../../psdtoolsx/api/smart_object.py) module.

Smart object module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / smart_object
    - [SmartObject](#smartobject)
        - [SmartObject().data](#smartobjectdata)
        - [SmartObject().filename](#smartobjectfilename)
        - [SmartObject().filesize](#smartobjectfilesize)
        - [SmartObject().filetype](#smartobjectfiletype)
        - [SmartObject().is_psd](#smartobjectis_psd)
        - [SmartObject().kind](#smartobjectkind)
        - [SmartObject().open](#smartobjectopen)
        - [SmartObject().resolution](#smartobjectresolution)
        - [SmartObject().save](#smartobjectsave)
        - [SmartObject().unique_id](#smartobjectunique_id)
        - [SmartObject().warp](#smartobjectwarp)

## SmartObject

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L15)

```python
class SmartObject(object):
    def __init__(layer):
```

Smart object that represents embedded or external file.

Smart objects are attached to
:pyclass `psdtoolsx.api.layers.SmartObjectLayer`.

### SmartObject().data

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L84)

```python
@property
def data():
```

Embedded file content, or empty if kind is `external` or `alias`

### SmartObject().filename

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L51)

```python
@property
def filename():
```

Original file name of the object.

### SmartObject().filesize

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L98)

```python
@property
def filesize():
```

File size of the object.

### SmartObject().filetype

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L105)

```python
@property
def filetype():
```

Preferred file extension, such as `jpg`.

### SmartObject().is_psd

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L110)

```python
def is_psd():
```

Return True if the file is embedded PSD/PSB.

### SmartObject().kind

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L46)

```python
@property
def kind():
```

Kind of the link, 'data', 'alias', or 'external'.

### SmartObject().open

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L56)

```python
@contextlib.contextmanager
def open(external_dir=None):
```

Open the smart object as binary IO.

#### Arguments

- `external_dir` - Path to the directory of the external file.

Example

```python
with layer.smart_object.open() as f:
    data = f.read()
```

### SmartObject().resolution

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L119)

```python
@property
def resolution():
```

Resolution of the object.

### SmartObject().save

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L124)

```python
def save(filename=None):
```

Save the smart object to a file.

#### Arguments

- `filename` - File name to export. If None, use the embedded name.

### SmartObject().unique_id

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L93)

```python
@property
def unique_id():
```

UUID of the object.

### SmartObject().warp

[[find in source code]](../../../psdtoolsx/api/smart_object.py#L114)

```python
@property
def warp():
```

Warp parameters.
