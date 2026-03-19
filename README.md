# API Data Collector

这是一个用于练习 requests、JSON、CSV 和异常处理的 Python 项目。

## 功能
- 请求公开 API
- 获取 JSON 数据
- 保存原始 JSON
- 提取关键字段并保存为 CSV
- 处理请求异常

## 项目结构
- `main.py`：主程序
- `requirements.txt`：依赖列表
- `output/result.json`：原始 JSON 数据
- `output/result.csv`：提取后的 CSV 数据

## 运行方式
1. 安装依赖：
   `pip install -r requirements.txt`
2. 运行：
   `python main.py`

## 当前使用的 API
- GitHub Public Events API