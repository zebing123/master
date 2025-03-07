import pygame
import random
import math

# 初始化pygame
pygame.init()

# 设置屏幕尺寸
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('黄心悦生日快乐')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 105, 180), (255, 165, 0), (255, 20, 147)]

# 定义烟花粒子类
class Firework:
    def __init__(self, x, y, color, text_points=None):
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.num_particles = random.randint(50, 100)
        self.text_points = text_points  # 文字点集合
        self.create_particles()

    def create_particles(self):

            # 否则创建普通的烟花粒子
            for _ in range(self.num_particles):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(2, 5)
                dx = math.cos(angle) * speed
                dy = math.sin(angle) * speed
                size = random.randint(2, 4)
                self.particles.append([self.x, self.y, dx, dy, size])

    def update(self):
        for particle in self.particles:
            particle[0] += particle[2]
            particle[1] += particle[3]
            particle[4] *= 0.98  # 粒子逐渐减小
        self.particles = [p for p in self.particles if p[4] > 0.5]  # 过滤掉消失的粒子

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, self.color, (int(particle[0]), int(particle[1])), int(particle[4]))

# 将文字转化为点阵
def get_text_points(text, font, color=WHITE):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # 文字居中
    points = []
    for x in range(text_rect.width):
        for y in range(text_rect.height):
            if text_surface.get_at((x, y))[3] != 0:  # 非透明像素
                points.append((x + text_rect.left, y + text_rect.top))
    return points

# 绘制文字
font = pygame.font.Font(r"D:\peek\美人の字.ttf", 62)
text = "黄心悦生快"
text_points = get_text_points(text, font)

# 主程序
def main():
    clock = pygame.time.Clock()
    fireworks = []
    running = True
    while running:
        screen.fill(BLACK)

        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 随机产生烟花并让其显示文字
        if random.random() < 0.05:
            x = random.randint(100, WIDTH - 100)
            y = random.randint(100, HEIGHT // 2)
            color = random.choice(COLORS)
            fireworks.append(Firework(x, y, color, text_points))

        # 更新和绘制烟花
        for firework in fireworks[:]:
            firework.update()
            firework.draw(screen)
            if len(firework.particles) == 0:
                fireworks.remove(firework)

        # 绘制文字
        screen.blit(font.render(text, True, WHITE), (WIDTH // 2 - font.size(text)[0] // 2, HEIGHT // 2 - font.size(text)[1] // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
