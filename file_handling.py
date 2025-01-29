def file_handling():
    try:
        with open('msd.txt','w+') as file:
            user_input=input("Enter your content : ")
            file.write(user_input)
            file =open("msd.txt",'a')
            file.writelines('\nwelcome to python \n ---------')
            img = open('dhoni.jpg','rb')
            view = open('dhoni1.jpg', 'wb')
            for i in img:
                view.write(i)
            print(view)
            with open('dhoni.jpg','rb') as img1:
                print(img1.read())    
            
            print(file.closed)
                
    except FileNotFoundError as error:
        print(f'File_Not_Found_Error : {error}')

    finally:
        print('code executed scuessfully!..')
