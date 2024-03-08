import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
        "h1", 
        "hi there", 
        None, 
        {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"'
        )

    def test_to_html_no_children(self):
        node = LeafNode("p","this is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>this is a paragraph of text.</p>")
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")      


if __name__ == "__main__":
    unittest.main()