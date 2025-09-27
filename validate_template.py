#!/usr/bin/env python3
"""
验证模板是否符合样式指南
"""

from pathlib import Path
import re

def check_template_compliance():
    """检查模板是否符合样式指南"""
    template_path = Path("src/templates/base_template.html")
    
    if not template_path.exists():
        print("❌ 模板文件不存在")
        return False
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🎨 模板样式合规性检查")
    print("=" * 50)
    
    # 检查关键样式要素
    checks = [
        ("渐变背景", r"background.*gradient", "应该包含渐变背景"),
        ("字体家族", r"font-family.*Noto Sans SC", "应该使用Noto Sans SC字体"),
        ("标题字体大小", r"font-size.*80px", "标题应为80px"),
        ("正文字体大小", r"font-size.*48px", "正文应为48px"),
        ("行间距", r"line-height.*2", "行间距应为2.0"),
    ]
    
    all_passed = True
    for check_name, pattern, expectation in checks:
        if re.search(pattern, content, re.IGNORECASE):
            print(f"✅ {check_name}: 符合要求")
        else:
            print(f"❌ {check_name}: 不符合要求 - {expectation}")
            all_passed = False
    
    # 检查颜色方案
    color_checks = [
        ("渐变开始色", r"#FFC3A0", "应该包含#FFC3A0"),
        ("渐变结束色", r"#FFAFBD", "应该包含#FFAFBD"),
        ("标题文字色", r"#333333", "标题应为#333333"),
    ]
    
    print("\n🎨 颜色方案检查:")
    for color_name, hex_code, expectation in color_checks:
        if hex_code in content:
            print(f"✅ {color_name}: 包含{hex_code}")
        else:
            print(f"❌ {color_name}: 缺少{hex_code} - {expectation}")
            all_passed = False
    
    return all_passed

def generate_test_with_guide():
    """使用样式指南生成测试图片"""
    import sys
    sys.path.append("src/scripts")
    
    from generator import generate_images
    
    # 使用样式指南中的示例内容
    test_data = [
        {
            'title': '小红书风格测试',
            'content': '这是根据样式指南优化的模板测试。字体大小、颜色和间距都应符合规范。',
            'footer': '样式指南验证'
        }
    ]
    
    output_dir = Path("output/style_guide_test")
    output_dir.mkdir(exist_ok=True)
    
    print("\n🔄 生成样式指南测试图片...")
    generate_images(test_data, str(output_dir))
    
    return output_dir

def main():
    """主函数"""
    print("📋 样式指南合规性验证")
    print("=" * 50)
    
    # 检查模板合规性
    is_compliant = check_template_compliance()
    
    if is_compliant:
        print("\n🎉 模板符合样式指南要求！")
        # 生成测试图片
        test_dir = generate_test_with_guide()
        print(f"✅ 测试图片已生成到: {test_dir}")
        
        print("\n📝 下一步建议:")
        print("1. 打开生成的图片检查视觉效果")
        print("2. 与参考图片进行对比")
        print("3. 如有需要，进一步微调样式")
    else:
        print("\n⚠️ 模板需要进一步优化以符合样式指南")
        print("💡 建议使用Gemini CLI继续优化模板")

if __name__ == "__main__":
    main()