import json

# 要尋找的行開頭字串
target_line_start = 'frmInputMsg.btn_Define_Click → cmdMySQL_Oven_QueryArea'

# 從檔案中讀取並解析 JSON
def parse_json_from_file(filename, target_string):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            if target_string in line:
                # 1. 擷取 SelectCommand 後面的 SQL 命令
                command = line.split('SelectCommand=')[1].strip()

                # 2. 從 SQL 命令中，擷取 JSON 字串
                # 找到 JSON 內容的起始與結束位置
                json_start_index = command.find('mach_remark=\'') + len('mach_remark=\'')
                json_end_index = command.rfind("' where mach_name=")
                json_string = command[json_start_index:json_end_index]

                try:
                    # 3. 解析 JSON 字串
                    json_data = json.loads(json_string)
                    return json_data
                except json.JSONDecodeError as e:
                    print(f"JSON 解析錯誤：{e}")
                    return None
    return None

# 執行函式並印出結果
json_output = parse_json_from_file('MySQL_0802.csv', target_line_start)

if json_output:
    print("成功從檔案中解析出 JSON 內容：")
    print(json.dumps(json_output, indent=2, ensure_ascii=False))
