# ！/usr/bin/env python
# _*_ coding:utf-8 _*_

'''

@author: yerik

@contact: xiangzz159@qq.com

@time: 2020/3/7 10:07

@desc:

'''


import xlrd
from docx import Document

def fieldCheck(rowFields, checkFields):
    count = len(checkFields)
    idx = 0
    for field in rowFields:
        if field in checkFields:
            idx += 1
            if idx / count > 0.5:
                return True
    return False

def fieldIndex(rowField, refFields):
    result = {}
    for field in refFields:
        if field in rowField:
            result[field] = rowField.index(field)
        else:
            result[field] = None
    return result



if __name__ == '__main__':
    excelFile = input("Pls set excel file path:")
    while (True):
        sheetName = input("Pls set which sheet need export:")
        inputDict = {}
        outputDict = {}
        idxMap = {}
        # sheetName = 'initaddr'
        # excelFile = 'fps.xls'

        excel = xlrd.open_workbook(excelFile)
        sheet = excel.sheet_by_name(sheetName)

        printFlg = False
        wordHead = ["字段名", "中文名称", "数据类型", "长度", "是否可为空", "描述"]
        excelHead = ["字段码", "字段名", "中文名", "类型", "长度", "列表值", "是否必输", "描述", "别名中文名"]
        d = inputDict
        for i in range(sheet.nrows):
            row = sheet.row_values(i)
            cols = list(row)
            if printFlg == False and fieldCheck(cols, excelHead) == True:
                printFlg = True
                cols = [val.replace(" ", "") for val in cols]
                if idxMap == {}:
                    idxMap = fieldIndex(cols, excelHead)
                continue
            if row[0].startswith("输出接口") or row[0].startswith("打印接口"):
                printFlg = False
                d = outputDict

            if printFlg == False:
                continue

            fieldName = row[idxMap[excelHead[1]]] if idxMap[excelHead[0]] is None else row[idxMap[excelHead[0]]]
            if fieldName in d.keys():
                ll = d[fieldName]
                val = row[idxMap[excelHead[5]]]
                ll[-1] += " " + val
            else:
                cnName = row[idxMap[excelHead[8]]] if idxMap[excelHead[2]] is None else row[idxMap[excelHead[2]]]
                # sourceType = row[4]
                fieldType = row[idxMap[excelHead[3]]]
                fieldLen = abs(int(row[idxMap[excelHead[4]]])) if type(0.0) == type(row[idxMap[excelHead[4]]]) else row[idxMap[excelHead[4]]]
                val = row[idxMap[excelHead[5]]]
                required = "M" if row[idxMap[excelHead[6]]] == "是" else row[idxMap[excelHead[6]]]
                required = "O" if required == "否" else required
                remark = row[idxMap[excelHead[7]]]
                d[fieldName] = [fieldName,
                                cnName, fieldType, str(fieldLen).replace("(", "").replace(")", ""), required, str(remark + " " + str(val)).strip()]

        document = Document()
        table = document.add_table(rows=1, cols=6, style='Table Grid')
        # 获取第一行的单元格列表
        hdr_cells = table.rows[0].cells
        # 下面三行设置上面第一行的三个单元格的文本值
        hdr_cells[0].text = '字段名'
        hdr_cells[1].text = '中文名称'
        hdr_cells[2].text = '数据类型'
        hdr_cells[3].text = '长度'
        hdr_cells[4].text = '是否可为空'
        hdr_cells[5].text = '描述'
        for key in inputDict.keys():
            # 表格添加行，并返回行所在的单元格列表
            record = inputDict[key]
            row_cells = table.add_row().cells
            row_cells[0].text = record[0]
            row_cells[1].text = record[1]
            row_cells[2].text = record[2]
            row_cells[3].text = record[3]
            row_cells[4].text = record[4]
            row_cells[5].text = record[5]
        row_cells = table.add_row().cells
        row_cells[0].text = '字段名'
        row_cells[1].text = '中文名称'
        row_cells[2].text = '数据类型'
        row_cells[3].text = '长度'
        row_cells[4].text = '是否可为空'
        row_cells[5].text = '描述'
        for key in outputDict.keys():
            # 表格添加行，并返回行所在的单元格列表
            record = outputDict[key]
            row_cells = table.add_row().cells
            row_cells[0].text = record[0]
            row_cells[1].text = record[1]
            row_cells[2].text = record[2]
            row_cells[3].text = record[3]
            row_cells[4].text = record[4]
            row_cells[5].text = record[5]

        document.add_page_break()

        # 保存.docx文档
        document.save(sheetName + '.docx')
        print(sheetName + '.docx file completed!')

