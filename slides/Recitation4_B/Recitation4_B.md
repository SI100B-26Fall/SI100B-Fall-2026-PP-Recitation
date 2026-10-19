---
title: SI100B_Fall_2026_Recitation_4_B
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css: assets/custom.css
autoTitlePage: true
makeTitle:
    lecture: SI100B Fall 2026 Recitation 4 (B)
    title: Lecture 7–9 正课知识体系复习
    detail: SI100B 2026 Staff | 2026-10-16
makeThanks: true
---

<style>
  .reveal h1 code,
  .reveal h2 code,
  .reveal h3 code,
  .reveal h4 code {
    font-size: 0.78em;
    padding: 0 4px;
  }
</style>

<div class="middle center"><div style="width: 100%">

# How to Use These Slides

</div></div>

<!--v-->

## 这节课要做什么

Lecture 7 – 9 讲的是同一件事的两面：数据放进容器之后会怎样，以及程序出错时该怎么办。

- 列表（lists）：一个能装很多元素、而且允许改动的容器
- 别名与克隆（aliasing / cloning）：改一个名字指向的内容，为什么会连带改到另一个
- 列表推导式（list comprehension）：把"逐个处理再收集"压缩成一行
- 测试与调试（testing / debugging）：怎么知道程序错了，以及错在哪
- 异常与断言（exceptions / assertions）：出错时程序该怎么反应
- 字典（dictionaries）：用"名字"而不是"序号"去取数据

<!--v-->

## 学习路线图

<div class="three-line">

| 这一块要解决的问题 | 关键工具 | 对应章节 |
|:---|:---|:---|
| 一堆数据怎么存、怎么改 | 列表的索引、方法与可变性 | Lecture 7 |
| 改了一个变量，另一个也跟着变 | 别名、克隆、浅拷贝与深拷贝 | Lecture 8 |
| 逐个处理写起来太啰嗦 | 列表推导式 | Lecture 8 |
| 程序错了，但不知道错在哪 | 测试分类、调试策略 | Lecture 8 |
| 遇到意外输入时该怎么办 | `try` / `except` / `raise` / `assert` | Lecture 8 – 9 |
| 按名字取数据，而不是按位置 | 字典与哈希键 | Lecture 9 |

</div>

前两块是"数据怎么变"，中间两块是"怎么保证它变对了"，最后一块换一种存数据的方式。

<!--s-->

<div class="middle center"><div style="width: 100%">

# Lists

</div></div>

<!--v-->

## 列表是什么

列表（list）是一个有序的序列，用方括号写出来，里面的元素按位置排好。

```python
empty_list = []
short_list = [2]
hello_list = [2, "a", 4, [1, 2]]
```

- 有序：每个元素都有一个整数下标，从 0 开始数
- 可以混合类型：`hello_list` 里同时有整数、字符串，甚至另一个列表
- 允许重复：同一个值出现多次没有问题

上面三行粘进交互环境就能逐条试下标：`hello_list[0]` 是 `2`，`hello_list[3]` 是 `[1, 2]`。

<!--v-->

## 下标、切片与常用操作

```python
hello_list = [2, "a", 4, [1, 2]]
hello_list[0]     # 2
hello_list[1:3]   # ["a", 4]
hello_list[4]     # IndexError: list index out of range
len(hello_list)   # 4
[1, 2] + [3, 4]   # [1, 2, 3, 4]
[1, 2] * 2        # [1, 2, 1, 2]
max([3, 5, 0])    # 5
```

- `hello_list[4]` 越界：合法下标只能取 `0` 到 `len(L) - 1`
- `hello_list[1:3]` 是切片：取下标 1、2 两个元素，不含 3
- `+` 把两个列表拼成一个新列表，`*` 把列表重复若干遍

<!--v-->

## 列表可以被改动

这是列表和字符串最重要的差别：列表可变（mutable），能直接改某个位置上的值。

```python
L = [2, 4, 3]
L[1] = 5
print(L)      # [2, 5, 3]
```

`L[1] = 5` 并没有新建列表，它改的就是 `L` 自己 —— `L` 还是原来那个对象，只是内容变了。

字符串做不到这件事：`s = "abc"` 之后写 `s[0] = "x"` 会直接报错，因为字符串不可变。

<!--v-->

## 那个点号是什么意思

写 `L.append(5)` 时，`L` 后面的 `.append` 到底是什么？

- 列表是 Python 对象，对象身上挂着一组属于它的操作
- `L.append(...)` 的意思是"让 `L` 这个对象执行 `append` 这个操作"
- 它相当于 `append(L, 5)`，只是把 `L` 挪到了点号前面

所以点号左边是"谁来做"，右边是"做什么"。

```python
L = [2, 1, 3]
L.append(5)
print(L)          # [2, 1, 3, 5]
```

<!--v-->

## append 返回的是 None

`append` 把元素加到了列表末尾，但它的返回值是 `None`，**而不是列表本身**。这是最容易出错的地方：

```python
L = [2, 1, 3]
L.append(5)
print(L)          # [2, 1, 3, 5]   ← 列表变了
L = L.append(5)   # 把返回值赋给了 L
print(L)          # None          ← 列表没了
```

