import codewars_test as test

def bucket_of(said):
    said = said.lower()
    W = None
    S = None
  
    
    if "water" in said or "wet" in said or "wash" in said:
        #return "water"
        W = 'W'
    if "i don't know" in said or "slime" in said:
        #return "slime"
        S = 'S'
        
    if W =='W' and S == 'S':
        return "sludge"
    elif W =='W' and S == None:
        return "water"
    elif W == None and S == 'S':
        return "slime"
    else:
        return "air"
