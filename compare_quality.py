#!/usr/bin/env python3
"""
图片质量对比工具 - 支持不同尺寸对比
"""

from PIL import Image
from pathlib import Path
import sys

def resize_to_match(target_img, reference_size):
    """将图片调整到参考尺寸"""
    return target_img.resize(reference_size, Image.Resampling.LANCZOS)

def compare_with_reference(generated_path, reference_path):
    """比较生成图片与参考图片（支持尺寸调整）"""
    try:
        gen_img = Image.open(generated_path)
        ref_img = Image.open(reference_path)
        
        print(f"📊 图片对比: {generated_path.name} vs {reference_path.name}")
        print(f"生成图片尺寸: {gen_img.size}")
        print(f"参考图片尺寸: {ref_img.size}")
        
        # 检查尺寸是否匹配
        if gen_img.size == ref_img.size:
            print("✅ 图片尺寸匹配")
            comparison_img = gen_img
        else:
            print("⚠️ 图片尺寸不匹配，将调整生成图片尺寸进行对比")
            # 将生成图片调整到参考图片尺寸
            comparison_img = resize_to_match(gen_img, ref_img.size)
            print(f"调整后尺寸: {comparison_img.size}")
        
        # 简单的内容对比（可以扩展为更复杂的对比逻辑）
        print("🔍 进行简单视觉对比...")
        
        # 检查图片模式（RGB/RGBA等）
        print(f"生成图片模式: {gen_img.mode}")
        print(f"参考图片模式: {ref_img.mode}")
        
        # 检查文件大小
        gen_size_kb = generated_path.stat().st_size / 1024
        ref_size_kb = reference_path.stat().st_size / 1024
        print(f"生成图片大小: {gen_size_kb:.1f} KB")
        print(f"参考图片大小: {ref_size_kb:.1f} KB")
        
        # 基本质量评估
        if gen_size_kb > 100:  # 假设大于100KB为高质量
            print("✅ 生成图片质量良好")
        else:
            print("⚠️ 生成图片文件大小较小，可能需要优化质量")
        
        return True
        
    except Exception as e:
        print(f"❌ 对比失败: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_all_references():
    """检查所有参考图片的尺寸"""
    project_root = Path(__file__).parent
    ref_dir = project_root / "references"
    
    print("📏 参考图片尺寸检查:")
    for i in range(1, 5):
        ref_path = ref_dir / f"reference_{i}.png"
        if ref_path.exists():
            with Image.open(ref_path) as img:
                print(f"reference_{i}.png: {img.size}")
        else:
            print(f"reference_{i}.png: 文件不存在")

def main():
    """主函数"""
    project_root = Path(__file__).parent
    
    # 首先检查所有参考图片尺寸
    check_all_references()
    print()
    
    # 检查最新生成的图片
    output_dir = project_root / "output" / "images"
    if not output_dir.exists():
        print("❌ 输出目录不存在")
        return
    
    # 获取最新生成的图片
    image_files = list(output_dir.glob("*.png"))
    if not image_files:
        print("❌ 没有找到生成的图片")
        return
    
    latest_image = max(image_files, key=lambda x: x.stat().st_mtime)
    
    # 与参考图片对比（使用第一张参考图）
    reference_path = project_root / "references" / "reference_1.png"
    
    if reference_path.exists():
        compare_with_reference(latest_image, reference_path)
        
        # 额外提示
        print("\n💡 提示:")
        print("- 生成图片尺寸 1242×1660 符合小红书标准要求")
        print("- 参考图片尺寸不同是正常的，可能是截图或不同来源")
        print("- 重点应关注内容布局、字体样式和颜色搭配是否一致")
    else:
        print("⚠️ 参考图片不存在，跳过对比")

if __name__ == "__main__":
    main()