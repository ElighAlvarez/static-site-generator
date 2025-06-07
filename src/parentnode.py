from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # returns an HTML string representation of this HTMLNode
    def to_html(self):
        if self.tag == None:
            raise ValueError("parent nodes must have a tag")
        if self.children == None:
            raise ValueError("parent nodes must have children")
        children_html = "".join(list(map(lambda child: child.to_html(), self.children)))
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
