# 项目交付清单与打包指南

本指南用于项目交付和打包，确保在不同环境中可以顺利运行。

## 1. 核心文件清单

确保以下文件和目录包含在交付包中：

- **`src/`**: 核心源代码目录
  - `src/scripts/generator.py`: 图片生成器主脚本
  - `src/templates/base_template.html`: HTML样式模板
- **`docs/`**: 项目文档
  - `docs/style_guide.md`: 样式规范文档
  - `docs/project_summary.md`: 项目总结文档
- **`requirements.txt`**: Python依赖项列表
- **`run.bat`**: (Windows) 一键运行脚本
- **`run.sh`**: (Linux/macOS) 一键运行脚本

## 2. 环境配置说明

在运行项目之前，请确保已完成以下环境配置：

1. **安装Python**: 确保已安装Python 3.8或更高版本。
2. **安装依赖**: 在项目根目录下运行以下命令，安装所有必需的Python库。
   ```bash
   pip install -r requirements.txt
   ```
3. **安装Playwright浏览器**: Playwright需要下载浏览器文件才能工作。运行以下命令进行安装。
   ```bash
   playwright install
   ```

## 3. 一键运行脚本

为了方便使用，我们提供了跨平台的运行脚本。这些脚本会自动调用`generator.py`并传递参数。

### `run.bat` (适用于Windows)

```batch
@echo off
python src/scripts/generator.py %*
```

### `run.sh` (适用于Linux/macOS)

```bash
#!/bin/bash
python3 src/scripts/generator.py "$@"
```
*注意：在Linux/macOS上，首次使用前请为`run.sh`添加执行权限：`chmod +x run.sh`*

## 4. 使用示例

使用一键运行脚本，可以更简洁地执行命令。

**示例1：通过命令行生成图片**
```bash
# Windows
.\run.bat --texts "这是标题一" "这是内容一"

# Linux/macOS
./run.sh --texts "这是标题一" "这是内容一"
```

**示例2：从JSON文件批量生成**
```bash
# Windows
.\run.bat --json-file data.json

# Linux/macOS
./run.sh --json-file data.json
```
