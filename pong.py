import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

paddle_width = 20
paddle_height = 100
paddle_speed = 5
left_paddle = pygame.Rect(50, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
right_paddle = pygame.Rect(screen_width - 50 - paddle_width, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
ball_size = 20
ball_speed = [5, 5]
ball = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)

game_running = True
clock = pygame.time.Clock()
while game_running:
    # Limit the frame rate to 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Update the game logic
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    # Detect collisions and update ball direction
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed[1] = -ball_speed[1]
    if ball.left <= left_paddle.right and ball.bottom >= left_paddle.top and ball.top <= left_paddle.bottom:
        ball_speed[0] = -ball_speed[0]
    if ball.right >= right_paddle.left and ball.bottom >= right_paddle.top and ball.top <= right_paddle.bottom:
        ball_speed[0] = -ball_speed[0]
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < screen_height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < screen_height:
        right_paddle.y += paddle_speed

    # Draw the game elements
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.display.flip()

pygame.quit()
