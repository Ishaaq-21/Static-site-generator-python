from textnode import TextNode, TextType
def main(): 
    dummyTN = TextNode("Hello World", TextType.LINK, "https://www.boot.dev")
    print(dummyTN)



if __name__ == "__main__": 
    main()