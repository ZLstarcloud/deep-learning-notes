# -*- coding: utf-8 -*-
"""生成第 1 周每日练习 notebook：D:/deep-learning/week1/day1-7.ipynb"""
import json, os

def nb(cells):
    out = []
    for kind, lines in cells:
        src = [l + "\n" for l in lines[:-1]] + [lines[-1]]
        if kind == "md":
            out.append({"cell_type": "markdown", "metadata": {}, "source": src})
        else:
            out.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                        "outputs": [], "source": src})
    return {"cells": out,
            "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                         "language_info": {"name": "python", "version": "3.10"}},
            "nbformat": 4, "nbformat_minor": 5}

def code(*lines): return ("code", list(lines))
def md(*lines): return ("md", list(lines))

days = {}

days["day1"] = nb([
    md("# Day 1 · Python 语法骨架 + Jupyter"),
    md("**上午**：过一遍官方教程第 1–3 章（变量、类型、缩进、if/while）\n"
       "**下午**：字符串、列表、切片、循环\n"
       "**晚上**：完成 6 个练习函数\n\n"
       "> 规则：所有代码亲手敲，不许复制粘贴。"),
    md("## 1. 变量与类型：观察 type() 的输出"),
    code("x = 10\n"
         "y = 3.5\n"
         "s = 'hello'\n"
         "flag = True\n"
         "print(type(x), type(y), type(s), type(flag))\n"
         "# 再试试 x / y、x // y、x % y、x ** y，先猜结果再运行"),
    md("## 2. 真值判断与 None"),
    code("for v in [0, 1, '', 'a', [], [1], None]:\n"
         "    print(v, bool(v))"),
    md("## 3. 字符串常用方法：猜输出，再运行验证"),
    code("s = '  Deep Learning Is Fun  '\n"
         "print(s.strip())\n"
         "print(s.strip().lower())\n"
         "print(s.split())\n"
         "print(','.join(['a','b','c']))\n"
         "print(s.replace('Fun', 'Hard'))\n"
         "# 补充：f-string 格式化\n"
         "name, score = 'model', 0.92\n"
         "print(f'{name}: {score:.2%}')"),
    md("## 4. 列表与切片"),
    code("nums = list(range(10))\n"
         "print(nums[2:5], nums[:3], nums[-2:], nums[::2], nums[::-1])\n"
         "nums.append(10); nums += [11, 12]\n"
         "print(nums)"),
    md("## 5. 循环：range / enumerate / zip"),
    code("for i, v in enumerate(['a','b','c']):\n"
         "    print(i, v)\n"
         "for a, b in zip([1,2,3], 'xyz'):\n"
         "    print(a, b)"),
    md("## 6. 晚间练习（全部自己写）"),
    code("# 练习 1：FizzBuzz —— 1~30，3 的倍数印 Fizz，5 的倍数印 Buzz，既是 3 又是 5 印 FizzBuzz\n"
         "# 练习 2：反转字符串（先切片法，再 reversed() 法）\n"
         "# 练习 3：统计一段英文里每个单词出现的次数（用 dict）\n"
         "text = 'the cat sat on the mat the cat'\n"
         "# 练习 4：找出列表中第二大且不重复的数\n"
         "# 练习 5：判断一个数是否为质数（写函数 is_prime(n)）\n"
         "# 练习 6：斐波那契前 30 项，放进列表"),
    md("## 7. 今日 3 行记录：学会了 / 卡住了 / 明天第一件事"),
    code("# 在这里写今天的学习记录"),
])

