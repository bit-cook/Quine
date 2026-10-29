-- SQL "Quine" — 概念说明 (conceptual, not executable)
-- =====================================================
-- 标准 SQL 没有 eval / 动态执行任意字符串的能力，因此无法写出严格意义上
-- “运行后逐字节输出自身源代码”的 Quine。下面给出最接近的几种思路，仅供学习。
--
-- 思路 1：自引用字符串（MySQL / PostgreSQL 的 REPLACE）
--   把整条查询作为字符串常量，再用 REPLACE 还原引号，得到与自身同形的文本。
SELECT REPLACE(
    'SELECT REPLACE(%s, CHAR(34), %s)%s',
    '%s', CHAR(34), CHAR(34)
) AS quine;
--
-- 思路 2：递归 CTE（PostgreSQL）——展示“自指”的数据结构
-- WITH RECURSIVE q AS (
--     SELECT 'WITH RECURSIVE q AS (SELECT ''quine'') SELECT * FROM q' AS code
-- )
-- SELECT code FROM q;
--
-- 结论：SQL 缺少图灵完备的“打印自身”原语，严格 Quine 在纯 SQL 中不可行。
-- 这正体现了 Quine 与语言表达力之间的关系（参见 THEORY.md）。
