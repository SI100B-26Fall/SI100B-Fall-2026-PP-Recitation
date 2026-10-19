Recitation 4 Supplement 配套文件

解压后，在 VS Code 中打开 examples 文件夹。

debug_functions.py  断点调试示例；第 12 行设置断点。
sum_input.py        从一行输入读取整数并求和。
sample.in           示例输入：4 6 2。
expected.txt        预期输出：12。
run.log             cat、grep 和管道演示所用的示例日志。

在 examples 目录下运行（Bash）：
python3 debug_functions.py
python3 sum_input.py < sample.in > actual.txt
diff -u expected.txt actual.txt

actual.txt 由运行命令生成。debug_functions.py 最后一行输出：3x5 + 4x7 = 43。
