#!/usr/bin/env python3
"""
样式验证工具 - 检查优化效果
"""

from pathlib import Path
import time

def check_template_updates():
    """检查模板文件更新情况"""
    template_path = Path("src/templates/base_template.html")
    
    if not template_path.exists():
        print("❌ 模板文件不存在")
        return False
    
    # 获取文件修改时间
    mod_time = template_path.stat().st_mtime
    mod_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
    
    print(f"📄 模板文件信息:")
    print(f"   路径: {template_path}")
    print(f"   最后修改: {mod_time_str}")
    print(f"   文件大小: {template_path.stat().st_size} 字节")
    
    return True

def generate_test_images():
    """生成测试图片来验证样式"""
    import sys
    sys.path.append("src/scripts")
    
    from generator import generate_images
    
    test_texts = [
        "样式优化测试 - 标题文字",
        "这是正文内容区域，用于测试字体大小、行间距和颜色效果",
        "底部信息和行动号召按钮区域"
    ]
    
    output_dir = Path("output/style_test")
    output_dir.mkdir(exist_ok=True)
    
    print("🎨 生成样式测试图片...")
    generate_images(test_texts, str(output_dir))
    
    # 列出生成的测试图片
    image_files = list(output_dir.glob("*.png"))
    print(f"✅ 生成 {len(image_files)} 张测试图片")
    
    return image_files

def main():
    """主函数"""
    print("🎯 样式优化验证工具")
    print("=" * 50)
    
    # 检查模板状态
    if not check_template_updates():
        return
    
    print("\n🔍 验证步骤:")
    print("1. 检查模板文件是否已更新")
    print("2. 生成测试图片")
    print("3. 与参考图片进行视觉对比")
    print("4. 评估优化效果")
    
    # 生成测试图片
    test_images = generate_test_images()
    
    print(f"\n📋 下一步操作建议:")
    print("1. 打开 output/style_test/ 文件夹查看生成的测试图片")
    print("2. 同时打开参考图片进行视觉对比")
    print("3. 检查以下样式要素:")
    print("   - 字体大小和颜色")
    print("   - 行间距和段落间距")
    print("   - 背景颜色和渐变效果")
    print("   - 整体布局平衡")
    
    print(f"\n💡 如果样式不满意，可以继续优化:")
    print('   gemini -f gemini.md "请进一步优化模板样式，重点关注: [具体问题]"')

if __name__ == "__main__":
    main()