days["day2"] = nb([
    md("# Day 2 · 容器与函数式写法"),
    md("**上午**：dict/set、推导式、解包、*args/**kwargs、lambda、sorted(key=)\n"
       "**下午**：完成练习 1–4\n"
       "**晚上**：做一个 JSON 通讯录小程序\n\n"
       "> 这是 Python 最有味道的部分，也是读懂别人代码的钥匙。"),
    md("## 1. dict 与 set 基本操作"),
    code("d = {'a': 1, 'b': 2}\n"
         "print(d.get('a'), d.get('z', 0))\n"
         "d['c'] = 3\n"
         "for k, v in d.items():\n"
         "    print(k, v)\n"
         "s = {1, 2, 2, 3}\n"
         "print(s, len(s), 2 in s)"),
    md("## 2. 推导式：同一逻辑写两遍，对比"),
    code("sq_loop = []\n"
         "for i in range(10):\n"
         "    if i % 2 == 0:\n"
         "        sq_loop.append(i * i)\n"
         "sq = [i * i for i in range(10) if i % 2 == 0]\n"
         "print(sq_loop == sq)\n"
         "# 再来：字典推导 {单词: 长度}；集合推导 {x % 5 for x in range(100)}"),
    md("## 3. 解包与 *args / **kwargs"),
    code("def profile(name, age, *hobbies, **extra):\n"
         "    print(name, age, hobbies, extra)\n"
         "profile('x', 20, 'code', 'run', city='BJ')\n"
         "a, *rest = [1, 2, 3, 4]\n"
         "print(a, rest)"),
    md("## 4. lambda 与 sorted(key=)"),
    code("words = ['pear', 'fig', 'banana']\n"
         "print(sorted(words, key=len))\n"
         "students = [('ann', 85), ('bob', 92), ('cid', 78)]\n"
         "# 按成绩从高到低排序，先自己想，再运行下面这行验证：\n"
         "print(sorted(students, key=lambda t: -t[1]))"),
    md("## 5. 练习"),
    code("# 练习 1：统计文本词频，输出出现次数最多的前 10 个词（sorted + key=lambda）\n"
         "text = 'the quick brown fox jumps over the lazy dog the fox runs'\n"
         "# 练习 2：列表去重并保持原有顺序\n"
         "nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\n"
         "# 练习 3：嵌套字典展平：{'a': {'b': 1, 'c': 2}} -> {'a.b': 1, 'a.c': 2}\n"
         "# 练习 4：用嵌套推导式转置矩阵 [[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]]"),
    md("## 6. 晚间项目：JSON 通讯录\n要求：add / find / delete / list 四个函数；数据存 contacts.json；程序重启后数据还在"),
    code("import json\n# 在这里实现"),
])

days["day3"] = nb([
    md("# Day 3 · 类、模块、异常、文件"),
    md("**上午**：class / __init__ / 继承 / __repr__ / 模块导入 / try-except / with open\n"
       "**下午**：实现 CSVReader 类\n"
       "**晚上**：把 Day1–2 练习拆成模块\n\n"
       "> 类比：类 = 数据 + 行为，和你用过的语言一样。重点记 Python 写法：self、双下划线方法。"),
    md("## 1. 最小的类"),
    code("class Counter:\n"
         "    def __init__(self, start=0):\n"
         "        self.count = start\n"
         "    def add(self, n=1):\n"
         "        self.count += n\n"
         "        return self\n"
         "    def __repr__(self):\n"
         "        return f'Counter({self.count})'\n"
         "c = Counter(5).add().add(3)\n"
         "print(c)"),
    md("## 2. 继承"),
    code("class Animal:\n"
         "    def __init__(self, name):\n"
         "        self.name = name\n"
         "    def speak(self):\n"
         "        return '...'\n"
         "class Dog(Animal):\n"
         "    def speak(self):\n"
         "        return f'{self.name}: wang!'\n"
         "print(Dog('wangcai').speak())"),
    md("## 3. 异常与文件"),
    code("try:\n"
         "    f = open('not_exist.csv', encoding='utf-8')\n"
         "except FileNotFoundError as e:\n"
         "    print('文件不存在:', e)\n"
         "with open('demo.txt', 'w', encoding='utf-8') as f:\n"
         "    f.write('line1\\nline2\\n')\n"
         "with open('demo.txt', encoding='utf-8') as f:\n"
         "    print(f.read())"),
    md("## 4. 下午项目：CSVReader 类"),
    code("# 要求：\n"
         "# 1. __init__(path) 读文件：第一行是表头，其余是数据（提示 str.split(',')）\n"
         "# 2. column(name) -> 返回该列所有值的列表\n"
         "# 3. mean(name) -> 返回该数值列的平均值\n"
         "# 4. 文件不存在给出友好报错；列名写错抛 KeyError\n"
         "# 先造一个 sales.csv（date,amount 共 5 行）再测试\n"
         "class CSVReader:\n"
         "    pass"),
    md("## 5. 模块"),
    code("# 把 Day1 的 is_prime 写进 mytools.py（和 notebook 同目录），然后：\n"
         "# from mytools import is_prime\n"
         "# 注意：改完 mytools.py 后内核可能还在用旧版本，菜单 Kernel -> Restart 再重跑\n"
         "# 理解 if __name__ == '__main__': 的作用——直接运行才执行，被 import 时不执行"),
])

