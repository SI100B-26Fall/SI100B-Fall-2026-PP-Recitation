---
title: SI100B_Fall_2026_Recitation_5_A
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
autoTitlePage: true
makeTitle:
  lecture: SI100B Fall 2026 Recitation 5 (A)
  title: Lec09–10 回顾 · 测试、字典与递归
  detail: SI100B 2026 Staff
makeThanks: true
---

# Today's Roadmap

<!--v-->

## 这节课要做什么？

- 用列表推导式整理数据，用返回的函数保存一组计算规则。
- 用测试发现错误，用调试定位错误，用异常和断言说明错误。
- 用字典按名字查数据，完成一次词频统计。
- 从循环走向递归，分清「继续调用」和「返回结果」。

配套 `Recitation5_A.ipynb` 按相同顺序提供场景、演示、练习和参考答案。
建议先预测输出，再运行单元格。

<!--v-->

## 对照老师的课件

<div class="three-line">

| 本讲内容 | 正课位置（PDF 页码） | Notebook 小节 |
|:---|:---|:---|
| 列表推导式、返回函数 | Lec09，第 2–23 页 | 1–2 |
| 测试与调试 | Lec09，第 24–38 页 | 3 |
| 异常、断言、成绩汇总 | Lec09，第 39–60 页；Lec10，第 3–10 页 | 4 |
| 字典、嵌套结构 | Lec09，第 61–87 页；Lec10，第 11–37 页 | 5 |
| 词频统计与分组 | Lec10，第 38–51 页 | 6 |
| 递归乘法、幂与阶乘 | Lec10，第 52–88 页 | 7 |

</div>

两份课件重复的内容合并讲解，例子从单个操作逐步走向综合应用。

<!--s-->

# List Comprehension

<!--v-->

## 场景：挑出及格成绩，再计算加分结果

假设原始成绩为 `[48, 60, 75, 92]`，只保留及格成绩，并各加 5 分。

```python
scores = [48, 60, 75, 92]
adjusted = []
for score in scores:
    if score >= 60:
        adjusted.append(score + 5)

print(adjusted)  # [65, 80, 97]
```

这段循环只做三件事：**遍历、筛选、计算新元素**。

<!--v-->

## 列表推导式怎么读？

```python
[expression for elem in iterable if condition]
```

```python
scores = [48, 60, 75, 92]
adjusted = [score + 5 for score in scores if score >= 60]
print(adjusted)  # [65, 80, 97]
print(scores)  # [48, 60, 75, 92]
```

- 先看 `for`，确定遍历谁。
- 再看 `if`，确定保留谁；不需要筛选时可省略。
- 最后看最左边的表达式，确定放进新列表的值。

**推导式创建新列表**；这里没有修改原成绩列表。

<!--v-->

## You Try It：什么时候执行 len？

```python
data = ["xy", "abcd", 7, "4.0"]
result = [len(x) for x in data if type(x) == str]
```

1. `7` 会被保留吗？会执行 `len(7)` 吗？
2. `'4.0'` 是字符串还是浮点数？
3. 最终结果是什么？

先自己追踪；答案见下一页。

<!--v-->

## 筛选在前，计算在后

<div class="three-line">

| 当前元素 | `type(x) == str` | 放入结果 |
|:---|:---:|:---|
| `'xy'` | `True` | `2` |
| `'abcd'` | `True` | `4` |
| `7` | `False` | 跳过，不执行 `len(7)` |
| `'4.0'` | `True` | `3` |

</div>

结果为 `[2, 4, 3]`。有引号的 `'4.0'` 仍然是字符串。

<!--s-->

# Functions Returning Functions

<!--v-->

## 场景：为不同打印机生成计价函数

黑白打印每页 2 元，彩色打印每页 5 元。计价过程相同，单价不同。

```python
def make_cost(unit_price):
    def cost(pages):
        return unit_price * pages

    return cost


black_white = make_cost(2)
color = make_cost(5)
print(black_white(3))  # 6
print(color(3))  # 15
```

