# -*- coding: utf-8 -*-
"""
我的第一个 Python 程序
------------------------------------
用法：
  1. 在 VS Code 里打开本文件
  2. 点右上角的 ▶ 三角形按钮运行
  3. 看下方「终端」里的输出

想做实验？随便改改下面的数字和文字，再运行一次。
"""

import math

# ========== 1. 最基础的输出 ==========
print("你好，Python！")
print("=" * 45)

# ========== 2. 变量与计算 ==========
名字 = "小明"
年龄 = 18
身高 = 1.75

print(f"{名字}今年 {年龄} 岁，身高 {身高} 米")
print(f"他的 BMI 指数是 {年龄 and 65 / 身高 ** 2:.1f}")
print("圆周率保留两位：", round(math.pi, 2))
print()

# ========== 3. 判断与循环 ==========
分数 = 87
if 分数 >= 90:
    等级 = "优秀"
elif 分数 >= 80:
    等级 = "良好"
else:
    等级 = "继续加油"
print(f"考了 {分数} 分，等级：{等级}")

print("1 到 5 的平方：", [i ** 2 for i in range(1, 6)])
print()

# ========== 4. 定义一个函数 ==========
def 打招呼(姓名):
    """一个最简单的函数"""
    return f"嗨，{姓名}！欢迎学习 Python。"

print(打招呼("小红"))
print(打招呼(名字))
print()

# ========== 5. 用第三方库画一张图 ==========
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

月份 = ["1月", "2月", "3月", "4月", "5月", "6月"]
销量 = [120, 155, 98, 187, 210, 176]

plt.figure(figsize=(7, 4))
plt.plot(月份, 销量, marker="o", linewidth=2, color="#2E86DE", label="销量")
plt.bar(月份, 销量, alpha=0.25, color="#54A0FF")
plt.title("上半年销量走势")
plt.xlabel("月份")
plt.ylabel("销量（件）")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()

输出图片 = r"C:\Users\yianb\Desktop\销量图.png"
plt.savefig(输出图片, dpi=130)
print(f"图表已保存到：{输出图片}")
print("（运行完去桌面看看这张图）")
print()

# ========== 6. 用 pandas 处理表格 ==========
import pandas as pd

数据 = pd.DataFrame({
    "月份": 月份,
    "销量": 销量,
    "成本": [70, 88, 60, 105, 120, 99],
})
数据["利润"] = 数据["销量"] - 数据["成本"]

print("上半年经营数据：")
print(数据.to_string(index=False))
print()
print(f"总销量：{数据['销量'].sum()} 件")
print(f"总利润：{数据['利润'].sum()} 元")
print(f"最赚钱的月份：{数据.loc[数据['利润'].idxmax(), '月份']}")
print()
print("全部完成，环境一切正常！")
