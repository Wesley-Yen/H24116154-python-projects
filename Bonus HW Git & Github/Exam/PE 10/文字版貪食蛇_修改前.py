import os
import shutil
import curses
import random

def get_terminal_size():
    # 獲取終端窗口的大小，返回列數和行數
    size = shutil.get_terminal_size((80, 20))
    return size.columns, size.lines

# 獲取終端窗口的大小
width, height = get_terminal_size()

# 初始化屏幕
stdscr = curses.initscr()
curses.curs_set(0)  # 隱藏光標
sh, sw = height, width  # 使用獲取的終端大小
w = curses.newwin(sh, sw, 0, 0)  # 創建新窗口
w.keypad(1)  # 啟用鍵盤
w.timeout(100)  # 設置延遲時間（毫秒）

# 初始化蛇的位置和設置
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],         # 蛇頭
    [snake_y, snake_x - 1],     # 蛇身
    [snake_y, snake_x - 2]      # 蛇尾
]

# 初始化普通食物的位置
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)  # 在窗口中顯示普通食物

# 初始化特殊食物的位置
special_food = [sh // 2 + 1, sw // 2 + 1]
w.addch(int(special_food[0]), int(special_food[1]), 'X')  # 在窗口中顯示特殊食物

# 初始化障礙物
obstacles = []
for _ in range(int(sh * sw * 0.05 / 5)):  # 障礙物佔5%的屏幕面積
    if random.choice([True, False]):
        y = random.randint(1, sh - 2)
        x = random.randint(1, sw - 7)
        for i in range(5):
            obstacles.append([y, x + i])
    else:
        y = random.randint(1, sh - 7)
        x = random.randint(1, sw - 2)
        for i in range(5):
            obstacles.append([y + i, x])

for obs in obstacles:
    w.addch(obs[0], obs[1], curses.ACS_CKBOARD)  # 在窗口中顯示障礙物

key = curses.KEY_RIGHT  # 初始方向向右
normal_food_eaten = 0
special_food_eaten = 0
paused = False  # 遊戲初始未暫停

while True:
    next_key = w.getch()  # 獲取下一個鍵
    if next_key == -1:
        key = key  # 沒有按鍵時保持原方向
    elif next_key == 32:  # 按空格鍵暫停/恢復
        paused = not paused
    else:
        key = next_key  # 更新方向

    if paused:
        continue  # 暫停狀態下不更新蛇的位置

    if key == curses.KEY_DOWN:
        w.timeout(50)  # 向下移動時加速
    else:
        w.timeout(100)

    head = [snake[0][0], snake[0][1]]  # 獲取蛇頭的位置

    # 根據按鍵更新蛇頭的位置
    if key == curses.KEY_DOWN:
        head[0] += 1
    if key == curses.KEY_UP:
        head[0] -= 1
    if key == curses.KEY_LEFT:
        head[1] -= 1
    if key == curses.KEY_RIGHT:
        head[1] += 1

    # 讓蛇的移動能夠穿過屏幕邊界
    head[0] = head[0] % sh
    head[1] = head[1] % sw

    # 檢查是否撞到自己或障礙物
    if head in snake or head in obstacles:
        break  # 結束遊戲

    snake.insert(0, head)  # 在蛇頭位置插入新位置

    # 檢查是否吃到普通食物
    if snake[0] == food:
        normal_food_eaten += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 2),
                random.randint(1, sw - 2)
            ]
            food = nf if nf not in snake and nf not in obstacles else None
        w.addch(food[0], food[1], curses.ACS_PI)
    elif snake[0] == special_food:  # 檢查是否吃到特殊食物
        special_food_eaten += 1
        if len(snake) > 1:
            snake.pop()  # 縮短蛇的長度
        special_food = None
        while special_food is None:
            sf = [
                random.randint(1, sh - 2),
                random.randint(1, sw - 2)
            ]
            special_food = sf if sf not in snake and sf not in obstacles else None
        w.addch(special_food[0], special_food[1], 'X')
    else:
        tail = snake.pop()  # 移除蛇尾
        w.addch(tail[0], tail[1], ' ')  # 清除蛇尾顯示

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)  # 顯示新的蛇頭

curses.endwin()  # 結束curses模式
print(f"Game Over! Normal food eaten: {normal_food_eaten}, Special food eaten: {special_food_eaten}")
print("Reason: Snake collided with itself or an obstacle.")