`make_cost` 返回一个**函数对象**；调用这个函数时才计算总价。

<!--v-->

## return cost 和 return cost(3) 有什么不同？

<div class="three-line">

| 写法 | 执行的事情 | 返回值 |
|:---|:---|:---|
| `return cost` | 把函数交给调用者 | 函数对象 |
| `return cost(3)` | 立即调用函数 | 3 页的费用 |

</div>

```python
printer = make_cost(2)
print(callable(printer))  # True
print(printer(3))  # 6
print(make_cost(2)(3))  # 6，同样分成两次调用
```

没有括号是在使用函数对象；加上括号是在调用函数。

<!--v-->

## unit_price 从哪里来？

- `pages` 来自本次 `cost(...)` 调用的局部作用域。
- `unit_price` 来自定义 `cost` 时外层 `make_cost(...)` 的作用域。
- 返回的内部函数保留了对所需外层绑定的访问，这称为 **closure（闭包）**。

```python
cheap = make_cost(2)
expensive = make_cost(5)
print(cheap(4), expensive(4))  # 8 20
```

两次 `make_cost` 调用建立不同的外层绑定。闭包不意味着复制外层的所有数据。

<!--s-->

# Testing and Debugging

<!--v-->

## 先写清楚什么叫「正确」

场景：给非空成绩列表计算平均分。

```python
def average(grades):
    """grades 是非空数值列表；返回算术平均值。"""
    assert len(grades) > 0, "no grades data"
    return sum(grades) / len(grades)
```

- 输入约定是什么？是否允许空列表？
- 输出是什么？是否应修改输入？
- 测试前，先为具体输入写出期望结果。

**测试**检查结果是否符合约定，**调试**寻找不符合约定的原因。

<!--v-->

## 三类测试分别检查什么？

<div class="three-line">

| 类型 | 场景中的例子 |
|:---|:---|
| Unit testing，单元测试 | 单独检查 `average([60, 80]) == 70` |
| Integration testing，集成测试 | 学生记录经过汇总函数，得到姓名、成绩、平均分 |
| Regression testing，回归测试 | 修好「漏算最后一项」后，保留触发它的用例 |

</div>

同一个用例可以既是单元测试，又是防止旧问题复发的回归测试。
测试通过说明这些用例符合约定，**不能证明所有输入都正确**。

<!--v-->

## 黑盒测试：从约定挑输入

不看实现，先按问题的自然边界选用例。

<div class="three-line">

| `average` 的输入 | 期望 | 想检查什么 |
|:---|:---|:---|
| `[80]` | `80.0` | 只有一项 |
| `[0, 100]` | `50.0` | 分数的两端 |
| `[60, 80, 100]` | `80.0` | 多项累加与除数 |
| `[]` | `AssertionError` | 是否守住非空约定 |

</div>

对循环，还应考虑执行 **0 次、1 次、多次** 的情况。

<!--v-->

## 白盒测试：两个分支都走过就够了吗？

下面的函数想计算整数的绝对值。

```python
def absolute_buggy(x):
    if x < -1:
        return -x
    return x
```

- 用 `-2` 和 `2` 测试，两个分支都执行过，结果也正确。
- 但 `absolute_buggy(-1)` 返回 `-1`，违反约定。
- 修正为 `x < 0`，并把 `-1` 加入回归测试。

**分支覆盖与边界测试需要结合使用。**

<!--v-->

## 调试：把猜想变成能重复的实验

场景：平均分总是偏小。

```python
grades = [60, 100]
total = 0
for i in range(len(grades) - 1):
    total += grades[i]
    print("i =", i, "total =", total)
print(total / len(grades))  # 30.0，期望 80.0
```

只打印了 `i = 0`；`range` 的右端点不包含在内，最后一项漏算。

先用最小反例定位，再修正循环范围，最后重跑原用例与边界用例。

<!--s-->

# Exceptions and Assertions

<!--v-->

## 先读异常类型，再看发生的位置

<div class="three-line">

