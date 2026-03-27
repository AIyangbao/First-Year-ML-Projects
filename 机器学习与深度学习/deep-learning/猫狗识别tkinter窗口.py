import tkinter as tk
from tkinter import filedialog
import numpy as np
import tensorflow as tf
# 加载图片 是需要pillow
#pip install pillow
# 导入两个库 image 打开缩放图片 imageTK 转换为 图片展示到窗口的格式
from PIL import Image,ImageTk

root = tk.Tk()

root.title('猫狗图片预测')

root.geometry('300x300')

model = tf.keras.models.load_model('机器学习与深度学习\deep-learning\cat_dog_model.keras')

    # 点击选择图片跳转的 函数
def predict_image():
    #去本地选择上传图片
    img_path = filedialog.askopenfilename(title='选择图片文件',filetypes=[("PNG files","*.png"),("JPEG files","*.jpg")])

    if img_path:
        img = tf.keras.preprocessing.image.load_img(img_path,target_size=(150,150))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array.reshape(1,150,150,3)

        img_array = img_array/255.0

        prediction = model.predict(img_array)
        #最终预测结果
        data = '狗' if prediction[0]>0.5 else '猫'

        #更新组件文本内容
        result.config(text=data)

        img_display = Image.open(img_path).resize((150,150))

        img_tk = ImageTk.PhotoImage(img_display)

        image_label.config(image=img_tk)

        #引用图片
        image_label.image = img_tk


button = tk.Button(root,text='选择图片进行预测',command=predict_image)
button.pack(pady=20)

result = tk.Label(root,text='预测结果是:')
result.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

#启动tkinter的主循环
root.mainloop()
