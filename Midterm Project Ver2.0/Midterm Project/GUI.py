from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import update
from Clock import DigitalClock
import Database

class GUI:
    def __init__(self, root, account):
        self.window = root
        self.window.title("Newspaper Management Application")
        self.window.geometry("1000x700")
        self.window.grid()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # This variable to open different accounts
        self.account = account
        
        # Variable
        self.article_title = StringVar()
        self.author = StringVar()
        self.date = StringVar()
        self.category = StringVar()
        self.link = StringVar()

        self.frame_left = Frame(self.window, bg="#DAE5D0")
        self.frame_left.place(x=0, y=0, width=242, height=700, relwidth=1, relheight=1)

        self.frame_right = Frame(self.window, bg="#FEFBE7")
        self.frame_right.place(x=242, y=0, relwidth=1, relheight=1)

        # Label that show clock
        clockLabel = Label(self.frame_left, font=('calibri', 34, 'bold'), background='#F9EBC8', foreground='black')
        digital_clock = DigitalClock(self.frame_left, clockLabel)


        # Button in the left frame
        self.save_news = Button(self.frame_left, text="Save News", highlightthickness=0, bg="#A0BCC2", command=self.save_data).place(x=33, y=464, width=175, height=36)
        self.update_news = Button(self.frame_left, text="Update News", highlightthickness=0, bg="#A0BCC2", command=self.update_data).place(x=33, y=520, width=175, height=36)
        self.delete_news = Button(self.frame_left, text="Delete News", highlightthickness=0, bg="#A0BCC2", command=self.delete_data).place(x=33, y=577, width=175, height=36)
        self.reset_news = Button(self.frame_left, text="Reset News", highlightthickness=0, bg="#A0BCC2",command=self.delete_all_data).place(x=33, y=633, width=175, height=36)
        Button(self.frame_left, text="Logouts", highlightthickness=0, bg="#A0BCC2",command=self.logout).place(x=33, y=400, width=175, height=36)


        # Button in the right frame
        
        #This variable to choose what kind of search do you want to use
        self.type_of_search = StringVar()
        self.search = StringVar()
        
        self.search_news = Button(self.frame_right, text="Search", highlightthickness=0, bg="#A0BCC2", command=self.search_data).place(x=80, y=76, width=70, height=30)
        Button(self.frame_right, text="Show all", highlightthickness=0, bg="#A0BCC2", command=self.display_data).place(x=80, y=96, width=70, height=30)
        self.search_news_text = Entry(self.frame_right, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.search).place(x=270, y=76, width=411, height=30)

        self.search_choose = ttk.Combobox(self.frame_right, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.type_of_search)
        self.search_choose['values'] = ('Option', 'Title', 'Author', 'Date', 'Category')
        self.search_choose.current(0)
        self.search_choose.place(x=159, y=76, width=100, height=30)


        # Middle Frame that contain input information of the newspaper
        self.mid_frame = Frame(self.frame_right, bg="#C4C4C4")
        self.mid_frame.place(x=80, y=138, width=599, height=203)

        # Widget for the middle frame
        self.title_news = Label(self.mid_frame, text="Article Title", highlightthickness=0, bg="#A0BCC2").place(x=15, y=15, width=121, height=21)
        self.author_news = Label(self.mid_frame, text="Author", highlightthickness=0, bg="#A0BCC2").place(x=15, y=55, width=121, height=21)
        self.date_news = Label(self.mid_frame, text="Write in date: ", highlightthickness=0, bg="#A0BCC2").place(x=15, y=95, width=121, height=21)
        self.category_news = Label(self.mid_frame, text="Category: ", highlightthickness=0, bg="#A0BCC2").place(x=15, y=135, width=121, height=21)
        self.link_news = Label(self.mid_frame, text="Link: ", highlightthickness=0, bg="#A0BCC2").place(x=15, y=175, width=121, height=21)

        # Entry for the middle frame
        self.title_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.article_title)
        self.title_text.place(x=159, y=15, width=400, height=21)

        self.author_text = Entry(self.mid_frame, font=('arial', 12, 'bold'),  width=404, justify=LEFT, textvariable=self.author)
        self.author_text.place(x=159, y=55, width=400, height=21)

        self.date_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.date)
        self.date_text.place(x=159, y=95, width=400, height=21)

        #self.category_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT).place(x=159, y=135, width=400, height=21)
        self.category_choose = ttk.Combobox(self.mid_frame, width=39, font=('Century Gothic', 12), state='readonly', textvariable=self.category)
        self.category_choose['values'] = ('Business',
                                        'Travel',
                                        'Life',
                                        'Sport',
                                        'Weather',
                                        'Criminal',
                                        'Medical')
        self.category_choose.current()
        self.category_choose.place(x=159, y=135, width=400, height=25)
        self.link_text = Entry(self.mid_frame, font=('arial', 12, 'bold'), width=404, justify=LEFT, textvariable=self.link)
        self.link_text.place(x=159, y=175, width=400, height=21)

        # Bottom Frame that list information of the newspaper
        self.bottom_frame = Frame(self.frame_right, bg="#A0BCC2")
        self.bottom_frame.place(x=80, y=351, width=599, height=301)

        # -------------------------------Treeview-------------------------------
        scroll_x = Scrollbar(self.bottom_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.bottom_frame, orient=VERTICAL)

        columns = ('ID', 'title', 'author', 'date', 'category', 'link')
        self.newspaper_list = ttk.Treeview(self.bottom_frame, height=12,
                                           columns=columns,
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set,)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.newspaper_list.heading('ID', text='ID')
        self.newspaper_list.heading('title', text='Title')
        self.newspaper_list.heading('author', text='Author')
        self.newspaper_list.heading('date', text='Date')
        self.newspaper_list.heading('category', text='Category')
        self.newspaper_list.heading('link', text='Link')


        self.newspaper_list['show'] = 'headings'

        self.newspaper_list.column('ID', width=20)
        self.newspaper_list.column('title', width=70)
        self.newspaper_list.column('author', width=70)
        self.newspaper_list.column('date', width=70)
        self.newspaper_list.column('category', width=70)
        self.newspaper_list.column('link', width=70)

        self.newspaper_list.pack(fill=BOTH, expand=1)

        self.newspaper_list.bind('<ButtonRelease-1>', self.clicker)
        self.display_data()

        self.choose_row()

    def save_data(self):
        if self.article_title.get() == "" or self.author.get() == "" or self.category.get() == "" or self.link.get() == "":
            tkinter.messagebox.askokcancel(title='Nả ní',
                                           message='Please enter valid data')
        else:
            try:
                Database.add(self.account,
                             self.article_title.get(),
                             self.author.get(),
                             self.date.get(),
                             self.category.get(),
                             self.link.get())
                self.display_data()
                tkinter.messagebox.showinfo(title='Message',
                                            message='Sucessful added news')
                self.title_text.delete(0, END)
                self.author_text.delete(0, END)
                self.date_text.delete(0, END)
                self.link_text.delete(0, END)
            except Exception as es:
                tkinter.messagebox.showerror(title='ERROR',
                                             message=f'Because {str(es)}')

    def display_data(self):
        """Display all data by fetch data"""
        data = Database.display(account=self.account)
        if len(data) >= 0:
            self.newspaper_list.delete(*self.newspaper_list.get_children())
            for i in data:
                self.newspaper_list.insert("", END, value=i)

    def choose_row(self):
        """Choose a row and return values into entries"""
        self.title_text.delete(0, END)
        self.author_text.delete(0, END)
        self.date_text.delete(0, END)
        self.link_text.delete(0, END)
        # Choose a value of a row
        choose_row = self.newspaper_list.focus()
        # Grab the value of the chosen row
        self.data = self.newspaper_list.item(choose_row, 'value')
        try:
            self.id = self.data[0]
            self.article_title.set(self.data[1])
            self.author.set(self.data[2])
            self.date.set(self.data[3])
            self.category.set(self.data[4])
            self.link.set(self.data[5])
        except:
            pass

    def clicker(self, event):
        """Click handler when you click into a row"""
        self.choose_row()

    def update_data(self):
        if self.article_title.get() == "" or self.author.get() == "" or self.category.get() == "" or self.link.get() == "":
            tkinter.messagebox.askretrycancel(title='Oh no', message='Please choose a data')
        else:
            try:
                answer = tkinter.messagebox.askyesno("Chotto matte", "Do you want to update information?")
                if answer:
                    Database.update(self.account,
                                    self.id,
                                    self.article_title.get(),
                                    self.author.get(),
                                    self.date.get(),
                                    self.category.get(), 
                                    self.link.get())
                else:
                    if not update:
                        return
                self.display_data()
            except Exception as e:
                tkinter.messagebox.showerror("ERROR", f"Because of {str(e)}")

        # Fill in empty into the entries
        self.title_text.delete(0, END)
        self.author_text.delete(0, END)
        self.date_text.delete(0, END)
        self.link_text.delete(0, END)
        
    def delete_data(self):
        if not self.newspaper_list.selection():
            tkinter.messagebox.showwarning("ERROR", "Please choose a data you want to delete")
        else:
            answer = tkinter.messagebox.askyesno("Hmm", "Do you really want to delete this?")
            if answer:
                Database.delete(self.account, self.id)
                self.display_data()
                self.title_text.delete(0, END)
                self.author_text.delete(0, END)
                self.date_text.delete(0, END)
                self.link_text.delete(0, END)
                tkinter.messagebox.showinfo("Delete", "You deleted the data")
            
    def delete_all_data(self):
        """A function to delete all data and drop table"""
        answer = tkinter.messagebox.askyesno("Wait", "Do You really want to delete all data!")
        if answer:
            Database.delete_all(self.account)
            self.display_data()
            # Fill in empty into the entries
            self.title_text.delete(0, END)
            self.author_text.delete(0, END)
            self.date_text.delete(0, END)
            self.link_text.delete(0, END)

    def logout(self):
        self.window.destroy()

    def on_closing(self):
        quit()

    def search_data(self):
        if self.type_of_search == "Option" or self.search == "":
            tkinter.messagebox.showwarning("Opps", "Please choose the attribute?")
        else:
            try:
                data = Database.search(self.account, self.type_of_search.get(), self.search.get())
                if len(data) >= 0:
                    self.newspaper_list.delete(*self.newspaper_list.get_children())
                    for i in data:
                        self.newspaper_list.insert("", END, value=i)
            except:
                tkinter.messagebox.showwarning("Warning", "Please choose the attribute?")