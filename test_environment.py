#!/usr/bin/env python3
"""
环境测试脚本
检查必要的包和文件是否存在
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """检查Python版本"""
    print("检查Python版本...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print(f"❌ Python版本过低，需要3.6以上，当前版本：{sys.version}")
        return False
    else:
        print(f"✅ Python版本满足要求：{sys.version}")
        return True

def check_package(package_name):
    """检查指定的包是否已安装"""
    try:
        __import__(package_name)
        print(f"✅ 包 {package_name} 已安装")
        return True
    except ImportError:
        print(f"❌ 包 {package_name} 未安装")
        return False

def check_files():
    """检查必要的文件是否存在"""
    print("检查必要的文件...")
    project_root = Path(__file__).parent
    required_files = [
        project_root / "src" / "templates" / "base_template.html",
        project_root / "references" / "reference_1.png",
        project_root / "references" / "reference_2.png",
        project_root / "references" / "reference_3.png",
        project_root / "references" / "reference_4.png",
    ]
    all_exists = True
    for file_path in required_files:
        if file_path.exists():
            print(f"✅ 文件存在：{file_path}")
        else:
            print(f"❌ 文件不存在：{file_path}")
            all_exists = False
    return all_exists

def main():
    """主函数"""
    print("开始环境测试...")
    success = True
    success &= check_python_version()
    success &= check_package("playwright")
    success &= check_package("PIL")
    success &= check_files()

    if success:
        print("🎉 环境测试通过！")
        print("下一步，我们将使用Gemini CLI生成图片生成脚本。")
    else:
        print("❌ 环境测试失败，请检查上述问题。")

if __name__ == "__main__":
    main()