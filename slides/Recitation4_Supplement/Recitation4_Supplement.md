---
title: SI100B_Fall_2026_Recitation_4_Supplement
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
autoTitlePage: true
makeTitle:
  lecture: SI100B Fall 2026 Recitation 4
  title: Supplement · VS Code 与 Linux 终端
  detail: SI100B 2026 Staff
makeThanks: true
---

## 今天练习什么？

- **VS Code**：运行程序、打断点、观察变量、单步执行。
- **Linux 终端**：找文件、运行程序、保存输出、查看日志。
- **与 AI 配合**：读懂它给出的命令，用运行结果验证建议。

示例文件位于配套的 `examples/` 文件夹。

VS Code 截图包含 Windows / macOS 界面；操作名称相同。终端命令按 **Linux / WSL 的 Bash** 演示，PowerShell 的语法有区别。

<!--s-->

# VS Code：运行与调试

<!--v-->

## 创建文件：打开文件夹

- 首先打开VSCode, 选择打开文件夹以打开你的工作目录

<img src="images/spring2026/PixPin_2026-04-19_20-11-13.png" width="85%" style="float: middle;">

Note: 原课件：Spring_2026/Recitation6/Recitation6.md，“VSCode运行Python程序”部分；原截图直接沿用，仅精简说明并补充保存文件。

<!--v-->

## 创建文件：新建文件

- 点击左上角**文件** - **创建新文件**；或者点屏幕中间的创建新文件也行

<img src="images/spring2026/PixPin_2026-04-19_20-11-42.png" width="85%" style="float: middle;">

Note: 原课件：Spring_2026/Recitation6/Recitation6.md，“VSCode运行Python程序”部分；原截图直接沿用，仅精简说明并补充保存文件。

<!--v-->

## 创建文件：选择 Python

- 文件类型选择 Python；保存时使用 `.py` 后缀。

<img src="images/spring2026/PixPin_2026-04-19_20-12-09.png" width="85%" style="float: middle;">

Note: 原课件：Spring_2026/Recitation6/Recitation6.md，“VSCode运行Python程序”部分；原截图直接沿用，仅精简说明并补充保存文件。

<!--v-->

## 运行代码

- 写好代码后先保存，点击右上角小三角运行；结果显示在下方终端。

<img src="images/spring2026/PixPin_2026-04-19_20-14-28.png" width="85%" style="float: middle;">

Note: 原课件：Spring_2026/Recitation6/Recitation6.md，“VSCode运行Python程序”部分；原截图直接沿用，仅精简说明并补充保存文件。

<!--v-->

## 语法错误：查看 Problems

- 当你的代码有语法上的错误时，VSCode会直接察觉，并体现在Problems中

<img src="images/spring2026/PixPin_2026-04-19_20-17-09.png" width="85%" style="float: middle;">

Note: 原课件：Spring_2026/Recitation6/Recitation6.md，“VSCode运行Python程序”部分；原截图直接沿用，仅精简说明并补充保存文件。

<!--v-->

## 运行报错：查看 Terminal

- 当你的代码在运行时报错，terminal中会提供报错信息

<img src="images/spring2026/PixPin_2026-04-19_20-16-45.png" width="85%" style="float: middle;">

Note: 原课件：Spring_2026/Recitation6/Recitation6.md，“VSCode运行Python程序”部分；原截图直接沿用，仅精简说明并补充保存文件。


<!--v-->

## 选择 Python 解释器

安装 Microsoft 的 **Python / Python Debugger** 扩展。

命令面板：Windows / Linux `Ctrl+Shift+P`，macOS `⌘+Shift+P`。

输入 **Python: Select Interpreter**，选择课程使用的 Python 环境。

<img src="images/02-interpreter.png" width="88%" alt="Python 解释器选择菜单，列出本机的多个 Python 环境" />

这里选的是“用哪个 Python 来运行”，不是选择代码文件。

Note: 官方说明：https://code.visualstudio.com/docs/python/environments 。截图中的路径属于演示机器；学生应选择自己的课程环境，不必复制路径。

<!--v-->

## debug 常用方法

