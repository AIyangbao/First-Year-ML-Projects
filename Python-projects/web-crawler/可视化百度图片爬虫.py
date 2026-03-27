import tkinter as tk
from tkinter import ttk, filedialog,messagebox
import requests
import os
import threading

# 请求基础设置
image_src = 'https://image.baidu.com/search/acjson'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}
params = {
    'tn': 'resultjson_com',
    'logid': '7008269991081857061',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'fr': '',
    'word': '',
    'queryWord': '',
    'cl': '2',
    'lm': '',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': '-1',
    'z': '',
    'ic': '0',
    'hd': '',
    'latest': '',
    'copyright': '',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '0',
    'istype': '2',
    'qc': '',
    'nc': '1',
    'expermode': '',
    'nojc': '',
    'isAsync': '',
    'pn': '',
    'rn': '30',
    '1716190281723': ''
}

# 爬虫逻辑
def image_crawler(image_name,image_count,text_widget,save_path):
    count = 1
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    image_folder = os.path.join(save_path,image_name)
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    
    if os.path.exists(image_folder): #判断关键字目录是否已经存在
        current_num = len(os.listdir(image_folder))
        count = int(current_num/30) + 3

    while True:
        params['word'] = image_name
        params['pn'] = count*30
        try:
            resp = requests.get(url=image_src,headers=headers,params=params)
            resp.raise_for_status() #检查是否成功
            print(f"请求成功,状态码:{resp.status_code}")
            data = resp.json().get('data',[])[:30]
            if not data:
                print(f"没有找到图片数据!")
        except Exception as e:
            text_widget.insert(tk.END,f'请求失败:{e}\n')
            print(f"请求失败:{e}")
        for item in data:
            if 'thumbURL' not in item:
                continue
            try:
                img = requests.get(url=item['thumbURL'],headers=headers).content
                file_num = len(os.listdir(image_folder))
                with open(os.path.join(image_folder,f"{image_name}{file_num+1}.png"),'wb') as f:
                    f.write(img)
                text_widget.insert(tk.END,f'正在下载第{file_num+1}张图片\n')
                text_widget.see(tk.END)
                if file_num + 1 >= image_count:
                    text_widget.insert(tk.END,'✅ 下载完成！\n')
                    return
            except Exception as e:
                text_widget.insert(tk.END,f'下载失败:{e}\n')
        count+=1

# 启动 爬虫并使用多线程
def start_download(name,count,text_widget,path):
    try:
        image_count = int(count)
        threading.Thread(target=image_crawler,args=(name,image_count,text_widget,path),daemon=True).start()
    except ValueError():
        messagebox.showerror("输入错误","请输入有效的图片数量")

# 创建美化后的界面
def create_gui():
    root = tk.Tk()
    root.title("🌟 百度图片爬虫工具")
    root.geometry("600x450")
    root.resizable(False,False)

    #样式美化
    style = ttk.Style()
    style.theme_use("default")
    style.configure("TLabel",font=('Arial',12))
    style.configure("TButton",font=('Arial',11),padding=6)
    style.configure('TEntry',font=('Arial',11))

    # 顶部标题
    ttk.Label(root,text="📷 百度图片爬虫工具",font=('Arial',16,'bold')).pack(pady=10)
    frame = ttk.Frame(root)
    frame.pack(padx=20,pady=5,fill=tk.X)

    ttk.Label(frame,text="关键词:").grid(row=0,column=0,sticky=tk.E,pady=5)
    entry_name = ttk.Entry(frame,width=40)
    entry_name.grid(row=0,column=1,pady=5,sticky=tk.W)

    ttk.Label(frame,text="数量").grid(row=1,column=0,sticky=tk.E,pady=5)
    entry_count = ttk.Entry(frame,width=40)
    entry_count.grid(row=1,column=1,pady=5,sticky=tk.W)

    ttk.Label(frame,text="保存路径:").grid(row=2,column=0,sticky=tk.E,pady=5)
    path_var = tk.StringVar()
    entry_path = ttk.Entry(frame, textvariable=path_var,width=32)
    entry_path.grid(row=2,column=1,sticky=tk.W,pady=5)

    def choose_folder():
        folder = filedialog.askdirectory()
        if folder:
            path_var.set(folder)
    
    ttk.Button(frame,text="选择文件夹",command=choose_folder).grid(row=2,column=2,padx=5)

    #分割线
    ttk.Separator(root,orient="horizontal").pack(fill="x",padx=10,pady=10)

    #输出框 + 滚动条
    text_frame = ttk.Frame(root)
    text_frame.pack(fill=tk.BOTH,expand=True,padx=15)

    text_box = tk.Text(text_frame,wrap=tk.WORD,font=('Consolas',10),height=10,relief=tk.GROOVE,bd=2)
    text_box.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

    scroll = ttk.Scrollbar(text_frame,command=text_box.yview)
    scroll.pack(side=tk.RIGHT,fill=tk.Y)
    text_box.config(yscrollcommand=scroll.set)

    #开始按钮
    ttk.Button(
        root,
        text="🚀 开始爬取",
        command=lambda: start_download(entry_name.get(),entry_count.get(),text_box,path_var.get())
    ).pack(pady=15)
    
    root.mainloop()

    #启动程序
if __name__ == '__main__':
        create_gui()