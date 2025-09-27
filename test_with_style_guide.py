#!/usr/bin/env python3
"""
使用样式指南进行综合测试
"""

import sys
from pathlib import Path

# 添加路径
project_root = Path(__file__).parent
sys.path.append(str(project_root / "src" / "scripts"))

from generator import generate_images

def test_various_styles():
    """测试多种样式场景"""
    test_cases = [
        {
            'name': '短标题测试',
            'data': [{'title': '简洁标题', 'content': '简短内容测试', 'footer': '底部信息'}]
        },
        {
            'name': '长内容测试', 
            'data': [{
                'title': '较长的标题文字测试',
                'content': '这是一段较长的正文内容，用于测试文字换行和行间距效果。多行文字可以更好地检验排版质量。',
                'footer': '较长的底部信息文字'
            }]
        },
        {
            'name': '多条目测试',
            'data': [
                {'title': '第一条', 'content': '内容一', 'footer': '底部一'},
                {'title': '第二条', 'content': '内容二', 'footer': '底部二'},
                {'title': '第三条', 'content': '内容三', 'footer': '底部三'}
            ]
        }
    ]
    
    for test_case in test_cases:
        print(f"\n🧪 测试: {test_case['name']}")
        output_dir = project_root / "output" / "style_tests" / test_case['name'].replace(' ', '_')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            generate_images(test_case['data'], str(output_dir))
            print(f"✅ {test_case['name']} 测试通过")
        except Exception as e:
            print(f"❌ {test_case['name']} 测试失败: {e}")

def main():
    """主函数"""
    print("🎯 样式指南综合测试")
    print("=" * 50)
    
    test_various_styles()
    
    print("\n📊 测试完成总结:")
    print("请检查 output/style_tests/ 文件夹中的生成结果")
    print("重点关注:")
    print("1. 字体大小和颜色是否符合样式指南")
    print("2. 行间距和段落间距是否合适")
    print("3. 不同长度内容的显示效果")
    print("4. 整体布局是否平衡美观")

if __name__ == "__main__":
    main()