- `print()`：输出中间结果，检查程序执行到了哪里。
- `pdb` 是 Python 内置调试器；用 `breakpoint()` 暂停并进入调试。
- **VS Code 断点调试**：暂停程序，在界面中查看变量变化。

下面使用 `main` 调用 `add_numbers` 的例子，观察函数内部的执行过程。

Note: 原课件：Spring_2025/Recitation_4/Recitation_4B.md，“debug常用方法”。沿用 print、pdb、breakpoint 与 VS Code 调试的内容；将原文 breakpoint 补为可调用的 breakpoint()。

<!--v-->

## 断点调试示例

```python
# 一个如何打断点进行debug的演示
def add_numbers(x, y):
    print(f"Adding {x} to {y}")
    result = x + y
    print(f"Result:{result}")
    return result


def main(x0, y0):
    x1 = x0 * 3
    y1 = y0 * 4
    return add_numbers(x1, y1)

a = 5
b = 7
c = main(a, b)
print(f'3x{a} + 4x{b} = {c}')
```

示例文件：`debug_functions.py`。先预测：最后的 `c` 是多少？

Note: 代码直接取自 Spring_2025/Recitation_4/Recitation_4B.md 的断点演示，未修改程序逻辑。预期最后输出 3x5 + 4x7 = 43。

<!--v-->

## ① 设置断点，查看变量

在 `debug_functions.py` **第 12 行**左侧点击，按 **F5** 调试。

<img src="images/15-functions-main.png" width="88%" alt="暂停在 main 的第 12 行；局部变量 x0=5、x1=15、y0=7、y1=28，调用堆栈显示 main" />

黄色行**尚未执行**：`x1=15`、`y1=28`，即将调用 `add_numbers`。

首次启动时选择 **Python Debugger → Python File**。

Note: 截图为旧课件的原始代码在 VS Code 中实际运行。官方说明：https://code.visualstudio.com/docs/python/debugging 。演示工作区已配置启动文件；学生可直接选择调试当前 Python 文件。

<!--v-->

## ② 单步进入，观察函数内部

<img src="images/16-functions-step.png" width="92%" alt="F11 进入 add_numbers，再按两次 F10 后，局部变量 x=15、y=28、result=43；调用堆栈包含 add_numbers 和 main" />

- 从上一页按 **F11** 进入 `add_numbers`，再按两次 **F10**。
- 此时 `result=43`；左侧“调用堆栈”显示函数之间的调用关系。
- 按 **F5** 继续运行，在终端检查最后的输出：`3x5 + 4x7 = 43`。

Note: 截图实际暂停在第 5 行，表示第 4 行的加法赋值已执行，第 5 行的打印尚未执行。代码来自 Spring_2025 Recitation 4B；截图为本次补充。官方说明：https://code.visualstudio.com/docs/debugtest/debugging 。

<!--v-->

## 调试工具栏

<img src="images/debug-toolbar.png" width="55%" alt="VS Code 调试工具栏：继续、逐过程、单步进入、单步跳出、重启、停止" />

- **F5 继续**：运行到下一个断点，或程序结束。
- **F10 逐过程**：执行当前语句；遇到函数调用时通常不进入。
- **F11 单步进入**：进入可调试的函数，查看内部过程。
- **Shift+F11 跳出**：执行到当前函数返回。
- **Shift+F5 停止**：结束本次调试。
- **绿色圆箭头**：重新开始本次调试。

笔记本可能需要配合 `Fn`；也可以直接点击工具栏。

Note: 官方说明：https://code.visualstudio.com/docs/debugtest/debugging 。断点、异常仍可能提前中断“逐过程”或“跳出”；工具栏中的绿色圆箭头是重启。

<!--v-->

## 写代码时常用的功能

- **快速打开文件**：`Ctrl+P`；macOS 用 `⌘+P`。
- **查找文本**：`Ctrl+F`；整个文件夹查找用 `Ctrl+Shift+F`。
- **注释 / 取消注释**：选中几行，按 `Ctrl+/`。
- **跳到定义 / 重命名变量**：`F12` / `F2`。
- **查看问题**：`Ctrl+Shift+M`，定位报错和警告。

