from utilities import copy_static_to_dir, generate_pages_recursive
import sys

def main():
    if len(sys.argv) == 2:
        root = sys.argv[1]
    else:
        root = "/"

    public_dir = "docs"
    copy_static_to_dir(public_dir)
    generate_pages_recursive(root, "content", "template.html", public_dir)

if __name__ == '__main__':
    main()
