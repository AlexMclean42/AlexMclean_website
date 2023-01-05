import math

def myAdd(first_number_chosen,second_number_chosen):
   result = int(first_number_chosen) + int(second_number_chosen)
   
   return result
def mySub(first_number_chosen, second_number_chosen):
   result = int(first_number_chosen) - int(second_number_chosen)
   return result
   
def myMul (first_number_chosen, second_number_chosen):
   result = int(first_number_chosen) * int(second_number_chosen)
   
   return result
  
def myDiv (first_number_chosen, second_number_chosen):
   if int(second_number_chosen) == 0:
        result = print('Error can not divide by 0')
        exit()
        
   else:
        result = int(first_number_chosen) // int(second_number_chosen)

   return result

def print_answer(final_answer, list_of_chosen_numbers, list_of_chosen_operations):
   print(str(list_of_chosen_numbers[0]) + " " + str(list_of_chosen_operations[0]) + " " + str(list_of_chosen_numbers[1]) + " " + str(list_of_chosen_operations[1]) + " " + str(list_of_chosen_numbers[2]) +  " = " + str(final_answer))


def input_validator(first_number_chosen, second_number_chosen, third_number_chosen):
 
   while first_number_chosen.isdigit() != True:
       if first_number_chosen.strip('-').isdigit():
           break
       first_number_chosen = (input("Value 1 is invalid. Please input again: "))
       if first_number_chosen.strip('-').isdigit():
           break
 
   while second_number_chosen.isdigit() != True:
       if second_number_chosen.strip('-').isdigit():
           break
       second_number_chosen = (input("Value 2 is invalid. Please input again: "))
       if second_number_chosen.strip('-').isdigit():
           break
 
   while third_number_chosen.isdigit() != True:
       if third_number_chosen.strip('-').isdigit():
           break
       third_number_chosen = (input("Value 3 is invalid. Please input again: "))
       if third_number_chosen.strip('-').isdigit():
           break
   list_numberss = [first_number_chosen,second_number_chosen,third_number_chosen]
   return (list_numberss)


   
def operation_validation (operator_value_1, operator_value_2):
   list_operation = ['+', '-', '*', '/']
 
   while operator_value_1 not in list_operation:
       operator_value_1 = (input("Operator 1 is invalid. Please input operator 1 again: "))
       if operator_value_1 in list_operation:
           break
   while operator_value_2 not in list_operation:
       operator_value_2 = (input("Operator 2 is invalid. Please input operator 2 again: "))
       if operator_value_2 in list_operation:
           break
   list_operations = [operator_value_1,operator_value_2]
   return list_operations

def evaluator (list_of_chosen_numbers,list_of_chosen_operations):
   number_1 = list_of_chosen_numbers[0]
   operator_value_1  = list_of_chosen_operations[0]
   number_2 = list_of_chosen_numbers[1]
   operator_value_2  = list_of_chosen_operations[1]
   number_3 = list_of_chosen_numbers[2]
   if operator_value_2 == '*': 
       if operator_value_1 == '*': 
           final_answer = myMul(myMul(number_1, number_2), number_3)
       if operator_value_1 == '/': 
           final_answer = myMul(myDiv(number_1, number_2), number_3)


 
   if operator_value_2 == '/': 
       if operator_value_1 == '*': 
           final_answer = myDiv(myMul(number_1, number_2), number_3)
       if operator_value_1 == '/': 
           final_answer = myDiv(myDiv(number_1, number_2), number_3)


   if operator_value_2 == '+': 
       if operator_value_1 == '*': 
           final_answer = myAdd(myMul(number_1,number_2), number_3)
       if operator_value_1 == '/': 
           final_answer = myAdd(number_3, myDiv(number_1,number_2))
       if operator_value_1 == '+': 
           final_answer = myAdd(myAdd(number_1,number_2), number_3)

   if operator_value_1 == '-': 
       if operator_value_2 == '*': 
           final_answer = mySub(number_1, myMul(number_2,number_3))
       if operator_value_2 == '/': 
           final_answer = mySub(number_1, myDiv(number_2, number_3))
       if operator_value_2 == '+': 
           final_answer = myAdd(mySub(number_1, number_2),number_3)
 
   if operator_value_2 == '-':   
       if operator_value_1 == '*': 
           final_answer = mySub(myMul(number_1,number_2),number_3)
       if operator_value_1 == '/': 
           final_answer = mySub(myDiv(number_1,number_2),number_3)
       if operator_value_1 == '+': 
           final_answer = mySub(myAdd(number_1,number_2),number_3)
       if operator_value_1 == '-': 
           final_answer = mySub(mySub(number_1,number_2),number_3)
   if operator_value_1 == '+': 
       if operator_value_2 == '*': 
           final_answer = myAdd(number_1, myMul(number_2,number_3))
       if operator_value_2 == '/': 
           final_answer = myAdd(number_1, myDiv(number_2, number_3))
   
   print_answer(final_answer, list_of_chosen_numbers, list_of_chosen_operations)

   return

if __name__ == '__main__':
   first_number_chosen_user = (input("Enter the first number: "))
   operator_value_1_user = str(input("Enter the first operator: "))
   second_number_chosen_user = (input("Enter the second number: "))
   operator_value_2_user = str(input("Enter the second operator: "))
   third_number_chosen_user = (input("Enter the third number: "))
   answer = evaluator (input_validator(first_number_chosen_user, second_number_chosen_user, third_number_chosen_user),operation_validation(operator_value_1_user,operator_value_2_user))