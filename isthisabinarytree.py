

prevVal = -1
resultVal = 1

def check_binary_search_tree_(root):
  inOrder(root)
  if resultVal == 1:
    return True
  elif resultVal == 0:
    return False

# perform an in order traversal 
def inOrder(root):
  if root is None:
    return
  else:
    inOrder(root.left)
     
    global prevVal
    if prevVal < root.data:
      prevVal = root.data
    else:
      global resultVal
      resultVal = 0
      return
    
    inOrder(root.right)
