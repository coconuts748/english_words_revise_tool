from tkinter import ttk,messagebox
import tkinter as tk
from loguru import logger
import sys
import time
from revise_progress import revise_progress
from about_vocabulary import cet_4_default_vocabulary,self_vocabulary,create_self_vocabulary

def ui_page_2():    #模式选择

    def main_functions_menu_descriptions():
        logger.info('main functions menu descriptions routine....')
        ######内置text......###################
        def quit_descriptions_show():
            if messagebox.askyesno('tips', 'be sure to quit?'):
                descriptions_show_root.destroy()
        def descriptions_show():
            descriptions_show_text.insert(tk.END,'firstly,you’d better choose one mode which you like………\n')
            time.sleep(2)
            descriptions_show_root.update_idletasks()

            descriptions_show_text.insert(tk.END,'then you could use default vocabulary or something you input \n')
            time.sleep(2)
            descriptions_show_root.update_idletasks()

            descriptions_show_text.insert(tk.END,'lastly,set up the fractions you wanna get,then start it!\n')
            time.sleep(2)
            descriptions_show_root.update_idletasks()

            time.sleep(2)
            ttk.Button(descriptions_show_root,text='finish reading ',command=quit_descriptions_show).pack()
            descriptions_show_root.update_idletasks()


        descriptions_show_root=tk.Tk()
        descriptions_show_root.title('descriptions')

        descriptions_show_text=tk.Text(descriptions_show_root)
        descriptions_show_text.pack()

        ttk.Button(descriptions_show_root,text='start reading ',command = descriptions_show).pack()

        descriptions_show_root.mainloop()

    def default_vocabulary_revise_mode():
        logger.info('default_vocabulary_revise_mode running.....')
        revise_progress(object___=cet_4_default_vocabulary)

    def diy_vocabulary_revise_mode():
        logger.info('diy_vocabulary_revise_mode running.....')
        create_self_vocabulary()
        revise_progress(object___=self_vocabulary)

    def quit_ui_page_2():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            ui_page_2_root.destroy()
            sys.exit()

    ui_page_2_root = tk.Tk()
    ui_page_2_root.title('main functions menu')

    ttk.Button(ui_page_2_root,text='description',command = main_functions_menu_descriptions).pack()
    ttk.Button(ui_page_2_root,text='cet-4 revise',command = default_vocabulary_revise_mode).pack()
    ttk.Button(ui_page_2_root,text='fiy revise',command = diy_vocabulary_revise_mode).pack()
    ttk.Button(ui_page_2_root,text='quit',command = quit_ui_page_2).pack()
    ui_page_2_root.mainloop()