| 操作 | 异常 | 含义 |
|:---|:---|:---|
| `int('two')` | `ValueError` | 值无法按要求转换 |
| `10 / 0` | `ZeroDivisionError` | 除数为零 |
| `[80][1]` | `IndexError` | 列表下标越界 |
| `{'Ana': 80}['Bob']` | `KeyError` | 字典中没有这个键 |
| `'80' + 5` | `TypeError` | 操作不支持这些类型 |
| 使用未定义的变量 | `NameError` | 找不到这个名字 |

</div>

看 traceback 最后一行的异常类型和信息，再找到自己代码中出错的行。

<!--v-->

## 场景：把文本转换成每人费用

```python
total_text = "12"
people_text = "3"

try:
    total = int(total_text)
    people = int(people_text)
    print(total / people)
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("人数不能为 0")
```

把 `people_text` 分别改成 `'three'` 和 `'0'`，会进入不同处理分支。
**只捕获打算处理的异常**，避免无类型的 `except` 把其他错误一起遮住。

<!--v-->

## 异常之后，从哪里继续？

```python
try:
    print("A")
    value = int("oops")
    print("B")
except ValueError:
    print("C")
print("D")
```

输出依次为 `A`、`C`、`D`。

异常发生后，`try` 中剩余的 `print('B')` 被跳过；处理完成后继续执行整个结构后面的语句。

<!--v-->

## else 与 finally（了解）

```python
try:
    value = int("12")
except ValueError:
    print("转换失败")
else:
    print("转换成功", value)
finally:
    print("本次处理结束")
```

- `else` 在 `try` 正常完成、没有抛出异常时执行。
- 正常的 Python 控制流离开该结构时，`finally` 会执行，常用于清理。
- `else` 中抛出的异常不会由这里的 `except` 捕获。

<!--v-->

## raise 与 assert 各自表达什么？

```python
raise ValueError("人数必须大于 0")
```

`raise` 主动抛出异常，交给调用者处理；没有匹配的处理器时会向外传播。

```python
def average(grades):
    assert len(grades) > 0, "no grades data"
    return sum(grades) / len(grades)
```

`assert` 检查程序约定，失败时抛出 `AssertionError`，同样可以被调用者捕获。
本讲用它检查输入约定与测试结果；Python 的 `-O` 模式会移除断言。

<!--v-->

## 没有成绩，不等于平均分为零

老师的例子为每位学生增加一项平均分。遇到空成绩列表，必须先决定规则。

<div class="three-line">

| 处理策略 | 空列表的结果 | 需要说清楚什么 |
|:---|:---|:---|
| 打印提示后返回 `None` | 缺少平均分 | 后续不能直接拿它做数值运算 |
| 打印提示后返回 `0.0` | 按零分处理 | 这是业务规则，会影响统计 |
| 用断言中止当前计算 | 抛 `AssertionError` | 调用者违反了非空约定 |

</div>

Notebook 分别演示三种策略，再把正常成绩送入 `get_stats` 做集成检查。

<!--v-->

## You Try It：逐项相除

实现 `pairwise_div(numerators, denominators)`。

- 两个参数都是非空、等长的数值列表。
- 返回对应位置的商组成的新列表，不修改输入。
- 若分母中包含 `0`，按题目约定抛出 **`ValueError`**。

```text
[4, 5, 6], [1, 2, 3]  → [4.0, 2.5, 2.0]
[4, 5, 6], [1, 0, 3]  → ValueError
```

提示：捕获 `ZeroDivisionError` 后，用 `raise ValueError(...)` 转换为约定的异常。

<!--s-->

# Dictionaries

<!--v-->

## 场景：根据姓名查询成绩

平行列表需要先找位置，再用同一位置取另一个列表中的内容。

```python
names = ["Ana", "Bob", "Chen"]
scores = [80, 95, 72]
print(scores[names.index("Bob")])  # 95
```

字典直接表达「姓名 → 成绩」的对应关系。

```python
grades = {"Ana": 80, "Bob": 95, "Chen": 72}
print(grades["Bob"])  # 95
```