第二行里 `L.append(5)` 先执行（列表确实变成了 `[2, 1, 3, 5]`），然后它返回的 `None` 被赋给了 `L`，变量 `L` 就从"指向列表"变成了"指向 `None`"。

所以：**靠副作用改数据的操作，不要用赋值去接它的返回值。**

<!--v-->

## 一个可以自己推一遍的例子

```python
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.append(L4)
L = L1.append(L3)
```

- `L4 = L1 + L2`：`+` 生成新列表，`L4` 是 `['re', 'mi']`
- `L3.append(L4)`：`L3` 变成 `['do', ['re', 'mi']]`（整个 `L4` 作为一个元素塞进去）
- `L = L1.append(L3)`：`L1` 变成 `['re', ['do', ['re', 'mi']]]`，而 `L` 拿到的是 `None`

注意 `L1` 也被改了 —— 因为 `append` 改的就是 `L1` 本身，它并不需要 `L` 去接收。

<!--v-->

## 字符串和列表互相转换

两者经常需要来回换，Python 给了三个工具：

```python
s = "I<3 cs &u?"
list(s)          # ['I','<','3',' ','c','s',' ','&','u','?']
s.split(' ')     # ['I<3', 'cs', '&u?']
s.split('<')     # ['I', '3 cs &u?']

L = ['a', 'b', 'c']
''.join(L)       # 'abc'
'_'.join(L)      # 'a_b_c'
```

- `list(s)` 把字符串按字符拆开，每个字符是一个元素
- `s.split(分隔符)` 按分隔符切开；不传参数时按空白切
- `分隔符.join(L)` 反过来，把列表里的字符串拼成一个

`join` 只接受字符串元素：`''.join([1, 2, 3])` 会抛 `TypeError`，得先把它们变成字符串。

<!--v-->

## 排序：sorted 和 sort

```python
L = [9, 6, 0, 3]
a = sorted(L)     # a 是 [0, 3, 6, 9]，L 不变
b = L.sort()      # L 变成 [0, 3, 6, 9]，b 是 None
L.reverse()       # L 变成 [9, 6, 3, 0]，返回 None
```

<div class="three-line">

| 写法 | 改原列表吗 | 返回值 |
|:---|:---|:---|
| `sorted(L)` | 不改 | 排好序的新列表 |
| `L.sort()` | 改 | `None` |
| `L.reverse()` | 改 | `None` |

</div>

`sorted` 是函数，`sort` 和 `reverse` 是列表自己的方法。名字只差一个 `d`，行为却完全相反。

<!--v-->

## 要改每个元素，得迭代下标

想给列表里每个元素平方，第一反应可能是这样：

```python
def square_list(L):
    for elem in L:
        elem = elem ** 2     # 没用！
```

`elem` 只是从列表里取出来的一个值，改它不会影响列表本身。要让改动落回列表，必须拿到下标：

```python
def square_list(L):
    for i in range(len(L)):
        L[i] = L[i] ** 2
```

`range(len(L))` 生成 `0, 1, ..., len(L)-1`，正好是全部合法下标；`for i, e in enumerate(L)` 也能同时拿到下标和元素。这个函数没有 `return`，因为它的目的就是改输入 —— 实测 `Lin = [2, 3, 4]` 调用后变成 `[4, 9, 16]`。

<!--v-->

## 边迭代边改列表：写法一

同一个列表，改法不同，行为可能完全不同。

```python
L = [1, 2, 3, 4]
for i in range(len(L)):
    L.append(i)
```

`range(len(L))` 在循环开始的那一刻就算好了，是 `0, 1, 2, 3`。之后往 `L` 里追加多少元素，都不会让这个范围变长。

结果：`[1, 2, 3, 4, 0, 1, 2, 3]`，长度 8，循环正常结束。

<!--v-->

## 写法二：循环停不下来

```python
L = [1, 2, 3, 4]
i = 0
for e in L:
    L.append(i)
    i += 1
```

这次循环直接盯着 `L` 本身。每转一圈就往 `L` 末尾加一个元素，而循环还没取完，于是永远有下一个元素 —— 循环不会结束。

两种写法的差别在于：**循环范围的边界，是开头就定好的，还是边走边看的。**

<!--v-->

## 写法三：长度翻倍

```python
L = [1, 2, 3, 4]
for e in L:
    L = L + L
```

`L = L + L` 用 `+` 生成一个新列表，再让 `L` 指向它。循环本身仍然在迭代**最初那个** 4 元素的列表，所以循环体只执行 4 次。

但每执行一次长度就翻一倍：`4 → 8 → 16 → 32 → 64`。循环结束时 `L` 有 64 个元素。

如果换成 `L.extend(L)`（原地追加），列表会边循环边翻倍，循环永远取不到末尾，长度一路涨到内存装不下为止。

<!--v-->

## 三种写法对照

<div class="three-line">

| 写法 | 循环看的是什么 | 结果 |
|:---|:---|:---|
| `for i in range(len(L))` + `append` | 开头定好的数字范围 | 正常结束，长度 8 |
| `for e in L` + `append` | 边走边变的 `L` | 永不停止 |
| `for e in L` + `L = L + L` | 最初那个 4 元素列表 | 执行 4 次，长度 64 |

