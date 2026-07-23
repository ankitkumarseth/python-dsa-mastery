# Markdown Image to HTML Image

Given a string containing a Markdown image link of the format `![alt text](image_url)`, convert it to a proper HTML image tag of the format `<img src="image_url" alt="alt text">`.

### Examples

```python
>>> markdown_to_html_image("![awesome dog](dog.jpg)")
'<img src="dog.jpg" alt="awesome dog">'
>>> markdown_to_html_image("![python logo](python.png)")
'<img src="python.png" alt="python logo">'
```
