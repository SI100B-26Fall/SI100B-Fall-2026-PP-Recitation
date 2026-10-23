---
title: SI100B_Fall_2026_Recitation_5_B
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
mermaid: false
autoTitlePage: true
makeTitle:
    lecture: SI100B · 第 5 次习题课（B 班）
    title: HW2、异常、字典与递归
    detail: SI100B 助教组 | 2026-10-23
makeThanks: false
---
# 第二次作业讲解（HW2）

<!--v-->

## HW2 中的原地修改与历史记录

- Q1 / Q2：函数返回什么？有没有改变传入的列表？
- Q3 打印站：当前队列会变化，已经保存的快照不能变化。

本次作业部分重点讲 Q3；函数和列表基础见上一讲。

<!--v-->

## 打印站：任务和队列

```text
time = 0
打印机 0: [[1, 2], [2, 1]]  # [任务编号, 剩余页数]
打印机 1: [[3, 1]]
completed = []
snapshots = []
```

- 一个列表表示一台打印机的有序队列；只打印队首。
- 只有 `TICK` 推进时间；空闲的秒也算时间。
- `MOVE` 保留已打印的进度；`CANCEL` 不记为完成。

<!--v-->

## MOVE：位置按哪一刻的队列算？

```text
原队列的 ID: [10, 20, 30, 40]
MOVE 20 0 2

先移除 20: [10, 30, 40]
再插到位置 2: [10, 30, 20, 40]
```

`position` 表示插入后前面有几个任务；同队列移动也先移除。

练习：若把队首移到队尾，插入位置应该是多少？

<!--v-->

## TICK：所有打印机同时工作

沿用前面的两台打印机，执行 `TICK 2`。

| 秒末 | 打印机 0 | 打印机 1 | 本秒完成 |
| --- | --- | --- | --- |
| 0 | `[[1, 2], [2, 1]]` | `[[3, 1]]` | — |
| 1 | `[[1, 1], [2, 1]]` | `[]` | 任务 3 |
| 2 | `[[2, 1]]` | `[]` | 任务 1 |

任务 2 要到第 3 秒才开始；不要在同一秒连续清空队列。

<!--v-->

## SNAP：只复制最外层，够吗？

```python
queues = [[[1, 2]], []]
shallow = queues[:]
snapshot = [[job[:] for job in queue] for queue in queues]
queues[0][0][1] -= 1
print(shallow)   # [[[1, 1]], []]
print(snapshot)  # [[[1, 2]], []]
```

这里一条任务只有整数 ID 和剩余页数；逐层复制到任务列表即可。
完整快照还要保存时间。这个片段只演示队列的独立性。

<!--v-->

## HW2：函数怎么拆

1. 查询：找到任务所在的打印机和队列位置。
2. 更新：按题意的先后顺序改变当前状态。
3. 保存：任务完成时记入完成记录；执行 `SNAP` 时复制时间和队列。
4. 输出：Q3 在全部命令执行后报告状态，按题目要求处理格式。

测试时分别检查：空队列、同队列 MOVE、连续 SNAP、同一秒多台打印机完成任务。

<!--s-->

# 异常处理（Exceptions）

<!--v-->

## 这段代码会抛出哪一种异常？
```python
def divide_unsafe(a, b):
    return a / b  # b 为 0 时抛出异常

# 测试
print(divide_unsafe(10, 0))
```

执行 `a / b` 时抛出 `ZeroDivisionError`，外层 `print` 没有拿到返回值。
看报错时，先读最后一行的类型和原因，再沿 traceback 找出错位置。

<!--v-->

## 常见异常：名字、类型和数值

下列例子分别运行，不要拼成一个程序。

| 类型 | 触发例子 | 原因 |
| --- | --- | --- |
| `NameError` | `print(total)` | `total` 尚未定义 |
| `TypeError` | `"3" + 1` | 不能把字符串和整数相加 |
| `ValueError` | `int("three")` | 字符串内容不能转成整数 |
| `ZeroDivisionError` | `10 / 0` | 除数是零 |

