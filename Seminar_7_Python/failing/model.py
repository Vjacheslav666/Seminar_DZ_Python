from failing import saving_data as sd


def input_firstname(): 
    first = input("Введите ваше имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname
 
# фамилия 
def input_lastname(): 
    last = input("Введите вашу фамилию: ") 
    remlname = last[1:]
    firstchar = last[0] 
    return firstchar.upper() + remlname
 
# сохранение новых данных контакта 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input("Введите ваш номер телефона: ") 
    emailID = input("Введите Описание: ")
    contactDetails = (f"Имя пользователя: {firstname}\nФамилия пользователя: {lastname}\nТелефон пользователя:{phoneNum}\nОписание пользователя: {emailID}\n\n") 
    myfile = open(sd.filename, "a", encoding='utf-8') 
    myfile.write(contactDetails) 
    print(f"Новая запись в телефонном справочнике:\n\n{contactDetails}\nуспешно создана!")