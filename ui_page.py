from tkinter import ttk,messagebox
import tkinter as tk
from loguru import logger
import time
import sys
import json

from vocabulary_cite_here import vocabulary_tool_encryption
from accounts_else import vocabulary_tool_add_account,vocabulary_tool_check_account
from ui_page_2 import ui_page_2

def vocabulary_tool_login():

    def registration_function():
        logger.info('registration_function running...')
        def ui_register():
            ui_register_name_before = str(ui_register_name.get().strip())
            ui_register_code_before = str(ui_register_code.get().strip())

            try:
                if ui_register_name_before is None or len(ui_register_name_before) == 0:
                    messagebox.showwarning('Error','Invalid Input!')
                elif ui_register_code_before is None or len(ui_register_code_before) == 0:
                    messagebox.showwarning('Error','Invalid Input!')
                else:
                    if messagebox.askyesno('Tips',f'The relevant message :\n{ui_register_name_before}:{ui_register_code_before}\be sure about it?'):
                        vocabulary_tool_add_account(name=ui_register_name_before, code=ui_register_code_before)
                        messagebox.showinfo('Success','Successfully Registered!')

                        registration_button.config(text='done')
                        return

            except Exception as e:
                logger.error(e)

        def quit_ui_register():
            if messagebox.askyesno('Tips','be sure about it?'):
                ui_register_root.destroy()
                return

        ui_register_root = tk.Tk()
        ui_register_root.title('registration page')

        ttk.Label(ui_register_root,text='account:').grid(row=1,column=0,columnspan=2)
        ui_register_name = ttk.Entry(ui_register_root)
        ui_register_name.grid(row=1,column=3,columnspan=3)

        ttk.Label(ui_register_root,text='name:').grid(row=2,column=0,columnspan=2)
        ui_register_code = ttk.Entry(ui_register_root)
        ui_register_code.grid(row=2,column=3,columnspan=3)

        registration_button  =ttk.Button(ui_register_root,text='store',command=ui_register)
        registration_button.grid(row=3,column=0,columnspan=2)

        ttk.Button(ui_register_root,text='quit',command=quit_ui_register).grid(row=3,column=3,columnspan=2)
        ui_register_root.mainloop()

    def login_function():
        logger.info('login_function running...')
        def ui_login():
            ui_login_name_before = str(ui_login_name.get().strip())
            ui_login_code_before = str(ui_login_code.get().strip())
            try:
                if ui_login_name_before is None or len(ui_login_name_before) == 0:
                    messagebox.showwarning('Error','Invalid Input!')
                elif ui_login_code_before is None or len(ui_login_code_before) == 0:
                    messagebox.showwarning('Error','Invalid Input!')
                else:
                    if messagebox.askyesno('Tips',f'be sure about it?\n{ui_login_name_before}:{ui_login_code_before}'):
                        vocabulary_tool_check_account(verify_name=ui_login_name_before, verify_code=ui_login_code_before)
                        try:
                            with open('whether_check_correct.json','rb') as f:
                                test_result = json.load(f)
                                print(test_result)
                                # test_result_ = json.loads(test_result)
                                # print(test_result_)
                                if test_result['result'] == 'correct':   #验证成功
                                    logger.info('login success............')
                                    ui_login_root.destroy()
                                    if messagebox.askyesno('login successfully!','enter the next step?'):
                                        functions_main_root.destroy()
                                        #####
                                        ui_page_2()
                                        #####
                                elif test_result['result'] == 'wrong':
                                    ui_login_root.destroy()
                                    messagebox.showwarning('Login Failed!','your message is incorrect')
                                    return  #?
                                else:
                                    logger.info('something wrong.....')

                        except Exception as ee:
                            logger.error(ee)

            except Exception as e:
                logger.error(e)

        def quit_ui_login():
            if messagebox.askyesno('Tips','be sure about it?'):
                ui_login_root.destroy()
                return

        ui_login_root = tk.Tk()
        ui_login_root.title('login page')

        ttk.Label(ui_login_root,text='name:').grid(row=1,column=0,columnspan=2)
        ui_login_name = ttk.Entry(ui_login_root)
        ui_login_name.grid(row=1,column=3,columnspan=3)

        ttk.Label(ui_login_root,text='code:').grid(row=2,column=0,columnspan=2)
        ui_login_code = tk.Entry(ui_login_root)
        ui_login_code.grid(row=2,column=3,columnspan=3)

        ttk.Button(ui_login_root,text='Login!',command=ui_login).grid(row=3,column=0,columnspan=2)
        ttk.Button(ui_login_root,text='Quit!',command=quit_ui_login).grid(row=3,column=3)
        ui_login_root.mainloop()

    def quit_function():
        logger.info('quit_function running...')
        if messagebox.askyesno('tips','be sure to quit?'):
            messagebox.showinfo('.....','thanks for using')
            time.sleep(2)
            sys.exit()

    functions_main_root = tk.Tk()
    functions_main_root.title('.........')

    ttk.Label(functions_main_root,text='registration below....').pack()
    ttk.Button(functions_main_root,text='registration',command=registration_function).pack()

    ttk.Label(functions_main_root,text='login below....').pack()
    ttk.Button(functions_main_root,text='login',command=login_function).pack()

    ttk.Button(functions_main_root,text='quit',command=quit_function).pack()

    functions_main_root.mainloop()


if __name__ == '__main__':
    vocabulary_tool_login()