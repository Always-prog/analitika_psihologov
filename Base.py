import matplotlib.pyplot as plt


def razdel(file):
    output = []
    file = open(file,"r",encoding="utf-8")
    for i in file.readlines():
        i = i[0:-1]
        output.append(i)
    file.close()
    return output

def search(lists,char):
    lists = lists
    char = char
    list_char = list(char)
    pov = 0
    povtr = 0
    for i in range(len(list(lists))):
        if list_char[pov] == lists[i]:
            pov += 1
        else:
            pov = 0
        if pov >= len(list_char):
            povtr += 1
            pov = 0
    return povtr



result_small = razdel("b17_mini_text.txt")
result_zag = razdel("b17_zag.txt")

def vibor1():
    s = input("повторение какого слова вы хотите найти в статях: ")
    result_search = 0
    for small in result_small:
        result_search += search(small,s)
    print("слово '"+s+"' найдено: " + str(result_search) + " раз")

def vibor2():
    print("впишите в тесктовый файл слова в столбик, и я их прочитаю 'slova.txt', не забудте на последнем слове поставить '/'")
    s = razdel("slova.txt")
    s_num = []
    s_name = []
    result_search = 0
    for j in range(len(s)):
        for small in result_small:
            result_search += search(small,s[j])
        s_num.append(result_search)
        s_name.append(s[j])
        result_search = 0
    plt.bar(s_name,s_num) 
    plt.show() 

def vibor3():
    list_pov = []
    list_pov_names = razdel("RUS.txt")
    for index in range(len(list_pov_names)):
        for small in result_small:
            result_search += search(small,list_pov_names[index])
        list_pov.append(result_search)
        result_search = 0
    list_pov,list_pov_names = puzirok(list_pov,list_pov_names)


def puzirok(list_pov,list_pov_names):
    for i in range(len(list_pov) + 1):
        if list_pov[i-1] > list_pov[i]:
            list_pov[i],list_pov[i-1] = list_pov[i-1],list_pov[i]
            list_pov_names[i],list_pov_names[i-1] = list_pov_names[i-1],list_pov_names[i]
    return list_pov, list_pov_names

print("если вы хотите увидеть чило использований одного слова, впишите '1'")
print("если вы хотите увидеть график на основе слов из файла 'slova.txt' впишите 2")
print("если же вы хотите выйти из программы вишите 'конец'")
while True:
    try:
        vibor = input("вписывайте: ")
        if vibor == "1":
            vibor1()
        elif vibor == "2":
            vibor2()
        elif vibor == "3":
            vibor3()
        elif vibor == "конец":
            print("программа закончена")
            break
        else:
            print("вы не вписали кикакой из вариантов")
    except(BaseException):
        print("произошла ошибка в получении данных пользователем, попробуйте еще раз")



