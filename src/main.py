from textnode import TextNode, TextType

def main():
    node = TextNode("Test Node", TextType.IMAGE, "static/doge.png")
    print(node)

if __name__ == '__main__':
    main()
