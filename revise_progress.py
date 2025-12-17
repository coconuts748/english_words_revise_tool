import random
from about_vocabulary import cet_4_default_vocabulary,self_vocabulary
from loguru import logger
import tkinter as tk
from tkinter import ttk,messagebox
import time



def revise_progress(object___):
    inner_test_list = []
    random_vocabulary = []
    answer_list = []

    logger.info(len(object___))
    for i in object___:
        # logger.info(i)
        inner_test_list.append(i)

    for x in list(range(0,len(object___)+1)):
        logger.info(x)
        random_test_word = random.choice(inner_test_list)
        random_vocabulary.append(random_test_word)
    logger.info('random vocabulary is stored successfully')

    ######### calculate correct rate############
    def calculate_correct_rate(calculate_object,default_object):
        right_number = []
        logger.info('calculate correct rate running .....')
        try:
            for r in list(range(0,len(calculate_object)+1)):
                if calculate_object[r] == default_object[r]:
                    right_number.append('right')
                elif calculate_object[r] != default_object[r]:
                    logger.info('wrong answer')
                else:
                    logger.info('something else wrong')

            right_rate = len(right_number)/len(calculate_object)
            return f'{right_rate}%'
        except Exception as e:
            logger.info(e)

    ######### calculate correct rate############
    try:
        def revise_check_question():
            logger.info('revise check question running ....')
            def show_random_questions():
                for o in random_vocabulary:
                    combine_question = f'{o}:\n'
                    logger.info(combine_question)
                    random_questions_text.insert(tk.END, f'{o}:\n')
                    time.sleep(0.5)
                    show_random_questions_root.update_idletasks()

                random_questions_text.insert(tk.END, 'all words are shown ,please answer them in sequences........')
                show_random_questions_button.config(text='then start answer the questions......')

            show_random_questions_root = tk.Tk()
            show_random_questions_root.title('watching the questions')

            random_questions_text = tk.Text(show_random_questions_root)
            random_questions_text.pack()

            show_random_questions_button = ttk.Button(show_random_questions_root, text='show random questions', command=show_random_questions)
            show_random_questions_button.pack()
            show_random_questions_root.mainloop()

        def revise_input_answer():
            logger.info('revise input answer running ....')
            def show_input_answer():
                show_input_answer_root.destroy()
                for p in list(range(1,len(random_vocabulary)+2)):
                    def single_answer_page():
                        single___answer_before = str(single___answer.get().strip())
                        try:
                            if single___answer_before is None or len(single___answer_before) == 0:
                                input_answer = 'none'
                                logger.info(f'question{p} is none......')
                                answer_list.append(input_answer)
                                single_answer_page_root.destroy()
                                show_input_answer_root.quit()
                            else:
                                input_answer = single___answer_before
                                answer_list.append(input_answer)
                                logger.info(f'question{p} answer : {single___answer_before} is stored')
                                single_answer_page_root.destroy()
                                show_input_answer_root.quit()
                        except Exception as e:
                            logger.error(f'{e}')
                            single_answer_page_root.destroy()
                            show_input_answer_root.quit()

                    single_answer_page_root = tk.Tk()
                    single_answer_page_root.title("it's number {}".format(p))

                    ttk.Label(single_answer_page_root,text=f'question{p}:').grid(row=1,column=0,columnspan=2)
                    single___answer = ttk.Entry(single_answer_page_root)
                    single___answer.grid(row=1,column=3,columnspan=3)

                    single_answer___button = ttk.Button(single_answer_page_root,text='next question',command=single_answer_page)
                    single_answer___button.grid(row=2,column=0,columnspan=2)
                    single_answer_page_root.mainloop()

                calculate_correct_rate(calculate_object=answer_list,default_object=random_vocabulary)

            show_input_answer_root = tk.Tk()
            show_input_answer_root.title('answering the questions in sequences')

            ttk.Button(show_input_answer_root, text='start answer', command=show_input_answer).pack()
            show_input_answer_root.mainloop()

        def quit_revise_page():
            if messagebox.askyesno('tips','be sure to quit?'):
                revise_main_page.destroy()

        revise_main_page = tk.Tk()
        revise_main_page.title('revise menu')

        ttk.Label(revise_main_page,text='please click "check" button firstly,then click answer to input the answer in sequences').pack()

        ttk.Button(revise_main_page,text='check',command=revise_check_question).pack()
        ttk.Button(revise_main_page,text='answer',command=revise_input_answer).pack()
        ttk.Button(revise_main_page,text='quit',command=quit_revise_page).pack()
        revise_main_page.mainloop()

    except Exception as error:
        logger.error(error)

if __name__ == '__main__':
    revise_progress(object___=cet_4_default_vocabulary)