import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'bold')
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode('This is a text node', 'bold')
        node2 = TextNode('This is a text node', 'italic')
        self.assertNotEqual(node, node2)    

    def test_urlempty(self):
        node = TextNode('This is a text node', 'bold')
        self.assertTrue(node)
        
if __name__ == '__main__':
    unittest.main()