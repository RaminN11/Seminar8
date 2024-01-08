from logger import*

def interface():
    with open("phonebook.txt", "a"):
        pass
    command = "-1"
    while command != "4":
        print("Возможные варианты взаимодействия: \n"
              "1. Добавить контакт\n"
              "2. Вывести на экран\n"
              "3. Поиск контакта\n"
              "4. Выход из программы")
        command = input("Введите пункт меню: ")

        while command not in ("1", "2", "3", "4"):
            print("Некорректные данные, нужно ввести число команды: ")
            command = input("Введите пункт меню: ")

        match command:
            case "1":
                add_contact()
            case "2":
                show_info()
            case "3":
                search_contact()
            case "4":
                print("Всего хорошего!")

interface()