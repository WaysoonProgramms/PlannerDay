import customtkinter as CTk  # Импортируется под пользовательским названием CTk
from PIL import Image
import datetime
import configparser


# Выставление параметров стиля окна
CTk.set_appearance_mode("System")  # Тема окна
CTk.set_default_color_theme("dark-blue")  # Стандартный цвет


# Функции
def note():  # Функция создания новой заметки
    global create

    # Создание окна
    create = CTk.CTk()
    create.geometry("430x280")
    create.title("Создать новую заметку...")
    create.iconbitmap("resources/images/icon.ico")
    create.resizable(False, False)

    # Объявление заголовка для поля ввода заголовка заметки
    create.lable_name = CTk.CTkLabel(master=create, text="Заголовок:")
    create.lable_name.place(y=5, x=10)

    # Объявление поля ввода заголовка заметки
    create.entry_name = CTk.CTkEntry(master=create, width=260)
    create.entry_name.place(x=8, y=30)

    # Объявление заголовка для выпадающего списка (поля ввода) со временем
    create.lable_time = CTk.CTkLabel(master=create, text="Время:")
    create.lable_time.place(x=280, y=5)

    # Объявление выпадающего списка (combobox) для времени
    create.combobox_time = CTk.CTkComboBox(master=create, values=["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00",
                                                                  "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00",
                                                                  "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"])
    time = datetime.datetime.now()
    create.combobox_time.set(time.strftime("%X"))
    create.combobox_time.place(x=280, y=30)

    # Объявление заголовка для описания заметки
    create.lable_description = CTk.CTkLabel(master=create, text="Описание:")
    create.lable_description.place(x=8, y=60)

    # Объявление поля ввода для описания заметки
    create.entry_description = CTk.CTkEntry(master=create, width=415, height=100)
    create.entry_description.place(x=8, y=83)

    # Объявление заголовка для бара меток
    create.lable_mark = CTk.CTkLabel(master=create, text="Метки:")
    create.lable_mark.place(x=8, y=190)

    # Объявление чекбокса для отметки важности
    create.checkBox_important = CTk.CTkCheckBox(master=create, text="Важно")
    create.checkBox_important.place(x=64, y=193)

    # Объявление кнопки для завершения заметки
    create.button_confirm = CTk.CTkButton(master=create, text="Создать", command=take, width=200)
    create.button_confirm.place(x=8, y=230)

    # Объявление кнопки отмены создания
    create.button_cancel = CTk.CTkButton(master=create, text="Отмена", command=close, width=200)
    create.button_cancel.place(x=220, y=230)

    create.mainloop()

def take():  # Функция обработки и вывода заметки

    data = configparser.ConfigParser()

    # Объявление фрейма заметки
    app.note_frame = CTk.CTkFrame(master=app.scrollbarFrame, width=420, height=120)
    app.note_frame.pack(pady=5, padx=5)

    # Объявление заголовка заметки в фрейме основного окна
    app.note_name = CTk.CTkLabel(master=app.note_frame, text=create.entry_name.get(), font=('Arial Black', 20))
    app.note_name.place(x=10, y=5)

    # Объявление описания заметки
    app.note_description = CTk.CTkLabel(master=app.note_frame, text=create.entry_description.get(), font=('Arial', 12))  # TODO Перевод строки
    app.note_description.place(x=10, y=30)

    # Объявление отображения введенного времени
    app.note_date = CTk.CTkLabel(master=app.note_frame, text=create.combobox_time.get())
    app.note_date.place(x=315, y=10)

    # Объявление кнопки удаления заметки
    app.note_delete = CTk.CTkButton(master=app.note_frame, text="Удалить", width=10, command=delete)
    app.note_delete.place(x=300, y=40)

    data[create.entry_name.get()] = {"Name": create.entry_name.get(),
                                     "Description": create.entry_description.get(),
                                     "Date": create.combobox_time.get()}

    with open('resources/saves/data.ini', 'w') as configfile:
        data.write(configfile)

    create.destroy()  # Закрытие окна после создания

def close():  # Функция закрытия окна создания заметки
    create.destroy()

def delete():  # Функция удаления заметки
    app.note_frame.destroy()

# Основной класс приложения. Здесь производится изначальная сборка окна
class App(CTk.CTk):

    def __init__(self):  # Объявление конструктора класса App
        super().__init__()

        # Создание основного окна
        self.geometry("430x630")
        self.title("DayPlanner")
        self.iconbitmap("resources/images/icon.ico")
        self.resizable(False, False)

        # Объявление иконки для кнопки
        self.button_image = CTk.CTkImage(dark_image=Image.open("resources/images/plus.png"))

        # Объявление кнопки создания заметки в основном окне
        self.button_add = CTk.CTkButton(master=self, text="Создать...", image=self.button_image, command=note, width=420)
        self.button_add.pack(pady=10, padx=10)

        # Объявления прокручевомаего фрейма
        self.scrollbarFrame = CTk.CTkScrollableFrame(master=self, width=390, height=560)
        self.scrollbarFrame.place(x=10, y=50)

        self.data = configparser.ConfigParser()

        with open('resources/saves/data.ini', 'r') as configfile:
            self.data.read(configfile)


# Запуск приложения в стандартном режиме
if __name__ == "__main__":
    app = App()  # Объявление объекта App
    app.mainloop()  # Сборка окна

# @WaysoonPrograms 2023