from tkinter import ttk,messagebox
import tkinter as tk
from loguru import logger

cet_4_default_vocabulary = {
    '益处,好处;救济金': 'benefit',
    '平均的;平常的':'average',
    '计划,方案,节目':'program',
    '集中;焦点':'focus',
    '据...所说':'according to',
    '影响':'effect',
    '单独的，个别的':'individual',
    '缺乏,不足':'lack',
    '最近的,近来的':'recent',
    '系统,体系;制度':'system',
    '倾向;趋于':'tend',
    '(数量上)达到;相当于':'amount',
    '质量,品质;品德':'quality',
    '影响;使感动;假装':'affect',
    '影响;使感动':'impact',
    '议题;问题;担忧':'issue',
    '履历,生涯,工作经历':'career',
    '减少,缩小': 'reduce',
    '十年;十年期': 'decade',
    '毕业;大学毕业生': 'graduate',
    '潜在的,可能的': 'potential',
    '关心;关爱;担心': 'concern',
    '时机,机会': 'opportunity',
    '进程,过程': 'process',
    '数据,资料': 'data',
    '因素,要素': 'factor',
    '获得,受益': 'gain',
    '各种不同的,各种各样的': 'various',
    '挑战,质疑': 'challenge',
    '捐献,投稿': 'contribute',
    '促进;提升;晋级': 'promote',
    '要求,需要': 'decline',
    '数字;人物': 'demand',
    '转移;快速移动': 'figure',
    '账户;叙述': 'shift',
    '应用;申请': 'account',
    '速度;比率': 'apply',
    '参加;雇用': 'rate',
    '购买;买': 'engage',
    '遭受;受苦': 'purchase',
    '吸引注意': 'suffer',
    '作家;作者': 'attract',
    '当前的;趋势': 'author',
    '牵涉,影响': 'current',
    '参加;参与': 'involve',
    '一系列;范围': 'range',
    '认识到,知道': 'realize',
    '唯一的,独一无二的': 'unique',
    '使用权,机会,入口': 'access',
}

self_vocabulary = {}

def create_self_vocabulary():
    def creat__self():
        logger.info('creat__self running.....')
        def param_detail_setting_step_one():
            ensure_dic_number_before = int(ensure_dic_number.get().strip())
            try:
                # if ensure_dic_number_before is None :
                #     messagebox.showwarning('error','input invalid')
                # elif ensure_dic_number_before is not int:
                #     messagebox.showwarning('error', 'input invalid')
                # else:
                    if messagebox.askyesno('tips',f'your input is {ensure_dic_number_before},\n enter next step?'):

                        param_detail_setting_step_one_root.destroy()
                        param_detail_setting_step_one_root.quit() #???

                        for u in list(range(1, ensure_dic_number_before + 2)):
                            logger.info('number {} single vocabulary setting'.format(u))

                            def param_detail_setting_step_two():
                                if messagebox.askyesno('tips',f'messages: {diy_meaning}:{diy_word}\n be sure about it?'):
                                    self_vocabulary[diy_meaning] = diy_word
                                    param_detail_setting_step_two_root.destroy()
                                    param_detail_setting_step_two_root.quit()
                                    return self_vocabulary

                            param_detail_setting_step_two_root = tk.Tk()
                            param_detail_setting_step_two_root.title(f"it's number {u}")

                            ttk.Label(param_detail_setting_step_two_root,text='meaning:').grid(row=1,column=0,columnspan=2)
                            diy_meaning = ttk.Entry(param_detail_setting_step_two_root)
                            diy_meaning.grid(row=1,column=4,columnspan=3)

                            ttk.Label(param_detail_setting_step_two_root,text='word:').grid(row=2,column=0,columnspan=2)
                            diy_word = ttk.Entry(param_detail_setting_step_two_root)
                            diy_word.grid(row=2,column=4,columnspan=3)
                            ttk.Button(param_detail_setting_step_two_root,text='save',command=param_detail_setting_step_two).grid(row=3,column=0,columnspan=2)
                            param_detail_setting_step_two_root.mainloop()

            except Exception as e:
                logger.error(e)

        param_detail_setting_step_one_root = tk.Tk()
        param_detail_setting_step_one_root.title('setting your revise vocabulary number')

        ttk.Label(param_detail_setting_step_one_root,text='number:').grid(row=1,column=0)
        ensure_dic_number = ttk.Entry(param_detail_setting_step_one_root)
        ensure_dic_number.grid(row=1,column=1,columnspan=3)

        ttk.Button(param_detail_setting_step_one_root,text='enter next step',command=param_detail_setting_step_one).grid(row=2,column=0,columnspan=2)

        param_detail_setting_step_one_root.mainloop()


    def quit__self():
        if messagebox.askyesno('tips','be sure to quit?'):
            self_self.destroy()
            self_self.quit()

    self_self = tk.Tk()
    self_self.title('diy option details')

    ttk.Button(self_self,text='param setting',command=creat__self).pack(side='left')
    ttk.Button(self_self,text='quit',command=quit__self).pack(side='right')

    self_self.mainloop()

