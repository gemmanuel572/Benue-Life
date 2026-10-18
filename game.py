import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Benue Life")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

x = 100
y = 250
speed = 5

wall = 20
size = 40

market = pygame.Rect(400, 100, 200, 120)

# COLORS (red, green, blue)
skin = (150, 100, 60)
shirt = (30, 80, 200)
trousers = (40, 40, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    old_x = x
    old_y = y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - speed
    if keys[pygame.K_RIGHT]:
        x = x + speed
    if keys[pygame.K_UP]:
        y = y - speed
    if keys[pygame.K_DOWN]:
        y = y + speed

    if x < wall:
        x = wall
    if x > 800 - wall - size:
        x = 800 - wall - size
    if y < wall:
        y = wall
    if y > 500 - wall - size:
        y = 500 - wall - size

    player = pygame.Rect(x, y, size, size)
    if player.colliderect(market):
        x = old_x
        y = old_y

    # DRAW THE WORLD
    screen.fill((50, 150, 50))
    pygame.draw.rect(screen, (90, 60, 30), (0, 0, 800, 500), wall)
    pygame.draw.rect(screen, (180, 120, 60), market)
    label = font.render("Market", True, (255, 255, 255))
    screen.blit(label, (market.x + 60, market.y + 50))

    # DRAW THE PERSON
    pygame.draw.rect(screen, trousers, (x + 10, y + 30, 8, 10))    # left leg
    pygame.draw.rect(screen, trousers, (x + 22, y + 30, 8, 10))    # right leg
    pygame.draw.rect(screen, shirt, (x + 10, y + 16, 20, 14))      # body
    pygame.draw.rect(screen, skin, (x + 4, y + 16, 6, 12))         # left arm
    pygame.draw.rect(screen, skin, (x + 30, y + 16, 6, 12))        # right arm
    pygame.draw.circle(screen, skin, (x + 20, y + 8), 8)           # head

    pygame.display.flip()
    clock.tick(60)

pygame.quit()