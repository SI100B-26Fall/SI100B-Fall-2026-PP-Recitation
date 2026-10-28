# 专业教学参考与采用说明

核对日期：2026-10-28。本讲面向已有基础 Python 知识、正在学习 OOP 的学生。示例围绕课程 Coordinate 自行编写，网络资料用于校核语义和组织讲解，不逐段复制外部课程。

## 正课衔接

教授 Lec11_A.pdf 第 42-49 页用于嵌套列表递归，第 50-68 页用于类、对象和初始化。实例方法、类型对象、继承与后续进阶机制均为本次扩展。

## 对象与继承

- [Python 官方类教程](https://docs.python.org/3/tutorial/classes.html)：核对实例、普通属性、绑定方法、类属性、继承和重写。
- [Python 数据模型](https://docs.python.org/3/reference/datamodel.html)：核对对象的身份、类型和状态，初始化职责及特殊方法协议。
- [Helsinki Python MOOC：Class hierarchies](https://programming-26.mooc.fi/part-10/1-class-hierarchies/)：参考从复用已有状态和方法逐步引出子类、super 与重写的顺序。
- [Harvard CS50P Lecture 8](https://cs50.harvard.edu/python/notes/8/)：参考通过完整可运行类解释继承、对象表示和操作符行为的教学方式。

## 类型与查找

- [内置函数文档](https://docs.python.org/3/library/functions.html)：核对 type、isinstance、issubclass、super 及三类方法的绑定规则。
- [官方 MRO HOWTO](https://docs.python.org/3/howto/mro.html)：核对 C3 与菱形继承的线性查找次序。标题为历史文档，但其中 C3 机制延续至 Python 3。
- [Descriptor Guide](https://docs.python.org/3/howto/descriptor.html)：核对方法绑定、property 数据描述符，以及它与普通实例属性的查找差异。本讲不扩展为完整自定义描述符开发教程。
- [mypy 官方入门](https://mypy.readthedocs.io/en/stable/getting_started.html)：核对不执行源程序的静态分析，以及诊断与 Python 运行时异常的区别。
- [mypy arg-type 诊断](https://mypy.readthedocs.io/en/stable/error_code_list.html#check-argument-types-arg-type)：核对字符串实参与整数参数注解不匹配的诊断。
- [typing 文档](https://docs.python.org/3/library/typing.html)：核对类型注解默认不在运行时强制检查，也不自动转换数值。

## 抽象接口与数据类

- [abc 文档](https://docs.python.org/3/library/abc.html)：核对 abstractmethod、不可实例化条件和继承获得的具体实现。虚拟子类注册与自定义元类不展开。
- [dataclasses 文档](https://docs.python.org/3/library/dataclasses.html)：核对生成方法、相等的类型限制、default_factory、frozen 及其可变性边界。不依赖最新版本专有的新增参数。

## 本讲保留的区分

对象属于某个类型、类对象由元类构造、类之间的继承，以及对象内部的组合是不同关系。super 根据实际 MRO 继续查找，不固定等于直接父类。属性管理不自动提供安全隔离；方法重写也不自动证明满足接口的全部业务合同。

类名、变量名和书写风格不再作为独立教学内容。重点是对象行为及其运行机制，所有结果通过实际运行示例核对。