</div>

共同点是：**循环的边界一旦和"正在被改的列表"绑在一起，行为就变得难以预测。** 安全的做法是让循环只读、改动留到循环外，或者迭代一个副本。

<!--v-->

## 合并两个列表：`+` 和 `extend`

```python
L1 = [2, 1, 3]
L2 = [4, 5, 6]
L3 = L1 + L2        # L3 是 [2, 1, 3, 4, 5, 6]，L1 不变
L1.extend([0, 6])   # L1 变成 [2, 1, 3, 0, 6]
```

- `+` 生成一个新列表，两个原列表都不动
- `extend` 是原地追加，把参数里的元素逐个接到 `L1` 末尾

`extend` 不会把参数当成一个整体塞进去：`L2.extend([[1,2], [3,4]])` 之后 `L2` 是 `[4, 5, 6, [1,2], [3,4]]`，两个子列表是作为两个元素加进去的。

<!--v-->

## 清空列表：还是同一个对象吗

`L.clear()` 会把元素全删掉，但它**没有新建列表**。想验证这一点，用 `id()` 看内存地址：

```python
L = [4, 5, 6]
id(L)          # 比如 140234...
L.append(8)
id(L)          # 和上面相同：还是同一个对象
L.clear()
id(L)          # 仍然相同：对象没换，只是空了
```

对比 `L = []`：这是让 `L` 指向一个**新的**空列表，`id` 会变。

这个区别在别处还有名字指向它的时候很关键 —— `L.clear()` 会让那个名字也看到空列表，`L = []` 不会。

<!--v-->

## 删除元素：三种方式

```python
L = [2, 1, 3, 6, 3, 7, 0]
L.remove(2)     # 按值删，L 变成 [1, 3, 6, 3, 7, 0]
L.remove(3)     # 只删第一个 3，L 变成 [1, 6, 3, 7, 0]
del L[1]        # 按下标删，L 变成 [1, 3, 7, 0]
x = L.pop()     # 删末尾并返回它，x 是 0，L 变成 [1, 3, 7]
```

<div class="three-line">

| 写法 | 按什么删 | 返回值 |
|:---|:---|:---|
| `L.remove(e)` | 值（只删第一个） | `None` |
| `del L[i]` | 下标 | 无 |
| `L.pop()` | 末尾（也可给下标） | 被删掉的那个元素 |

</div>

`remove` 找的是**第一个**匹配的元素；值不在列表里时，它会直接报错。

<!--s-->

<div class="middle center"><div style="width: 100%">

# Aliasing and Cloning

</div></div>

<!--v-->

## 边迭代边删除：结果为什么是错的

需求很简单：把列表里所有等于 `e` 的元素删掉。两种写法看起来差不多，结果却不同。

```python
# 写法一：可以
def remove_all(L, e):
    while e in L:
        L.remove(e)

# 写法二：错的
def remove_all(L, e):
    for elem in L:
        if elem == e:
            L.remove(e)
```

拿 `L = [1, 2, 2, 2]`、`e = 2` 试：写法一得到 `[1]`，写法二得到 `[1, 2]` —— 漏删了一个。

<!--v-->

## 漏删是怎么发生的

`for elem in L` 在背后维护着一个位置计数：第一次取下标 0，第二次取下标 1，第三次取下标 2……

但删除元素会让后面的元素整体前移，而计数器**不会**跟着回退：

<div class="three-line">

| 轮次 | 取到的下标 | 取到的值 | 当时 L | 动作 | 删完后 L |
|:---:|:---:|:---:|:---|:---|:---|
| 1 | 0 | 1 | `[1,2,2,2]` | 不是 2，跳过 | `[1,2,2,2]` |
| 2 | 1 | 2 | `[1,2,2,2]` | 是 2，删掉 | `[1,2,2]` |
| 3 | 2 | 2 | `[1,2,2]` | 是 2，删掉 | `[1,2]` |
| 4 | 3 | —— | `[1,2]` | 下标越界，循环结束 | `[1,2]` |

</div>

第 2 轮删掉下标 1 之后，原来在下标 2 的那个 `2` 前移到了下标 1，而计数器下一步读的是下标 2 —— 前移过来的这个 `2` 被跳过了。最后结果是 `[1, 2]`，比 `while` 版多留了一个。

<!--v-->

## 同一个错误：remove_dups

下面这个函数想从 `L1` 里删掉所有也出现在 `L2` 中的元素：

```python
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
```

期望 `L1` 变成 `[30, 40]`，实际得到 `[20, 30, 40]` —— `20` 被漏掉了。

原因和上一页一模一样：删掉 `10` 之后，`20` 前移到下标 0，而计数器已经走到下标 1，正好跳过它。

<!--v-->

## 修法：迭代副本

```python
def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
```

`L1[:]` 是切片，它**新建**一个列表，把 `L1` 的元素逐个复制进去。这样循环遍历的是那个副本，长度和下标不会因为删除而改变；删除仍然作用在 `L1` 上，删到最后一个也不会有元素被跳过。

