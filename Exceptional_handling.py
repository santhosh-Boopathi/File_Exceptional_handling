def exception_handling():

    #index_out_of_range
    try:
        my_list=[1,2,3]
        print(my_list[5])

    except IndexError as error:
        print(f"Index_Error: {error}")

    finally:
        print('Excecuted successfully')
        print()

    #arithmetic_error
    try:
        value=10/0
        print(value)

    except ArithmeticError as error:
        print(f"Arithmetic_Error : {error}")

    finally:
        print("Executed successfully")
        print()

    #assertion_error
    try:
        x=1
        assert x>5

    except AssertionError as error:
        print(f"Assertion_Error : {error}")

    finally:
        print("Executed successfully")
        print()

    #key_error
    try:
        my_dict={'name':'santhosh'}
        print(my_dict['age'])

    except KeyError as error:
        print(f'Key_Error : {error}')

    finally:
        print("executed successfully")
        print()

    #name_error
    try:
        # a,b=10,20
        sum=a+b
        print(sum)

    except NameError as error:
        print(f'Name_Error : {error}')

    finally:
        print("executed successfully")
        print()

    #type_error
    try:
        add='msd'+7
        print(add)

    except TypeError as error:
        print(f'Type_Error : {error}')

    finally:
        print("executed successfully")
        print()

    #value_error
    try:
        num=int('MSD')
        print(num)

    except ValueError as error:
        print(f'Value_Error : {error}')

    finally:
        print("executed successfully")
        print() 

    #exceptions
    try:
        user_value='00'+7
        print(user_value)

    except Exception as error:
        print(f'Exception_Error : {error}')

    finally:
        print("executed successfully")
        print()
