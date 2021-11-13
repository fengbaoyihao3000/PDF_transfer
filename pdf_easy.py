import pdfplumber
import os
from pdf_Process import process_run
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


def easy_readpdf(pdf_name, content_path, pdf_short, pdf_path):
    """
    速度模式：对输入的PDF文件进行“速度模式”识别
    :param pdf_name: 需要识别的PDF文件绝对路径
    :param content_path: 输出文件夹的绝对路径
    :param pdf_short: 除去扩展名后的PDF文件名
    :param pdf_path: 需要进行识别的PDF文件总数
    :return: 在指定路径下按照“{pdf_short}.txt”名字保存识别文本内容
    """
    global counter
    counter = 0
    result = []
    # print(f'------------{pdf_short}.pdf开始识别--------------')
    time_start = time.time()
    with pdfplumber.open(pdf_name) as pdf:
        for page in range(len(pdf.pages)):
            #  输出的是一页PDF识别出的字符串
            first_page = pdf.pages[page]
            text = first_page.extract_text()
            result.append(text)
    time_end = time.time()
    counter += 1
    print(f'----------------已完成{counter / pdf_path * 100:.2f}%----------------------')
    # print(f'----------{pdf_short}.pdf识别共用时{time_end - time_start}------------')
    try:
        with open(f'{content_path}\\{pdf_short}.txt', 'w') as f:
            result = ''.join(result)
            if check(result):
                f.write(result)
            else:
                raise Exception
    except Exception:
        print(f'{pdf_short}.pdf没有识别出内容')


def run(input_path, output_path):
    """
    用以控制循环遍历文件夹的主程序
    :param input_path: 输入PDF文件的文件夹路径
    :param output_path: 输出识别内容的文件夹路径
    :param counter: 计数器，用来计算识别整体完成度
    :return: 在输出路径下新建名为“PDF识别内容”的文件夹，将识别内容存储在里面
    """
    global counter
    counter = 0
    process_num = 4  # 线程数量
    arg = []
    file_path = input_path
    content_path = output_path + '\PDF识别内容'

    mkdir_path(content_path)
    pdf_path = os.listdir(file_path)

    # 筛选pdf文件格式的文件
    pdf_path = list(filter(lambda x: '.pdf' in str(x), pdf_path))
    if len(pdf_path) != 0:
        time_first = time.time()
        for i in range(len(pdf_path)):
            pdf = pdf_path[i]
            pdf_name = file_path + '\\' + pdf
            pdf_short = pdf.split('.')[0]
            if i == len(pdf_path) - 1:
                #  遍历文件夹中所有的PDF文件，将其绝对路径以及参数交给process_run用以建立多线程运行
                arg.append((pdf_name, content_path, pdf_short, len(pdf_path)))
                process_run(len(arg), easy_readpdf, arg)
            elif i % (process_num + 1) != process_num:
                arg.append((pdf_name, content_path, pdf_short, len(pdf_path)))
            else:
                process_run(process_num, easy_readpdf, arg)
                arg = []
                arg.append((pdf_name, content_path, pdf_short, len(pdf_path)))
        time_last = time.time()

        print(f'----------------已完成{100}%----------------------')

        print(f'---------------所有文件总共用时{time_last - time_first:.2f}s----------------')
    else:
        print(f'{input_path}路径下无PDF文件')


if __name__ == '__main__':
    input_path = r''
    output_path = r''
    run(input_path, output_path)