`SyntaxError` 是语法解析失败，如漏写冒号；同一文件里的 `try` 无法接住它自身的语法错误。

<!--v-->

## 常见异常：查找和文件

| 类型 | 触发例子 | 原因 |
| --- | --- | --- |
| `IndexError` | `[10, 20][2]` | 列表下标越界 |
| `KeyError` | `{"name": "Alice"}["age"]` | 字典里没有这个键 |
| `AttributeError` | `(123).upper()` | 整数没有 `upper` 方法 |
| `FileNotFoundError` | `open("missing.txt")` | 该路径没有文件 |

数字字面量外加括号，避免把方法调用写成语法错误。
递归调用过深还会遇到 `RecursionError`，后面再看。

<!--v-->

## try / except：出错后从哪里继续？

```python
raw = "abc"
try:
    number = int(raw)
    print("转换成功")
except ValueError as error:
    print("请输入整数")
print("本次处理结束")
```

输出两行：`请输入整数`、`本次处理结束`。

- `int` 出错后，跳过 `try` 中剩余语句，进入匹配的 `except`。
- 处理完成后继续往下走，不会自动重试失败的那一行。
- `as error` 取得异常对象；需要详细原因时可 `print(error)`。

<!--v-->

## 多个 except：只执行第一个匹配项

```python
raw = "0"
try:
    number = int(raw)
    print(10 / number)
except ValueError:
    print("不是整数")
except ZeroDivisionError:
    print("不能除以零")
```

`raw` 为 `"2"` 时输出 `5.0`；为 `"abc"` 时输出 `不是整数`；为 `"0"` 时输出 `不能除以零`。

- 具体异常写在宽泛异常前。
- 相同处理可合写：`except (ValueError, TypeError):`

<!--v-->

## try / except / else / finally

```python
raw = "2"  # 再分别试 "x"、"0"
try:
    print("try")
    value = 10 / int(raw)
except ValueError:
    print("except")
else:
    print("else", value)
finally:
    print("finally")
print("after")
```

先预测三种输入的输出。这里只捕获 `ValueError`。

<!--v-->

## 三条执行路径

| `raw` | 标准输出（按行） | 后续结果 |
| --- | --- | --- |
| `"2"` | `try` / `else 5.0` / `finally` / `after` | 正常结束 |
| `"x"` | `try` / `except` / `finally` / `after` | 异常已处理 |
| `"0"` | `try` / `finally` | `ZeroDivisionError` 继续向外抛出 |

- `else`：`try` 正常执行完、没有异常时才进入。
- `finally`：离开这个结构前执行清理；它不会自动消除异常。
- `except` 只接住对应 `try` 内的异常，不接住同级 `else` 或其他 `except` 的新异常。

<!--v-->

## return 前也会执行 finally

```python
def demo():
    try:
        return "结果"
    finally:
        print("清理")

print(demo())
```

输出顺序是 `清理`，然后 `结果`。先准备返回值，再执行 `finally`，最后返回。

不要在 `finally` 里写 `return`：它可能覆盖原返回值，甚至压掉正在传播的异常。

<!--v-->

## 读文件：用 with 负责关闭

```python
try:
    with open("score.txt", encoding="utf-8") as file:
        score = int(file.read())
except FileNotFoundError:
    print("找不到 score.txt")
except ValueError:
    print("文件里应当是一个整数")
else:
    print("读到的分数：", score)
```

文件打开成功后，无论读取、转换成功还是抛出异常，离开 `with` 都会关闭文件。
常见资源清理优先用 `with`；`finally` 可处理其他必须执行的收尾操作。

<!--v-->

## raise：主动说明输入不符合要求

```python
def parse_score(text):
    score = int(text)
    if not 0 <= score <= 100:
        raise ValueError("分数必须在 0 到 100 之间")
    return score

print(parse_score("85"))  # 85
```

