import pygame
from sys import exit

def display_score():
    time = int(pygame.time.get_ticks() * 0.001) - start_time
    score_surf = test_font.render(f"Score: {time}", True, "purple")
    score_reft = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_reft)
    return time

pygame.init()
screen_dimensions = (800, 400)
screen = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("very cool jumber game jeaaaahhhhhhhhhhh")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

# Ground
test_surface_dimensions = (800, 100)
test_surface = pygame.Surface(test_surface_dimensions)
test_surface.fill("darkgreen")

# Sky
sky_surface_dimensions = (800, 400)
sky_surface = pygame.Surface(sky_surface_dimensions)
sky_surface.fill("lightblue")

# Text
# text_surface = test_font.render("helo world", False, "#231b36")
# text_rect = text_surface.get_rect(center = (screen_dimensions[0] / 2, screen_dimensions[1] / 2))

# Little shit
snail_dimensions = (50, 50)
snail_surface = pygame.Surface(snail_dimensions)
snail_surface.fill("orange")

snail_x_pos = 600
snail_y_pos = 300

snail_speed = 4

snail_rect = snail_surface.get_rect(midbottom = (600, 300))

# Health bar
# health = 100
# bar_dimensions = (health * 4, 1)
# bar_surface = pygame.Surface(bar_dimensions)
# bar_surface.fill("red")

# Player
player_dimensions = (50, 150)
player_surface = pygame.Surface(player_dimensions)
player_surface.fill("blue")
player_x_pos = 200
player_speed = 5

player_rect = player_surface.get_rect(midbottom = (player_x_pos, 300))
player_grav = 0

player_scaled = pygame.transform.scale(player_surface, (20, 50))
player_menu_rect = player_scaled.get_rect(center = (screen_dimensions[0] / 2, screen_dimensions[1] / 2))

# Main Menu Text
menu_text = test_font.render("Press SPACE to start!", True, "#815cde")
menu_text_rect = menu_text.get_rect(center = (screen_dimensions[0] / 2, 350))

game_title = test_font.render("Very cool runner jumber gameaa ahhhhhh", True, "#815cde")
game_title_rect = game_title.get_rect(center = (screen_dimensions[0] / 2, 100))

# Main Update
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_grav = -10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_grav = -13
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() * 0.001)
                snail_speed = 4

    if game_active:

        # bar_dimensions = (health * 4, 10)
        # bar_surface = pygame.Surface(bar_dimensions)
        # bar_surface.fill("red")

        screen.blit(sky_surface, (0, 0))
        screen.blit(test_surface ,((screen_dimensions[0] / 2) - (test_surface_dimensions[0] / 2), 300))
        # pygame.draw.rect(screen, "#815cde", text_rect)
        # pygame.draw.rect(screen, "#815cde", text_rect, 10)
        # pygame.draw.line(screen, "red", (0, 0), pygame.mouse.get_pos())
        # pygame.draw.ellipse(screen, "brown", pygame.Rect(50, 200, 100, 100))
        # screen.blit(text_surface, text_rect)
        snail_rect.x -= snail_speed
        if snail_rect.right <= 0:
            snail_rect.left = 800
            snail_speed += 1
            
        # snail_rect.right += snail_x_speed
        # snail_rect.bottom += snail_y_speed +1
        # if snail_rect.left <= 0 or snail_rect.right >= screen_dimensions[0] - snail_dimensions[0]:
        #     snail_x_speed *= -1
        #     # health -= 10
        # if snail_rect.top <= 0 or snail_rect.bottom >= screen_dimensions[1] - snail_dimensions[1]:
        #     snail_y_speed *= -1
        #     # health -= 10
        screen.blit(snail_surface, snail_rect)
        # player_rect.x += player_speed
        # if player_rect.colliderect(snail_rect):
        #     player_speed *= -1
        #     player_rect.x += -1
        # if player_rect.x <= 0 or player_rect.x >= screen_dimensions[0]:
        #     player_rect.x += 1
        #     player_speed *= -1

        # Player
        player_grav += 0.5
        player_rect.y += player_grav
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        # screen.blit(bar_surface, (20, 20))

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

        score = display_score()

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())

    else:
        screen.fill("#231b36")
        screen.blit(player_scaled, player_menu_rect)

        score_message = test_font.render(f"Your score: {score}", True, "#815cde")
        score_message_rect = score_message.get_rect(center = (screen_dimensions[0] / 2, 350))
        screen.blit(game_title, game_title_rect)

        if score == 0:
            screen.blit(menu_text, menu_text_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)