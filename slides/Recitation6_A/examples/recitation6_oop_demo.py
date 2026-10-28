# -*- coding: utf-8 -*-
"""Recitation 6 (A): complete runnable OOP demonstrations."""

# deep_rev：逐层构造结果
def deep_rev(L):
    result = []
    for e in L[::-1]:
        if type(e) == list:
            result.append(deep_rev(e))
        else:
            result.append(e)
    return result

# 空列表与结果返回
L = [1, [2, 3], []]
print(deep_rev(L))  # [[], [3, 2], 1]
print(deep_rev([])) # []
print(L)           # [1, [2, 3], []]

# count_elem：统计所有整数
def count_elem(L):
    total = 0
    for e in L:
        if type(e) == list:
            total += count_elem(e)
        else:
            total += 1
    return total

# 贯穿示例：Coordinate
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def as_tuple(self):
        return self.x, self.y

    def describe(self):
        return f"({self.x}, {self.y})"

# 实例化、属性与方法调用
p = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(p.x, p.y)           # 3 4
print(p.as_tuple())       # (3, 4)
print(origin.describe())  # (0, 0)

# self 与实例方法调用
p = Coordinate(3, 4)
p.move(1, -2)
print(p.as_tuple())  # (4, 2)
Coordinate.move(p, -1, 2)
print(p.as_tuple())  # (3, 4)

# 绑定方法保存实例与函数
p = Coordinate(3, 4)
bound = p.move  # 取得方法，尚未调用
print(bound.__self__ is p)  # True
print(bound.__func__ is Coordinate.move)  # True
bound(1, -2)
print(p.as_tuple())  # (4, 2)

# 更新状态与返回结果
p = Coordinate(3, 4)
result = p.move(1, -2)
print(result)        # None
print(p.as_tuple())  # (4, 2)
print(p.describe())  # (4, 2)

# 实例属性与类属性
class PointRecord:
    kind = "point"

    def __init__(self, x, y):
        self.x = x
        self.y = y

# 普通属性的查找与遮蔽
a = PointRecord(1, 2)
b = PointRecord(3, 4)
print(a.kind, b.kind)  # point point
a.kind = "special"
print(a.kind, b.kind)  # special point
print(PointRecord.kind)  # point
print(vars(a))  # {'x': 1, 'y': 2, 'kind': 'special'}

# 类属性中的列表由多个实例共享
class SharedGroup:
    points = []  # 执行类定义时创建一个列表

first = SharedGroup()
second = SharedGroup()
first.points.append(Coordinate(1, 2))
print(len(second.points))  # 1
print(first.points is SharedGroup.points)  # True
print(second.points is SharedGroup.points)  # True

# 修改共享对象与重新绑定属性
first.points = []  # 在 first 中保存一个新列表
first.points.append(Coordinate(5, 6))
print(len(first.points), len(second.points))  # 1 1
print(first.points is SharedGroup.points)  # False
print(second.points is SharedGroup.points)  # True
print(first.points[0].as_tuple())   # (5, 6)
print(second.points[0].as_tuple())  # (1, 2)

# 每个实例建立自己的容器
class PointGroup:
    def __init__(self):
        self.points = []

    def add(self, point):
        self.points.append(point)

first = PointGroup()
second = PointGroup()
first.add(Coordinate(1, 2))
print(len(first.points), len(second.points))  # 1 0

# 内置类型与自定义类型
values = [7, 2.5, "hi", [1, 2], {"x": 1}]
print([type(v).__name__ for v in values])
# ['int', 'float', 'str', 'list', 'dict']
p = Coordinate(3, 4)
print(type(p) is Coordinate)  # True

# 动态类型与名字绑定
value = 3
print(type(value).__name__)  # int
value = "three"
print(type(value).__name__)  # str

# 类本身也是对象
p = Coordinate(3, 4)
print(type(p) is Coordinate)  # True
print(type(Coordinate) is type)  # True
print(isinstance(Coordinate, type))  # True
print(type(int) is type)  # True

# object 与 type 的不同角色
print(Coordinate.__bases__ == (object,))  # True
print(issubclass(Coordinate, object))     # True
print(type(object) is type)              # True
print(type(type) is type)                # True
print(issubclass(type, object))           # True

# 内置类型的继承关系
print(issubclass(bool, int))   # True
print(issubclass(float, int))  # False
print(True + 2)               # 3

# 精确类型与继承关系判断
print(type(True) is bool)      # True
print(type(True) is int)       # False
print(isinstance(True, int))   # True
print(isinstance(3, object))   # True
print(issubclass(bool, object)) # True

# isinstance 接纳列表子类
class PointList(list):
    pass

data = PointList([1, 2])
print(type(data) is list)       # False
print(isinstance(data, list))   # True
print(issubclass(PointList, list))  # True

