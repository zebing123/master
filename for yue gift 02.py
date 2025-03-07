import pygame
import random
import math

# 初始化pygame
pygame.init()

# 设置屏幕尺寸
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('黄心悦生日快乐')

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 105, 180), (255, 165, 0), (255, 20, 147)]

# 定义烟花粒子类
class Firework:
    def __init__(self, x, y, color, shape='heart'):
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.particles = []
        self.num_particles = random.randint(100, 200)  #调整粒子数量
        self.create_particles()

    def create_particles(self):
        for _ in range(self.num_particles):
            if self.shape == 'heart':
                # 使用爱心形状的轨迹
                angle = random.uniform(0, 2 * math.pi)
                r = math.sin(angle) - 1
                speed = random.uniform(4, 9)
                dx = r * math.cos(angle) * speed
                dy = r * math.sin(angle) * speed
            elif self.shape == 'cake':
                # 使用圆形轨迹
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(5, 9)
                dx = math.cos(angle) * speed
                dy = math.sin(angle) * speed
            else:
                # 默认使用随机的角度和速度
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

# 绘制文字
font = pygame.font.Font(r"D:\peek\美人の字.ttf", 48)
text = font.render("黄心悦生日快乐", True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

# 主程序
def main():
    clock = pygame.time.Clock()
    fireworks = []
    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(text, text_rect)  # 显示文字

        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 随机产生烟花
        if random.random() < 0.05:
            x = random.randint(100, WIDTH - 100)
            y = random.randint(100, HEIGHT // 2)
            color = random.choice(COLORS)
            shape = random.choice(['heart', 'cake'])  # 随机选择形状
            fireworks.append(Firework(x, y, color, shape))

        # 更新和绘制烟花
        for firework in fireworks[:]:
            firework.update()
            firework.draw(screen)
            if len(firework.particles) == 0:
                fireworks.remove(firework)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
