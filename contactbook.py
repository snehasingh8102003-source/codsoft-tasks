from tkinter import*
from tkinter import messagebox
contact=Tk()
contact.title("Contact Book")


contacts = []
def add_contact():
    name=name_entry.get().strip()
    phonenumber=phone_entry.get().strip()
    email=email_entry.get().strip()
    address=address_entry.get().strip()

    if name == " " or phonenumber == " ":
        messagebox.showerror("Error","Name and phonenumber are required")
        return
    
    contacts.append([name,phonenumber,email,address])
    update_listbox()

def update_contact():
    try:
        selected_index = contact_list.curselection()[0]
    except IndexError:
        messagebox.showerror("Error", "Select a contact to update")
        return
    
    name=name_entry.get()
    phonenumber=phone_entry.get()
    email=email_entry.get()
    address=address_entry.get()

    if name == " " or phonenumber == " ":
        messagebox.showerror("Error","Name and Phonenumber are required")
        return
    
    contacts[selected_index] = [name,phonenumber,email,address]
    update_listbox()

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        del contacts[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showerror("Error", "Select a contact to delete")

def view_contact():
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contacts[selected_index]
        name_entry.delete(0, END)
        name_entry.insert(END, selected_contact[0])
        phone_entry.delete(0, END)
        phone_entry.insert(END, selected_contact[1])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_contact[2])
        address_entry.delete(0, END)
        address_entry.insert(END,selected_contact[3])
    except:
        pass

def update_listbox():
    contact_list.delete(0, END)
    for contact in contacts:
        contact_list.insert(END, contact[0]+"|"+contact[1])


frame = Frame(contact)
frame.pack(pady=10)

Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
Label(frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
Label(frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
Label(frame, text="Address").grid(row=3, column=0, padx=5)

name_entry = Entry(frame)
phone_entry = Entry(frame)
email_entry = Entry(frame)
address_entry = Entry(frame)

name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry.grid(row=2, column=1, padx=5, pady=5)
address_entry.grid(row=3, column=1, padx=5, pady=5)

button_frame= Frame(contact)
button_frame.pack(pady=5)

add_button=Button(button_frame, text="Add",width=10,command=add_contact)
update_button=Button(button_frame, text="Update",width=10,command=update_contact)
delete_button=Button(button_frame, text="Delete",width=10,command=delete_contact)
view_button=Button(button_frame,text="view",width=10,command=view_contact)

add_button.grid(row=0, column=0, padx=5)
update_button.grid(row=0, column=1, padx=5)
delete_button.grid(row=0, column=2, padx=5)
view_button.grid(row=0, column=4, padx=5)

contact_list=Listbox(contact,height=10,width=50)
contact_list.pack(pady=10)
contact_list.bind('<<ListboxSelect>>',view_contact)

contact.mainloop()