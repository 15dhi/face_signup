运行：
教师端页面：在终端运行（Vscode\Anaconda3等）。第一行try_st为运行环境，需要安装有python及streamlit包；第二行文件所在路径。
activate try_st
cd /d C:\Users\bys\Desktop\streamlit\
streamlit run teacher_term.py
学生端页面：
activate try_st
cd /d C:\Users\bys\Desktop\streamlit\
streamlit run student_term.py

数据：
data.txt文件需沿用既定格式，否则报错。图片名称需与名称列表内名称相同，放在student_term.py相同文件夹下。

样例格式如下（UTF-8）：
namelist 张三 李四 王五 毕业生 老板娘 气态氧 汤圆
clock 8:50
date 03-07 02-26 02-25 02-24 02-23 02-22 02-21 02-20 02-19 02-17 02-16
attendence_record:
张三20200000 10:30 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25 8:25
李四20200001 NaN 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35 8:35
王五20200002 8:25 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30 8:30
毕业生20200003 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20 10:20
老板娘 10:30 NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN NaN
气态氧20200004 NaN 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00 0:00
汤圆20200005 8:30 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10 12:10

