import streamlit as st
import pandas as pd
import argparse
import os
import sys

#调用data_st.txt文件中所有数据：人名、日期、签到时限、缺勤时限、签到记录
path = os.path.abspath(os.path.dirname(sys.argv[0]))
with open(path+'\\data.txt','r+',encoding='utf-8') as f:
    namelist = f.readline()[:-1]
    namelist = (namelist.split(' '))[1:]
    clock = f.readline()[:-1]
    clock = (clock.split(' '))[1:]
    old_clock = clock[0]
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
#截取最近10天的签到记录
for i in range(len(attendance_record)):
    attendance_record[i]=attendance_record[i][:10]
#网页标题:教师端签到系统
st.title('签到统计')

#显示签到记录表
st.write('签到记录如下：')
df = pd.DataFrame(
        attendance_record,                               #保留10次签到数据
        index=('%s' % name for name in namelist),       #行数=人员数，命名为人名
        columns=tuple(date_time)[:10]
    )
st.write(df)

#签到统计:计算准点率与签到率并输出
col1, col2 = st.columns(2)
qiandaorenshu = 0
zhundianlv = 0
for i in range(len(namelist)):
    if attendance_record[i][0] != 'NaN':
        qiandaorenshu += 1.00
        tran_time = attendance_record[i][0].split(":")
        for j in range(len(tran_time)):
            tran_time[j] = int(tran_time[j])
        if tran_time[0] <= int(clock[0][0]):
            if tran_time[1] <= int(clock[0][1]):
                zhundianlv += 1
qiandaolv = qiandaorenshu/len(namelist)
qiandaolv = round(qiandaolv,2)
zhundianlv = zhundianlv/len(namelist)
zhundianlv = round(zhundianlv,2)
col1.metric("签到率", qiandaolv)
col2.metric("准点率", zhundianlv)

#设置签到时间

st.write('签到时间:')

parser = argparse.ArgumentParser()
parser.add_argument('--clock_change', default=old_clock, type=str, help="以英文冒号分割")
args = parser.parse_args()

st.sidebar.title("设置参数：")
clock_change = st.sidebar.text_input("签到时间", args.clock_change)
st.write(clock_change)
if clock_change != old_clock:
    old_clock = "clock"+" "+old_clock
    clock_change = "clock"+" "+clock_change
with open('data.txt','r',encoding='utf-8') as f:
    str1 = f.read()
    str2 = str1.replace(old_clock,clock_change)    
with open('data.txt', "w",encoding='utf-8') as ff:
    ff.write(str2)
    ff.flush()
