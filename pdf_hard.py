# -*- coding: UTF-8 -*-
import easyocr
import os
from pdf2image import convert_from_path
import time


def mkdir_path(path):
    """
    创建指定目录
    :param path: 需要创建的目录
    :return: 创建好输入的目录或者判断出已经存在该目录
    """
    if os.path.exists(path):
        return f"---------文件夹 {path} 已存在，即将开始写入---------"
    else:
        os.makedirs(path)
        return f"---------文件夹 {path} 创建完毕---------"


def check(cnstr):
    '''
    判断字符串是否包含有效文本内容
    :param cnstr:需要进行判断的字符串
    :return: 判断字符串中是否包含中英文和数字（若需包含其他语言的字符，则需自行设置）
    '''
    for s in cnstr.encode('utf-8').decode('utf-8'):
        if u'\u4e00' <= s <= u'\u9fff' or u'\u0030' <= s <= u'\u0039' or u'\u0041' <= s <= u'\u005a' or u'\u0061' <= s <= u'\u007a':
            return True
    return False


def run(input_path, output_path):
    """
    用以控制循环遍历文件夹的主程序
    :param input_path: 输入PDF文件的文件夹路径
    :param output_path: 输出识别内容的文件夹路径
    :param counter: 计数器，用来计算识别整体完成度
    :param reader: easyocr的识读器
    :return: 在输出路径下新建名为“PDF识别内容”的文件夹，将识别内容存储在里面
    """
    global counter, reader
    counter = 0
    file_path = input_path
    content_path = output_path + '\PDF识别内容'
    #  创建指定文件夹
    mkdir_path(content_path)
    pdf_path = os.listdir(file_path)

    # 筛选出pdf文件格式的文件
    pdf_path = list(filter(lambda x: '.pdf' in str(x), pdf_path))
    if len(pdf_path) != 0:
        reader = easyocr.Reader(['ch_sim', 'en'])
        time_first = time.time()
        for i in range(len(pdf_path)):
            #  遍历文件夹中所有的PDF文件，将其绝对路径交给hard_readpdf用以识别
            pdf = pdf_path[i]
            pdf_name = file_path + '\\' + pdf
            pdf_short = pdf.split('.')[0]

            hard_readpdf(pdf_name, content_path, pdf_short, len(pdf_path))

        time_last = time.time()
        print(f'---------------所有文件总共用时{time_last - time_first:.2f}s----------------')
    else:
        print(f'{input_path}路径下无PDF文件')


def hard_readpdf(pdf_name, content_path, pdf_short, pdf_path):
    """
    准确模式：对输入的PDF文件进行“准确模式”识别
    :param pdf_name: 需要识别的PDF文件绝对路径
    :param content_path: 输出文件夹的绝对路径
    :param pdf_short: 除去扩展名后的PDF文件名
    :param pdf_path: 需要进行识别的PDF文件总数
    :return:在指定路径下按照“{pdf_short}.txt”名字保存识别文本内容
    """
    global counter, reader
    result = []
    pages = convert_from_path(pdf_name, 500, poppler_path=r'.\poppler-0.68.0\bin')
    print(f'---------------正在识别{pdf_short}.pdf----------------------')
    time_start = time.time()
    for page in range(len(pages)):
        #  识别每一页的内容
        first_page = pages[page]
        first_page.save(f'{page}.jpg', 'JPEG')
        try:
            #  将尝试使用GPU加速，若失败则使用CPU
            text = reader.readtext(f'{page}.jpg', detail=0)
        except Exception:
            reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
            text = reader.readtext(f'{page}.jpg', detail=0)
        os.remove(f'{page}.jpg')
        #  识别出来的结果为列表，将其join后添加至新的列表中那个，用于最后的合并
        result.append(''.join(text))
    counter += 1
    time_end = time.time()
    print(f'----------------已完成{counter / pdf_path * 100:.2f}%----------------------')
    print(f'----------{pdf_short}.pdf识别共用时{time_end - time_start}------------')
    try:
        #  对识别出来的内容进行检查，芝澳邨包含有效内容（中英文+数字）的文本
        with open(f'{content_path}\\{pdf_short}.txt', 'w') as f:
            result = ''.join(result)
            if check(result):
                f.write(result)
            else:
                raise Exception
    except TypeError:
        print(f'{pdf_short}.pdf没有识别出内容')


if __name__ == '__main__':
    #  可修改输入和输出路径，此处仅为示例
    input_path = r''
    output_path = r''
    run(input_path, output_path)