按位置找用列表；按键找用字典。空字典写成 `{}`。

<!--v-->

## 查、增、改、删

```python
grades = {"Ana": 80, "Bob": 95}
print(grades["Ana"])  # 80
grades["Chen"] = 72  # 新键，增加记录
grades["Ana"] = 88  # 已有键，更新记录
del grades["Bob"]  # 删除记录
print(grades)  # {'Ana': 88, 'Chen': 72}
```

直接查询不存在的键会抛出 `KeyError`。
同一个键只能对应当前的一个值；重复赋值会覆盖旧值。

<!--v-->

## in 检查键，items 同时给出键和值

```python
grades = {"Ana": 80, "Bob": 95}
print("Ana" in grades)  # True
print(80 in grades)  # False
print(80 in grades.values())  # True
print(list(grades.keys()))  # ['Ana', 'Bob']
print(list(grades.values()))  # [80, 95]

for name, score in grades.items():
    print(name, score)
```

`keys()`、`values()`、`items()` 返回可迭代的视图；需要列表时再用 `list(...)`。

<!--v-->

## 顺序与键的限制

- Python 3.7 起，字典保证**插入顺序**；这不等于按键排序。
- 要按姓名顺序输出，可以写 `for name in sorted(grades): ...`。
- 键必须 **hashable（可哈希）**。字符串、整数、只含可哈希元素的元组都可以。
- 列表和字典不能作为键；值可以是任意对象。

```python
seats = {("A", 1): "Ana", ("A", 2): "Bob"}
print(seats[("A", 2)])  # Bob
```

这里补充现代 Python 的顺序保证；老师课件的「不要假设排序」仍适用于按序输出的题目。

<!--v-->

## 为什么要可哈希？

字典用键的哈希值帮助定位记录，再通过相等比较识别键。

```text
键 → 计算哈希值 → 定位候选记录 → 比较键 → 取出值
```

- 键在使用期间，哈希值和相等关系需要保持一致。
- 可变列表不满足作为内建字典键的要求。
- 不同键可能具有相同哈希值，字典会处理这种冲突。

课件里的「字母编号相加再取余」是教学模型，不是 Python 的实际字符串哈希算法。

<!--v-->

## 字典也是可变对象

```python
original = {"Ana": [80, 90]}
alias = original
shallow = original.copy()

alias["Bob"] = [70]
shallow["Ana"].append(100)
print(original)  # {'Ana': [80, 90, 100], 'Bob': [70]}
print(shallow)  # {'Ana': [80, 90, 100]}
```

- `=` 创建别名，指向同一个字典。
- `copy()` 只复制外层，里面的列表仍然共享。
- 需要连嵌套内容一起独立复制时，用 `copy.deepcopy(...)`。

<!--v-->

## 嵌套字典：一次方括号走一层

```python
students = {
    "Ana": {"mq": [8, 10], "ps": [9]},
    "Bob": {"mq": [6], "ps": [7, 8]},
}
print(students["Ana"]["mq"][0])  # 8
```

汇总所有小测分数时，要把每份列表里的**元素**并进来。

```python
all_scores = []
for record in students.values():
    all_scores.extend(record["mq"])
print(all_scores)  # [8, 10, 6]
```

用 `append(record['mq'])` 会得到 `[[8, 10], [6]]`，结构不同。

<!--v-->

## 每条成绩的平均，与每位学生平均的平均

沿用上一页的数据。

- 所有成绩放在一起，平均为 $(8 + 10 + 6) / 3 = 8$。
- 先求每人的平均再求平均，为 $(9 + 6) / 2 = 7.5$。

两位学生的小测次数不同，两种平均的权重也不同。
老师的 `get_average(data, what)` 要求的是**所有对应成绩的平均**。

```python
def get_average(data, what):
    all_scores = []
    for record in data.values():
        all_scores.extend(record[what])
    assert len(all_scores) > 0, "no grades data"
    return sum(all_scores) / len(all_scores)
```

<!--s-->

# Word Frequency

<!--v-->

