value = input("Please enter an expression to be evaluated(in a pre-fix form): ")
initialValues = list(value.split(" "))

stack = []
ahadu = len(initialValues) - 1

for i in range(len(initialValues)):
    if ((initialValues[ahadu]).isnumeric()):        
        stack.append(initialValues[ahadu])
        ahadu -= 1
    else:
        if (len(stack) >= 2):
            first_number = int(stack.pop())
            second_number = int(stack.pop())
            swtich = {
                "*" : first_number * second_number,
                "/" : first_number / second_number,
                "+" : first_number + second_number,
                "-" : first_number - second_number
            }
            
            result = swtich.get( initialValues[ahadu] )
            stack.append(result)
            ahadu -= 1

if((ahadu < 0) & (len(stack) == 1)):
    print("Result = {}".format(stack.pop()))

else:
    print("Please enter a valid prefix form expression!")

        


     
