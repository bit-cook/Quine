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

```python
# 练习 2：创建一个输出 "Hello" 然后自身代码的 Quine
s = ???
```

<details>
<summary>点击查看答案</summary>

```python
s = "print('Hello')\ns=%r\nprint(s%%s)"
exec(s)
print(s % s)
```

</details>
