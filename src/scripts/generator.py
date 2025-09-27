import os
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

def generate_images(data, output_dir, template_path='src/templates/base_template.html'):
    """
    Generates images with the given texts using Playwright.
    """
    # ===== 新增：数据格式检查和转换 =====
    # 检查数据格式并统一处理
    if not data:
        print("Error: No data provided")
        return
    
    # 如果是字符串列表，转换为字典格式
    if isinstance(data, list) and data and isinstance(data[0], str):
        print("Info: Converting string list to dictionary format")
        data = [{'content': text} for text in data]
    
    # 如果是单个字符串，转换为字典列表
    elif isinstance(data, str):
        print("Info: Converting single string to dictionary format")
        data = [{'content': data}]
    # ===== 数据格式检查结束 =====
    
    # ===== 原有代码保持不变 =====
    # 使用pathlib处理路径，确保正确性
    current_script_dir = Path(__file__).parent
    project_root = current_script_dir.parent.parent
    
    # 处理模板路径
    if not os.path.isabs(template_path):
        template_path = project_root / template_path
    else:
        template_path = Path(template_path)
    
    # 确保输出目录存在
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    # 检查模板文件是否存在
    if not template_path.exists():
        print(f"Error: Template file not found at {template_path}")
        return

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_html = f.read()
    except Exception as e:
        print(f"Error reading template file: {e}")
        return

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
            page = browser.new_page(device_scale_factor=2) # Higher device scale factor for better quality
            page.set_viewport_size({'width': 1242, 'height': 1660})

            for i, item in enumerate(data):
                print(f"Generating image {i+1}/{len(data)}...")
                title = item.get('title', f"Title {i+1}")
                content = item.get('content', '')
                footer = item.get('footer', "Shared on Xiaohongshu")

                html = template_html.replace('{{TITLE}}', title)
                html = html.replace('{{CONTENT}}', content)
                html = html.replace('{{FOOTER}}', footer)

                page.set_content(html, wait_until='networkidle')
                screenshot_path = output_dir / f'image_{i+1}.png'
                # For PNG, the image is lossless. For JPEG, you could set quality.
                page.screenshot(path=str(screenshot_path), type='png')

            browser.close()
            print("Image generation complete.")
        except Exception as e:
            print(f"An error occurred during image generation: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate images from text using a template.')
    parser.add_argument('--texts', nargs='+', help='The texts to generate images for.')
    parser.add_argument('--text-file', help='Path to a text file with one piece of content per line.')
    parser.add_argument('--json-file', help='Path to a JSON file with structured data.')
    parser.add_argument('--output-dir', default='output/images', help='The directory to save the generated images.')
    parser.add_argument('--template-path', default='src/templates/base_template.html', help='The path to the HTML template.')
    args = parser.parse_args()

    data = []
    if args.texts:
        data = [{'content': text} for text in args.texts]
    elif args.text_file:
        try:
            with open(args.text_file, 'r', encoding='utf-8') as f:
                data = [{'content': line.strip()} for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: Text file not found at {args.text_file}")
            return
    elif args.json_file:
        try:
            with open(args.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: JSON file not found at {args.json_file}")
            return
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {args.json_file}")
            return

    if not data:
        print("No input data provided. Please use --texts, --text-file, or --json-file.")
        return

    generate_images(data, args.output_dir, args.template_path)

if __name__ == '__main__':
    main()