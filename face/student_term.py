import streamlit as st
import time
import os
import sys
import datetime
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# 定义一个继承FileSystemEventHandler的类，监测文件变化
class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.modified = False

    def on_modified(self, event):
        self.modified = True

# 定义一个函数，实时读取文件内容
def read_file():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    with open(path+'\\data.txt','r+',encoding='utf-8') as f:
        global namelist,clock,date_time,attendance_record,output_tx2
        namelist = f.readline()[:-1]
        namelist = (namelist.split(' '))[1:]
        clock = f.readline()[:-1]
        clock = (clock.split(' '))[1:]
        for i in range(len(clock)):
            clock[i] = clock[i].split(':')
        date_time = f.readline()[:-1]
        date_time = (date_time.split(' '))[1:]
        check =  f.readline()[:-1]
        attendance_record = []
        for i in range(len(namelist)):
            attendance_read = f.readline()[:-1]
            attendance_read = (attendance_read.split(' '))[1:]
            attendance_record.append(attendance_read)
    return 


# 在Streamlit页面中显示文件内容
def show_file_contents():
    global namelist_flag,output_area1,output_area2,output_tx2_str
    if date_time[0] != check_date:
        st.title("Date has not been refreshed")  #若日期列表中无当前日期，报错
    else:                                        #若有当前日期，扫描当日签到列表，如果非默认值且flag=0，反馈，flag=1，不反馈
        for i in range(len(attendance_record)):
            if attendance_record[i][0] != 'NaN':            #如果某人当日签到时间非默认值‘NaN’，判断flag,若为0,时间标准化并进行反馈                      
                if namelist_flag[i] == 0:
                    namelist_flag[i] = 1                #反馈后flag置1
                    filename = namelist[i]+'.jpg'           #显示头像
                    path = os.path.join(os.getcwd(), filename)
                    if os.path.isfile(path):
                        image = Image.open(path)
                        image_dsp.image(image, caption=namelist[i])
                    else:
                        path = os.path.abspath(os.path.dirname(sys.argv[0]))
                        image = Image.open(path+'\\example.jpg')
                        image_dsp.image(image, caption='No picture found')
                    output_tx2.append(namelist[i])
                    tran_attend = attendance_record[i][0].split(':')    #签到时间转换为tran_attend
                    for j in range(len(tran_attend)):           
                        tran_attend[j] = int(tran_attend[j])
                    if tran_attend[0] <= int(clock[0][0]) and tran_attend[1] <= int(clock[0][1]):   #输出反馈：按时签到
                        output_tx = namelist[i]+"，你已签到成功，感谢你对签到工作的支持	:kissing_heart:"
                        output_area1.header(output_tx)
                        st.balloons()
                    else:                                                                           #输出反馈：迟到
                        if attendance_record[i][1] == 'NaN':                             #检查上次签到情况：缺勤/正常/迟到
                            output_tx = namelist[i]+"，请向导师说明上次缺勤原因 :face_with_one_eyebrow_raised:"
                            output_area1.header(output_tx)
                        else :
                            tran_attend = attendance_record[i][1].split(':')   
                            for j in range(len(tran_attend)):           
                                tran_attend[j] = int(tran_attend[j])
                            if tran_attend[0] <= int(clock[0][0]) and tran_attend[1] <= int(clock[0][1]):
                                output_tx = namelist[i]+"，你迟到了！下次请注意	:anguished:"
                                output_area1.header(output_tx)
                            else:
                                output_tx = namelist[i]+"，你迟到不止一次了！如有特殊情况请向导师说明 :angry:"
                                output_area1.header(output_tx)
        output_tx2_str = ""
        for i in output_tx2:
            output_tx2_str += (" "+i) 
        output_tx2_str = "已签到名单："+output_tx2_str
        output_area2.subheader(output_tx2_str)
        
                            


#签到页面

st.title("	:classical_building:  这里是实验室签到页面	:classical_building:")
st.title(" ")


# 显示文件内容
read_file()
output_area1 = st.empty()
image_dsp = st.empty()
st.title(" ")
output_area2 = st.empty()
check_date = datetime.datetime.now().strftime('%m-%d')  #获取当前日期
namelist_flag = []       #判断是否签到标志
output_tx2 = []
for i in range(len(namelist)):
    namelist_flag.append(0)
show_file_contents()



# 监测文件变化并自动刷新页面
event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, os.getcwd(), recursive=False)
observer.start()

while True:
    time.sleep(1)
    if event_handler.modified:
        event_handler.modified = False
        contents = read_file()
        show_file_contents()