本页的 `Ctrl` 快捷键在 macOS 中换成 `⌘`。

拿不准快捷键时，打开命令面板，直接搜索功能名称。

Note: 官方说明：https://code.visualstudio.com/docs/editing/codebasics 。函数和变量的语义导航依赖 Python 语言支持；快捷键可被用户配置覆盖。

<!--v-->

## 终端和调试控制台

**终端 Terminal**：输入系统命令；也接收程序的 `input()`。

```bash
python3 debug_functions.py
```

**调试控制台 Debug Console**：程序暂停时，查看 Python 表达式。

```python
x
y
result
```

想给 `input()` 输入内容时，切到 **终端**，不要输在调试控制台。

Note: 官方说明：https://code.visualstudio.com/docs/python/debugging 。本课件使用 integratedTerminal 控制台配置；调试控制台求值可能调用函数并改变程序状态，入门练习只查看变量。

<!--s-->

# Linux 终端：文件、命令与 AI

<!--v-->

## 终端：神秘的黑客工具？

- 你可能听过命令行、命令提示符、终端、交互式 Bash。
- 终端是**交互式**的：输入一句指令，立刻执行并得到结果。
- VS Code 运行代码时，也会弹出终端，输入命令来运行程序。

打开 **终端 → 新建终端**，试试：

```bash
echo Hello, World
```

本节使用 **Bash**（Linux / WSL；macOS 也可使用）。Windows 的 PowerShell / CMD 语法不同。

提示符 `$` 不用输入；若看到 `>>>`，先用 `exit()` 退出 Python。

Note: 原课件：Example/Example_1.md（SI100+ 2024），“终端：神秘的黑客工具？”。沿用交互式命令行、echo 练习及 VS Code 运行机制，补充 Bash 环境区别。参考：https://code.visualstudio.com/docs/terminal/basics ；https://ubuntu.com/tutorials/command-line-for-beginners 。

<!--v-->

## 我在哪里？文件在哪里？

<img src="images/09-paths.png" width="92%" alt="Bash 终端中依次运行 pwd、ls、cd ..、cd si100b-demo 和 ls *.py" />

- 使用 `cd` 切换目录；空格用来区分命令和参数。
- `pwd` 显示当前目录；`ls` 列出文件。
- `..` 上一级，`~` 家目录；`ls *.py` 查看 Python 文件。
- `ls -la` 查看详细信息和隐藏文件；Linux 文件名区分大小写。

<!--v-->

## 相对路径与文件操作

下面的命令在示例文件夹中执行：

```bash
mkdir practice  # 创建文件夹
cp sample.in practice/input.txt  # 复制
mv practice/input.txt practice/data.txt
ls practice  # 查看结果：data.txt
rm -i practice/data.txt  # 确认后删除副本
```

- `practice/data.txt` 是相对于 **当前目录** 的路径。
- 路径中有空格时加引号，例如 `cd "my project"`。
- `mv` 可移动或重命名；`rm` 通常不会放入回收站。

Note: mkdir 示例假设 practice 尚不存在；重复跟做可改用 mkdir -p practice。所有删除都只针对刚创建的练习副本。参考：https://ubuntu.com/tutorials/command-line-for-beginners 。

<!--v-->

## 终端常用技巧

- **Tab**：补全文件名、目录名；有多个候选时再按一次。
- **↑ / ↓**：找回上一条或下一条历史命令。
- **Ctrl+R**：在 Bash 中搜索历史；`Esc` 退出搜索。
- **Ctrl+A / Ctrl+E**：移到行首 / 行尾。
- **Ctrl+L**：清理当前显示；不会停止程序。
- **右键粘贴（VS Code 终端）**：Windows 无选区时右键粘贴；Linux / macOS 右键打开菜单后选择“粘贴”。

程序一直在运行：按 **Ctrl+C** 中断。

进入 `less` 或 `man` 后：按 **q** 返回终端。

