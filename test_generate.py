#!/usr/bin/env python3
"""
测试图片生成功能 - 简单版本
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def test_basic_setup():
    """测试基础设置"""
    print("🧪 开始测试基础设置...")
    
    # 检查必要文件夹是否存在
    required_dirs = [
        "src/templates",
        "src/scripts", 
        "references",
        "output/images"
    ]
    
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"✅ 文件夹存在: {dir_path}")
        else:
            print(f"❌ 文件夹缺失: {dir_path}")
            return False
    
    # 检查必要文件是否存在
    required_files = [
        "src/templates/base_template.html",
        "references/reference_1.png"
    ]
    
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"✅ 文件存在: {file_path}")
        else:
            print(f"❌ 文件缺失: {file_path}")
            return False
    
    return True

def test_python_imports():
    """测试Python模块导入"""
    print("\n🧪 测试Python模块导入...")
    
    try:
        import playwright
        print("✅ playwright 模块可以导入")
    except ImportError:
        print("❌ 无法导入 playwright，请运行: pip install playwright")
        return False
    
    try:
        from PIL import Image
        print("✅ PIL (Pillow) 模块可以导入") 
    except ImportError:
        print("❌ 无法导入 PIL，请运行: pip install pillow")
        return False
    
    return True

def main():
    """主测试函数"""
    print("=" * 50)
    print("🎯 开始测试图片生成功能")
    print("=" * 50)
    
    # 运行所有测试
    setup_ok = test_basic_setup()
    imports_ok = test_python_imports()
    
    print("\n" + "=" * 50)
    if setup_ok and imports_ok:
        print("🎉 基础测试通过！环境配置正确。")
        print("\n📝 下一步：需要创建实际的图片生成代码。")
        print("   请运行: gemini -f gemini.md '请创建图片生成代码'")
    else:
        print("❌ 测试失败，请检查上述错误信息。")
        print("\n💡 解决方法：")
        if not setup_ok:
            print("   - 确保所有必要的文件夹和文件都已创建")
        if not imports_ok:
            print("   - 重新安装Python包: pip install playwright pillow")
    
    print("=" * 50)

if __name__ == "__main__":
    main()