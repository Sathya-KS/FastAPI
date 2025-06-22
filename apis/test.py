def addition_two_numbers(num1=40,num2 = 50,num3 =50):
    try:
        sum_of_two = int(num1) + int(num2)
        return {"sum_of_two":sum_of_two}
    except Exception as ex:
        print(ex)




add = addition_two_numbers(num1=20,num2=40)
print(add)