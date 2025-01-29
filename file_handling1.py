try :
    with open('msd1.txt','w+') as file:
        content=input("Enter some content : ")
        file.write(content)
        with open('msd1.txt','a'):
            file.writelines('\nWelcome to python\nhello world')
            img=open('dhoni.jpg','rb')
            view=open('dhoni2.jpeg','wb')
            for i in img:
                view.write(i)
            print(view)

        with open('dhoni.jpg','rb') as file2:
            print(file2.read())

        print(file.closed)
    print(file.closed)

except FileNotFoundError as error:
    print(f'File_Not_Found_Error : {error}')

except PermissionError as error:
    print(f'Permission_Error : {error}')  

finally:
    print('code executed sucessfully')



'''
    create a file -> ask the content from user -> handle possible exceptions ->file not found,permission error
read the content and append few lines -> use keywords for file operators -> add an image file read it in a binary format, else read itas image format
display the output
'''