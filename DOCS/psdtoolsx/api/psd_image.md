# psd_image

> Auto-generated documentation for [psdtoolsx.api.psd_image](../../../psdtoolsx/api/psd_image.py) module.

PSD Image module.

- [Psdtoolsx](../../README.md#psdtoolsx-index) / [Modules](../../README.md#psdtoolsx-modules) / [psdtoolsx](../index.md#psdtoolsx) / [api](index.md#api) / psd_image
    - [PSDImage](#psdimage)
        - [PSDImage().bbox](#psdimagebbox)
        - [PSDImage().bottom](#psdimagebottom)
        - [PSDImage().channels](#psdimagechannels)
        - [PSDImage().color_mode](#psdimagecolor_mode)
        - [PSDImage().compose](#psdimagecompose)
        - [PSDImage().composite](#psdimagecomposite)
        - [PSDImage().depth](#psdimagedepth)
        - [PSDImage.frompil](#psdimagefrompil)
        - [PSDImage().has_preview](#psdimagehas_preview)
        - [PSDImage().has_thumbnail](#psdimagehas_thumbnail)
        - [PSDImage().height](#psdimageheight)
        - [PSDImage().image_resources](#psdimageimage_resources)
        - [PSDImage().is_group](#psdimageis_group)
        - [PSDImage().is_visible](#psdimageis_visible)
        - [PSDImage().kind](#psdimagekind)
        - [PSDImage().left](#psdimageleft)
        - [PSDImage().name](#psdimagename)
        - [PSDImage.new](#psdimagenew)
        - [PSDImage().numpy](#psdimagenumpy)
        - [PSDImage().offset](#psdimageoffset)
        - [PSDImage.open](#psdimageopen)
        - [PSDImage().parent](#psdimageparent)
        - [PSDImage().right](#psdimageright)
        - [PSDImage().save](#psdimagesave)
        - [PSDImage().size](#psdimagesize)
        - [PSDImage().tagged_blocks](#psdimagetagged_blocks)
        - [PSDImage().thumbnail](#psdimagethumbnail)
        - [PSDImage().top](#psdimagetop)
        - [PSDImage().topil](#psdimagetopil)
        - [PSDImage().version](#psdimageversion)
        - [PSDImage().viewbox](#psdimageviewbox)
        - [PSDImage().visible](#psdimagevisible)
        - [PSDImage().width](#psdimagewidth)

## PSDImage

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L21)

```python
class PSDImage(GroupMixin):
    def __init__(data):
```

Photoshop PSD/PSB file object.

The low-level data structure is accessible at :pyattribute `PSDImage._record`.

Example

```python
from psdtoolsx import PSDImage

psd = PSDImage.open('example.psd')
image = psd.compose()

for layer in psd:
    layer_image = layer.compose()
```

#### See also

- [GroupMixin](layers.md#groupmixin)

### PSDImage().bbox

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L335)

```python
@property
def bbox():
```

Minimal bounding box that contains all the visible layers.

Use :pyattribute `~psdtoolsx.api.psd_image.PSDImage.viewbox` to get
viewport bounding box. When the psd is empty, bbox is equal to the
canvas bounding box.

#### Returns

(left, top, right, bottom) `tuple`.

### PSDImage().bottom

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L290)

```python
@property
def bottom():
```

Bottom coordinate.

#### Returns

`int`

### PSDImage().channels

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L370)

```python
@property
def channels():
```

Number of color channels.

#### Returns

`int`

### PSDImage().color_mode

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L360)

```python
@property
def color_mode():
```

Document color mode, such as 'RGB' or 'GRAYSCALE'. See
:pyclass `psdtoolsx.constants.ColorMode`.

#### Returns

:pyclass `psdtoolsx.constants.ColorMode`

### PSDImage().compose

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L138)

```python
@deprecated
def compose(force=False, bbox=None, layer_filter=None):
```

Deprecated, use :py:func:`~psdtoolsx.PSDImage.composite`.

Compose the PSD image.

#### Arguments

- `bbox` - Viewport tuple (left, top, right, bottom).

#### Returns

:pyclass `PIL.Image`, or `None` if there is no pixel.

#### See also

- [deprecated](index.md#deprecated)

### PSDImage().composite

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L174)

```python
def composite(
    viewport=None,
    force=False,
    color=1.0,
    alpha=0.0,
    layer_filter=None,
    ignore_preview=False,
):
```

Composite the PSD image.

#### Arguments

- `viewport` - Viewport bounding box specified by (x1, y1, x2, y2)
    tuple. Default is the viewbox of the PSD.
- `ignore_preview` - Boolean flag to whether skip compositing when a
    pre-composited preview is available.
- `force` - Boolean flag to force vector drawing.
- `color` - Backdrop color specified by scalar or tuple of scalar.
    The color value should be in [0.0, 1.0]. For example, (1., 0., 0.)
    specifies red in RGB color mode.
- `alpha` - Backdrop alpha in [0.0, 1.0].
- `layer_filter` - Callable that takes a layer as argument and
    returns whether if the layer is composited. Default is
    :py:func:`~psdtoolsx.api.layers.PixelLayer.is_visible`.

#### Returns

:pyclass `PIL.Image`.

### PSDImage().depth

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L379)

```python
@property
def depth():
```

Pixel depth bits.

#### Returns

`int`

### PSDImage.frompil

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L66)

```python
@classmethod
def frompil(image, compression=Compression.RLE):
```

Create a new PSD document from PIL Image.

#### Arguments

- `image` - PIL Image object.
- `compression` - ImageData compression option. See
    :pyclass `psdtoolsx.constants.Compression`.

#### Returns

A :pyclass `psdtoolsx.api.psd_image.PSDImage` object.

### PSDImage().has_preview

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L226)

```python
def has_preview():
```

Returns if the document has real merged data. When True, `topil()`
returns pre-composed data.

### PSDImage().has_thumbnail

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L442)

```python
def has_thumbnail():
```

True if the PSDImage has a thumbnail resource.

### PSDImage().height

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L308)

```python
@property
def height():
```

Document height.

#### Returns

`int`

### PSDImage().image_resources

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L397)

```python
@property
def image_resources():
```

Document image resources.
:pyclass `psdtoolsx.psd.image_resources.ImageResources` is a
dict-like structure that keeps various document settings.

See :py:class:[Resource](../constants.md#resource) for available keys.

#### Returns

:pyclass `psdtoolsx.psd.image_resources.ImageResources`

Example

```python
from psdtoolsx.constants import Resource
version_info = psd.image_resources.get_data(Resource.VERSION_INFO)
slices = psd.image_resources.get_data(Resource.SLICES)
```

Image resources contain an ICC profile. The following shows how to
export a PNG file with embedded ICC profile

```python
from psdtoolsx.constants import Resource
icc_profile = psd.image_resources.get_data(Resource.ICC_PROFILE)
image = psd.compose(apply_icc=False)
image.save('output.png', icc_profile=icc_profile)
```

### PSDImage().is_group

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L218)

```python
def is_group():
```

Return True if the layer is a group.

#### Returns

`bool`

### PSDImage().is_visible

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L205)

```python
def is_visible():
```

Returns visibility of the element.

#### Returns

`bool`

### PSDImage().kind

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L245)

```python
@property
def kind():
```

Kind.

#### Returns

`'psdimage'`

### PSDImage().left

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L263)

```python
@property
def left():
```

Left coordinate.

#### Returns

`0`

### PSDImage().name

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L236)

```python
@property
def name():
```

Element name.

#### Returns

`'Root'`

### PSDImage.new

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L45)

```python
@classmethod
def new(mode, size, color=0, depth=8, **kwargs):
```

Create a new PSD document.

#### Arguments

- `mode` - The color mode to use for the new image.
- `size` - A tuple containing (width, height) in pixels.
- `color` - What color to use for the image. Default is black.

#### Returns

A :pyclass `psdtoolsx.api.psd_image.PSDImage` object.

### PSDImage().numpy

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L163)

```python
def numpy(channel=None):
```

Get NumPy array of the layer.

#### Arguments

- `channel` - Which channel to return, can be 'color',
    'shape', 'alpha', or 'mask'. Default is 'color+alpha'.

#### Returns

:pyclass `numpy.ndarray`

### PSDImage().offset

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L326)

```python
@property
def offset():
```

(left, top) tuple.

#### Returns

`tuple`

### PSDImage.open

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L90)

```python
@classmethod
def open(fp, **kwargs):
```

Open a PSD document.

#### Arguments

- `fp` - filename or file-like object.
- `encoding` - charset encoding of the pascal string within the file,
    default 'macroman'. Some psd files need explicit encoding option.

#### Returns

A :pyclass `psdtoolsx.api.psd_image.PSDImage` object.

### PSDImage().parent

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L213)

```python
@property
def parent():
```

Parent of this layer.

### PSDImage().right

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L281)

```python
@property
def right():
```

Right coordinate.

#### Returns

`int`

### PSDImage().save

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L107)

```python
def save(fp, mode='wb', **kwargs):
```

Save the PSD file.

#### Arguments

- `fp` - filename or file-like object.
- `encoding` - charset encoding of the pascal string within the file,
    default 'macroman'.
- `mode` - file open mode, default 'wb'.

### PSDImage().size

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L317)

```python
@property
def size():
```

(width, height) tuple.

#### Returns

`tuple`

### PSDImage().tagged_blocks

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L424)

```python
@property
def tagged_blocks():
```

Document tagged blocks that is a dict-like container of settings.

See :py:class:[Tag](../constants.md#tag) for available
keys.

#### Returns

:pyclass `psdtoolsx.psd.tagged_blocks.TaggedBlocks` or
    `None`.

Example

```python
from psdtoolsx.constants import Tag
patterns = psd.tagged_blocks.get_data(Tag.PATTERNS1)
```

### PSDImage().thumbnail

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L449)

```python
def thumbnail():
```

Returns a thumbnail image in PIL.Image. When the file does not
contain an embedded thumbnail image, returns None.

### PSDImage().top

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L272)

```python
@property
def top():
```

Top coordinate.

#### Returns

`0`

### PSDImage().topil

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L122)

```python
def topil(channel=None, apply_icc=False):
```

Get PIL Image.

#### Arguments

- `channel` - Which channel to return; e.g., 0 for 'R' channel in RGB
    image. See :pyclass `psdtoolsx.constants.ChannelID`. When `None`,
    the method returns all the channels supported by PIL modes.
- `apply_icc` - Whether to apply ICC profile conversion to sRGB.

#### Returns

:pyclass `PIL.Image`, or `None` if the composed image is not
    available.

### PSDImage().version

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L388)

```python
@property
def version():
```

Document version. PSD file is 1, and PSB file is 2.

#### Returns

`int`

### PSDImage().viewbox

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L351)

```python
@property
def viewbox():
```

Return bounding box of the viewport.

#### Returns

(left, top, right, bottom) `tuple`.

### PSDImage().visible

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L254)

```python
@property
def visible():
```

Visibility.

#### Returns

`True`

### PSDImage().width

[[find in source code]](../../../psdtoolsx/api/psd_image.py#L299)

```python
@property
def width():
```

Document width.

#### Returns

`int`
