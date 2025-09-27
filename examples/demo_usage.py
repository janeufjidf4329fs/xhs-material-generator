#!/usr/bin/env python3
"""
小红书宣传图生成器 - 使用示例（修复版）
"""

import sys
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "src" / "scripts"))

def demo_basic_usage():
    """基础使用示例"""
    print("🎯 小红书宣传图生成器 - 使用示例")
    print("=" * 50)
    
    try:
        from generator import generate_images
        
        # 示例1: 简单文本生成（修复版）
        print("1. 生成简单宣传图...")
        # 修复：使用字典格式而不是字符串
        simple_data = [{'content': '欢迎使用小红书宣传图生成器！'}]
        generate_images(simple_data, "output/examples/simple")
        print("✅ 简单示例生成完成")
        
        # 示例2: 多条目生成
        print("\n2. 生成多张宣传图...")
        multiple_items = [
            {
                'title': '功能特点', 
                'content': '批量生成、样式统一、高质量输出', 
                'footer': '特点介绍'
            },
            {
                'title': '技术优势', 
                'content': '基于Playwright、支持自定义模板', 
                'footer': '技术说明'
            },
            {
                'title': '使用场景', 
                'content': '营销推广、内容创作、社交媒体', 
                'footer': '应用领域'
            }
        ]
        generate_images(multiple_items, "output/examples/multiple")
        print("✅ 多条目示例生成完成")
        
        # 示例3: 从文件生成（演示）
        print("\n3. 文件生成示例（演示）...")
        # 创建示例文本文件
        text_file_path = Path("examples/sample_texts.txt")
        text_file_path.parent.mkdir(exist_ok=True)
        
        with open(text_file_path, 'w', encoding='utf-8') as f:
            f.write("第一条宣传内容\n")
            f.write("第二条宣传内容，可以包含多行文字\n")
            f.write("第三条宣传内容，展示批量生成能力\n")
        
        print(f"✅ 示例文本文件已创建: {text_file_path}")
        print("💡 实际使用时可以运行: python src/scripts/generator.py --text-file examples/sample_texts.txt")
        
        print(f"\n📁 示例图片已生成到 output/examples/ 文件夹")
        print("💡 请查看生成的图片文件")
        
    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        print("请先运行安装脚本: python setup.py")
    except Exception as e:
        print(f"❌ 生成过程中出错: {e}")
        import traceback
        traceback.print_exc()

def show_usage_instructions():
    """显示使用说明"""
    print("\n📖 使用说明")
    print("=" * 50)
    
    print("1. 基本使用:")
    print("   python src/scripts/generator.py --texts \"您的宣传内容\"")
    
    print("\n2. 从文件批量生成:")
    print("   python src/scripts/generator.py --text-file 您的文件.txt")
    
    print("\n3. 使用JSON格式数据:")
    print("   python src/scripts/generator.py --json-file 数据.json")
    
    print("\n4. 自定义输出目录:")
    print("   python src/scripts/generator.py --texts \"内容\" --output-dir 自定义路径")

if __name__ == "__main__":
    demo_basic_usage()
    show_usage_instructions()