days["day4"] = nb([
    md("# Day 4 · numpy 核心"),
    md("**上午**：读 numpy 官方 Quickstart\n"
       "**下午**：数组创建/索引 + 手写矩阵乘法 + 广播实验\n"
       "**晚上**：用 numpy 重写前两天的练习\n\n"
       "> 核心思想：**向量化代替 for 循环**。这是后面所有 PyTorch 代码的思维方式。"),
    md("## 1. 创建数组与基本属性"),
    code("import numpy as np\n"
         "a = np.array([[1,2,3],[4,5,6]])\n"
         "print(a.shape, a.ndim, a.dtype)\n"
         "print(np.zeros((2,3)), np.ones(4), np.arange(0,10,2))\n"
         "print(np.linspace(0, 1, 5))\n"
         "print(np.random.randn(2,3))"),
    md("## 2. 索引、切片、布尔索引"),
    code("a = np.arange(12).reshape(3,4)\n"
         "print(a[1, 2], a[:, 1], a[::2, -1])\n"
         "print(a[a > 6])\n"
         "a[a > 6] = 0\n"
         "print(a)"),
    md("## 3. 广播：亲手验证规则"),
    code("a = np.ones((3,4))\n"
         "b = np.array([1,2,3,4])\n"
         "print((a + b).shape)  # 规则：从尾部对齐，维度相同或一方为 1 才能广播\n"
         "# 下面哪个会报错？先猜再运行：\n"
         "# c = np.ones((3,5)); c + b\n"
         "# d = np.ones((1,4)); d + b"),
    md("## 4. 下午：手写矩阵乘法并对比速度"),
    code("import time\n"
         "A = np.random.rand(200, 200); B = np.random.rand(200, 200)\n"
         "t = time.time(); C1 = A @ B; print('np.matmul:', time.time()-t, '秒')\n"
         "# 用三重 for 循环实现 C2，再 np.allclose(C1, C2) 验证\n"
         "# 然后换 1000x1000 只跑 np.matmul，感受差距"),
    md("## 5. 练习：不用 for 循环"),
    code("# 练习 1：X 是 (100,3) 随机矩阵，每行减去该行的均值\n"
         "X = np.random.rand(100,3)\n"
         "# 练习 2：每列做标准化（减均值除标准差）\n"
         "# 练习 3：one-hot：labels = np.array([0,2,1,0]) -> np.eye(3)[labels]\n"
         "# 练习 4：对 10000 个正态样本求平方和、均值、标准差"),
    md("## 6. 晚间：用 numpy 重写 Day2 的词频统计"),
    code("# 提示：np.unique(text.split(), return_counts=True)"),
])

days["day5"] = nb([
    md("# Day 5 · numpy 进阶 + matplotlib"),
    md("**上午**：axis 参数、聚合、拼接、np.linalg\n"
       "**下午**：matplotlib 画图\n"
       "**晚上**：余弦相似度综合练习"),
    md("## 1. axis 是本周最大的坑"),
    code("a = np.arange(12).reshape(3,4)\n"
         "print(a.sum())        # 全部元素之和\n"
         "print(a.sum(axis=0))  # 沿行方向压扁 -> 每列的和\n"
         "print(a.sum(axis=1))  # 沿列方向压扁 -> 每行的和\n"
         "print(a.mean(axis=1, keepdims=True).shape)  # keepdims 为什么重要？（想想广播）"),
    md("## 2. 拼接与线性代数"),
    code("a = np.ones((2,3)); b = np.zeros((2,3))\n"
         "print(np.concatenate([a,b], axis=0).shape, np.concatenate([a,b], axis=1).shape)\n"
         "A = np.random.rand(3,3)\n"
         "print(np.linalg.det(A))\n"
         "print(np.linalg.inv(A) @ A)  # 应接近单位矩阵"),
    md("## 3. matplotlib 基础"),
    code("import matplotlib.pyplot as plt\n"
         "x = np.linspace(0, 10, 100)\n"
         "fig, axes = plt.subplots(1, 2, figsize=(10,4))\n"
         "axes[0].plot(x, np.sin(x), label='sin')\n"
         "axes[0].plot(x, np.cos(x), '--', label='cos')\n"
         "axes[0].legend(); axes[0].set_title('trig')\n"
         "axes[1].scatter(np.random.rand(50)*10, np.random.rand(50)*10, s=20)\n"
         "axes[1].set_xlabel('x'); axes[1].set_ylabel('y')\n"
         "plt.show()"),
    md("## 4. 练习：随机游走"),
    code("# 用 np.random.choice([-1,1], size=1000) + np.cumsum 生成 1000 步随机游走并画折线图"),
    md("## 5. 晚间综合：余弦相似度"),
    code("# 5 个 8 维随机向量（np.random.randn(5,8)）\n"
         "# 1) 按公式 cos = a·b / (|a||b|) 算两两相似度矩阵 (5x5)\n"
         "# 2) 对每个向量，输出与它最相似的另一向量编号\n"
         "# 3) 验证：全部归一化后直接算点积，结果应相同\n"
         "# 思考：这就是第 15 周向量数据库检索的本质"),
    md("## 6. 练习：直方图验证"),
    code("# 生成 10000 个 N(0,1) 样本，画 plt.hist，打印 mean/std 验证接近 0 和 1"),
])

