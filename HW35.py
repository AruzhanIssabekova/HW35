from tkinter import *
from db_con import *

def re_render_list(listbox):
    listbox.delete(0, END)
    values =show_contacts(mycursor)
    for contact in values:
        listbox.insert(END, contact)

window=Tk()
window.title("Контакты")
window.geometry("720x480")
# window.iconbitmap(r'./assets/icon.ico')
window.resizable(False, False)


left_frame= Frame()

Label(left_frame, text='Список').pack()
user_list=Listbox(left_frame)
re_render_list(user_list)

user_list.pack(side=LEFT, fill=BOTH, expand=True)

left_frame.pack(fill=BOTH, side=LEFT, expand=True)


right_frame = Frame(bg="#eee")
Label(right_frame, text='Добавить контакт').pack()

username_text = Text(right_frame, height=1, width=30)
username_text.pack()

def create_contact_handler():
    create_contact(username_text.get(1.0, END))
    re_render_list(user_list)

def update_contact_handler():
    selected_contact = user_list.curselection()
    if selected_contact:
        new_name = username_text.get(1.0, END)
        update_contact(mycursor, user_list.get(selected_contact), new_name)
        re_render_list(user_list)

def delete_contact_handler():
    selected_contact = user_list.curselection()
    if selected_contact:
        delete_contact(mycursor, user_list.get(selected_contact))
        re_render_list(user_list)

Button(right_frame, text="Сохранить", command=create_contact_handler).pack()
Button(right_frame, text="Обновить", command=update_contact_handler).pack()
Button(right_frame, text="Удалить", command=delete_contact_handler).pack()

right_frame.pack(fill=BOTH, side=RIGHT, expand=True)

window.mainloop()