Note: Tab 补全、上下键历史、右键粘贴直接沿用 Example/Example_1.md（SI100+ 2024）的终端内容，并补充不同系统的默认行为。Bash 默认 Emacs 编辑模式下的 Readline 快捷键：https://www.gnu.org/software/bash/manual/html_node/Readline-Interaction.html 。右键默认行为参考：https://code.visualstudio.com/docs/terminal/basics 。Windows 有选区时右键会复制；macOS 默认还会选择光标处单词。终端设置或用户自定义快捷键可能覆盖默认值。

<!--v-->

## 看文件、找错误、数行数

<img src="images/12-grep-pipe.png" width="92%" alt="用 cat 查看日志，grep -n 找到第 3 行 ERROR，再通过管道和 wc -l 统计错误行数为 1" />

- `cat` 看短文件；长文件用 `less run.log`。
- `grep -n "ERROR" run.log` 查找匹配行，并显示行号。
- `|` 把前一个命令的标准输出交给后一个；`wc -l` 数行。

<!--v-->

## 用文件代替反复输入

`sum_input.py`：读取一行整数，输出总和。

```python
values = input().split()
total = 0
for value in values:
    total += int(value)
print(total)
```

`sample.in` 内容为 `4 6 2`；`expected.txt` 内容为 `12`。

```bash
python3 sum_input.py < sample.in > actual.txt
```

`<` 从文件读输入；`>` 将标准输出写入文件，**会覆盖原内容**。

<!--v-->

## 运行并比较结果

<img src="images/11-redirection.png" width="94%" alt="使用输入和输出重定向运行程序，再以 diff 比较预期与实际输出；结果一致，没有差异输出" />

```bash
diff -u expected.txt actual.txt
```

- 文件相同：没有差异输出，返回提示符。
- 文件不同：`-` 表示预期文件中的行，`+` 表示实际文件中的行。
- `>>` 是追加；`2> error.log` 单独保存错误输出。

Note: diff 的符号对应此处的参数顺序。文件不存在等错误仍会报错，不能把所有“未显示差异”都视为测试通过。完整程序可直接用重定向；只要求提交函数的题目需另写本地测试调用。

<!--v-->

## 常见问题的第一步

- **找不到文件**：先运行 `pwd` 和 `ls`，检查路径和大小写。
- **command not found**：检查拼写，以及命令是否安装。
- **ModuleNotFoundError**：检查运行程序的 Python 环境。
- **看起来卡住了**：程序可能在等待 `input()`；切到终端输入。

```bash
python3 --version
python3 -c "import sys; print(sys.executable)"
```

编辑器选中的解释器与终端中的 `python3`，可能不是同一个。

<!--v-->

## AI 工具为什么离不开终端？

- **执行明确操作**：读文件、运行程序、执行测试。
- **处理大量文件**：查找日志、批量处理、重复执行命令。
- **使用远程环境**：服务器和训练任务常通过 Linux / SSH 操作。

AI 编程助手也会调用这些工具：

**查看代码 → 提出修改 → 执行命令 → 阅读结果 → 再检查**

会用终端，才能看懂它做了什么，并判断结果是否正确。

Note: AI agent 的编辑器、终端、测试等工具能力参考：https://code.visualstudio.com/docs/agents/overview 。Linux/SSH 入门参考：https://ubuntu.com/tutorials/command-line-for-beginners 。本页是工具工作方式的概括，不承诺任意 AI 产品都有全部能力。

<!--v-->

## 把问题说清楚，验证 AI 的建议

提问时提供：**环境 + 完整命令 + 完整报错 + 预期结果**。

```text
我在 Linux 的 Bash 中运行：
python3 sum_input.py < sample.in
终端提示：sample.in: No such file or directory
请解释这个错误，并告诉我先检查什么。
```

拿到建议后：读懂命令 → 确认目录 → 执行 → 检查输出。

**课程作业遵守课程规定：不要用 AI 代写作业代码。**

Note: 课程要求见本仓库 slides/Recitation1/Recitation1.md 与 slides/Recitation2/Recitation2.md。例子只讨论路径错误，不涉及作业答案。遇到求助问题时保留完整文本，不只截最后一行。
