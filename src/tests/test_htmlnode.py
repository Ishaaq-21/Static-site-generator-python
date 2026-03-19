import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a p tag",None,  {"class": "color: red; font-size:20px; padding:5px; border: 1px black solid;"})
        node2 = HTMLNode("p", "This is a p tag",None,  {"class": "color: red; font-size:20px; padding:5px; border: 1px black solid;"})
      
        
        self.assertEqual(node, node2)


        linkNode = HTMLNode("link", "This is a link tag", None, {"class": "color: green; font-size: 22px;", "href": "www.google.com"})
        linkNode2 = HTMLNode("link", "This is a link tag", None, {"class": "color: green; font-size: 22px;", "href": "www.facebook.com"})
        self.assertNotEqual(linkNode, linkNode2)

class TestLeafNode(unittest.TestCase): 
    def test_eq(self): 
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

class TestParentNode(unittest.TestCase): 
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
       grandchild_node = LeafNode("b", "grandchild")
       child_node2 = ParentNode("span", [grandchild_node])
       parent_node2 = ParentNode("div", [child_node2])
       self.assertEqual(
           parent_node2.to_html(),
           "<div><span><b>grandchild</b></span></div>",
       )


if __name__ == "__main__":
    unittest.main()