结果正确：`L1` 变成 `[30, 40]`。

<!--v-->

## 为什么 `L1_copy = L1` 不行

只差一对中括号，效果完全不同：

```python
L1_copy = L1        # 别名：两个名字，一个列表
L1_copy = L1[:]     # 克隆：两个名字，两个列表
```

`=` 在可变对象上**不会复制内容**，它只是让新名字也指向同一个对象。于是 `for e in L1_copy` 和 `for e in L1` 完全是同一件事，漏删照旧。

判断标准很简单：用 `L1_copy is L1` 检查。`=` 得到 `True`，`[:]` 得到 `False`。

<!--v-->

## 画出来看：别名和克隆

两种写法在内存里的样子完全不同：

<svg viewBox="0 0 920 215" width="94%" style="display:block;margin:6px auto;">
  <text x="240" y="24" text-anchor="middle" font-size="18" font-weight="bold" fill="#003fa3">L1_copy = L1（别名）</text>
  <text x="690" y="24" text-anchor="middle" font-size="18" font-weight="bold" fill="#2e7d32">L1_copy = L1[:]（克隆）</text>
  <g font-size="17" fill="#333">
    <text x="60" y="90">L1</text>
    <text x="60" y="150">L1_copy</text>
  </g>
  <polyline points="130,84 160,84 160,144 130,144" fill="none" stroke="#003fa3" stroke-width="1.5"/>
  <line x1="160" y1="114" x2="248" y2="114" stroke="#003fa3" stroke-width="1.5"/>
  <rect x="250" y="84" width="200" height="60" rx="6" fill="#e3f2fd" stroke="#003fa3" stroke-width="1.5"/>
  <text x="350" y="120" text-anchor="middle" font-size="16" fill="#003fa3">[10, 20, 30, 40]</text>
  <text x="240" y="192" text-anchor="middle" font-size="15" fill="#c62828">只有一个列表对象，改一处两处都变</text>
  <g font-size="17" fill="#333">
    <text x="510" y="82">L1</text>
    <text x="510" y="162">L1_copy</text>
  </g>
  <line x1="600" y1="76" x2="690" y2="76" stroke="#2e7d32" stroke-width="1.5"/>
  <rect x="692" y="52" width="200" height="48" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="792" y="82" text-anchor="middle" font-size="16" fill="#2e7d32">[10, 20, 30, 40]</text>
  <line x1="600" y1="156" x2="690" y2="156" stroke="#2e7d32" stroke-width="1.5"/>
  <rect x="692" y="132" width="200" height="48" rx="6" fill="#e8f5e9" stroke="#2e7d32" stroke-width="1.5"/>
  <text x="792" y="162" text-anchor="middle" font-size="16" fill="#2e7d32">[10, 20, 30, 40]</text>
  <text x="690" y="192" text-anchor="middle" font-size="15" fill="#2e7d32">两个独立的列表对象，互不影响</text>
</svg>

<!--v-->

## 把列表传进函数，就是建立别名

函数调用时的参数传递，对可变对象来说同样是别名。

```python
def remove_dups(L1, L2):
    L1_copy = L1        # L1_copy 和 L1 指向同一个列表
    for e in L1_copy:
        if e in L2:
            L1.remove(e)   # 这个改动会传回调用处
```

调用 `remove_dups(La, Lb)` 时，形参 `L1` 和实参 `La` 是同一个对象的两个名字。函数里删元素，函数外的 `La` 跟着变。

好处是函数能"原地修改"传进来的列表；代价是必须清楚哪些改动会漏到外面。

<!--v-->

## 浅拷贝：只复制顶层

如果列表里装的还是列表（嵌套），`L[:]` 就不够用了。`copy` 模块给了两个工具：

```python
import copy
L = [1, 2, 3, 4]
Lcopy = copy.copy(L)   # 等价于 Lcopy = L[:]
```

`copy.copy` 是**浅拷贝**：只把最外层复制一份，里面每个元素仍然是"原来那个"。元素本身是不可变类型（整数、字符串）时够用；元素是列表时，两个外层列表会共用同一批内层列表。

<!--v-->

## 浅拷贝留下的问题

```python
import copy
old_list = [[1, 2], [3, 4], [5, 6]]
new_list = copy.copy(old_list)
old_list.append([7, 8])     # 只动顶层
old_list[1][1] = 9          # 动的是内层！
```

实测结果：

- `old_list` 是 `[[1,2], [3,9], [5,6], [7,8]]`
- `new_list` 是 `[[1,2], [3,9], [5,6]]`

顶层追加的 `[7,8]` 没有影响 `new_list`（顶层确实分开了），但 `old_list[1][1] = 9` **同时改了 `new_list`** —— 因为 `new_list[1]` 和 `old_list[1]` 是同一个内层列表。

<!--v-->

## 深拷贝：每一层都复制

想让嵌套结构彻底独立，用 `copy.deepcopy`：

```python
import copy
old_list = [[1, 2], [3, 4], [5, 6]]
new_list = copy.deepcopy(old_list)
old_list.append([7, 8])
old_list[1][1] = 9
```