# 类型注解与运行时检查
def twice(value: int) -> int:
    return value * 2

print(twice(3))     # 6
print(twice("hi"))  # hihi

# 显式检查在调用时拒绝不合法的值
def twice_checked(value: int) -> int:
    if not isinstance(value, int):
        raise TypeError("value must be an int")
    return value * 2

print(twice_checked(3))  # 6
try:
    twice_checked("hi")
except TypeError as error:
    print(type(error).__name__, str(error))
# TypeError value must be an int

# 继承复用已有类型的行为
class PlainCoordinate(Coordinate):
    pass

plain = PlainCoordinate(3, 4)
plain.move(1, -2)
print(plain.as_tuple())  # (4, 2)
print(isinstance(plain, Coordinate))  # True

# 子类扩展状态并重写行为
class NamedCoordinate(Coordinate):
    def __init__(self, x, y, name="P"):
        super().__init__(x, y)
        self.name = name

    def describe(self):
        return f"{self.name}: {super().describe()}"

# 继承的方法与子类方法协同工作
named = NamedCoordinate(3, 4, "A")
print(named.describe())  # A: (3, 4)
named.move(1, -2)
print(named.describe())  # A: (4, 2)
print(named.as_tuple())  # (4, 2)

# super 复用同一个实例上的基类实现
named = NamedCoordinate(3, 4, "A")
print(vars(named))  # {'x': 3, 'y': 4, 'name': 'A'}
print(type(named) is NamedCoordinate)  # True
print(super(NamedCoordinate, named).describe())
# (3, 4)

# 重写初始化时显式完成初始化链
class IncompleteCoordinate(Coordinate):
    def __init__(self, name):
        self.name = name

incomplete = IncompleteCoordinate("A")
try:
    incomplete.as_tuple()
except AttributeError:
    print("x and y are not initialized")

# 方法重写与动态分派
def describe_all(points):
    return [point.describe() for point in points]

items = [Coordinate(1, 2), NamedCoordinate(3, 4, "B")]
print(describe_all(items))
# ['(1, 2)', 'B: (3, 4)']

# 父子类成员与类型关系
parent_point = Coordinate(1, 2)
child_point = NamedCoordinate(3, 4, "A")
print(child_point.as_tuple())  # (3, 4)，继承的方法
print(child_point.name)        # A，子类新增属性
print(hasattr(parent_point, "name"))  # False
print(isinstance(child_point, Coordinate))  # True
print(isinstance(parent_point, NamedCoordinate))  # False
print(issubclass(NamedCoordinate, Coordinate))    # True
print(issubclass(Coordinate, NamedCoordinate))    # False

# 鸭子类型依赖对象提供的行为
class ForeignCoordinate:
    def describe(self):
        return "external coordinate"

print(describe_all([ForeignCoordinate()]))
# ['external coordinate']
print(isinstance(ForeignCoordinate(), Coordinate))
# False

# 组合把对象保存在另一个对象中
group = PointGroup()
group.add(Coordinate(1, 2))
group.add(NamedCoordinate(3, 4, "A"))
print([p.describe() for p in group.points])
# ['(1, 2)', 'A: (3, 4)']
group.points[0].move(1, 0)
print(group.points[0].as_tuple())  # (2, 2)
print(isinstance(group, Coordinate))  # False

# 单继承的 MRO
print([cls.__name__ for cls in NamedCoordinate.__mro__])
# ['NamedCoordinate', 'Coordinate', 'object']

# 协作式多重继承的基类
class TraceRoot:
    def steps(self):
        return ["root"]

class LeftTrace(TraceRoot):
    def steps(self):
        return ["left"] + super().steps()

class RightTrace(TraceRoot):
    def steps(self):
        return ["right"] + super().steps()

# 菱形继承的查找次序
class CombinedTrace(LeftTrace, RightTrace):
    pass

combined = CombinedTrace()
print([cls.__name__ for cls in CombinedTrace.__mro__])
# ['CombinedTrace', 'LeftTrace', 'RightTrace',
#  'TraceRoot', 'object']
print(combined.steps())  # ['left', 'right', 'root']

# super 可以继续到兄弟类
print(super(LeftTrace, combined).steps())
# ['right', 'root']
print(TraceRoot.steps(combined))
# ['root']

