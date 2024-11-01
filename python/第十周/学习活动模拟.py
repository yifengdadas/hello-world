import threading
import time
import random

class Student(threading.Thread):
    def __init__(self, name, task):
        super().__init__()
        self.name = name
        self.task = task
    def run(self):
        # 模拟任务耗时
        task_duration = random.randint(1, 5)
        print(f"学生 {self.name} 开始任务 {self.task}")
        time.sleep(task_duration)
        print(f"学生 {self.name} 完成任务 {self.task}，耗时 {task_duration} 秒")
# 创建学生线程列表
students = [
    Student("Alice", "数学作业"),
    Student("Bob", "物理实验"),
    Student("Charlie", "编程练习"),
    Student("Diana", "历史报告"),
    Student("Evan", "美术创作"),
]
# 启动所有学生线程
for student in students:
    student.start()
# 等待所有学生线程完成
for student in students:
    student.join()
# 打印所有线程的状态（尽管此时它们都应该已经完成了）
for student in students:
    print(f"学生线程 {student.name} 的ID是 {student.ident}，是否存活: {student.is_alive()}")