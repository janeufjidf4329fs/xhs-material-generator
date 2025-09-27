#!/usr/bin/env python3
"""
项目安装和设置脚本
"""

from pathlib import Path
import subprocess
import sys

def check_python_version():
    """检查Python版本"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python版本符合要求: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python版本过低，需要3.8+，当前: {version.major}.{version.minor}")
        return False

def install_requirements():
    """安装依赖包"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依赖包安装完成")
        return True
    except subprocess.CalledProcessError:
        print("❌ 依赖包安装失败")
        return False

def install_playwright_browsers():
    """安装Playwright浏览器"""
    try:
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        print("✅ Playwright浏览器安装完成")
        return True
    except subprocess.CalledProcessError:
        print("❌ Playwright浏览器安装失败")
        return False

def main():
    """主安装函数"""
    print("🚀 小红书宣传图生成器 - 环境设置")
    print("=" * 50)
    
    steps = [
        ("Python版本检查", check_python_version),
        ("安装依赖包", install_requirements),
        ("安装浏览器", install_playwright_browsers)
    ]
    
    all_passed = True
    for step_name, step_func in steps:
        print(f"\n🔧 {step_name}...")
        if not step_func():
            all_passed = False
            break
    
    if all_passed:
        print("\n🎉 环境设置完成！")
        print("\n💡 下一步:")
        print("1. 运行示例: python examples/demo_usage.py")
        print("2. 查看文档: docs/project_summary.md")
    else:
        print("\n❌ 环境设置失败，请检查错误信息")

if __name__ == "__main__":
    main()