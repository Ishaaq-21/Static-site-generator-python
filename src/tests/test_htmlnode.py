import unittest

from src.htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a p tag",None,  {"class": "color: red; font-size:20px; padding:5px; border: 1px black solid;"})
        node2 = HTMLNode("p", "This is a p tag",None,  {"class": "color: red; font-size:20px; padding:5px; border: 1px black solid;"})
      
        
        self.assertEqual(node, node2)


        linkNode = HTMLNode("link", "This is a link tag", None, {"class": "color: green; font-size: 22px;", "href": "www.google.com"})
        linkNode2 = HTMLNode("link", "This is a link tag", None, {"class": "color: green; font-size: 22px;", "href": "www.facebook.com"})
        self.assertNotEqual(linkNode, linkNode2)

if __name__ == "__main__":
    unittest.main()