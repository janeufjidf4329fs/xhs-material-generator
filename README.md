开始使用: 查看 examples/ 目录中的示例代码
获取帮助: 阅读 docs/ 目录中的详细文档
项目仓库: https://github.com/janeufjidf4329fs/xhs-material-generator


# 小红书宣传图批量生成器

一个基于Python和Playwright的自动化工具，用于批量生成符合小红书平台标准的宣传图片。

## ✨ 功能特点

- 🚀 **批量生成** - 支持从文本文件、JSON文件或命令行参数批量处理
- 🎨 **样式统一** - 基于统一的HTML模板，确保所有图片风格一致
- 📱 **平台优化** - 专为小红书平台优化（1242×1660像素）
- 🔧 **易于使用** - 简单的命令行界面，无需设计技能
- ✅ **质量保证** - 包含完整的测试框架和质量验证

## 🛠️ 技术栈

- **编程语言**: Python 3.8+
- **浏览器自动化**: Playwright
- **模板引擎**: HTML/CSS
- **图片处理**: Pillow (PIL)
- **测试框架**: pytest


## 📦 安装

### 环境要求
- Python 3.8 或更高版本
- 现代浏览器（Chromium）

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/janeufjidf4329fs/xhs-material-generator.git
   cd xhs-material-generator

2. **安装依赖**
   ```bash
   pip install -r requirements.txt

3. **安装Playwright浏览器**
   ```bash
   playwright install chromium


## 🚀 操作流程

### 第一步：环境验证
   ```bash
   # 运行快速测试，验证环境配置是否正确
python final_test.py

   # 如果显示"所有测试通过"，说明环境配置成功
   ```

### 第二步：生成示例图片
   ```bash
   # 运行演示脚本，生成示例图片
   python examples/demo_usage.py

   # 查看生成的图片
   # 打开 output/examples/ 文件夹查看结果
   ```

### 第三步：自定义内容生成

**方式一：命令行直接生成**
   ```bash
   # 生成单张图片
   python src/scripts/generator.py --texts "您的宣传内容"

   # 生成多张图片
   python src/scripts/generator.py --texts "第一条内容" "第二条内容" "第三条内容"
   ```

**方式二：从文本文件批量生成**
   ```bash
   # 1. 创建文本文件（每行一条内容）
   echo "第一条宣传内容" > content.txt
   echo "第二条宣传内容" >> content.txt
   echo "第三条宣传内容" >> content.txt

   # 2. 批量生成图片
   python src/scripts/generator.py --text-file content.txt   
   ```

**方式三：使用JSON格式数据**
   ```bash
   # 1. 创建data.json文件，内容如下：
   [
  {
    "title": "产品介绍",
    "content": "这是一款强大的宣传图生成工具",
    "footer": "了解更多"
  },
  {
    "title": "功能特点", 
    "content": "支持批量处理、多种格式、高质量输出",
    "footer": "立即体验"
  }
   ]

   # 2. 生成图片
   python src/scripts/generator.py --json-file data.json
   ```

### 第四步：查看生成结果
   -**所有生成的图片保存在 output/ 文件夹中**
   -**图片命名格式：image_001.png, image_002.png 等**
   -**默认输出目录：output/images/**


## 🎯 极速体验

如果您想最快速体验功能，只需运行：

  ```bash
  # 一键安装和体验（推荐新手）
   python setup.py
   python examples/demo_usage.py
   ```

## 📁 项目结构

xhs-material-generator/
├── src/                    # 源代码
│   ├── scripts/           # Python脚本
│   └── templates/         # HTML模板
├── references/            # 参考图片
├── output/               # 生成结果
├── docs/                # 项目文档
├── test/                # 测试代码
└── examples/            # 使用示例


## 📚 文档
   -**样式指南[validate_template]** - 设计规范和样式标准
   -**项目总结[docs/project_summary.md]** - 完整的技术文档
   -**开发日志[dev_log.md]** - 项目开发过程记录



## 🧪 测试

运行完整测试套件：

  ```bash
  python final_test.py
  ```

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目。


## 📄 许可证

本项目采用MIT许可证。


