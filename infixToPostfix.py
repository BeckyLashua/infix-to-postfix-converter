# Date: 6/17/2020 
# Date Last Modified: 6/18/2020
# Programmer: Rebecca Lashua
# A program that implements an infix->postfix converter. It reads an infix 
# expression from the user and prints out the corresponding postfix expression.


### FUNCTION DESCRIPTION DO THESE ON ALL
def runProgram():
    # Get a string from the user
    userInput = getInput()
    
    # Fully paranthesize expression before converting
    paranthesizedInput = paranthesize(userInput)
    
    # Convert to postfix notation 
    result = convertToPostfix(paranthesizedInput)
    
    # Display result to user
    print(result)
    

def getInput():
    return input("Enter an infix expression: ")
    

# precondition: string passed to function must be already fully paranthesized and a valid 
# infix expression.
def convertToPostfix(infixExpression):
    output = ''             # this will hold the postfix expression
    stackList = []          # will be used as a stack for non operand chars
    notValid = "Error. This is not a valid infix expression"
    brackets = []           # needed for validating balance in expression
    hasOperators = False    # an infix expressio needs to have operators
    
    if len(infixExpression) < 3:
        return notValid
    
    for letter in infixExpression: 
        if isLeftParan(letter):
            brackets.append(')')
            stackList.append(letter)
        elif isRightParan(letter):
            # first check to make sure the string is balanced so far
            if len(brackets) == 0 or brackets[-1] != ')':
                return notValid    # no need to continue. Not valid.
            else:   # otherwise, pop the matching bracket off the stack
                brackets.pop()
            # leftParanFound = False
            leftParanFound = False
            # while not leftParanFound
            while leftParanFound == False and len(stackList) != 0:
                # if i == '(', 
                if isLeftParan(stackList[-1]):
                    # leftParanFound = True:
                    leftParanFound = True
                    # remove '(' from list
                    stackList.pop()
                # else  
                else:
                    # pop from stack and add to output string 
                    output += stackList.pop()
        elif isOperator(letter):
            hasOperators = True 
            # if length of stack list is 0 or top of stack is '('
            if len(stackList) == 0 or isLeftParan(stackList[-1]):
                # add to stack list
                stackList.append(letter)
            # else
            else:
                # if end/top of stack is also an operator, 
                if isOperator(stackList[-1]):
                    # compare precendence. 
                    precedence = determinePrecedence(letter, stackList[-1])
                    # if top/end of stack takes precedence, 
                    if precedence == -1:
                        # remove top and add to output string
                        output += stackList.pop()
                        # add current letter to stackList
                        stackList.append(letter)
                    # else if the current letter has precedence
                    elif precedence == 1:
                        # add current operator to output string
                        output += letter
                    # else they have equal precedence
                    else:
                        pass
                                                                 
        else: 
            output += letter
    
    # if there are no operators in expression, it is not valid
    if hasOperators == False:
        return notValid
        
    # if there is anything remaining in brackets stack, it's not balanced
    if len(brackets) != 0:
        return notValid
    
    # if stack List is not empty 
    if len(stackList) != 0:
        while len(stackList) != 0:
            # add element to output
            output += stackList.pop()
    
    return output
    
def paranthesize(expression):
    # Returns an infix expression fully paranthesized. 
    
    return expression
    
def determinePrecedence(operatorOne, operatorTwo):
    operators = {
        '^': 3,
        '*': 2, 
        '/': 2, 
        '+': 1,
        '-': 1
    }
    
    firstVal = operators[operatorOne]
    secondVal = operators[operatorTwo]
    
    return firstVal - secondVal

def isLeftParan(character):
    if character == '(':
        return True
    return False
    
def isRightParan(character):
    if character == ')':
        return True
    return False
    

def isOperator(character):  # will likely need to convert these operators later
    operators = ['^', '*', '/', '+', '-']
    for char in operators:
        if char == character:
            return True
    return False


runProgram() 
 
