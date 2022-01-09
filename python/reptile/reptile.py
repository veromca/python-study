import requests
import json
import openpyxl

wk=openpyxl.Workbook()
sheet=wk.create_sheet('Sheet1',0)
#添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
#爬取评论数据
for item in range(0,50):
    url1='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100016034400&score=0&sortType=5&page='+str(item)+'&pageSize=10&isShadowSku=0&fold=1'
    response_1=requests.get(url1, headers=headers)
    response_1.encoding='gbk'
    resp=response_1.text
    content=resp.replace('fetchJSON_comment98(','').replace(');','')
    json_data=json.loads(content)
    comments=json_data['comments']
    for i in comments:
        pcontent=i['content']
        color=i['productColor']
        psize=i['productSize']
        sheet.append([color,psize])
        wk.save('/Users/liusongqing/pythone-study01-test.xlsx')
        print(color+' '+psize)
        print(pcontent)
        print('-----------------------')

