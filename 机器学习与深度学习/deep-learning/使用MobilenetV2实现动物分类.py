import time
import tensorflow as tf

#导入我们的mobilenetv2模型
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#将数据集加载函数
datagen = ImageDataGenerator(
    # #去除除以255 归一化操作
    validation_split = 0.2
)

training_generator = datagen.flow_from_directory(
    '机器学习与深度学习\deep-learning\data',
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

validation_generator = datagen.flow_from_directory(
    '机器学习与深度学习\deep-learning\data',
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical',
    subset='validation',
    shuffle=True
)

class_names = list(training_generator.class_indices.keys())
print(class_names)

#加载模型
base_model = MobileNetV2(
    input_shape=(224,224,3), #指定图像输入的大小
    include_top=False,       #不包含最后一层:输出层 (1000类别的Dense层)
    weights='imagenet'       #加载在imagenet上 预训练的权重
)

#训练模型
base_model.trainable=False #冻结主干网络 预训练的主干网络的参数部分'锁死'

#建立模型
model = models.Sequential([
    #对于mobilenentv2而言 输入的像素点_缩放到[-1,1]
    #将像素点[0,255]缩放到[-1,1]
    tf.keras.layers.Rescaling(1./127.5,offset=-1,input_shape=(224,224,3)),
    base_model, #加载mobilenetv2的主干网络
    tf.keras.layers.GlobalAveragePooling2D(), #将卷积压缩为一个特征向量
    #输出层
    tf.keras.layers.Dense(9,activation='softmax') #最后的分类器层
])

#编译模型
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

#训练模型
start = time.time()
history = model.fit(training_generator,validation_data=validation_generator,epochs=10)

#保存模型
import os
if not os.path.exists('models'):
    os.mkdir('models')

model.save('./models/moilenetv2_new.keras')

end = time.time()

print('训练总耗时为:',end-start,'s')

#展示训练过程的 准确率和损失率的图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.subplot(2,1,1)
plt.plot(history.history['accuracy'],label='训练准确率')
plt.plot(history.history['val_accuracy'],label='验证准确率')
plt.legend()
plt.title("训练和验证的准确率")

plt.subplot(2,1,2)
plt.plot(history.history['loss'],label='训练损失率')
plt.plot(history.history['val_loss'],label='验证损失率')
plt.legend()
plt.tight_layout() # 自动调整子图之间的距离

if not os.path.exists('results'):
    os.mkdir('results')

plt.savefig('./results/results_new.png')