实测结果：`old_list` 是 `[[1,2], [3,9], [5,6], [7,8]]`，而 `new_list` 仍然是 `[[1,2], [3,4], [5,6]]`。

两个改动都没有波及 `new_list`。代价是深拷贝要把整棵结构递归复制一遍，比浅拷贝慢。

<!--v-->

## 四种"复制"对照

<div class="three-line">

| 写法 | 新建对象吗 | 内层元素是否独立 |
|:---|:---|:---|
| `new = old` | 否（别名） | 完全共享 |
| `new = old[:]` | 是（浅拷贝） | 共享 |
| `new = copy.copy(old)` | 是（浅拷贝） | 共享 |
| `new = copy.deepcopy(old)` | 是（深拷贝） | 独立 |

</div>

怎么选，只看列表里装的是什么：**是不可变的值，还是又一层可变结构？** 前者浅拷贝足够，后者才需要深拷贝。

<!--v-->

## 小结：列表在内存里是什么

- 列表本身是一个对象，变量名只是指向它的一张标签
- 多个名字可以指向同一个对象，这就是别名
- 通过任何一个名字做的修改，其他名字都会看到
- 想要互不影响，必须显式复制：浅拷贝复制顶层，深拷贝复制每一层

这也解释了为什么可变类型比不可变类型更容易出问题：不可变对象根本改不了，自然不会连累别人。

<!--s-->

<div class="middle center"><div style="width: 100%">

# List Comprehension

</div></div>

<!--v-->

## 从四行循环到一行

"对序列里每个元素做同样的处理，收集成新列表"是极常见的需求：

```python
def f(L):
    Lnew = []
    for e in L:
        Lnew.append(e ** 2)
    return Lnew
```

Python 为这个模式准备了一行写法，叫列表推导式（list comprehension）：

```python
Lnew = [e ** 2 for e in L]
```

两段代码做的事完全一样：新建一个列表，把 `L` 里每个元素的平方放进去。

<!--v-->

## 加上筛选条件

只想处理满足条件的元素，就在末尾补一个 `if`：

```python
def f(L):
    Lnew = []
    for e in L:
        if e % 2 == 0:
            Lnew.append(e ** 2)
    return Lnew
```

```python
Lnew = [e ** 2 for e in L if e % 2 == 0]
```

以 `L = [1, 2, 3, 4, 5]` 为例：不带条件得到 `[1, 4, 9, 16, 25]`，带条件只留下偶数的平方 `[4, 16]`。

<!--v-->

## 拆开看一个式子

```python
[len(x) for x in ['xy', 'abcd', 7, '4.0'] if type(x) == str]
```

按三步读它：

1. 遍历的序列是 `['xy', 'abcd', 7, '4.0']`，一共四个值
2. `if type(x) == str` 把 `7` 过滤掉，剩下 `'xy'`、`'abcd'`、`'4.0'`
3. 对这三个值各求一次 `len(x)`，得到 `2`、`4`、`3`

结果是 `[2, 4, 3]`。

写在一行不等于更好读：条件一多、表达式一长，写成循环反而更清楚。

<!--s-->

<div class="middle center"><div style="width: 100%">

# Testing and Debugging

</div></div>

<!--v-->

## 写代码、测试、调试

写完代码只是第一步：

1. 写代码（coding）
2. 测试与验证（testing / validation）：它真的按预期跑吗
3. 调试（debugging）：没按预期跑，问题在哪

第 2、3 步花的时间往往比第 1 步多，能不能做得顺利，很大程度上取决于第 1 步把代码拆得够不够清楚。

<!--v-->

## 为测试做准备

如果代码是一整块，出错时只能整块排查。更好的做法是从一开始就：

- 把程序拆成可以单独测试的模块
- 说明每个模块做什么
- 说明模块的约束：输入应该是什么、输出应该是什么
- 记录代码设计背后的假设

这些写下来，测试时就有了明确的"应该是什么样"，调试时也更容易判断是哪一块出了问题。

<!--v-->

## 什么时候可以开始测

先确保程序能跑起来：

- 没有语法错误（syntax error）
- 没有静态语义错误（static semantic error）

这两类错误 Python 解释器通常能直接指出来。然后还需要准备一组**测试用例**：每个输入配一个预期输出，其中要包含边界情况 —— 空列表、只有一个元素的列表、很大的数、很小的数。这些地方最容易出问题。

<!--v-->

## 三类测试

<div class="three-line">

| 类型 | 做什么 | 目的 |
|:---|:---|:---|
| 单元测试 | 单独测每个函数 | 确认每一块都对 |
| 回归测试 | 改动之后重跑旧测试 | 确认没有改坏已经对的东西 |
| 集成测试 | 让整个程序一起跑 | 确认拼起来还能用 |

</div>

常见的问题是跳过前两类直接做集成测试：整体跑通了就以为没事，其实某个函数在边界输入下一直是错的。

<!--v-->

## 调试：二分定位

发现程序行为不对之后，要做的是：定位问题 → 修掉 → 重测，直到所有情况都对。

定位问题最有效的手段是**二分法**：