## 场景：统计社团报名中的兴趣标签

用一段自造文本模拟报名标签；约定单词只由空白分隔，不处理标点。

```python
text = "Python art python music ART python music"


def generate_word_dict(text):
    counts = {}
    for word in text.lower().split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
```

结果为 `{'python': 3, 'art': 2, 'music': 2}`。

<!--v-->

## 最热门标签可能不止一个

```python
def find_frequent_word(counts):
    assert len(counts) > 0, "empty frequency dictionary"
    highest = max(counts.values())
    words = []
    for word, frequency in counts.items():
        if frequency == highest:
            words.append(word)
    return words, highest
```

```python
print(find_frequent_word({"art": 2, "music": 2}))
# (['art', 'music'], 2)
```

返回 `(列表, 次数)`，用列表保留所有并列第一的标签。

<!--v-->

## 按频率分组，只保留次数大于 x 的词

```python
def occurs_often(counts, x):
    remaining = counts.copy()
    groups = []
    while remaining:
        words, highest = find_frequent_word(remaining)
        if highest <= x:
            break
        groups.append((words, highest))
        for word in words:
            del remaining[word]
    return groups
```

输入 `{'python': 3, 'art': 2, 'music': 2}` 与 `x = 1`，得到
`[(['python'], 3), (['art', 'music'], 2)]`。

<!--v-->

## 为什么要先检查 remaining？

- 若所有词都被删除，下次不能再执行 `max(remaining.values())`。
- `while remaining` 同时覆盖「输入本来为空」和「后来删空」。
- `highest <= x` 就停止，因此只收集**严格大于** `x` 的频率。
- 遍历的是独立的 `words` 列表，删除的是 `remaining` 中的键。
- 本讲先复制字典；频率值都是整数，浅拷贝已足够保留原数据。

相较正课的原地删除版本，这个版本明确保留输入，并补上删空时的终止条件。
Notebook 检查空文本、并列、阈值相等与全部删除的情况。

<!--s-->

# Recursion

<!--v-->

## 场景：每袋 5 颗糖，4 袋有多少颗？

循环的思路是反复累加，并保存当前总数。

```python
def mult_iter(a, b):
    assert type(b) == int and b >= 0
    result = 0
    for _ in range(b):
        result += a
    return result
```

递归的思路是「一袋的糖 + 剩下的糖」。

$$a \times b = a + a \times (b - 1)$$

还需要一个不再继续拆分、可以直接回答的情况。

<!--v-->

## 递归必须回答的三个问题

1. **Base case**：什么时候直接返回？`b == 0` 时返回 `0`。
2. **Recursive step**：怎么变成更小的同类问题？计算 `a × (b - 1)`。
3. **Progress**：为什么会到达 base case？非负整数 `b` 每次减 `1`。

```python
def mult_recur(a, b):
    assert type(b) == int and b >= 0
    if b == 0:
        return 0
    return a + mult_recur(a, b - 1)
```

正课用 `b == 1` 作为基例，要求 `b >= 1`；这里扩展为允许 `b == 0`。

<!--v-->

## 递归先向下调用，再向上返回

```text
mult_recur(5, 3)
  等待 5 + mult_recur(5, 2)
             等待 5 + mult_recur(5, 1)
                        等待 5 + mult_recur(5, 0)
                                   返回 0
                        返回 5 + 0 = 5
             返回 5 + 5 = 10
  返回 5 + 10 = 15
```

前面的调用还没有结束，它们在等下一层的结果。
**调用自己不够，还要把结果返回给上一层。**

<!--v-->

## You Try It：幂的递归

计算 $n^p$，约定 `p` 是非负整数，本练习将零次幂定义为 `1`。

$$n^0 = 1, \qquad n^p = n \times n^{p-1}\quad (p > 0)$$

```python
def power_recur(n, p):
    assert type(p) == int and p >= 0
    if ______:
        return ______
    return ______________________
```

先测试 `power_recur(2, 0)`，再测试 `power_recur(2, 3)`。
参考实现见 Notebook。

