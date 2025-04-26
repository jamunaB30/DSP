def paranthisis_matching(expression):
    stack=[]
    pairst={']':'[','}':'{',')':'('}
    
    for char in expression:
        if char =='('or char == '{' or char == '[':
            stack.append(char)

        elif char ==')'or char =='}'or char == ']':
            if(len(stack)==0):
                return False

            top_element=stack[-1]

            if char==')':
                closing_breacket ='('
            elif char=='}':
                closing_breacket='{'
            elif char==']':
                closing_breacket="["

            if top_element!=closing_breacket:
                return false
            stack.pop()
    if(len(stack)==0):
        return True
    else:
        return False


expression="{()}
"
result = paranthisis_matching(expression)
if(result==True):
    print("the pranthsis are matching")
else:
    print("the parnthsis are not matching")

              
