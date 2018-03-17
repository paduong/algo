import sys

from algopy import bintree
from algopy.bintree import BinTree


def _deserialize_content(content, pos, end):
    """Produce a BinTree from input string.

    Args:
        content (str): String to parse as BinTree.
        pos (int): Current character index in `content`.
        end (int): Length of `content`.

    Returns:
        (BinTree, int): BinTree parsed and next character index to use.

    Raises:
        ExempleSyntaxError: If any format error is encountered.

    """

    # Check missing content
    if pos >= end:
        raise Exception("Unexpected end of content")
    # Check and skip opening parenthesis
    if content[pos] != '(':
        raise Exception("Missing '(' in exemple data")
    pos += 1
    # Check for empty tree
    if content[pos] == ')':
        return None, pos + 1
    # Get BinTree key and create node
    key = ""
    while pos < end and "(" != content[pos] and ")" != content[pos]:
        key += content[pos]
        pos += 1
    tree = BinTree(key, None, None)
    # Parse children
    tree.left, pos = _deserialize_content(content, pos, end)
    tree.right, pos = _deserialize_content(content, pos, end)
    # Final tree and skip closing parenthesis
    if content[pos] != ')':
        raise Exception("Missing terminal ')' in exemple data")
    return tree, pos + 1


def load_bintree(path):
    """Load a BinTree from a text file.

    Args:
        path (str): Path to the text file.

    Returns:
        (BinTree): BinTree parsed from `path`.

    Raises:
        FileNotFoundError: If `path` is wrong.

    """

    # Open file and get full content
    file = open(path, 'r')
    content = file.read()
    # Remove all whitespace characters for easier parsing
    content = content.replace('\n', '').replace('\r', '') \
                     .replace('\t', '').replace(' ', '')
    # Parse content, close file and return tree
    tree, _ = _deserialize_content(content, 0, len(content))
    file.close()
    return tree


def error(message, exit_code=0):
    """Simple error printing tool.

    Args:
        message (str): Message to print on standard error stream.
        exit_code (int): Exit with givent code if not 0.

    """

    print('Error:', message, file=sys.stderr)
    if exit_code:
        sys.exit(exit_code)


# Only executed if run from the command line
if __name__ == '__main__':
    # Check if file path was passed on the command line
    if len(sys.argv) < 2:
        error('Missing file path argument', exit_code=1)
        sys.exit(1)
    # Get the file path and load
    file_path = sys.argv[1]
    try:
        tree = load_bintree(file_path)
        # Print tree if successfully loaded
        if tree is not None:
            print(bintree.dot_simple(tree))
    except FileNotFoundError:
        error('No such file "{}"'.format(file_path), exit_code=2)