`"abc"` 会在 `int` 处失败；`"120"` 能转成整数，但会在 `raise` 处失败。

`raise` 后，本次函数调用不再执行后面的 `return`。由调用者决定提示、重试或继续抛出。

<!--v-->

## 自定义异常：给范围错误一个名字

```python
class ScoreRangeError(ValueError):
    pass

def parse_score(text):
    score = int(text)
    if not 0 <= score <= 100:
        raise ScoreRangeError("分数超出 0 到 100")
    return score

try:
    print(parse_score("120"))
except ScoreRangeError as error:
    print(error)
```

输出 `分数超出 0 到 100`。它是 `ValueError` 的子类，也能被 `except ValueError` 捕获。

<!--v-->

## 需要重试，就明确写循环

```python
while True:
    try:
        number = int(input("请输入整数："))
    except ValueError:
        print("格式不对，请重试")
    else:
        break
print("得到", number)
```

- 只有转换成功才离开循环；这里只检查格式，没有限定数值范围。
- `try` 尽量只包住要处理的操作，别把整个程序都塞进去。
- 不用 `except: pass` 隐藏错误；拼写或逻辑错误应修正代码。

<!--s-->

# 字典（Dictionary）

<!--v-->

## 字典的键和值

- 字典保存键（key）与值（value）的对应关系，按键查找。
- 键唯一；再次给同一个键赋值，会覆盖旧值。
- 键必须可哈希：字符串、整数通常可以，列表和字典不可以。
- 值可以是列表、字典等对象；Python 3.7+ 按插入顺序遍历。

例：`{"Alice": 85, "Bob": 90}`，`"Alice"` 是键，`85` 是对应的值。
本节练习字典，不改变 HW2 打印站使用列表的要求。

<!--v-->

## 创建、增加、修改、删除

```python
person = {"name": "Alice", "age": 18}
person["class"] = "B"  # 新键：增加
person["age"] = 19  # 已有键：修改
person.update({"age": 20})  # 更新同名键
age = person.pop("age")  # 删除，并返回旧值
del person["class"]  # 删除，不返回旧值
print(age)
print(person)
```

输出 `20` 和 `{'name': 'Alice'}`。

`pop`、`del` 删除不存在的键会抛出 `KeyError`；`pop(key, 默认值)` 可约定键不存在时的返回值。

<!--v-->

## 读取：下标、get 和 in

```python
scores = {"Alice": 85}
print(scores["Alice"])        # 85
print(scores.get("Bob", 0))    # 0
print("Bob" in scores)        # False
print(85 in scores)           # False：in 检查键
print(85 in scores.values())  # True
```

`scores["Bob"]` 抛出 `KeyError`；`get("Bob")` 返回 `None`。
`get` 只读取，不会把 `"Bob"` 加进字典。默认值要符合实际含义，不能一律用 `0`。

<!--v-->

## 遍历：一次取到键和值

```python
scores = {"Alice": 85, "Bob": 90}
for name, score in scores.items():
    print(name, score)
print(list(scores.keys()))
print(list(scores.values()))
```

输出依次为：

```text
Alice 85
Bob 90
['Alice', 'Bob']
[85, 90]
```

`for key in scores` 默认遍历键。`keys()`、`values()`、`items()` 是随字典变化的视图。

<!--v-->

## 应用：统计每个单词出现几次

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
```

```text
{'cat': 3, 'dog': 2, 'bird': 1}
```

第一次出现时，用 `0 + 1` 建立记录；之后取出旧次数再加一。
真正写回字典的是左边的 `counts[word] = ...`。

<!--v-->

## 按班级整理名单

已有 `class1`，没有 `class2`。两人都先执行 `try`，谁随后会进入 `except`？

```python
students = [
    ["Alice", "class1"], ["Bob", "class2"],
    ["Celine", "class1"], ["Dan", "class2"]
]
classMember = {"class1": []}
for [name, className] in students:
    try:
        classMember[className] += [name]
    except KeyError:
        classMember[className] = [name]
