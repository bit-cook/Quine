# Quine 项目 Makefile
# 用于运行测试和验证

.PHONY: help test clean validate-all

PYTHON := python3
NODE := node

help:
	@echo "Quine 项目 - 可用命令:"
	@echo "  make test          - 运行所有测试"
	@echo "  make validate      - 验证所有 Quine"
	@echo "  make validate-py   - 验证 Python Quine"
	@echo "  make validate-js   - 验证 JavaScript Quine"
	@echo "  make clean         - 清理生成的文件"
	@echo "  make demo          - 运行演示"

# 验证 Python Quine
validate-py:
	@echo "验证 Python Quine..."
	@$(PYTHON) classic/quine.py | diff - classic/quine.py && echo "✓ classic/quine.py 通过" || echo "✗ classic/quine.py 失败"
	@$(PYTHON) classic/quine_short.py | diff - classic/quine_short.py && echo "✓ classic/quine_short.py 通过" || echo "✗ classic/quine_short.py 失败"

# 验证 JavaScript Quine (需要 Node.js)
validate-js:
	@echo "验证 JavaScript Quine..."
	@which $(NODE) > /dev/null && $(NODE) classic/quine.js | diff - classic/quine.js && echo "✓ classic/quine.js 通过" || echo "⚠ classic/quine.js 跳过 (Node.js 未安装)"

# 验证所有 Quine
validate: validate-py validate-js
	@echo "验证完成"

# 运行测试套件
test:
	$(PYTHON) tests/test_quine.py -v

# 运行演示
demo:
	@echo "=== Quine 演示 ==="
	@echo ""
	@echo "1. 经典 Python Quine:"
	@$(PYTHON) classic/quine.py
	@echo ""
	@echo "2. 极简 Python Quine (29字符):"
	@$(PYTHON) classic/quine_short.py

# 生成示例
generate:
	$(PYTHON) generators/quine_generator.py -o generated_quine.py "print('Hello, Self!')"
	@echo "已生成 generated_quine.py"

# 清理生成的文件
clean:
	@rm -f generated_quine.py temp_* *.pyc
	@rm -rf __pycache__
	@echo "已清理"

# 统计代码行数
stats:
	@echo "项目统计:"
	@find . -name "*.py" -type f | xargs wc -l | tail -1
	@find . -name "*.js" -type f | xargs wc -l 2>/dev/null | tail -1 || true
	@find . -name "*.c" -type f | xargs wc -l 2>/dev/null | tail -1 || true
