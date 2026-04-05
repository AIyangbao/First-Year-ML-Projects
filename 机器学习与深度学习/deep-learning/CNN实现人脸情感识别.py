import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import models,layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Input,Dropout
import matplotlib.pyplot as plt
import os
import numpy as np
datagen = ImageDataGenerator(
    rescale=1./255,

)
train_generator = datagen.flow_from_directory(
    './RAF-DB/train',
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical',
    shuffle=True
)
validation_generator = datagen.flow_from_directory(
    './RAF-DB/val',
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical',
    shuffle=True
)
print(train_generator.class_indices)

model = Sequential([
    Input(shape=(224,224,3)),
    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    Conv2D(128,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    
    Flatten(),
    Dense(64,activation='relu'),
    Dropout(0.5),
    Dense(128,activation='relu'),
    Dropout(0.5),
    Dense(7,activation='softmax')
])

#编译模型
#学习率 修改的低一点 默认是0.001 修改为0.0001
from tensorflow.keras.optimizers import Adam
optimizers = Adam(learning_rate=0.0001)
model.compile(
    optimizer=optimizers, #优化器 梯度下降算法
    loss='categorical_crossentropy',
    metrics=['accuracy'] #评估的指标
)

#设置早停 机制 是一种防止过拟合的技术
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    monitor='val_loss', #监控验证集上面的损失
    patience=3, #连续三轮训练 损失不下降
    min_delta = 0.001, #只要损失下降达到了0.001 就算是下降
    verbose = 1,
    restore_best_weights =True #恢复最佳权重
)

#训练模型
import time
start = time.time()
history = model.fit(train_generator,validation_data=validation_generator,epochs=100,callbacks=early_stopping)
end = time.time()
print('模型训练时间为:',end-start)

model.save("Facial_Emotion_Recognition3.keras")

#可视化
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.subplot(2,1,1)
plt.plot(history.history['accuracy'],label='训练集准确率')
plt.plot(history.history['val_accuracy'],label='验证集准确率')
plt.xlabel('epochs')
plt.legend()
plt.title("训练和验证的准确率")

plt.subplot(2,1,2)
plt.plot(history.history['loss'],label='训练损失率')
plt.plot(history.history['val_loss'],label='验证损失率')
plt.legend()
plt.tight_layout() # 自动调整子图之间的距离

if not os.path.exists('result4'):
    os.mkdir('result4')

plt.savefig('./result4/result_new.png')
