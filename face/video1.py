# -*- coding: utf-8 -*-
# 摄像头头像识别
import face_recognition
import cv2
import time
import os
import sys

#source = "rtsp://admin:5417010101xx@192.168.1.61/Streaming/Channels/101"
source='kb3.mp4'
video_capture = cv2.VideoCapture(source)

# 本地图像
anxin_image = face_recognition.load_image_file("anxin.jpg")
anxin_face_encoding = face_recognition.face_encodings(anxin_image)[0]

# 本地图像二
xuzhong_image = face_recognition.load_image_file("xuzhong.jpg")
xuzhong_face_encoding = face_recognition.face_encodings(xuzhong_image)[0]

# 本地图片三
gaoqiqiang_image = face_recognition.load_image_file("gaoqiqiang.jpg")
gaoqiqiang_face_encoding = face_recognition.face_encodings(gaoqiqiang_image)[0]

# 本地图片四
jize_image = face_recognition.load_image_file("jize.jpg")
jize_face_encoding = face_recognition.face_encodings(jize_image)[0]

# 本地图片五
baijiangbo_image = face_recognition.load_image_file("baijiangbo.jpg")
baijiangbo_face_encoding = face_recognition.face_encodings(baijiangbo_image)[0]

# 本地图片六
mengyu_image = face_recognition.load_image_file("mengyu.jpg")
mengyu_face_encoding = face_recognition.face_encodings(mengyu_image)[0]

# 本地图片七
lixiang_image = face_recognition.load_image_file("lixiang.jpg")
lixiang_face_encoding = face_recognition.face_encodings(lixiang_image)[0]

# 本地图片八
xujiang_image = face_recognition.load_image_file("xujiang.jpg")
xujiang_face_encoding = face_recognition.face_encodings(xujiang_image)[0]

# Create arrays of known face encodings and their names
# 脸部特征数据的集合
known_face_encodings = [
    xuzhong_face_encoding,
    anxin_face_encoding,
    gaoqiqiang_face_encoding,
    jize_face_encoding,
    baijiangbo_face_encoding,
    mengyu_face_encoding,
    lixiang_face_encoding,
    xujiang_face_encoding
]

# 人物名称的集合
known_face_names = [
    "xuzhong",
    "anxin",
    "gaoqiqiang",
    "jize",
    "baijiangbo",
    "mengyu",
    "lixiang",
    "xujiang"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
dic = {}
for name in known_face_names:
    dic[name] = "NaN"

if __name__ == '__main__':
    while True:
        # 读取摄像头画面
        ret, frame = video_capture.read()

        if ret:
            yn = 0
            # 改变摄像头图像的大小，图像小，所做的计算就少
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
            rgb_small_frame = small_frame[:, :, ::-1]
            print(rgb_small_frame)
            # Only process every other frame of video to save time
            if process_this_frame:
                # 根据encoding来判断是不是同一个人，是就输出true，不是为flase
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                c_times = []

                for face_encoding in face_encodings:
                    # 默认为unknown
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
                    #阈值太低容易造成无法成功识别人脸，太高容易造成人脸识别混淆 默认阈值tolerance为0.6
                    name = "Unknown"

                    # if match[0]:
                    #  name = "michong"
                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                    
                        c_time = time.time()
                        local_time = time.localtime(c_time)
                        c_time = time.strftime("%H:%M",local_time)
                        date = time.strftime("%m-%d")
                    face_names.append(name)
                    if (name != 'Unknown') and (dic[name] == 'NaN'):
                        dic[name] = c_time

            process_this_frame = not process_this_frame

            # 将捕捉到的人脸显示出来
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # 矩形框
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                #加上标签
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                #各参数依次是：照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细

            # Display
            cv2.imwrite('text.jpeg',frame)
            cv2.imshow('monitor', frame)
            # 按Q退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            yn += 1
            if yn > 10:
                break

video_capture.release()
cv2.destroyAllWindows()

path = os.path.abspath(os.path.dirname(sys.argv[0]))
f = open(path+'\\data.txt','r',encoding='utf-8')
tmp = f.read()
f.close()
line = tmp.split('\n')#将内容按行分为列表
for i in range(len(line)):
    line[i] = line[i].split(' ')#将每行按空格分为二维数组
if line[2][1] == date:
    for name in known_face_names:
        if line[known_face_names.index(name)+4][1] == 'NaN':
            del line[known_face_names.index(name)+4][1]
            line[known_face_names.index(name)+4].insert(1,dic[name])#每行插入时间
else:
    line[2].insert(1,date)
    for name in known_face_names:
        line[known_face_names.index(name)+4].insert(1,dic[name])#每行插入时间
for i in range(len(line)):
    line[i] = ' '.join(line[i])
tmp = '\n'.join(line)
f = open(path+'\\data.txt','w',encoding='utf-8')
f.write(tmp)
f.close()