- 在代码中间插一个 `print`（或设一个断点），看走到这里时状态对不对
- 对，说明问题在后半段；不对，说明在前半段
- 每次都能把怀疑范围砍掉一半

这比从头一行行读代码快得多，也比随机改几行碰运气可靠得多。

<!--s-->

<div class="middle center"><div style="width: 100%">

# Exceptions and Assertions

</div></div>

<!--v-->

## 什么情况下会抛出异常

程序执行到"和预期不符"的状态时，Python 会抛出一个异常（exception）。常见的几种：

- 下标越界：`hello_list[4]` 而列表只有 4 个元素
- 类型不合适：把不能转成数字的字符串交给 `int()`
- 引用不存在的名字或键：`grades['Grace']` 而字典里没有 `Grace`
- 类型混用没有转换：`'3' + 4`

默认情况下，异常会让程序立刻停下，并打印出错误类型和信息。

<!--v-->

## 用 try / except 接住异常

不想让程序直接崩掉，可以把可能出问题的代码放进 `try`，把处理方案放进 `except`：

```python
try:
    # 可能出问题的代码
    val = int(char)
except:
    # 出问题之后怎么办
    print("can't convert", char)
```

规则很简单：

- `try` 里的语句全部顺利执行 → 跳过 `except`，继续往下走
- `try` 里任何一句抛出异常 → 立刻跳到 `except` 里执行

<!--v-->

## 一个例子：把字符串里的数字加起来

```python
def sum_digits(s):
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print("can't convert", char)
    return total
```

`s` 里混进非数字字符时，`int(char)` 会抛 `ValueError`。`except` 把这一轮接住、打印一条提示，循环继续处理下一个字符。

实测 `sum_digits('a1b2c3')` 打印三行 `can't convert a / b / c`，返回 `6`。

<!--v-->

## 分别处理不同的异常

一个 `except` 抓全部太粗糙。给不同类型的异常写各自的 `except`，才能针对性地处理：

```python
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a / b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went very wrong.")
```

`int('x')` 抛 `ValueError`，`1/0` 抛 `ZeroDivisionError`。按类型分开写，才能给出真正有用的提示；最后那个不带类型的 `except` 兜住剩下所有情况。

<!--v-->

## else 和 finally

`try` 还可以带两个可选块：

- `else`：`try` 全部顺利执行（没有异常）时才执行
- `finally`：无论有没有异常都执行

`finally` 适合放清理工作，比如关闭文件 —— 不管前面发生了什么，都要做。

```python
try:
    f = open('data.txt')
    ...
finally:
    f.close()
```

这两个块日常写代码用得不多，了解写法即可。

<!--v-->

## raise：主动报错

遇到不该继续的情况，除了自己处理，还可以选择**停下并报错**：

```python
raise ValueError("something is wrong")
```

`raise` 会抛出一个异常，把当前函数的执行中断掉。它的意义在于：**不让一个错误的结果继续往下传。**

举个例子，一个只接受非空字符串的函数，一旦拿到空串，与其算出一个没有意义的返回值，不如当场报错，让问题停在源头。

<!--v-->

## assert：检查"本该成立"的条件

`assert` 用来声明"这里必须成立"，不成立就抛 `AssertionError`：

```python
assert <应该为真的条件>, "不成立时打印的信息"
```

```python
def avg(grades):
    assert len(grades) != 0, 'no grades data'
    return sum(grades) / len(grades)
```

它通常用在两个位置：检查函数输入是否符合约定，以及检查函数输出是否合理。好处是让程序在第一个不对劲的地方就停下来，而不是带着错值继续跑。

注意 `assert` 只能让程序停，不能给出替代方案 —— 这正是它和 `except` 的分工。

<!--v-->

## 三种处理策略

假设要算每个学生的平均分，而某个学生一门成绩都没有：

<div class="three-line">

| 策略 | 做法 | 拿到空成绩时 |
|:---|:---|:---|
| 打印提示 | `except` 里打印警告 | 打印 `warning`，返回 `None` |
| 改政策 | `except` 里返回默认值 | 打印 `warning`，返回 `0.0` |
| 中断 | 用 `assert` 直接停 | 抛 `AssertionError: no grades data` |

</div>

三种都能跑，选哪种取决于"没有成绩"这件事有多严重：可以容忍就返回默认值，绝不能容忍就用 `assert` 拦住。

<!--v-->

## 什么时候用 assert，什么时候用 except

两者目标一致 —— 尽早发现问题、让问题出现在离原因最近的地方 —— 但适用场景不同：

<div class="three-line">

| | 用在什么时候 | 例子 |
|:---|:---|:---|
| `except` | 意外情况可以继续处理，不需要中断 | 用户输入了非法数据，提示他重输 |
| `assert` | 用来守住"约定"，是测试的补充 | 函数要求参数非空，为空就是调用方的问题 |

</div>

**能从意外里恢复就用 `except`，不该继续跑下去就用 `assert`。**

<!--s-->

<div class="middle center"><div style="width: 100%">

# Dictionaries

</div></div>

<!--v-->

## 用多个平行列表有多麻烦

