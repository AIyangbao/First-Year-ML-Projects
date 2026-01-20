import openpyxl
def demo():
    wb = openpyxl.Workbook()
    wb.create_sheet(title="网络热梗表")
    print(wb.worksheets)
    sheet=wb["网络热梗表"]
    hot_memes=[['编号', '热梗名称', '代表人物', '经典语录', '流行领域'],
    [1, '小黑子', '坤坤', '鸡你太美', '鬼畜/篮球'],
    [2, '退退退', '卖气球阿姨', '退！退！退！', '吵架/表情包'],
    [3, '尊嘟假嘟', '小狗文学', '这尊嘟假嘟？', '聊天/卖萌'],
    [4, '鼠鼠文学', '鼠鼠人', '鼠鼠我啊，真的破防了', '自嘲/emo'],
    [5, '疯狂星期四', '肯德基', 'V我50，今天疯狂星期四', '营销/段子'],]
    for hot in hot_memes:
        sheet.append(hot)
    wb.save('热梗表.XLSX')
if __name__ == '__main__':
    demo()