print(classMember)
```

<!--v-->

## 同一班级的学生保存在同一个列表中

```text
{'class1': ['Alice', 'Celine'], 'class2': ['Bob', 'Dan']}
```

| 学生 | 查找结果 | 执行操作 |
| --- | --- | --- |
| Alice | `class1` 已存在 | 在原列表中加入 Alice |
| Bob | `class2` 不存在 | 捕获 `KeyError`，建立新列表 |
| Celine / Dan | 对应班级已存在 | 加入对应列表 |

也可以先判断 `className in classMember`，不必为了用异常而使用异常。

<!--v-->

## setdefault：没有这个键时才放入默认值

```python
groups = {}
groups.setdefault("class1", []).append("Alice")
groups.setdefault("class1", []).append("Celine")
print(groups)  # {'class1': ['Alice', 'Celine']}

other = {}
other.get("class1", []).append("Alice")
print(other)   # {}：临时列表没有存进字典
```

`setdefault` 返回已有值；键不存在时，先存入默认值再返回。
已有键的值不会被新的默认值覆盖。

<!--v-->

## 值是列表时：copy 仍然是浅复制

```python
groups = {"class1": ["Alice"]}
backup = groups.copy()
backup["class1"].append("Bob")
print(groups)  # {'class1': ['Alice', 'Bob']}

backup["class1"] = ["Dan"]
print(groups)  # {'class1': ['Alice', 'Bob']}
print(backup)  # {'class1': ['Dan']}
```

`append` 改的是共享列表；给 `backup["class1"]` 重新赋值，只替换副本中的对应关系。
这与 HW2 只复制外层队列时遇到的问题相同。

<!--v-->

## 遍历时删除：先收集键，再修改

```python
scores = {"Alice": 85, "Bob": 0, "Celine": 90}
to_remove = [key for key in scores if scores[key] == 0]
for name in to_remove:
    del scores[name]
