
import csv
import json

def main(csv_string):
    # 将CSV字符串分割成行
    lines = csv_string.strip().split('\n')
    
    # 使用csv模块读取数据
    reader = csv.reader(lines)
    
    # 将所有行转换为列表
    data = [row for row in reader]
    # print('data ', data)

    dataX = []
    
    # 将数字字符串转换为浮点数
    for row in data[1:]:  # 跳过标题行
        dataX.append(row[0])
        for i in range(1, len(row)):
            try:
                row[i] = float(row[i])
            except ValueError:
                pass
    # print('dataX ', dataX)        
    result = json.dumps({"data": data, "dataX": dataX}, ensure_ascii=False)
    return {"result": result}

str = "产品,1月,2月,3月,4月,5月,6月\n产品A,22,28,33,46,21,55\n产品B,33,40,29,38,29,23\n产品C,33,36,24,29,26,28\n产品D,23,55,33,36,40,29"
result =main(str)
dataX = json.loads(result["result"])["dataX"]
data = json.loads(result["result"])["data"]
print(data, dataX)