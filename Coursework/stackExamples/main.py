class Stack:
  def __init__(self):
    self.items = []

#Checks to see if closings are balanced
def isBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(","{","["]:
            #Add that character to the stack
            stack.append(char)
        else:
            #If the character is not an opening bracket it must be a closing bracket
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{': 
                if char != "}": 
                    return False
            if current_char == '[': 
                if char != "]": 
                    return False
  
    # Check Empty Stack 
    if stack: 
        return False
    return True
  
  
# Driver Code 
  
if __name__ == "__main__":
    expr = "[{()}]("

    if isBalanced(expr):
        print("based")
    else:
        print("not based")