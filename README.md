# hexprint

The `hexprint` module provides functionality to display binary data in a hexdump format with optional coloring and highlighting. It also includes a function to compare and highlight differences between two sets of data, as well as a function to highlight specific sequences within the data.

## Installation

You can install the `hexprint` module using pip:

```bash
pip install hexprint
```

## Usage Examples

### hexprint

The `hexprint` function is used to print binary data in a hexdump format. You can optionally specify colored and highlighted indices.

#### Basic example:
```python
from hexprint import hexprint

data = b'This is an example'

# Print binary data in a hexdump format
hexprint(data)
```
![output](/docs/hexprint.png)
#### An example including coloring:
```python
from hexprint import hexprint

data = b'This is an example'

# Print binary data with colored and highlighted indices
colored_indices = {0: 'red', 5: 'green'}
highlighted_indices = {2: 'yellow', 8: 'blue'}
hexprint(data, colored_indices=colored_indices, highlighted_indices=highlighted_indices)
```
![output](/docs/hexprint_colors.png)

### compare

The `compare` function is used to compare and print two sets of data in a hexdump-like format, highlighting the differences.

```python
from hexprint import compare

data1 = b'This is the example!'
data2 = b'This was an example'

# Compare and print the differences between two sets of data
compare(data1, data2)
```
![output](/docs/compare.png)

### highlight

The `highlight` function is used to highlight specific sequences within binary data.

```python
from hexprint import highlight

data = b'This is an example. This is another example.'

# Highlight specific sequences within the data
sequences = [b'This', b'another']
highlight(data, sequences=sequences)
```
![output](/docs/highlight.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.