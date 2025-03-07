import pygame
import random
import math
import sys

# 初始化pygame
pygame.init()

# 设置屏幕大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("抽象礼物")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# 设置字体
font = pygame.font.Font(r"D:\peek\美人の字.ttf", 62)

# 烟花粒子类
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)  # 随机角度
        self.speed = random.uniform(3, 10)  # 随机速度
        self.size = random.randint(2, 4)  # 随机大小
        self.lifetime = random.randint(20, 40)  # 随机生命周期
        self.age = 0

    def move(self):
        # 根据角度和速度移动粒子
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.age += 2

    def is_alive(self):
        return self.age < self.lifetime

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# 烟花类
class Firework:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = height  # 从屏幕底部开始
        self.color = random.choice(COLORS)
        self.particles = []
        self.exploded = False

    def explode(self):
        # 生成多个粒子
        for _ in range(100):
            self.particles.append(Particle(self.x, self.y, self.color))
        self.exploded = True

    def update(self):
        if not self.exploded:
            self.y -= 5  # 烟花上升
            if self.y <= random.randint(100, 300):  # 随机高度爆炸
                self.explode()
        else:
            # 更新粒子
            for particle in self.particles:
                particle.move()

    def is_alive(self):
        if not self.exploded:
            return True
        return any(particle.is_alive() for particle in self.particles)

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        else:
            for particle in self.particles:
                particle.draw()

# 主循环
clock = pygame.time.Clock()
fireworks = []
color_index = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清屏
    screen.fill(BLACK)

    # 添加新的烟花
    if random.randint(0, 20) == 0:  # 控制烟花生成频率
        fireworks.append(Firework())

    # 更新和绘制烟花
    for firework in fireworks:
        firework.update()
        firework.draw()

    # 移除已经结束的烟花
    fireworks = [firework for firework in fireworks if firework.is_alive()]

    # 绘制生日祝福文字
    text = font.render("Happy Birthday !黄心悦", True, COLORS[color_index])
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

    # 更新颜色索引
    color_index = (color_index + 1) % len(COLORS)

    # 更新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出pygame
pygame.quit()
sys.exit()