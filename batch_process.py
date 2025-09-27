#!/usr/bin/env python3
"""
批量处理示例
"""

import sys
from pathlib import Path

# 添加路径
project_root = Path(__file__).parent
sys.path.append(str(project_root / "src" / "scripts"))

from generator import generate_images

def process_from_file(input_file):
    """从文件批量处理"""
    with open(input_file, 'r', encoding='utf-8') as f:
        texts = [line.strip() for line in f if line.strip()]
    
    output_dir = project_root / "output" / "images"
    
    print(f"📊 共读取 {len(texts)} 条文本")
    generate_images(texts, str(output_dir))

def main():
    """主函数"""
    # 示例文本数据
    sample_texts = [
        "小红书风格宣传图 - 第一张",
        "专业的内容创作工具，助力您的创意表达",
        "轻松生成高质量宣传素材，提升工作效率",
        "多种模板选择，满足不同场景需求"
    ]
    
    output_dir = project_root / "output" / "images"
    
    print("🚀 开始批量生成宣传图...")
    generate_images(sample_texts, str(output_dir))
    print("🎉 批量生成完成！")

if __name__ == "__main__":
    main()