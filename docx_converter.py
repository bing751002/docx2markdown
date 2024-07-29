import pypandoc
from bs4 import BeautifulSoup
import os
import shutil

def docx_to_html(docx_path):
    # 創建臨時目錄來存放提取的媒體文件
    temp_media_dir = 'temp_media'
    os.makedirs(temp_media_dir, exist_ok=True)

    # 使用 pypandoc 將 docx 轉換為 html，同時去掉目錄
    extra_args = [
        '--toc=false',  # 完全去除目錄
        '--no-highlight',  # 關閉語法高亮
        f'--extract-media={temp_media_dir}'  # 提取媒體文件到臨時目錄
    ]
    html_content = pypandoc.convert_file(docx_path, 'html', extra_args=extra_args)
    return html_content, temp_media_dir

def html_table_to_markdown(table):
    markdown_table = []
    rows = table.find_all('tr')
    
    # 處理表頭
    headers = rows[0].find_all(['th', 'td'])
    header_row = [header.get_text(strip=True) for header in headers]
    markdown_table.append('| ' + ' | '.join(header_row) + ' |')
    markdown_table.append('| ' + ' | '.join(['---' for _ in header_row]) + ' |')
    
    # 處理表格內容
    for row in rows[1:]:
        cells = row.find_all(['th', 'td'])
        row_data = [cell.get_text(strip=True) for cell in cells]
        markdown_table.append('| ' + ' | '.join(row_data) + ' |')
    
    return '\n'.join(markdown_table)

def extract_tables_to_markdown(html_content):
    # 使用 Beautiful Soup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 找到所有表格
    tables = soup.find_all('table')
    
    markdown_tables = []
    for i, table in enumerate(tables, 1):
        markdown_table = f"表格 {i}:\n\n" + html_table_to_markdown(table) + "\n\n"
        markdown_tables.append(markdown_table)
    
    return ''.join(markdown_tables)

def move_images(temp_media_dir, target_dir):
    # 創建目標目錄
    os.makedirs(target_dir, exist_ok=True)
    temp_media_dir = temp_media_dir + "\media"
    # 移動圖片文件
    for file in os.listdir(temp_media_dir):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            src = os.path.join(temp_media_dir, file)
            dst = os.path.join(target_dir, file)
            shutil.move(src, dst)                       

# 主程序
if __name__ == "__main__":
    docx_file = "input.docx"  # 輸入 docx 文件名
    output_file = "output_tables.md"  # 輸出 Markdown 文件名
    image_dir = "images"  # 圖片保存目錄
    
    # 檢查文件是否存在
    if not os.path.exists(docx_file):
        print(f"錯誤：找不到文件 '{docx_file}'")
        exit(1)

    # 將 docx 轉換為 HTML
    html_content, temp_media_dir = docx_to_html(docx_file)

    # 從 HTML 中提取表格並轉換為 Markdown
    markdown_content = extract_tables_to_markdown(html_content)

    # 將 Markdown 內容寫入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    # 移動圖片到指定目錄
    move_images(temp_media_dir, image_dir)

    # 刪除臨時目錄
    #shutil.rmtree(temp_media_dir)
    
    print(f"表格已成功轉換為 Markdown 格式並保存到 '{output_file}'")
    print(f"圖片已保存到 '{image_dir}' 目錄")