想存一组学生的姓名和成绩，最直接的做法是每个属性开一个列表：

```python
names = ['Ana', 'John', 'Matt', 'Katy']
grades = ['A+', 'B', 'A', 'A']
```

用的时候要拿姓名去 `names` 里找位置，再用同一个位置去 `grades` 里取值：

```python
def get_grade(student, name_list, grade_list):
    i = name_list.index(student)
    return (student, grade_list[i])
```

信息一多（平时作业一个列表、小测一个列表、期末一个列表），就要维护一堆列表、每次调用都全部传进去、新增或修改时还得记得每个列表都改一遍。而且永远只能靠整数下标取数据。

换成"列表的列表"（每个学生一个子列表）也救不了：想取某项成绩还是得先遍历找到这个人，再遍历找到这项，代码一样乱。

<!--v-->

## 换一种存法：key 到 value

字典（dictionary）把数据存成"键 → 值"的配对，用花括号写：

```python
grades = {'Ana': 'B', 'Matt': 'A', 'John': 'B', 'Katy': 'A'}
```

- 键（key）是查找用的名字，这里是学生姓名
- 值（value）是被查出来的内容，这里是成绩
- 空字典写成 `{}`

一个字典就能装下全部信息，查找直接按名字来，不用再记住谁排在第几个。

<!--v-->

## 按 key 取值

```python
grades = {'Ana': 'B', 'Matt': 'A', 'John': 'B', 'Katy': 'A'}
grades['John']    # 'B'
grades['Grace']   # KeyError: 'Grace'
```

写法跟列表下标一样，只是方括号里换成键。键不存在时抛 `KeyError`。

有一点和列表不同：字典**没有**"由值反查键"的简单写法。知道成绩是 `'B'`，不能直接问"谁得了 B"，得自己遍历一遍。

<!--v-->

## 增、改、删

```python
grades = {'Ana': 'B', 'Matt': 'A', 'John': 'B', 'Katy': 'A'}
grades['Grace'] = 'A'    # 键不存在 → 新增一条
grades['Grace'] = 'C'    # 键已存在 → 改掉它的值
del grades['Ana']        # 删除一条
```

同一个方括号赋值，按键在不在走两条不同的路：不在就新增，在就覆盖。字典本身也是可变对象，别名和拷贝的规则和列表一样（用 `=` 是别名，用 `d.copy()` 才是复制）。

<!--v-->

## 判断键在不在

```python
'John' in grades     # True
'Daniel' in grades   # False
'B' in grades        # False  ← 注意
```

`in` 检查的是**键**，不是值。`'B'` 明明是一个成绩，但它是值不是键，所以结果是 `False`。想查值要用 `'B' in grades.values()`。

<!--v-->

## 遍历字典：keys / values / items

```python
grades = {'Ana': 'B', 'Matt': 'A', 'John': 'B', 'Katy': 'A'}
grades.keys()     # dict_keys(['Ana', 'Matt', 'John', 'Katy'])
grades.values()   # dict_values(['B', 'A', 'B', 'A'])
grades.items()    # dict_items([('Ana','B'), ('Matt','A'), ...])
```

三个方法各返回一个可迭代对象，想要真正的列表就套一层 `list(...)`。

最常用的是 `items()`，它一次给出键和值，配合解包正好：

```python
for k, v in grades.items():
    print(k, 'got', v)
```

字典取数据只能靠键，没有下标。遍历顺序跟插入顺序一致，但**不要依赖它** —— 需要按某个顺序处理时，先自己排序。

<!--v-->

## 键的限制：唯一，且不可变

<div class="three-line">

| | 要求 | 可以是 |
|:---|:---|:---|
| 键（key） | 唯一、不可变 | 字符串、整数、浮点数、布尔、元组 |
| 值（value） | 任意类型、可以重复 | 上面这些，加上列表、字典 |

</div>

键必须唯一，否则查找时不知道该取哪一个；键必须不可变，这跟字典内部怎么存有关，下一页展开。

<!--v-->

## 为什么键必须不可变

字典底层不是一列挨着放的数组，而是靠一个"哈希函数"把键换算成整数，用这个整数决定值存在哪一格：

