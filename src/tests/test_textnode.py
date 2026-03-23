import unittest

from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    

    def test_split_nodes(self): 
        node = TextNode("This is a text node with *bold* and _italic_ text", TextType.TEXT)
        nodes = [node]
        from src.helpers.helper import split_nodes_delimiter
        nodes = split_nodes_delimiter(nodes, "*", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

        expected_nodes = [
            TextNode("This is a text node with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()