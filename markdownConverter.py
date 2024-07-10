import re

def process_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 移除 ** 标记
    content = re.sub(r'\*\*', '', content)
    content = re.sub(r'\*', '', content)
    content = re.sub(r'\ ', '', content)
    content = re.sub(r'\+ ', '', content)
    content = re.sub(r'\- ', '', content)


    # 移除表格边框
    #content = re.sub(r'\+[-+]+\+', '', content)

    # 移除多余的空行，但保留单个空行
    #content = re.sub(r'\n{3,}', '\n\n', content)

    # 移除行首和行尾的空格
    #content = '\n'.join(line.strip() for line in content.split('\n'))

    # 确保表格行之间没有空行
    content = re.sub(r'(\|[^\n]+\n)\n+(?=\|)', r'\1', content)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

# 使用脚本
input_file = 'example2.md'
output_file = 'output.md'
process_markdown(input_file, output_file)
print(f"处理完成，结果已保存到 {output_file}")