import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import time
import openpyxl
def demo():
 all_jobs=[]
#设置最初遍历循坏获取页数以及数据
 for j in range(1,50):
    time.sleep(0.01)
    url=f"https://yiqifu.baidu.com/g/aqc/joblist/getDataAjax?q=Python&page={j}&district=100000&salaryrange="
    head={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
          "referer":"https://yiqifu.baidu.com/g/aqc/joblist?q=Python"}
    resp = requests.get(url, headers=head)

    #跳过没有数据的页面
    if len(resp.json()["data"]["list"])==0:
         continue
    print(f"-----------{j}页---------------")

    #从json（字符串键值对）数据中分化各个数据对应类型
    for i in resp.json()["data"]["list"]:
        job={}
        job["工作岗位"]=i["jobName"].replace("<em>"," ").replace("</em>","")
        job["月薪"]=i["salary"]
        job["公司"]=i["company"]
        job["城市"]=i["city"]
        job["学历"]=i["edu"]
        job["资历"]=i["exp"]
        bid=i["bid"]
        jobid=i["jobId"]
        #获取网页详细岗位描述
        detail_url=f"https://yiqifu.baidu.com/g/aqc/jobDetail?bid={bid}&jobId={jobid}"
        detail_resp = requests.get(detail_url, headers=head)
        soup = BeautifulSoup(detail_resp.text,"html.parser")
        scripts=soup.find_all("script")
        for tag in scripts:
            if "window.pageData" in tag.text:
                data= tag.text.replace("window.pageData = ","").replace(" || {};","")
        data = json.loads(data)
        job["岗位职责"]=data["desc"]
        for keys,vlaue in job.items():
         try:
          print(f"{keys}:{vlaue}")
          print("---")
         except Exception as e:
             print(f"输出数据失败：{e}")
        all_jobs.append(job)

#将数据转为表格形式并且导入Excel
 df=pd.DataFrame(all_jobs)
 print(df)
 try:
  df.to_excel("Python的招聘数据信息.xlsx",index=False,sheet_name="Python岗位")
 except Exception as e:
     print(f"导出Excel失败的内容：{e}")
 else:
     print("成功使用pandas将数据导入Excel表格")
if __name__ == "__main__":
 demo()







