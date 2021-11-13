import tkinter as tk
from tkinter import *
import tkinter.filedialog
import pdf_hard
import pdf_easy
import pdf_normal

sys.setrecursionlimit(5000)


class Aef(object):
    def __init__(self):
        """
        主要用于定义框体布局和对应button的事件
        """
        self.title = 'PDF转换器'
        self.input_file_path = ''
        self.output_file_path = ''
        # 窗口取名
        self.root = tk.Tk(className=self.title)
        # 窗口大小
        self.root.geometry('600x250')
        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)

        # Menu菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        mp4menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='网络情报获取大作业', menu=mp4menu)

        # 控件内容设置
        group1 = tk.Label(frame_1, text='请选择文件夹路径（用于输入）：', fg='blue', font=("黑体", 10), anchor='w')
        self.entry1 = tk.Entry(frame_1, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        select1 = tk.Button(frame_1, text="选择PDF文件夹", font=('楷体', 10), fg='black', width=20, height=1,
                            command=self.input_path)
        group2 = tk.Label(frame_1, text='请选择文件夹路径（用于输出）：', fg='black', font=("黑体", 10), anchor='w')
        self.entry2 = tk.Entry(frame_1, highlightcolor='Fuchsia', highlightthickness=1, width=35, )
        select2 = tk.Button(frame_1, text="选择PDF文件夹", font=('楷体', 10), fg='black', width=20, height=1,
                            command=self.output_path)
        play_easy = tk.Button(frame_2, text="速度模式", font=('楷体', 12), fg='Purple', width=8, height=2, command=self.easy)
        play_normal = tk.Button(frame_2, text="普通模式", font=('楷体', 12), fg='Purple', width=8, height=2,
                                command=self.normal)
        play_hard = tk.Button(frame_2, text="准确模式", font=('楷体', 12), fg='Purple', width=8, height=2, command=self.hard)
        label_explain = tk.Label(frame_3, fg='red', font=('楷体', 12),
                                 text='\n速度模式：拥有最快的识别速度，但仅能保证标准内容的PDF文件识别准确率\n普通模式：拥有较快'
                                      '的识别速度，能保证识别出大多数情况下的PDF文件内容\n准确模式：拥有最慢的识别速度，但能保证识别出PDF文件中绝大部分的内容')
        label_warning = tk.Label(frame_3, fg='blue', font=('楷体', 12), text='\nPDF识别内容将会保存在输出文件夹目录下<PDF识别内容>\n')

        # 控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)
        select1.grid(row=0, column=2)
        group2.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        select2.grid(row=1, column=2)
        play_easy.grid(row=0, column=2, padx=5, pady=10)
        play_normal.grid(row=0, column=3, padx=5, pady=10)
        play_hard.grid(row=0, column=4, padx=5, pady=10)
        label_explain.grid(row=1, column=0)
        label_warning.grid(row=2, column=0)

    def input_path(self):
        """
        :return: 修改self.input_file_path和entry1的内容
        """
        input_filename = tk.filedialog.askdirectory()
        self.input_file_path = input_filename
        if input_filename != '':
            # 这里的思路是，需要先将entry1输入框改为”普通模式“，然后才能对其修改，修改后变为“只读模式”，不允许用户修改，下同理。
            self.entry1.config(state='normal')
            self.entry1.delete(0, END)
            self.entry1.insert(0, input_filename)
            self.entry1.config(state='readonly')
        else:
            self.entry1.config(text='您没有选择任何文件')

    def output_path(self):
        """
        :return: 修改self.output_file_path和entry2的内容
        """
        output_filename = tk.filedialog.askdirectory()
        self.output_file_path = output_filename
        if output_filename != '':
            self.entry2.config(state='normal')
            self.entry2.delete(0, END)
            self.entry2.insert(0, output_filename)
            self.entry2.config(state='readonly')
        else:
            self.entry2.config(text='您没有选择任何文件')

    def easy(self):
        """
        开启速度模式
        :return: 在指定位置输出识别的文本内容（准确率不高，速度最快）
        """
        if self.input_file_path != '' and self.output_file_path != '':
            pdf_easy.run(self.input_file_path, self.output_file_path)

    def hard(self):
        """
        开启准确模式
        :return: 在指定位置输出识别的文本内容（准确率最高，速度最慢）
        """
        if self.input_file_path != '' and self.output_file_path != '':
            pdf_hard.run(self.input_file_path, self.output_file_path)

    def normal(self):
        """
        开启普通模式
        :return: 在指定位置输出识别的文本内容（准确率较高，速度较慢）
        """
        if self.input_file_path != '' and self.output_file_path != '':
            pdf_normal.run(self.input_file_path, self.output_file_path)

    def loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    dd = Aef()
    dd.loop()
