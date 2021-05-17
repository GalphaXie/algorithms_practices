"""
场景:
1. 模拟一个学生排队使用老旧打印机的场景, 模拟计算出打印机在不同的打印速度下, 单位时间内不同学生的打印任务完成的情况(或者任务超时情况).
    1. 打印机的速度有两种:
        1.1 高分辨率(高质量): 5页/分钟
        1.2 低分辨率(低质量): 10页/分钟
    2. 给定1h内, 实验室都大约10个学生, 他们在这一小时内最多打印2次, 并且打印的页数从 1-20 不等;
2. 问题:
    1. 如何确定采用那种打印速度? (5页/分钟 or 10页/分钟)
    2. 学生平均多久拿到打印的材料(等价于 打印任务 在队列中的 平均时间)?
    3. 场景条件变化, 模拟方案的结论如何调整?
        2.1 周末学生愿意等待更长的时间.
        2.2 实验室人数增加到20个, 会怎么样?
        2.3 如果页数变少了怎么样?
3. 解答:
    1. 定义三个类: Printer、Task、PrintQueue
    2. 利用概率学的知识:
        2.1 学生打印页数1-20, 假设每种页数出现的概率情况相等, 那么真实的一次打印任务打印页数可以通过 random(1, 21) 随机模拟;
        2.2 假设10个学生1h内每个人都打印了2次, 那么一小时内打印任务是 20次, 也就是说 每 (1 * 60 * 60) / 20 = 180秒/次, 即每180秒出现一次任务;
        2.3 即每秒出现打印任务的概率是 1/180, 可以通过 random(1, 181)来模拟, 如果随机数的值是180就认为有一个任务被创建, 其实想了想随机数可以是1-180的任意值, 它们出现概率相等;
        2.4 要理解: 可能某一秒出现多个任务, 也可能很长一段时间都没有一个任务;
4. 模拟过程:
    1. 创建一个打印队列;
"""
import random
from pythonds import Queue


class Printer:
    def __init__(self, ppm: int) -> None:
        self.pagerate = ppm  # 打印速率(unit: pages/min)
        self.current_task = None
        self.time_remaining = 0  # 当前任务剩余时间

    def tick(self):
        """时钟单位的概念"""
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def is_busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next_task(self, new_task: "Task"):
        self.current_task = new_task
        self.time_remaining = new_task.page / self.pagerate * 60  # unit: 秒


class Task:
    def __init__(self, timestamp: int) -> None:
        self.pages = random.randint(1, 20)  # 等价于 random.randrange(1, 21)
        self.timestamp = timestamp  # 记录任务被创建并加入队列的时间, 用于计算在队列中的等待时间

    def get_timestamp(self) -> int:
        return self.timestamp

    @property
    def page(self) -> int:
        return self.pages

    def wait_time(self, current_time: int) -> int:
        """任务在队列中等待时间 = 任务被从队列取出交给打印机执行的时间 - 任务被创建的时间"""
        return current_time - self.timestamp


class PrintQueue(Queue):
    pass


def new_print_task() -> None:
    """
    模拟当下时间tick中是否有任务
    """
    n = random.randint(1, 180)

    if n == 180:
        return True
    return False


def simulating(sum_seconds: int, pages_per_minute: int) -> None:
    """
    params:
        sum_seconds: 总时长;
        pages_per_minute: 打印速率
    """

    lab_printer = Printer(pages_per_minute)
    print_queue = PrintQueue()
    waiting_times = []  # 用于后序记录 平均等待时间

    for current_second in range(sum_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.is_busy()) and (not print_queue.is_empty()):
            next_task: Task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next_task(next_task)

        lab_printer.tick()

    average_wait_time = sum(waiting_times) / len(waiting_times)
    print(f"Average Wait {average_wait_time: 6.2f} secs {print_queue.size: 3d} tasks remaining.")


if __name__ == '__main__':
    # 模拟1h内打印速率为 5pages/min 的情况:
    for i in range(10):
        simulating(1 * 60 * 60, 5)

    # 模拟1h内打印速率为 10pages/min 的情况:
    for i in range(10):
        simulating(3600, 10)