<svg viewBox="0 0 920 250" width="94%" style="display:block;margin:6px auto;">
  <text x="460" y="22" text-anchor="middle" font-size="16" fill="#333">哈希函数：字母序号相加，再对 16 取余（字母 a=1, b=2, …）</text>
  <g font-size="15" fill="#333">
    <text x="60" y="58">'Ana'  : 1+14+1 = 16 → 余 0</text>
    <text x="60" y="84">'Eric' : 5+18+9+3 = 35 → 余 3</text>
    <text x="60" y="110">'Kate' : 11+1+20+5 = 37 → 余 5</text>
    <text x="60" y="136">'John' : 10+15+8+14 = 47 → 余 15</text>
  </g>
  <g>
    <rect x="70" y="170" width="47" height="30" rx="3" fill="#e3f2fd" stroke="#003fa3" stroke-width="1.5"/>
    <text x="93" y="190" text-anchor="middle" font-size="12" fill="#003fa3">Ana</text>
    <rect x="119" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="168" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="217" y="170" width="47" height="30" rx="3" fill="#e3f2fd" stroke="#003fa3" stroke-width="1.5"/>
    <text x="240" y="190" text-anchor="middle" font-size="12" fill="#003fa3">Eric</text>
    <rect x="266" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="315" y="170" width="47" height="30" rx="3" fill="#e3f2fd" stroke="#003fa3" stroke-width="1.5"/>
    <text x="338" y="190" text-anchor="middle" font-size="12" fill="#003fa3">Kate</text>
    <rect x="364" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="413" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="462" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="511" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="560" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="609" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="658" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="707" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="756" y="170" width="47" height="30" rx="3" fill="#f4f6fa" stroke="#c3cbd8"/>
    <rect x="805" y="170" width="47" height="30" rx="3" fill="#e3f2fd" stroke="#003fa3" stroke-width="1.5"/>
    <text x="828" y="190" text-anchor="middle" font-size="12" fill="#003fa3">John</text>
  </g>
  <g font-size="12" fill="#889">
    <text x="93" y="218" text-anchor="middle">0</text>
    <text x="142" y="218" text-anchor="middle">1</text>
    <text x="191" y="218" text-anchor="middle">2</text>
    <text x="240" y="218" text-anchor="middle">3</text>
    <text x="289" y="218" text-anchor="middle">4</text>
    <text x="338" y="218" text-anchor="middle">5</text>
    <text x="387" y="218" text-anchor="middle">6</text>
    <text x="436" y="218" text-anchor="middle">7</text>
    <text x="485" y="218" text-anchor="middle">8</text>
    <text x="534" y="218" text-anchor="middle">9</text>
    <text x="583" y="218" text-anchor="middle">10</text>
    <text x="632" y="218" text-anchor="middle">11</text>
    <text x="681" y="218" text-anchor="middle">12</text>
    <text x="730" y="218" text-anchor="middle">13</text>
    <text x="779" y="218" text-anchor="middle">14</text>
    <text x="828" y="218" text-anchor="middle">15</text>
  </g>
</svg>

查找时用同样的函数再算一遍，就能直接跳到那一格。**如果键的内容可以被改，算出来的整数就会跟着变，值就找不回来了** —— 所以键必须不可变。

具体看：`'Kate'` 的字母和是 37，落在第 5 格；改成 `'Cate'` 后字母和是 29，落到第 13 格 —— 同一个人的成绩就查不到了。浮点数当键也是同理：浮点运算有精度误差，两个看起来相等的值未必真的相等，容易算出不同的格子。

<!--v-->

## 值里可以再放字典

值可以是任何类型，包括另一个字典。把学生的各项成绩收成一个小字典，就成了嵌套结构：

```python
grades = {'Ana': {'mq': [5,4,4], 'ps': [10,9,9], 'fin': 'B'},
          'Bob': {'mq': [6,7,8], 'ps': [8,9,10], 'fin': 'A'}}
```

取值时一层层往下走：

```python
grades['Ana']            # {'mq': [5,4,4], 'ps': [10,9,9], 'fin': 'B'}
grades['Ana']['mq']      # [5, 4, 4]
grades['Ana']['mq'][0]   # 5
```

每一步方括号都可以理解成"在这个容器里按这个名字/位置取"。多层结构写起来长，但规律是一致的。

<!--v-->

## 从嵌套字典里汇总数据

```python
my_d = {'Ana':  {'mq': [10], 'ps': [10, 10]},
        'Bob':  {'ps': [7, 8], 'mq': [8]},
        'Eric': {'mq': [3],  'ps': [0]}}

def get_average(data, what):
    all_data = []
    for stud in data.keys():
        all_data = all_data + data[stud][what]
    return sum(all_data) / len(all_data)
```

`data[stud]` 先取出这个学生的小字典，`[what]` 再按 `'mq'` 取出他的列表，`+` 把它并进汇总列表。

实测 `get_average(my_d, 'mq')` 汇总到 `[10, 8, 3]`，返回 `7.0`。

<!--v-->

## 列表和字典对照

<div class="three-line">

| | 列表 | 字典 |
|:---|:---|:---|
| 怎么取 | 按整数下标 | 按键 |
| 顺序 | 下标有先后 | 靠键取，顺序不可依赖 |
| 键/下标类型 | 只能是整数 | 任何不可变类型 |
| 值 | 任意类型 | 任意类型 |

</div>

选择依据是"你怎么找到它"：按位置找就用列表，按名字找就用字典。

<!--s-->

<div class="middle center"><div style="width: 100%">

# Q & A

</div></div>

<!--v-->

## 这一讲补齐了什么

Lecture 4 – 6 解决的是"怎么把程序拆成零件"，这一讲往前补了两块更基础的东西：

- **数据怎么组织**：列表按位置存，字典按名字存；两者都是可变对象，都要小心别名
- **出错怎么办**：先靠测试发现，再靠调试定位，最后用 `except` 恢复、用 `assert` 拦停

后面的练习会同时用到这两块：数据放进列表或字典，可能出错的地方用 `try` 或 `assert` 兜住。
