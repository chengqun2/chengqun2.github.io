
import csv
import json

def main(csv_string, sharp):
    if len(sharp) == 0:
        sharp = 'bar'
    elif sharp in '饼状图, 饼图':
        sharp = 'pie'
    elif sharp in '线状图, 线状图, 折线图':
        sharp = 'line'
    else:
        sharp = 'bar'
    # 将CSV字符串分割成行
    lines = csv_string.strip().split('\n')
    
    # 使用csv模块读取数据
    reader = csv.reader(lines)
    
    # 将所有行转换为列表
    data = [row for row in reader]
    
    # 将数字字符串转换为浮点数
    for row in data[1:]:  # 跳过标题行
        for i in range(1, len(row)):
            try:
                row[i] = float(row[i])
            except ValueError:
                pass
    
    # 创建完整的ECharts配置
    echarts_config = {
        "legend": {},
        "tooltip": {},
        "dataset": {
            "source": data
        },
        "xAxis": [
            {"type": "category", "gridIndex": 0},
            {"type": "category", "gridIndex": 1}
        ],
        "yAxis": [
            {"gridIndex": 0},
            {"gridIndex": 1}
        ],
        "grid": [
            {"bottom": "15%"},
            {"top": "15%"}
        ],
        "series": [
            {"type": sharp, "seriesLayoutBy": "row"},
            {"type": sharp, "seriesLayoutBy": "row"},
            {"type": sharp, "seriesLayoutBy": "row"},
            {"type": sharp, "seriesLayoutBy": "row"}
        ]
    }

    # 生成输出文件
    output = "```echarts\n" + json.dumps(echarts_config, indent=2, ensure_ascii=False) + "\n```"

    return {"output":output}

