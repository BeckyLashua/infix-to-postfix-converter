# Date: 6/17/2020 
# Date Last Modified: 6/18/2020
# Programmer: Rebecca Lashua
# A program that implements an infix->postfix converter. It reads an infix 
# expression from the user and prints out the corresponding postfix expression.


# FUNCTION DESCRIPTION DO THESE ON ALL
def run_program():
    # Get a string from the user
    user_input = get_input()

    # Fully parenthesize expression before converting
    parenthesized_input = parenthesize(user_input)

    # Convert to postfix notation 
    result = convert_to_postfix(parenthesized_input)

    # Display result to user
    print(result)


def get_input():
    return input("Enter an infix expression: ")


# precondition: string passed to function must be already fully parenthesized and a valid
# infix expression.
def convert_to_postfix(infix_expression):
    output = ''  # this will hold the postfix expression
    stack_list = []  # will be used as a stack for non operand chars
    not_valid = "Error. This is not a valid infix expression"
    brackets = []  # needed for validating balance in expression
    has_operators = False  # an infix expression needs to have operators

    if len(infix_expression) < 3:
        return not_valid

    for letter in infix_expression:
        if is_left_paran(letter):
            brackets.append(')')
            stack_list.append(letter)
        elif is_right_paran(letter):
            # first check to make sure the string is balanced so far
            if len(brackets) == 0 or brackets[-1] != ')':
                return not_valid  # no need to continue. Not valid.
            else:  # otherwise, pop the matching bracket off the stack
                brackets.pop()
            # left_paran_found = False
            left_paran_found = False
            # while not left_paran_found
            while left_paran_found == False and len(stack_list) != 0:
                # if i == '(', 
                if is_left_paran(stack_list[-1]):
                    # left_paran_found = True:
                    left_paran_found = True
                    # remove '(' from list
                    stack_list.pop()
                # else  
                else:
                    # pop from stack and add to output string 
                    output += stack_list.pop()
        elif is_operator(letter):
            has_operators = True
            # if length of stack list is 0 or top of stack is '('
            if len(stack_list) == 0 or is_left_paran(stack_list[-1]):
                # add to stack list
                stack_list.append(letter)
            # else
            else:
                # if end/top of stack is also an operator, 
                if is_operator(stack_list[-1]):
                    # compare precendence. 
                    precedence = determine_precedence(letter, stack_list[-1])
                    # if top/end of stack takes precedence, 
                    if precedence == -1:
                        # remove top and add to output string
                        output += stack_list.pop()
                        # add current letter to stack_list
                        stack_list.append(letter)
                    # else if the current letter has precedence
                    elif precedence == 1:
                        # add current operator to output string
                        output += letter
                    # else they have equal precedence
                    else:
                        pass
        elif letter == ' ':
            pass
        else:
            output += letter

    # if there are no operators in expression, it is not valid
    if not has_operators:
        return not_valid

    # if there is anything remaining in brackets stack, it's not balanced
    if len(brackets) != 0:
        return not_valid

    # if stack List is not empty 
    if len(stack_list) != 0:
        while len(stack_list) != 0:
            # add element to output
            output += stack_list.pop()

    return output


def parenthesize(expression):
    # Returns an infix expression fully parenthesized.

    return expression


def determine_precedence(operator_one, operator_two):
    operators = {
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    first_val = operators[operator_one]
    second_val = operators[operator_two]

    return first_val - second_val


def is_left_paran(character):
    if character == '(':
        return True
    return False


def is_right_paran(character):
    if character == ')':
        return True
    return False


def is_operator(character):  # will likely need to convert these operators later
    operators = ['^', '*', '/', '+', '-']
    for char in operators:
        if char == character:
            return True
    return False


run_program()
