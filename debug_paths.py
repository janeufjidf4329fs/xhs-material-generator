#!/usr/bin/env python3
"""
路径诊断脚本
"""

from pathlib import Path

print("🔧 路径诊断信息：")
print(f"当前工作目录: {Path.cwd()}")

project_root = Path(__file__).parent
print(f"项目根目录: {project_root}")

template_path = project_root / "src" / "templates" / "base_template.html"
print(f"模板文件路径: {template_path}")
print(f"模板文件是否存在: {template_path.exists()}")

# 尝试不同的路径组合
possible_paths = [
    "src/templates/base_template.html",
    "./src/templates/base_template.html",
    "../src/templates/base_template.html",
    "src\\templates\\base_template.html",
]

print("\n尝试不同路径格式：")
for path in possible_paths:
    test_path = Path(path)
    abs_path = project_root / test_path
    print(f"{path} -> 存在: {abs_path.exists()}")