# property 提供计算型属性
class RadialCoordinate(Coordinate):
    @property
    def radius(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

radial = RadialCoordinate(3, 4)
print(radial.radius)  # 5.0
radial.move(-3, 0)
print(radial.radius)  # 4.0

# setter 在赋值时维护约束
class NonnegativeXCoordinate(Coordinate):
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be nonnegative")
        self._x = value

# 属性赋值的完整执行结果
checked = NonnegativeXCoordinate(3, 4)
checked.x = 5
print(checked.x)  # 5
try:
    checked.x = -1
except ValueError:
    print("negative x rejected")
print(checked.x)  # 5
print(vars(checked))  # {'_x': 5, 'y': 4}

# 普通属性与 property 的查找差异
checked.__dict__["x"] = -100
print(checked.x)  # 5
try:
    radial.radius = 9
except AttributeError:
    print("radius is read-only")

# 类方法与静态方法的定义
class ParsedCoordinate(Coordinate):
    @classmethod
    def from_text(cls, text):
        x, y = text.split(",")
        return cls(float(x), float(y))

    @staticmethod
    def is_pair(value):
        return isinstance(value, (tuple, list)) and len(value) == 2

# cls 保留实际调用的子类
class DerivedParsedCoordinate(ParsedCoordinate):
    pass

parsed = DerivedParsedCoordinate.from_text("3,4")
print(type(parsed).__name__)  # DerivedParsedCoordinate
print(parsed.as_tuple())     # (3.0, 4.0)
print(ParsedCoordinate.is_pair((3, 4)))  # True
print(parsed.is_pair([1]))              # False

# 自定义 str 与 repr
class PrintableCoordinate(Coordinate):
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PrintableCoordinate({self.x!r}, {self.y!r})"

# 打印对象与打印对象容器
display_point = PrintableCoordinate(3, 4)
print(display_point)       # (3, 4)
print(repr(display_point)) # PrintableCoordinate(3, 4)
print([display_point])     # [PrintableCoordinate(3, 4)]

# 运算符重载：向量相加
class Vector(Coordinate):
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

v = Vector(1, 2) + Vector(3, 4)
print(v.as_tuple())  # (4, 6)

# NotImplemented 是协议返回值
v = Vector(1, 2)
print(Vector.__add__(v, 3) is NotImplemented)  # True
try:
    v + 3
except TypeError:
    print("unsupported addition")

# 值相等与对象身份
class ValueCoordinate(Coordinate):
    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.as_tuple() == other.as_tuple()

# 相等协议与哈希约束
a = ValueCoordinate(1, 2)
b = ValueCoordinate(1, 2)
print(a == b, a is b)  # True False
print(ValueCoordinate.__hash__ is None)  # True
try:
    hash(a)
except TypeError:
    print("unhashable value coordinate")

# 为组合容器实现内置协议
class Path(PointGroup):
    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return iter(self.points)

    def __getitem__(self, index):
        return self.points[index]

# 长度、迭代、索引与真假值
path = Path()
print(bool(path))  # False
path.add(Coordinate(1, 2))
path.add(NamedCoordinate(3, 4, "A"))
print(len(path))  # 2
print([p.as_tuple() for p in path])  # [(1, 2), (3, 4)]
print(path[0].as_tuple())  # (1, 2)
print(bool(path))  # True

# 抽象基类显式规定行为接口
from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self, dx, dy):
        raise NotImplementedError

# 未完成抽象接口的类不可实例化
class IncompleteMovable(Movable):
    pass

try:
    IncompleteMovable()
except TypeError:
    print("abstract method is not implemented")
print(type(Movable).__name__)  # ABCMeta

# 通过继承满足抽象接口
class MovableCoordinate(Coordinate, Movable):
    pass

movable = MovableCoordinate(3, 4)
movable.move(1, -2)
print(movable.as_tuple())  # (4, 2)
print(isinstance(movable, Movable))  # True

# dataclass 自动生成常用方法
from dataclasses import dataclass

@dataclass
class DataCoordinate:
    x: float
    y: float

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# 数据类的初始化、表示与相等
data_point = DataCoordinate(3, 4)
print(data_point)  # DataCoordinate(x=3, y=4)
print(data_point == DataCoordinate(3, 4))  # True
data_point.move(1, -2)
print(data_point)  # DataCoordinate(x=4, y=2)
print(type(data_point.x).__name__)  # int

# default_factory 建立独立可变字段
from dataclasses import field

@dataclass
class DataPath:
    points: list = field(default_factory=list)

data_first = DataPath()
data_second = DataPath()
data_first.points.append(DataCoordinate(1, 2))
print(len(data_first.points), len(data_second.points))  # 1 0

# frozen 数据类限制字段重新赋值
from dataclasses import FrozenInstanceError

@dataclass(frozen=True)
class FrozenCoordinate:
    x: float
    y: float

fixed = FrozenCoordinate(3, 4)
try:
    fixed.x = 8
except FrozenInstanceError:
    print("field assignment is blocked")

# 把类型、继承与协议串联使用
route = Path()
route.add(Coordinate(1, 2))
route.add(NamedCoordinate(3, 4, "A"))
for point in route:
    point.move(1, 0)
print([p.describe() for p in route])
# ['(2, 2)', 'A: (4, 4)']
print(isinstance(route, PointGroup))  # True
print(isinstance(route, Coordinate))  # False
