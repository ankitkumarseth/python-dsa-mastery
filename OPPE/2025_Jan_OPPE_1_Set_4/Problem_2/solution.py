def markdown_to_html_image(markdown_image: str) -> str:
    '''Converts a Markdown image link to an HTML image tag.

    Args:
        markdown_image (str): A string containing a Markdown image link.

    Returns:
        str: The corresponding HTML image tag.

    Examples:
    >>> markdown_to_html_image("![awesome dog](dog.jpg)")
    '<img src="dog.jpg" alt="awesome dog">'
    >>> markdown_to_html_image("![python logo](python.png)")
    '<img src="python.png" alt="python logo">'
    '''
    ...
