#!/usr/bin/env python3
"""
完整功能演示
"""

import sys
import json
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "src" / "scripts"))

def create_sample_files():
    """创建示例文件"""
    print("📝 创建示例文件...")
    
    # 创建示例文本文件
    text_content = """小红书宣传图生成器
批量生成高质量宣传素材
支持多种输入格式
简单易用的命令行工具"""
    
    text_file = Path("examples/sample_texts.txt")
    text_file.parent.mkdir(exist_ok=True)
    text_file.write_text(text_content, encoding='utf-8')
    print(f"✅ 创建文本文件: {text_file}")
    
    # 创建示例JSON文件
    json_data = [
        {
            "title": "产品介绍",
            "content": "这是一款强大的宣传图生成工具",
            "footer": "了解更多"
        },
        {
            "title": "功能特点", 
            "content": "支持批量处理、多种格式、高质量输出",
            "footer": "立即体验"
        }
    ]
    
    json_file = Path("examples/sample_data.json")
    json_file.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"✅ 创建JSON文件: {json_file}")
    
    return text_file, json_file

def run_demo():
    """运行完整演示"""
    print("🎬 小红书宣传图生成器 - 完整功能演示")
    print("=" * 60)
    
    try:
        from generator import generate_images
        
        # 演示1: 直接文本生成
        print("\n1. 直接文本生成演示...")
        texts = ["直接输入的宣传内容", "第二条宣传内容"]
        generate_images(texts, "output/demo/direct_text")
        print("✅ 直接文本生成完成")
        
        # 演示2: 结构化数据生成
        print("\n2. 结构化数据生成演示...")
        structured_data = [
            {
                'title': '结构化标题1',
                'content': '这是结构化的内容，包含标题和正文',
                'footer': '底部信息1'
            },
            {
                'title': '结构化标题2',
                'content': '第二条结构化内容',
                'footer': '底部信息2'
            }
        ]
        generate_images(structured_data, "output/demo/structured")
        print("✅ 结构化数据生成完成")
        
        # 创建示例文件
        text_file, json_file = create_sample_files()
        
        print("\n3. 文件生成演示准备完成")
        print(f"   文本文件: {text_file}")
        print(f"   JSON文件: {json_file}")
        print("💡 实际使用时可以运行以下命令:")
        print(f"   python src/scripts/generator.py --text-file {text_file}")
        print(f"   python src/scripts/generator.py --json-file {json_file}")
        
        print(f"\n🎉 演示完成！")
        print(f"📁 生成的图片保存在 output/demo/ 文件夹")
        
    except Exception as e:
        print(f"❌ 演示过程中出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_demo()