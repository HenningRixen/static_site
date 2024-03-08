import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_text_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a tex node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_text_type_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a tex node", "italic")
        self.assertEqual(node, node2)
    
    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(node, node2)
    
    def test_not_url_eq(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.foogle.com")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", bold, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