days["day6"] = nb([
    md("# Day 6 · pandas + Git + 综合"),
    md("**上午**：读 pandas 官方『10 minutes to pandas』\n"
       "**下午**：找一份 CSV 完整分析一遍\n"
       "**晚上**：用 Git 把本周练习提交到 GitHub"),
    md("## 1. pandas 基本操作"),
    code("import pandas as pd\n"
         "import numpy as np\n"
         "df = pd.DataFrame({'name': list('abcde'),\n"
         "                 'city': ['BJ','SH','BJ','SZ','SH'],\n"
         "                 'score': np.random.randint(60,100,5)})\n"
         "print(df)\n"
         "print(df.describe())\n"
         "print(df[df.score > 80])\n"
         "print(df.loc[df.city=='BJ', 'score'])\n"
         "print(df.groupby('city').score.mean())\n"
         "df.to_csv('demo_df.csv', index=False)"),
    md("## 2. 缺失值与新增列"),
    code("df2 = pd.DataFrame({'a':[1,None,3],'b':[None,2,3]})\n"
         "print(df2.isna().sum())\n"
         "print(df2.fillna(0))\n"
         "df2['a_x2'] = df2.a * 2"),
    md("## 3. 下午综合练习\n数据二选一：\n"
       "1. Kaggle Titanic 的 train.csv（第 6 周反正要注册 Kaggle，可以现在注册）\n"
       "2. 自己造：写 200 行『日期,城市,销量』的 CSV\n\n"
       "要做：读取 -> describe -> 缺失值处理 -> 条件筛选 -> groupby 统计 -> 画柱状图，全程写在本 notebook"),
    code("# df = pd.read_csv('...')\n# 从这里开始"),
    md("## 4. 晚间：Git\n"
       "1. 安装 Git for Windows（git-scm.com 下载，全部默认下一步；或让 Claude 帮你装）\n"
       "2. 在 **PowerShell** 里执行下面的命令（换成你的用户名邮箱，并先在 GitHub 建好空仓库 deep-learning-notes）"),
    code("# 这些在 PowerShell 里敲，不是在这里：\n"
         "# cd D:\\deep-learning\n"
         "# git init\n"
         "# git config --global user.name '你的名字'\n"
         "# git config --global user.email '你的邮箱'\n"
         "# git add week1\n"
         "# git commit -m 'week1 python practice'\n"
         "# git remote add origin https://github.com/你的用户名/deep-learning-notes.git\n"
         "# git push -u origin master"),
])

days["day7"] = nb([
    md("# Day 7 · 复盘 + 休息"),
    md("## 上午：重做本周卡住的 3 道练习\n不查资料、不查记录，独立写出来才算过关。候选：\n"
       "- 词频统计前 10\n- 每列标准化\n- 余弦相似度矩阵\n- CSVReader"),
    code("# 重做开始"),
    md("## 下午：问题清单\n把本周所有『当时没真懂』的问题列出来，能查文档解决的当场解决；解决不了的留着，之后会自然打通。"),
    code("# 问题清单：\n# 1.\n# 2.\n# 3."),
    md("## 傍晚：预习\n"
       "打开 `D:\\deep-learning\\pytorch\\chapter_preliminaries\\ndarray.ipynb`，只读不跑，标出看不懂的格子。下周正式开跑。\n\n"
       "然后休息。第 2 周见。"),
])

base = r"D:\deep-learning\week1"
os.makedirs(base, exist_ok=True)
for name, nb_obj in days.items():
    path = os.path.join(base, name + ".ipynb")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb_obj, f, ensure_ascii=False, indent=1)

for fn in sorted(f for f in os.listdir(base) if f.endswith(".ipynb")):
    with open(os.path.join(base, fn), encoding="utf-8") as f:
        json.load(f)
print("written & validated:", sorted(os.listdir(base)))
