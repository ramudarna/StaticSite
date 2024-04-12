import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
    def test_to_html_no_children(self):
        node = LeafNode('p', 'Hello, world')
        self.assertEqual(node.to_html(), "<p>Hello, world</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, 'Hello, world')
        self.assertEqual(node.to_html(), "Hello, world")

    def test_to_html_children(self):
        childnode = LeafNode('span', 'child')
        parentnode = ParentNode('div', [childnode])
        self.assertEqual(parentnode.to_html(), '<div><span>child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchildnode = LeafNode('b', 'grandchild')
        childnode = ParentNode('span', [grandchildnode])
        parentnode = ParentNode('div', [childnode])
        self.assertEqual(parentnode.to_html(), '<div><span><b>grandchild</b></span></div>')

    def test_to_html_many_children(self):
        node = ParentNode('p', [LeafNode('b', 'Bold Text'), LeafNode(None, 'Normal Text'), LeafNode('i', 'italic text'), LeafNode(None, 'Normal Text')])
        self.assertEqual(node.to_html(), '<p><b>Bold Text</b>Normal Text<i>italic text</i>Normal Text</p>')

    def test_hasheadings(self):
        node = ParentNode('h2', [LeafNode('b', 'Bold Text'), LeafNode(None, 'Normal Text'), LeafNode('i', 'italic text'), LeafNode(None, 'Normal Text')])
        self.assertEqual(node.to_html(), '<h2><b>Bold Text</b>Normal Text<i>italic text</i>Normal Text</h2>')

if __name__ == "__main__":
    unittest.main()