class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    # returns an HTML string representation of this HTMLNode's props
    # Ex: " prop1=1 prop2=2"
    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join(list(map(lambda prop: f' {prop}="{self.props[prop]}"', self.props)))

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
