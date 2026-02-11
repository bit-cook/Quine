#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多语言衔尾蛇链生成器

生成一个多语言循环链，例如:
Python → Ruby → Perl → C → Python

每种语言输出下一种语言的代码，最后一种输出第一种
"""

import json

class OuroborosChain:
    """生成多语言衔尾蛇链"""
    
    def __init__(self, languages):
        """
        languages: 语言配置列表
        每项格式: {'name': 'python', 'extension': 'py', 'template': ...}
        """
        self.languages = languages
        self.chain = []
    
    def generate_template(self, lang_name, next_code):
        """
        为指定语言生成输出下一种语言代码的模板
        
        这是简化的框架，实际需要为每种语言定制
        """
        templates = {
            'python': lambda nc: f'''#!/usr/bin/env python3
"""
衔尾蛇链 - Python 节点
"""
next_code = {repr(nc)}
print(next_code)
''',
            'ruby': lambda nc: f'''#!/usr/bin/env ruby
# 衔尾蛇链 - Ruby 节点
next_code = {json.dumps(nc)}
puts next_code
''',
            'perl': lambda nc: f'''#!/usr/bin/env perl
# 衔尾蛇链 - Perl 节点
my $next_code = {json.dumps(nc)};
print $next_code;
''',
            'c': lambda nc: f'''#include <stdio.h>
/* 衔尾蛇链 - C 节点 */
int main() {{
    const char* code = {json.dumps(nc)};
    printf("%s", code);
    return 0;
}}
''',
        }
        return templates.get(lang_name, templates['python'])(next_code)
    
    def build_chain(self):
        """构建完整的循环链"""
        n = len(self.languages)
        
        # 从后向前构建（最后一个语言输出第一个）
        current = self.languages[0]['template']
        
        for i in range(n - 1, 0, -1):
            lang = self.languages[i]
            current = self.generate_template(lang['name'], current)
        
        # 最后生成第一个语言的代码
        first = self.languages[0]
        current = self.generate_template(first['name'], current)
        
        return current

# 示例用法
if __name__ == '__main__':
    # 定义链中的语言
    chain_config = [
        {'name': 'python', 'extension': 'py', 'template': '...'},
        {'name': 'ruby', 'extension': 'rb', 'template': '...'},
        {'name': 'perl', 'extension': 'pl', 'template': '...'},
        {'name': 'c', 'extension': 'c', 'template': '...'},
    ]
    
    generator = OuroborosChain(chain_config)
    
    # 输出链的第一个节点
    print("# 多语言衔尾蛇链生成器")
    print("# 使用方法: 运行生成的文件，它会输出下一个语言的代码")
    print()
    
    # 这里只是演示框架
    # 真正的实现需要精心构造每种语言的代码
    result = generator.build_chain()
    print(result[:500] + "..." if len(result) > 500 else result)
