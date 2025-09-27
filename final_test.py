#!/usr/bin/env python3
"""
最终全面测试 - 验证所有功能
"""

import sys
from pathlib import Path

def test_environment():
    """测试环境配置"""
    print("🔧 环境配置测试...")
    
    # 检查必要文件
    required_files = [
        "src/templates/base_template.html",
        "src/scripts/generator.py",
        "docs/style_guide.md",
        "docs/project_summary.md"
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path} - 存在")
        else:
            print(f"❌ {file_path} - 缺失")
            all_exist = False
    
    return all_exist

def test_generation_function():
    """测试图片生成功能"""
    print("\n🖼️ 图片生成功能测试...")
    
    try:
        sys.path.append("src/scripts")
        from generator import generate_images
        
        # 测试数据
        test_data = [
            {
                'title': '最终功能测试',
                'content': '这是最终测试，验证所有功能是否正常运作。',
                'footer': '项目完成测试'
            }
        ]
        
        output_dir = Path("output/final_test")
        generate_images(test_data, str(output_dir))
        
        # 检查生成结果
        image_files = list(output_dir.glob("*.png"))
        if image_files:
            print(f"✅ 图片生成成功 - 生成 {len(image_files)} 张图片")
            return True
        else:
            print("❌ 图片生成失败 - 未找到输出文件")
            return False
            
    except Exception as e:
        print(f"❌ 生成功能测试失败: {e}")
        return False

def test_documentation():
    """测试文档完整性"""
    print("\n📚 文档完整性测试...")
    
    docs_to_check = [
        "README.md",
        "docs/style_guide.md", 
        "docs/project_summary.md",
        "dev_log.md"
    ]
    
    all_valid = True
    for doc_path in docs_to_check:
        path = Path(doc_path)
        if path.exists() and path.stat().st_size > 100:  # 大于100字节认为有效
            print(f"✅ {doc_path} - 完整")
        else:
            print(f"❌ {doc_path} - 不完整或缺失")
            all_valid = False
    
    return all_valid

def main():
    """主测试函数"""
    print("🎯 小红书宣传图生成器 - 最终测试")
    print("=" * 60)
    
    tests = [
        test_environment,
        test_generation_function, 
        test_documentation
    ]
    
    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ 测试执行错误: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 所有测试通过！ ({passed}/{total})")
        print("\n✅ 项目开发完成！")
        print("📦 准备交付...")
    else:
        print(f"⚠️ 测试结果: {passed}/{total} 通过")
        print("\n🔧 需要修复未通过的测试")

if __name__ == "__main__":
    main()