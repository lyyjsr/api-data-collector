# API Data Collector

一个基于 Python 的公开 API 数据采集项目。

当前版本功能：
- 输入 GitHub 用户名
- 请求 GitHub public API
- 提取用户公开信息
- 保存为本地 JSON 文件

## 技术栈
- Python
- requests
- JSON

## 项目结构
api-data-collector/
├─ src/
│  ├─ main.py
│  ├─ api_client.py
│  ├─ parser.py
│  └─ utils.py
├─ output/
├─ requirements.txt
└─ README.md

## 运行方式
pip install -r requirements.txt
python src/main.py

## 当前支持
- GitHub 用户公开信息采集

## 后续计划
- 支持更多公开 API
- 支持 CSV 导出
- 支持命令行参数
- 增强异常处理