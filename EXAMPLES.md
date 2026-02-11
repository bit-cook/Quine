# Quine 示例集

这里展示了各种 Quine 的实现示例，从最简到最复杂。

## 极简 Quine

### Python (29 字符)
```python
_='_=%r;print(_%%_)';print(_%_)
```

运行:
```bash
python -c "_='_=%r;print(_%%_)';print(_%_)"
```

### JavaScript (45 字符)
```javascript
(function $(){console.log('('+$+')()')})()
```

### Ruby (25 字符)
```ruby
s=%q{s=%q{s};printf s,s};printf s,s
```

### C (120 字符)
```c
main(){char*s="main(){char*s=%c%s%c;printf(s,34,s,34);}";printf(s,34,s,34);}
```

## 分步解析

让我们看看 Python Quine 是如何工作的：

```python
s='s=%r;print(s%%s)'
print(s%s)
```

### 第一步：定义数据
```
s = 's=%r;print(s%%s)'
```
变量 `s` 存储了代码的字符串表示。

### 第二步：格式化输出
```
print(s % s)
```
将 `s` 自身填入 `%r` 的位置。

### 展开过程
```
s % s 
=> 's=%r;print(s%%s)' % 's=%r;print(s%%s)'
=> "s='s=%r;print(s%%s)';print(s%%s)"
```

最终输出与源代码完全相同！

## 更复杂的例子

### 带注释的 Quine
```python
#!/usr/bin/env python3
# 这是一个 Quine
s='#!/usr/bin/env python3\n# 这是一个 Quine\ns=%r;print(s%%s)';print(s%s)
```

### 多行 Quine
```python
#!/usr/bin/env python3
"""
多行 Quine 示例
可以包含任意文档字符串
"""

s = '''#!/usr/bin/env python3
"""
多行 Quine 示例
可以包含任意文档字符串
"""

s = %r
print(s %% s)'''

print(s % s)
```

## 验证方法

### Unix/Linux/Mac
```bash
python quine.py | diff - quine.py
```

如果没有任何输出，说明验证通过！

### Windows (PowerShell)
```powershell
python quine.py | Out-File temp.txt; Compare-Object (Get-Content quine.py) (Get-Content temp.txt)
```

### Python 验证脚本
```python
import subprocess

with open('quine.py', 'r') as f:
    original = f.read()

result = subprocess.run(['python', 'quine.py'], 
                       capture_output=True, text=True)

if original == result.stdout:
    print("✓ Quine 验证通过!")
else:
    print("✗ Quine 验证失败!")
```

## 常见错误

### 错误 1：忘记转义
```python
# 错误！引号不匹配
s="s="s...""  

# 正确
s='s=%r;print(s%%s)'
```

### 错误 2：多余的空格
```python
# 可能有问题的末尾空格
s='...'  # <- 这里有空格

# 安全做法
s='...';print(s%s)  # 紧凑格式
```

### 错误 3：编码问题
```python
# 确保文件编码声明正确
# -*- coding: utf-8 -*-
```

## 进阶技巧

### 使用 chr() 避免引号
```python
s='s='+chr(39)+'s='+chr(39)+chr(37)+'r'+chr(39)+';print(s%%s)'+chr(39);print(s%s)
```

### 使用 base64 编码
```python
import base64
s='aW1wb3J0IGJhc2U2NA...';exec(base64.b64decode(s))
```
（注：这不是真正的 Quine，因为需要解码）

## 练习

尝试修改以下代码使其成为 Quine：

```python
# 练习 1：补全这个 Quine
s = ???
print(s % s)
```

<details>
<summary>点击查看答案</summary>

```python
s = 's = %r\nprint(s %% s)'
print(s % s)
```

</details>

## 分级教学：从第一个 Quine 到 Ouroboros 链

下面给出一个循序渐进的学习路径，对应仓库中的实际文件，方便你一边读文档一边跑代码。

### Level 1：5 行 Python Quine（入门版）

目标：写出一个结构清晰、便于理解的多行 Quine。

核心思路：

```python
s = 's = %r\nprint(s %% s)'
print(s % s)
```

- 第 1 行：把“程序本身”当作字符串模板存进 `s`  
- 第 2 行：用 `s` 自己去填充 `%r`，得到完整源码并打印出来  

建议：先在交互式环境里改动字符串内容，观察输出如何变化。

### Level 2：带注释与文档字符串的 Quine

对应示例：`classic/quine.py`

- 在 Level 1 的基础上，加上 shebang、编码声明、文档字符串、注释等“现实世界”元素  
- 难点在于：所有这些头部内容也必须被包含在字符串模板中，否则“输出 ≠ 源文件”

练习方向：尝试为自己的 Quine 增加模块级文档字符串、作者信息等，同时保持验证通过。

### Level 3：迭代 Quine（A → B → A）

对应示例：`variants/iterative_quine.py`

概念：  
不再要求“一个程序直接打印自己”，而是构造一个长度为 2 的循环：

- 程序 A 输出程序 B 的源码  
- 程序 B 输出程序 A 的源码  

当你像 `demo.py` 那样执行 A 并把输出保存为 B、再执行 B 时，整体行为形成 A → B → A 的闭环。

### Level 4：Multiquine（多语言自复制）

对应示例：`variants/multiquine.py`

目标：让同一个源文件在多种语言下都能作为 Quine 使用。典型做法是：

- 让不同语言把同一块文本“看成”各自语法下的注释或字符串  
- 巧妙安排分隔符，使得每种语言只执行属于自己的那部分代码

练习建议：

1. 阅读 `multiquine.py`，找出“属于 Python 的段落”和“属于其他语言的段落”  
2. 尝试扩展一个新的语言分支（例如再加一个 bash 或 Ruby 路径）

### Level 5：Ouroboros 链（衔尾蛇循环）

对应示例：`variants/ouroboros/chain.py` 及同目录下其他文件。

概念：  
构造一条长度为 N 的程序链：

> A 输出 B 的源码，B 输出 C，…，最后 Z 输出 A。

这是一种“多步不动点”的构造方式，直观呈现了间接自指：  
没有哪个程序直接打印自己，但整个环路作为一个整体却在“输出自身”。

建议体验方式：

1. 依次运行链条中的程序，观察每一步的输出与下一个文件内容的对应关系  
2. 尝试修改链条中的某一环节，观察整体是否仍能形成闭环  
3. 思考如何用验证脚本自动检查“从 A 出发 N 步之后是否回到 A”

#### 高级实战：三节点 Python Ouroboros + 自动验证

本仓库在 `variants/ouroboros/` 中提供了一条可验证的 3 节点 Python 链：

```text
py_chain_0.py → py_chain_1.py → py_chain_2.py → py_chain_0.py
```

- 每个节点都会读取链中“下一个节点”的源码并原样打印  
- 组合起来就是一个真正的闭环 Ouroboros 链

你可以使用专用验证脚本来自动检查整个环路：

```bash
python tools/ouroboros_validator.py
```

输出示例：

```text
Ouroboros chain validation
============================================================
OK  py_chain_0.py → py_chain_1.py
OK  py_chain_1.py → py_chain_2.py
OK  py_chain_2.py → py_chain_0.py
```

如果想构造自己的 N 节点链，只需要：

1. 在 `variants/ouroboros/` 下新增类似结构的 `py_chain_k.py` 文件  
2. 同步更新每个文件里的 `names = [...]` 顺序  
3. 调用验证器时显式指定链顺序：

```bash
python tools/ouroboros_validator.py py_chain_0.py py_chain_1.py py_chain_2.py
```
