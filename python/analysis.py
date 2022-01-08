import openpyxl
import matplotlib.pyplot as plt
wk=openpyxl.load_workbook('/Users/liusongqing/pythone-study01-test.xlsx')
sheet=wk['Sheet1']
colors=[]
sizes=[]
for i in range(1,501):
    colors.append(sheet['A'+str(i)].value)
    sizes.append(sheet['B'+str(i)].value)
color_class=set(colors)
count=len(colors)
color_parcent=[]
for clr in color_class:
    color_parcent.append(colors.count(clr)/count)
plt.pie(x=color_parcent,labels=color_class,autopct='%1.2f',shadow=False,startangle=150)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title("热销手机颜色分布图-样本数-"+str(count))
plt.axis('equal')
plt.legend()
plt.savefig('/Users/liusongqing/pythone-study01-test-analysis.png')

