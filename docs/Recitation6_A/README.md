# Recitation 6 (A)

本讲以 Coordinate 为主线，衔接 Lec11 的嵌套递归，展开 Python 对象模型、类型系统、继承和进阶 OOP。PDF 共 80 页，所有课堂示例直接给出实现与结果。

## 课件与配套内容

| 材料 | 用途 |
| --- | --- |
| [在线课件](https://si100b-26fall.github.io/SI100B-Fall-2026-PP-Recitation/Recitation6_A/) | 浏览器授课，仓库自动发布后可用 |
| [PDF](../../slides/Recitation6_A/Recitation6_A.pdf) | 离线投影或打印 |
| [Markdown 源文件](../../slides/Recitation6_A/Recitation6_A.md) | 使用 reveal-md 继续编辑 |
| [Notebook](../../slides/Recitation6_A/Recitation6_A.ipynb) | 顺序运行示例，查看完整输出 |
| [完整示例脚本](../../slides/Recitation6_A/examples/recitation6_oop_demo.py) | 独立运行全部课件代码 |
| [静态检查示例](../../slides/Recitation6_A/examples/type_check_demo.py) | 比较类型诊断与运行时行为 |
| [逐页助教讲稿](TeachingNotes.md) | 教学重点、机制说明与边界 |
| [专业教学参考](TeachingReferences.md) | Python 官方文档及课程参考 |

## 内容

- 嵌套列表递归、类、实例、属性、绑定方法与初始化。
- 实例属性、类属性、共享可变状态、属性赋值与对象修改。
- 内置类型、object 与 type、类型关系、类型注解、静态检查与显式运行时检查。
- 继承规则、各类成员的继承行为、方法重写、多态、组合、MRO 与 super。
- property 的 getter/setter、公开接口与内部存储、类方法与静态方法。
- 运算符和容器协议、相等与哈希、抽象基类、dataclass。

## 运行代码

在仓库根目录运行，课件和 Notebook 中的代码只依赖 Python 标准库：

```powershell
python slides/Recitation6_A/examples/recitation6_oop_demo.py
```

静态检查示例有意传入与注解不匹配的参数。直接执行会输出 `6` 和 `hihi`：

```powershell
python slides/Recitation6_A/examples/type_check_demo.py
```

选装 mypy 后运行下列命令，预期得到一次 `[arg-type]` 诊断：

```powershell
python -m pip install mypy
python -m mypy slides/Recitation6_A/examples/type_check_demo.py
```

该诊断用于演示类型注解不自动产生运行时验证。完整课件脚本与 Notebook 不依赖 mypy。

## 编辑和预览

课件沿用课程仓库的 reveal-md 模板及发布流程，预览命令见[助教讲稿](TeachingNotes.md#运行与预览)。讲稿和参考放在 docs 目录，避免被自动构建识别为额外课件。
