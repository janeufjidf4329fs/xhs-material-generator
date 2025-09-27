#!/usr/bin/env python3
"""
演示图片生成功能 - 修复版本
"""

import sys
from pathlib import Path

# 添加路径
project_root = Path(__file__).parent
sys.path.append(str(project_root / "src" / "scripts"))

try:
    from generator import generate_images
    
    # 修正：使用字典列表而不是字符串列表
    test_data = [
        {
            'title': '测试标题1',
            'content': '这是第一张测试图片的内容，展示小红书风格的宣传图',
            'footer': '关注了解更多'
        },
        {
            'title': '测试标题2', 
            'content': '这是第二张测试图片的内容，可以包含多行文字和不同的样式',
            'footer': '立即行动'
        }
    ]
    
    output_dir = project_root / "output" / "images"
    
    print("🔄 开始生成测试图片...")
    generate_images(test_data, str(output_dir))
    print("✅ 图片生成完成！")
    
except Exception as e:
    print(f"❌ 生成过程中出错: {e}")
    import traceback
    traceback.print_exc()  # 显示详细的错误信息