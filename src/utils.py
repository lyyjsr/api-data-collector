# 保存模块
import json
import os
def save_to_json(data:dict,filename:str) -> None:
    os.makedirs('output',exist_ok=True)
    file_path = os.path.join('output',filename)
    with open(file_path,"w",encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)