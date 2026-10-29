/* Quine official site — interactions */
(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  function escapeHTML(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  /* ---------- Hero typewriter ---------- */
  var QUINE_LINE = "s='s=%r;print(s%%s)';print(s%s)";
  var tw = $("#typewriter");
  if (tw) {
    var i = 0;
    (function type() {
      if (i <= QUINE_LINE.length) {
        tw.textContent = QUINE_LINE.slice(0, i);
        i++;
        setTimeout(type, 55);
      } else {
        setTimeout(function () { i = 0; type(); }, 2600);
      }
    })();
  }

  /* ---------- Stat counters ---------- */
  function animateCounters() {
    $$(".stat-num").forEach(function (el) {
      var target = parseInt(el.getAttribute("data-count"), 10) || 0;
      var cur = 0;
      var step = Math.max(1, Math.round(target / 30));
      var timer = setInterval(function () {
        cur += step;
        if (cur >= target) { cur = target; clearInterval(timer); }
        el.textContent = cur;
      }, 30);
    });
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animateCounters(); obs.disconnect(); }
      });
    }, { threshold: 0.3 });
    var stats = $(".hero-stats");
    if (stats) io.observe(stats);
  } else { animateCounters(); }

  /* ---------- Live JS quine ---------- */
  var runBtn = $("#run-js");
  if (runBtn) {
    var srcEl = $("#js-source");
    var SOURCE = srcEl ? srcEl.textContent : "";
    runBtn.addEventListener("click", function () {
      var captured = [];
      var origLog = console.log;
      console.log = function () {
        captured.push(Array.prototype.join.call(arguments, " "));
      };
      var err = null;
      try {
        new Function(SOURCE)();
      } catch (e) {
        err = e;
      } finally {
        console.log = origLog;
      }
      var outEl = $("#js-output");
      var verdict = $("#js-verdict");
      var output = captured.join("\n");
      if (err) {
        outEl.textContent = "错误: " + err.message;
        verdict.textContent = "✗ 运行出错";
        verdict.className = "live-verdict bad";
        return;
      }
      outEl.textContent = output;
      // The program prints its own source; compare ignoring a single trailing newline.
      var normOut = output.replace(/\n$/, "");
      var normSrc = SOURCE.replace(/\n$/, "");
      if (normOut === normSrc) {
        verdict.textContent = "✓ 输出与源代码逐字节一致 —— 这是一个真正的 Quine！";
        verdict.className = "live-verdict ok";
      } else {
        verdict.textContent = "✗ 输出与源代码不一致";
        verdict.className = "live-verdict bad";
      }
    });
  }

  /* ---------- Copy buttons ---------- */
  $$("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      function done() {
        var old = btn.textContent;
        btn.textContent = "已复制 ✓";
        btn.classList.add("done");
        setTimeout(function () { btn.textContent = old; btn.classList.remove("done"); }, 1500);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { fallback(); });
      } else { fallback(); }
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy"); } catch (e) {}
        document.body.removeChild(ta); done();
      }
    });
  });

  /* ---------- Gallery ---------- */
  var ITEMS = [
    {
      cat: "classic", title: "Python 极简 Quine", lang: "Python", tag: "classic/quine_short.py",
      desc: "仅 29 个字符，最短的自复制程序之一。变量 _ 同时充当代码与数据。",
      code: "_='_=%r;print(_%%_)';print(_%_)"
    },
    {
      cat: "classic", title: "Python 标准 Quine", lang: "Python", tag: "classic/quine.py",
      desc: "用 %r 让 repr() 自动处理所有转义，是大多数 Python Quine 的原型。",
      code: "s='s=%r;print(s%%s)';print(s%s)"
    },
    {
      cat: "classic", title: "C Quine", lang: "C", tag: "classic/quine.c",
      desc: "printf 的 %c 精确重构换行与引号，整份源码（含注释）被复现。",
      code: 'char *s = "...%c...";\nprintf(s, 10, 34, s, 34, 10, ...);'
    },
    {
      cat: "classic", title: "Rust Quine", lang: "Rust", tag: "classic/quine.rs",
      desc: "Rust 要求字面量格式串，故用 replacen + {:?} 完成自引用。",
      code: 'print!("{}", s.replacen(\'@\', &format!("{:?}", s), 1))'
    },
    {
      cat: "classic", title: "Go Quine", lang: "Go", tag: "classic/quine.go",
      desc: "借助 %q 的引号转义，fmt.Printf 逐字节还原源码。",
      code: "s := \"...%q...\";\nfmt.Printf(s, s)"
    },
    {
      cat: "classic", title: "JavaScript Quine", lang: "JavaScript", tag: "classic/quine.js",
      desc: "函数经 toString 取得自身源码；本站“在线体验”运行的就是同款。",
      code: "(function q(){console.log('('+q+')()')})()"
    },
    {
      cat: "classic", title: "Java Quine", lang: "Java", tag: "classic/quine.java",
      desc: "System.out.printf 用 %c 控制换行与双引号，还原整份类源码。",
      code: "System.out.printf(s, 10, 34, s, 34, 10, ...);"
    },
    {
      cat: "esoteric", title: "Shell Quine", lang: "Bash", tag: "esoteric/quine.sh",
      desc: "多行单引号模板 + printf 的 \\47（八进制单引号），不读取自身文件。",
      code: "s='...s=\\47%s\\47...'\nprintf \"$s\" \"$s\""
    },
    {
      cat: "esoteric", title: "Brainfuck Quine", lang: "Brainfuck", tag: "esoteric/quine.bf",
      desc: "Erik Bosman 的 505 字节真实 Quine，纯命令字符，仓库内置解释器可验证。",
      code: "-->+++>+>+>+>+++++>++>++>->+++>++>+> ..."
    },
    {
      cat: "variant", title: "迭代 Quine (2-循环)", lang: "Python", tag: "variants/iterative_quine.py",
      desc: "自包含的参数化旋转 Quine：A 输出 B，B 再输出 A，闭环且不读写文件。",
      code: "n = 0\nN = 2\ns = '...%d...%d...%r...'\nprint(s % ((n+1)%N, N, s))"
    },
    {
      cat: "variant", title: "多语言 Multiquine", lang: "Python 2/3", tag: "variants/multiquine.py",
      desc: "同一份源码在 Python 2 与 Python 3 下都输出自身。",
      code: "from __future__ import print_function\ns = '...%r...'\nprint(s % s)"
    },
    {
      cat: "variant", title: "Quine 生成器", lang: "Python", tag: "generators/quine_generator.py",
      desc: "把任意代码包装成真正的自复制程序；--run 时执行被包装的代码。",
      code: "_s = %r\n_p = %r\n...\nprint(_s % (_s, _p))"
    },
    {
      cat: "ouroboros", title: "自包含衔尾蛇链", lang: "Python", tag: "variants/ouroboros/py_chain_*.py",
      desc: "N 节点闭环：第 i 个程序输出第 i+1 个的源码。无文件读取，可生成任意长度。",
      code: "# 节点 i\nn = i; N = 3\ns = '...%d...%d...%r...'\nprint(s % ((n+1)%N, N, s))"
    },
    {
      cat: "art", title: "生命游戏 Quine", lang: "Python", tag: "artistic/game_of_life_quine.py",
      desc: "既是 Quine 又是可运行的生命游戏：默认打印自身，--play 播放演化动画。",
      code: "if '--play' in sys.argv:\n    exec(_p)   # 运行游戏\nelse:\n    print(_s % (_s, _p))"
    },
    {
      cat: "art", title: "音乐 / 二维码 / ASCII Quine", lang: "Python", tag: "artistic/",
      desc: "把旋律播放、二维码生成、ASCII 图案装进自复制程序里（模式 flag 触发）。",
      code: "_p = <payload>\nif '--play' in sys.argv: exec(_p)\nelse: print(_s % (_s, _p))"
    }
  ];

  var grid = $("#gallery-grid");
  if (grid) {
    ITEMS.forEach(function (it) {
      var card = document.createElement("div");
      card.className = "card";
      card.setAttribute("data-cat", it.cat);
      card.innerHTML =
        '<div class="card-head"><span class="card-title">' + escapeHTML(it.title) + "</span>" +
        '<span class="card-lang">' + escapeHTML(it.lang) + "</span></div>" +
        '<div class="card-desc">' + escapeHTML(it.desc) + "</div>" +
        "<pre><code>" + escapeHTML(it.code) + "</code></pre>" +
        '<div class="card-foot"><span class="card-tag">' + escapeHTML(it.tag) + "</span></div>";
      grid.appendChild(card);
    });
  }

  var filters = $("#filters");
  if (filters) {
    filters.addEventListener("click", function (e) {
      var btn = e.target.closest(".filter");
      if (!btn) return;
      $$(".filter").forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var f = btn.getAttribute("data-filter");
      $$(".card").forEach(function (c) {
        var show = f === "all" || c.getAttribute("data-cat") === f;
        c.classList.toggle("hidden", !show);
      });
    });
  }
})();
