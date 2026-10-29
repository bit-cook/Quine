# Quine 项目 Makefile
# 运行测试与一键验证所有 Quine

.PHONY: help validate test demo clean chain stats lint

PYTHON := python3
NODE := node

help:
	@echo "Quine 项目 - 可用命令:"
	@echo "  make validate   - 一键验证所有 Quine (推荐)"
	@echo "  make test       - 运行单元测试"
	@echo "  make demo       - 运行综合演示"
	@echo "  make chain N=5  - 生成 N 节点自包含衔尾蛇链"
	@echo "  make lint       - flake8 语法检查"
	@echo "  make stats      - 代码行数统计"
	@echo "  make clean      - 清理临时文件"

# 一键验证所有 Quine（类型感知：self/cycle/chain/emitter/multiling/brainfuck/generator）
validate:
	$(PYTHON) tools/validate_all.py -v

# 运行单元测试
test:
	$(PYTHON) -m unittest discover -s tests_new -v

# 运行综合演示
demo:
	@$(PYTHON) demo.py

# 生成 N 节点自包含衔尾蛇链 (默认 3)
chain:
	@$(PYTHON) variants/ouroboros/make_py_chain.py $(if $(N),$(N),3)
	@$(PYTHON) tools/ouroboros_validator.py

# flake8 语法检查
lint:
	@$(PYTHON) -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || true

# 统计代码行数
stats:
	@echo "Python:"; find . -name "*.py" -not -path './.git/*' -type f | xargs wc -l | tail -1

# 清理生成/临时文件
clean:
	@rm -f generated_* temp_* *.pyc
	@rm -rf __pycache__ .pytest_cache
	@echo "已清理"
