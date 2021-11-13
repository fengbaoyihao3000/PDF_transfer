# PDF识别器

---

[toc]

---

##  一、程序总体外观与功能介绍

### 1.运行main.py后出现以下界面

> ![image-20211113224359335](https://i.loli.net/2021/11/13/dNOeDZnMpTaC1s6.png)

### 2.之后可通过按键自定义选择输入的PDF文件夹和输出的内容识别文件夹

> ![image-20211113224530563](https://i.loli.net/2021/11/13/5FEnDKJMxbZOAdX.png)

> ![image-20211113224604326](https://i.loli.net/2021/11/13/r8SsYzQ49FWoD37.png)
>
> 不可通过键盘修改路径（即仅能通过按钮选择）

### 3.根据自身需要选择不同的模式对PDF文件进行识别

---

## 二、程序思路
### 1.文件介绍

> ```main.py```：主函数，运行后启动程序
>
> ```frame.py```：tkinter框架，内有布局和相应案件的函数调用
>
> `pdf_easy`：速度模式，使用库`pdfplumber`，识别速度较快，大约为0.5~1.5s一页PDF，可多线程运行，在PDF内容格式较为标准（字迹清晰，无图表）情况下识别准确率高。
>
> `pdf_hard`：准确模式，使用库`easyocr`，识别速度较慢，在使用GPU运行时大约为5~7s一页PDF，使用CPU运行时大约为40~50s一页PDF，不可多线程或多进程运行（该库默认调用所有CPU逻辑核），可识别出绝大多数PDF文件内容（包括各种图表，较为模糊的扫描件）
>
> `pdf_normal`：普通模式，使用库`pdfplumber`和`easyocr`，兼顾识别速度和精度。运行时首先使用`pdfplumber`初步扫描所有PDF内容，当未识别某一篇PDF内容时，调用`easyocr`进行深度扫描。
>
> `pdf_Process`：开启多线程函数

### 2.代码逻辑

> 详情可见代码内容，内有详细注释
>
> ![image-20211113231321285](https://i.loli.net/2021/11/13/WIdFHnbz4t3AGkm.png)

---

## 三、使用环境

```python
python 3.8.8
tkinter
easyocr
pdfplumber
pdf2image
```

可通过[requirements.bat](./requirements.bat)下载环境

---

## 四、作者

小吴同学

