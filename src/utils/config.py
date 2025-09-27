#!/usr/bin/env python3
"""
配置文件管理
"""

from pathlib import Path
import json

class Config:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.config_path = self.project_root / "config.json"
        self.default_config = {
            "image_width": 1242,
            "image_height": 1660,
            "output_format": "png",
            "output_quality": 95,
            "template_file": "src/templates/base_template.html",
            "output_dir": "output/images"
        }
        self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = self.default_config
            self.save_config()
    
    def save_config(self):
        """保存配置文件"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get(self, key, default=None):
        """获取配置值"""
        return self.config.get(key, default)

# 全局配置实例
config = Config()