from tree import *
EPSILON = '\u03B5'
import tkinter as tk
class TempNode:
    def __init__(self,left,right,terminal) -> None:
        self.__left = left
        self.__right = right
        self.terminal = terminal
    def drawnode(self,canvas=None,level=0,parent=None,left=0,right=0,curr=None):
        if not curr:
            curr = TreeNode(canvas,level,parent,left,right,label=self.terminal)
            curr.draw()
        if self.__left :
            curr.add_children([self.__left.terminal])
            children = curr.get_children()
            self.__left.drawnode(curr=children[0])

        if self.__right:
            curr.add_children([self.__right.terminal])
            children = curr.get_children()
            self.__right.drawnode(curr=children[-1])


var=["exp","term","exp'","term'","factor","factor'","comop","operand"]
terminals=["||",">","<","=","identifier","$","&&","!"]
priority={
    "||":3,
    "&&":2,
    ">": 1,
    "<": 1,
    "=": 1,
    "!":0,
    "identifier":-1
}

parsing_table = {'exp': {'identifier': "term exp'", '!': "term exp'"},
                     "exp'": {'||': "|| term exp'", '$': EPSILON},
                     'term': {'identifier': "factor term'", '!': "factor term'"},
                     "term'": {'&&': "&& factor term'", '$': EPSILON, '||': EPSILON},
                     'factor': {'identifier': "operand factor'", '!': "operand factor'"},
                     "factor'": {'>': "comop operand factor'", '<': "comop operand factor'", '=': "comop operand factor'", '$': EPSILON, '&&': EPSILON, '||': EPSILON},
                     'comop': {'>': '>', '=': '=', '<': '<'}, 'operand': {'!': '! operand', 'identifier': 'identifier'}}


def check_identifier(input):
    try:
        int(input[0])
        return False
    except:
        for char in input:
            if not ((char >= '1' and char <= '9') or (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
                return False
    return True

def generate_tree(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return TempNode(None, None, list[0])

    split_index =largest_pirority(list)
    return TempNode(generate_tree(list[:split_index]),
                    generate_tree(list[split_index + 1:]), list[split_index])
def largest_pirority(list):
    max_priority = 0
    for i in range(1, len(list)):
        str = 'identifier' if check_identifier(list[i]) else list[i]
        strMax = 'identifier' if check_identifier(list[max_priority]) else list[max_priority]
        if priority[str] > priority[strMax]:
            max_priority = i
    return max_priority

def generate(list):
    root = tk.Tk()
    root.title("Abstract Syntax Tree")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 1200 if w > 1200 else w
    h = 720 if h > 720 else h
    root.geometry("%dx%d+0+0" % (w, h))
    x2 = TreeCanvas(root)
    x2.grid(row=0, column=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    treeRoot = generate_tree(list)
    treeRoot.drawnode(x2.canvas, 0, None, 0,w)
    root.mainloop()
def parse(tokens):
    root = tk.Tk()
    root.title("Parse Tree")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 1200 if w > 1200 else w
    h = 720 if h > 720 else h

    root.geometry("%dx%d+0+0" % (w, h))
    x2 = TreeCanvas(root)
    x2.grid(row=0, column=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    nodes=[TreeNode(x2.canvas,0,None,0,w-100,label="exp")]
    stack=[]
    stack.append("exp")
    stack.append("$")
    tokens.append("$")
    nodes[0].draw()
    while len(tokens):
        print(stack, tokens)
        x=stack.pop(0)
        if x!="$":
            node=nodes.pop(0)
        if x==EPSILON:
            continue
        elif x in var:
            try:
                y=parsing_table[x][tokens[0]]
                rules=y.split(" ")
                node.add_children(rules)
                lst=node.get_children()
                for i in range(len(rules)):
                    stack.insert(i,rules[i])
                    nodes.insert(i,lst[i])

            except:
                print("Error")
                return "Error"
                break
        elif x in terminals:
            if x==tokens[0]:
                tokens.pop(0)
                # node.set_label(str(tokensName.pop(0)))
            else:
                print("Error")
                return "Error"
                break
        else:
            print("Error")
            return "Error"
            break


    # parse(['identifier', '||', 'identifier'],x)
    root.mainloop()
# generate(['!', 'x', '||', 'y', '>', '!', 'z'])

