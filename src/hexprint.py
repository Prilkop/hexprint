import re
from shutil import get_terminal_size
from typing import Dict

from termcolor import colored

DEFAULT_DIFF_COLOR = 'blue'
DEFAULT_HIGHLIGHT_COLOR = 'yellow'


def hexprint(data: bytes, width: int = None,
             colored_indices: Dict[int, str] = None,
             highlighted_indices: Dict[int, str] = None) -> None:
    """
    Print binary data in a hexdump format with optional coloring and highlighting.

    :param data: The input data as bytes.
    :param width: The number of bytes of the hexdump display (optional).
    :param colored_indices: A dictionary of byte indices to color codes (optional).
    :param highlighted_indices: A dictionary of byte indices to highlight codes (optional).
    """
    if not colored_indices:
        colored_indices = {}
    if not highlighted_indices:
        highlighted_indices = {}

    if not width:
        screen_width, _ = get_terminal_size()
        width = (screen_width - 10 - 5) // 4

    print(f'{"":10s} | {" ".join(f"{i:02X}" for i in range(width))} | ')
    print(f'{"":10s} +-{"-" * (width * 3 - 1)}-+ ')
    for i in range(0, len(data), width):
        hex_values = []
        ascii_values = []
        for index in range(i, i + width):
            if index < len(data):
                b = data[index]

                value = f'{b:02x}'
                c = chr(int(b)) if 32 <= int(b) <= 126 else '.'

                color = colored_indices.get(index)
                highlight = highlighted_indices.get(index)
                if highlight:
                    on_color = 'on_' + highlight
                else:
                    on_color = None
                value = colored(value, color, on_color)
                c = colored(c, color, on_color)
            else:
                value = '  '
                c = ' '

            hex_values.append(value)
            ascii_values.append(c)

        hex_line = ' '.join(hex_values)
        ascii_line = ''.join(ascii_values)

        print(f'0x{i:08x} | {hex_line} | {ascii_line}')


def compare(data1: bytes, data2: bytes, width: int = None, diff_color: str = DEFAULT_DIFF_COLOR) -> None:
    """
    Compare and print two sets of data in a hexdump-like format, highlighting differences.

    :param data1: The first set of data as bytes.
    :param data2: The second set of data as bytes.
    :param width: The width of the hexdump display (optional).
    :param diff_color: The color for highlighting differences (optional).
    """
    color_mapping = {index: diff_color for index in range(min(len(data1), len(data2))) if
                     data1[index:index + 1] != data2[index:index + 1]}
    color_mapping |= {index: diff_color for index in range(min(len(data1), len(data2)),
                                                           max(len(data1), len(data2)))}
    hexprint(data1, colored_indices=color_mapping, width=width)
    print()
    hexprint(data2, colored_indices=color_mapping, width=width)


def highlight(data: bytes, sequences: list[bytes] = (), width: int = None,
              color: str = DEFAULT_HIGHLIGHT_COLOR) -> None:
    """
    Print the data in a hexdump-like format, with specified sequences highlighted.

    :param data: The input data as bytes.
    :param sequences: A list of byte sequences to highlight (optional).
    :param width: The width of the hexdump display (optional).
    :param color: The color for highlighting sequences (optional).
    """
    marked_indices = set()
    for sequence in sequences:
        for match in re.finditer(re.escape(sequence), data):
            for index in range(match.start(), match.end()):
                marked_indices.add(index)

    hexprint(data, highlighted_indices={index: color for index in marked_indices}, width=width)