<!--v-->

## 场景：4 位同学排队，有多少种顺序？

第一个位置有 4 种选择，剩下 3 人的排列数是同一个问题。

$$n! = n \times (n-1)!, \qquad 0! = 1$$

```python
def factorial(n):
    assert type(n) == int and n >= 0
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

`factorial(4)` 为 `24`。正课以 `1!` 为基例；这里用 `0!` 覆盖空排列。

<!--v-->

## 每层调用有自己的局部变量

<div class="three-line">

| 本层调用 | 本层 `n` | 等待的结果 | 最后返回 |
|:---|:---:|:---|:---:|
| `factorial(3)` | 3 | `3 * factorial(2)` | 6 |
| `factorial(2)` | 2 | `2 * factorial(1)` | 2 |
| `factorial(1)` | 1 | `1 * factorial(0)` | 1 |
| `factorial(0)` | 0 | 直接返回 | 1 |

</div>

下一层的 `n` 不会覆盖上一层的 `n`。
局部名字各自独立，但若传入同一个可变对象，仍可能共享它。

<!--v-->

## 三种常见的递归错误

<div class="three-line">

| 错误 | 后果 | 检查办法 |
|:---|:---|:---|
| 没有基例 | 一直调用，最终可能 `RecursionError` | 从最小合法输入开始 |
| 参数不变或朝反方向变化 | 永远到不了基例 | 写出每次参数的变化 |
| 漏写 `return` | 调用完成却返回 `None` | 沿返回过程逐层追踪 |

</div>

Python 递归还受调用深度限制；本讲用小输入理解过程。
循环和递归都可以解决这些题目，递归不保证更快。

<!--s-->

# Exercises

<!--v-->

## 练习 1–3 · 数据与函数

1. **标签长度**：只保留字符串，用列表推导式返回长度至少为 3 的字符串的长度。
   输入 `['AI', 'Python', 7, 'art', '']`，结果为 `[6, 3]`。
2. **生成加分函数**：实现 `make_bonus(points)`，返回把成绩加上 `points` 的函数。
   `make_bonus(5)(80)` 应为 `85`。
3. **按名单查成绩**：实现 `find_grades(grades, students)`，按名单顺序返回成绩。
   假设姓名都存在；`students` 可以为空，也可以重复。

Notebook 为每题留了动手单元格，后面另列期望结果与参考实现。

<!--v-->

## 练习 4–6 · 测试、异常与字典

4. **补上测试**：为 `absolute_buggy` 找一个能暴露错误的输入，修正后保留该用例。
5. **逐项相除**：实现前面的 `pairwise_div`，检查正常结果和零分母对应的异常类型。
6. **查找与计数**：实现 `find_in_L(Ld, k)` 与 `count_matches(d)`。
   前者检查 `k` 是否为某个字典的键；后者统计「键等于值」的条目数。

注意区分 `25 in {5: 25}` 与 `25 in {5: 25}.values()`。

<!--v-->

## 练习 7–9 · 汇总与递归

7. **小测汇总**：为嵌套成绩字典计算所有 `'mq'` 分数的平均，解释为什么不能直接 `append` 整份列表。
8. **热门标签**：串联词频统计和 `occurs_often`，返回次数严格大于阈值的分组，保留原字典。
9. **递归三题**：补全 `power_recur`，写出 `factorial`，再递归计算 `1 + ... + n`，其中 `n >= 0`。

每个递归函数先写下基例、递推式、参数如何靠近基例，再写代码。

<!--s-->

# Q & A

<!--v-->

## 离开教室前，试着回答

- 推导式里的筛选与表达式，哪个先对当前元素执行？
- 返回函数对象与返回调用结果，有什么区别？
- 两个分支都测过，为什么仍可能遗漏错误？
- 异常处理完成后，程序从哪里继续？
- `in` 查字典的键还是值？浅拷贝会复制里面的列表吗？
- 递归的这一层在等谁？为什么一定能停止？

把解释写在 Notebook 的练习单元格中，再用代码验证自己的预测。