print(scores)
```

```text
{'Alice': 85, 'Celine': 90}
```

直接遍历字典时增加或删除键，可能触发 `RuntimeError` 或漏遍历。
这里先生成独立的键列表，第二个循环再修改字典。

<!--s-->

# 递归（Recursion）

<!--v-->

## 阶乘的递推关系

- 正整数 `n` 的阶乘是从 `1` 到 `n` 的所有整数之积。
  `5! = 5 * 4 * 3 * 2 * 1 = 120`
- 因此，`n! = n × (n - 1)!`。

```text
factorial(n) = n × factorial(n-1)
```

已知 `(n - 1)!`，再乘以 `n` 就能得到 `n!`。

<!--v-->

## 阶乘计算到哪里停止？

- 本例只考虑非负整数 `n`。
- `0! = 1`，`1! = 1`，这两个结果可以直接返回。
- 当 `n > 1` 时，再计算 `n × (n - 1)!`。

例如：`5! = 5 * 4 * 3 * 2 * 1 = 120`。

<!--v-->

## 循环写法（Iteration）

```python
def factorial_iterative(n):
    result = 1
    # 从 1 乘到 n
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # 输出：120
```

**执行过程：**

* `result` 初始为 `1`。
* `i` 从 `1` 取到 `5`，每次把 `i` 乘进 `result`。
* 循环结束后返回累计的乘积。

<!--v-->

## 递归写法

```python
def factorial_recursive(n):
    # 终止条件：直接返回
    if n == 0 or n == 1:
        return 1
    # 递归调用：先计算 (n - 1)!
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # 输出：120
```

**执行过程：**

* **终止条件（base case）**：`n` 为 `0` 或 `1` 时返回 `1`，不再调用自己。
* **递归步骤**：取得 `factorial_recursive(n - 1)` 的返回值，乘以当前的 `n`，再返回。

<!--v-->

## 调用展开与返回过程

```
factorial_recursive(5)
= 5 * factorial_recursive(4)
= 5 * (4 * factorial_recursive(3))
= 5 * (4 * (3 * factorial_recursive(2)))
= 5 * (4 * (3 * (2 * factorial_recursive(1))))
= 5 * (4 * (3 * (2 * 1)))  <-- n = 1，直接返回 1
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
```

前一层调用保留在调用栈（call stack）中，等待后一层返回。
`factorial_recursive(1)` 返回后，各层依次完成乘法，最终得到 `120`。

<!--v-->

## 循环与递归：状态放在哪里？

**执行方式：**

* 循环：重复执行循环体。
* 递归：函数调用自身，每次调用有各自的局部变量。

**阶乘中的状态：**

* 循环写法用 `i` 和 `result` 保存计算进度。
* 递归写法中，每层调用保留自己的 `n`，等待下一层的结果。

**停止条件：**

* 循环写法遍历完 `range(1, n + 1)` 后结束。
* 递归写法到 `n == 0` 或 `n == 1` 时停止继续调用。

<!--v-->

## 循环与递归：调用开销

**仍以阶乘为例：**

* 两种写法都要完成乘法；递归写法还要创建和恢复函数调用。
* 循环写法只保留固定数量的工作变量。
* 递归写法会保留多层调用，输入越大，调用栈越深。

**递归深度限制：**

* Python 限制递归深度，调用过深通常会抛出 `RecursionError`。
* 不要把“先调大限制”当作修复错误递归的办法。

<!--v-->

## 递归为什么没有停下来？

检查两处：

1. 是否写了终止条件？
2. 参数每次变化后，是否越来越接近这个条件？

在阶乘中，`n > 1` 时每次传入 `n - 1`，最终会到 `1`。

如果一直传入原来的 `n`，即使写了 `n == 1`，也可能永远到不了。


<!--v-->

## 什么时候用循环？

* 遍历一层列表、累计总和等任务，循环通常更直接。
* 输入可能很大，而递归会产生很深的调用栈时，优先考虑循环。
* 阶乘本身用循环就很好写；这里用它练习递归调用和返回过程。
<!--v-->

## 什么时候考虑递归？

* 当前问题能化成规模更小的同类问题。
* 规模不断缩小后，能到达可以直接求解的情况。
* 已知小问题的答案，就能算出当前问题的答案。

对阶乘而言，这三项分别是 `(n - 1)!`、`0! / 1!` 和乘以 `n`。

<!--v-->

## 练习：手推阶乘调用

1. `factorial_recursive(0)` 和 `factorial_recursive(1)` 返回什么？
2. `factorial_recursive(3)` 调用更小的问题后，当前这一层还要做什么？
3. 如果写成只调用 `factorial_recursive(n - 1)` 而不返回计算结果，会怎样？

先手推，再运行；区分“调用了函数”和“把结果返回给上一层”。

<!--v-->

## 写递归前，先确定什么？

| 要确定的内容 | 阶乘中的对应写法 |
| --- | --- |
| 终止条件 | `n == 0 or n == 1`，返回 `1` |
| 如何缩小问题 | 把 `n` 减为 `n - 1` |
| 递归调用返回什么 | `(n - 1)!` |
| 当前层怎样返回 | `return n * factorial_recursive(n - 1)` |

<!--s-->

# 本节小结

<!--v-->

## 四个容易出错的地方

- 只复制外层列表，内部列表仍可能共享；HW2 快照要保留独立的任务记录。
- `except` 处理匹配的异常，`else` 处理成功路径，`finally` 做清理，不会自动消除异常。
- 字典按键查找；键不存在时，要先建立对应的值或处理 `KeyError`。
- 递归既要能停止，也要把结果返回；只调用函数不等于返回结果。

<!--s-->

# 答疑
