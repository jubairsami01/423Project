from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

#defining a list to store the time interval globally hehe
time_interval = [1]


PI = 3.14159265359

def text(x, y, string):
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))



xone = yone = xtwo = ytwo = 0.0

def midcircle(h: float, k: float, r: float) -> None:
    """
    Implementation of midpoint circle drawing algorithm
    h, k: center coordinates
    r: radius
    """
    a = 0
    b = int(r)
    pk = 1 - int(r)
    
    while a <= b:
        # Draw 8 symmetric points
        glVertex2d(a + h, b + k)      # 2
        glVertex2d(b + h, a + k)      # 1
        glVertex2d(-a + h, b + k)     # 3
        glVertex2d(-b + h, a + k)     # 4
        glVertex2d(-b + h, -a + k)    # 5
        glVertex2d(-a + h, -b + k)    # 6
        glVertex2d(a + h, -b + k)     # 7
        glVertex2d(b + h, -a + k)     # 8
        
        if pk < 0:
            pk = pk + 2 * a + 1
        else:
            b -= 1
            pk = pk + 2 * a + 5 - 2 * b
        
        a += 1



def drawball(h: int, k: int, r: int) -> None:
    """Draw a filled ball using concentric circles"""
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    for i in range(1, r + 1):
        midcircle(h, k, i)
    glEnd()




def fillellipse(cx: int, cy: int, a: int, b: int):
    glBegin(GL_POINTS)
    for i in range(361):  # 0 to 360 inclusive
        angle = i * math.pi / 180.0
        glColor3ub(232, 190, 172)
        glVertex2f(cx + a * math.cos(angle), cy + b * math.sin(angle))
    glEnd()





def draw_filled_rectangle(x1, y1, x2, y2, color):
    glColor3ub(*color)
    glBegin(GL_POINTS)
    step = 0.5  # Smaller step size for higher density
    x = x1
    while x < x2:
        y = y1
        while y < y2:
            glVertex2f(x, y)
            y += step
        x += step
    glEnd()

def draw_filled_circle(cx, cy, radius, color):
    glColor3ub(*color)
    glBegin(GL_POINTS)
    step = 0.5  # Smaller step size for higher density
    for angle in range(360):
        rad = angle * math.pi / 180
        r = 0
        while r < radius:
            x = cx + r * math.cos(rad)
            y = cy + r * math.sin(rad)
            glVertex2f(x, y)
            r += step
    glEnd()

def batsman(x, y, flag):
    if current_player == 1:
        body_color = (0, 106, 78)  # Green
        accent_color = (218, 41, 28)  # Red
    else:
        body_color = (218, 41, 28)  # Red
        accent_color = (0, 106, 78)  # Green

    # head
    draw_filled_circle(x - 5, y + 400, 35, (232, 190, 172))

    # body
    draw_filled_rectangle(x + 20, y + 200, x + 70, y + 350, body_color)
    draw_filled_rectangle(x - 30, y + 200, x + 20, y + 350, body_color)

    # hand in shirt
    draw_filled_rectangle(x - 20, y + 280, x + 10, y + 330, body_color)

    # hand
    draw_filled_rectangle(x - 17, y + 260, x + 7, y + 280, (232, 190, 172))
    draw_filled_rectangle(x - 30, y + 200, x + 7, y + 260, (232, 190, 172))

    if flag == 0:
        # bat handle
        draw_filled_rectangle(x - 30, y + 188, x - 20, y + 198, (0, 0, 0))
        draw_filled_rectangle(x - 65, y + 228, x - 55, y + 238, (0, 0, 0))
    else:
        # bat handle
        draw_filled_rectangle(x - 45, y + 175, x - 35, y + 250, (0, 0, 0))

    # gloves
    draw_filled_rectangle(x - 50, y + 200, x - 30, y + 225, accent_color)

    # legs
    draw_filled_rectangle(x - 20, y + 140, x + 60, y + 200, accent_color)
    draw_filled_rectangle(x - 10, y + 140, x + 70, y + 200, accent_color)

    # shoes
    draw_filled_rectangle(x - 45, y, x + 5, y + 30, accent_color)
    draw_filled_rectangle(x - 25, y, x + 25, y + 30, accent_color)

    # pads
    draw_filled_rectangle(x - 30, y + 20, x + 20, y + 160, body_color)
    draw_filled_rectangle(x - 20, y + 20, x + 30, y + 160, body_color)

    # bat
    if flag == 0:
        draw_filled_rectangle(x - 153, y + 218, x - 45, y + 327, (186, 140, 99))
    else:
        draw_filled_rectangle(x - 55, y + 25, x - 25, y + 175, (186, 140, 99))





#used only glpoints for the following version of pitch:

# def draw_filled_rectangle_pitch(x1, y1, x2, y2, color):
#     glColor3ub(*color)
#     glBegin(GL_POINTS)
#     step = 2  # Smaller step size for higher density
#     x = x1
#     while x < x2:
#         y = y1
#         while y < y2:
#             glVertex2f(x, y)
#             y += step
#         x += step
#     glEnd()

#recursive approach to make it work faster:

def draw_filled_rectangle_pitch(x1, y1, x2, y2, color):
    glColor3ub(*color)
    glBegin(GL_POINTS)
    draw_rectangle_recursive(x1, y1, x2, y2)
    glEnd()

def draw_rectangle_recursive(x1, y1, x2, y2):
    # Base case: if rectangle is small enough, draw points
    if (x2 - x1) * (y2 - y1) < 2500:  # Threshold can be tuned
        step = 2  # Smaller step size for higher density
        x = x1
        while x < x2:
            y = y1 
            while y < y2:
                glVertex2f(x, y)
                y += step
            x += step
        return

    # Divide rectangle into four quadrants
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    # Recursively draw each quadrant
    draw_rectangle_recursive(x1, y1, mid_x, mid_y)         # Bottom left
    draw_rectangle_recursive(mid_x, y1, x2, mid_y)         # Bottom right  
    draw_rectangle_recursive(x1, mid_y, mid_x, y2)         # Top left
    draw_rectangle_recursive(mid_x, mid_y, x2, y2)         # Top right

def draw_tree(cx, cy):
    """Draw a tree with a trunk and leaves using GL_POINTS"""
    # Adjust the starting position to move the tree down
    trunk_height = 70
    branch_height = 20
    leaf_height = 40
    total_height = trunk_height + branch_height + leaf_height
    cy += total_height // 2

    # Draw trunk
    draw_filled_rectangle(cx - 5, cy, cx + 5, cy + trunk_height, (139, 69, 19))
    
    # Draw branches
    draw_filled_rectangle(cx - 15, cy + trunk_height - 10, cx - 5, cy + trunk_height + branch_height, (139, 69, 19))
    draw_filled_rectangle(cx + 5, cy + trunk_height - 10, cx + 15, cy + trunk_height + branch_height, (139, 69, 19))
    draw_filled_rectangle(cx - 25, cy + trunk_height, cx - 15, cy + trunk_height + branch_height + 10, (139, 69, 19))
    draw_filled_rectangle(cx + 15, cy + trunk_height, cx + 25, cy + trunk_height + branch_height + 10, (139, 69, 19))
    draw_filled_rectangle(cx - 35, cy + trunk_height + 10, cx - 25, cy + trunk_height + branch_height + 20, (139, 69, 19))
    draw_filled_rectangle(cx + 25, cy + trunk_height + 10, cx + 35, cy + trunk_height + branch_height + 20, (139, 69, 19))

    # Draw leaves
    draw_filled_circle(cx, cy + trunk_height + branch_height, 20, (34, 139, 34))
    draw_filled_circle(cx - 20, cy + trunk_height + branch_height + 10, 15, (34, 139, 34))
    draw_filled_circle(cx + 20, cy + trunk_height + branch_height + 10, 15, (34, 139, 34))
    draw_filled_circle(cx - 30, cy + trunk_height + branch_height + 20, 10, (34, 139, 34))
    draw_filled_circle(cx + 30, cy + trunk_height + branch_height + 20, 10, (34, 139, 34))
    draw_filled_circle(cx - 40, cy + trunk_height + branch_height + 30, 8, (34, 139, 34))
    draw_filled_circle(cx + 40, cy + trunk_height + branch_height + 30, 8, (34, 139, 34))
    draw_filled_circle(cx - 10, cy + trunk_height + branch_height + 40, 12, (34, 139, 34))
    draw_filled_circle(cx + 10, cy + trunk_height + branch_height + 40, 12, (34, 139, 34))

def draw_spectator(cx, cy):
    """Draw a small spectator clapping hands using GL_POINTS"""
    # Head
    draw_filled_circle(cx, cy + 20, 5, (232, 190, 172))
    
    # Body
    draw_filled_rectangle(cx - 5, cy, cx + 5, cy + 20, (0, 0, 255))
    
    # Left hand
    draw_filled_rectangle(cx - 10, cy + 10, cx - 5, cy + 15, (232, 190, 172))
    
    # Right hand
    draw_filled_rectangle(cx + 5, cy + 10, cx + 10, cy + 15, (232, 190, 172))

def draw_spectators():
    """Draw spectators near the trees"""
    spectators_positions = [
        (random.randint(30, 70), random.randint(30, 70)),  # Bottom-left corner
        (random.randint(1930, 1970), random.randint(30, 70)),  # Bottom-right corner
        (random.randint(30, 70), random.randint(1670, 1730)),  # Top-left corner
        (random.randint(1930, 1970), random.randint(1670, 1730)),  # Top-right corner
        (random.randint(30, 70), random.randint(30, 70)),  # Bottom-left corner
        (random.randint(1930, 1970), random.randint(30, 70)),  # Bottom-right corner
        (random.randint(30, 70), random.randint(1670, 1730)),  # Top-left corner
        (random.randint(1930, 1970), random.randint(1670, 1730))  # Top-right corner
    ]
    for pos in spectators_positions:
        draw_spectator(*pos)

def pitch():
    # pitch
    draw_filled_rectangle_pitch(700, 0, 1300, 1700, (205, 133, 63))

    # crease
    draw_filled_rectangle_pitch(700, 1500, 1300, 1510, (255, 255, 255))
    draw_filled_rectangle_pitch(750, 1500, 760, 1700, (255, 255, 255))
    draw_filled_rectangle_pitch(1250, 1500, 1260, 1700, (255, 255, 255))
    draw_filled_rectangle_pitch(700, 50, 1300, 60, (255, 255, 255))
    draw_filled_rectangle_pitch(750, 0, 760, 50, (255, 255, 255))
    draw_filled_rectangle_pitch(1250, 0, 1260, 50, (255, 255, 255))

    # wickets
    draw_filled_rectangle_pitch(975, 1700, 985, 1850, (255, 255, 0))
    draw_filled_rectangle_pitch(995, 1700, 1005, 1850, (255, 255, 0))
    draw_filled_rectangle_pitch(1015, 1700, 1025, 1850, (255, 255, 0))

    # Draw trees in the four corners
    draw_tree(50, 50)          # Bottom-left corner
    draw_tree(1950, 50)        # Bottom-right corner
    draw_tree(50, 1700)        # Top-left corner
    draw_tree(1950, 1700)      # Top-right corner

    # Draw spectators near the trees
    draw_spectators()



startangle = 0
endangle = 0
i = 0.0
mid = 0
speed = 0.0
cx, cy, a, b = 0, 0, 0, 0
x, y, flag = 0, 0, 0
ballposition = 0.0
side = -1.0
temp = 0
running = 0
score = 0
u = 0.0
started = 0
runcount = 0
ballcount = 0

overs = 0
balls_per_over = 6
total_balls = 0
player1_score = 0
player2_score = 0
current_player = 1

def set_overs():
    global overs, total_balls
    overs = int(input("Enter the number of overs for the match: "))
    total_balls = overs * balls_per_over

def display_winner():
    glClear(GL_COLOR_BUFFER_BIT)
    if player1_score > player2_score:
        text(950, 1000, "Player 1 Wins!")
    elif player2_score > player1_score:
        text(950, 1000, "Player 2 Wins!")
    else:
        text(950, 1000, "It's a Tie!")
    glFlush()

def info():
    str1 = "Instructions"
    text(200, 1100, str1)
    str2 = "Press left arrow to hit off side"
    text(100, 1000, str2)
    str3 = "Press right arrow to hit legside"
    text(100, 900, str3)
    str4 = "Press space bar to hit the ball"
    text(100, 800, str4)


def draw_filled_rectangle_scoreboard(x1, y1, x2, y2, color):
    glColor3ub(*color)
    glBegin(GL_POINTS)
    draw_rectangle_recursive1(x1, y1, x2, y2)
    glEnd()

def draw_rectangle_recursive1(x1, y1, x2, y2):
    # Base case: if rectangle is small enough, draw points
    if (x2 - x1) * (y2 - y1) < 2500:  # Threshold can be tuned
        step = 1  # Smaller step size for higher density
        x = x1
        while x < x2:
            y = y1 
            while y < y2:
                glVertex2f(x, y)
                y += step
            x += step
        return

    # Divide rectangle into four quadrants
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    # Recursively draw each quadrant
    draw_rectangle_recursive1(x1, y1, mid_x, mid_y)         # Bottom left
    draw_rectangle_recursive1(mid_x, y1, x2, mid_y)         # Bottom right  
    draw_rectangle_recursive1(x1, mid_y, mid_x, y2)         # Top left
    draw_rectangle_recursive1(mid_x, mid_y, x2, y2)         # Top right




#using only glpoints:
def scoreboard():
    # black background
    # black background using draw_filled_rectangle_scoreboard instead of GL_POLYGON
    draw_filled_rectangle_scoreboard(1570, 1350, 1810, 1870, (0, 0, 0))
    
    str_runs = "RUNS   " + str(runcount)
    text(1590, 1700, str_runs)
    
    str_balls = "BALLS  " + str(ballcount)
    text(1590, 1600, str_balls)

    if current_player == 1:
        str_target = "Target: N/A"
        str_player = "Player 1"
    else:
        str_target = "Target: " + str(player1_score + 1)
        str_player = "Player 2"
    text(1590, 1500, str_target)
    text(1590, 1800, str_player)
    
    str_balls_left = "Balls Left: " + str(total_balls - ballcount)
    text(1590, 1400, str_balls_left)


def scoreinfo():
    global score
    if score == 0:
        str = "Score is zero"
    elif score == 1:
        str = "Score is one"
    elif score == 2:
        str = "Score is two"
    elif score == 3:
        str = "Score is three"
    elif score == 4:
        str = "Score is four"
    elif score == 6:
        str = "Score is six"
    else:
        str = "Invalid score"
    
    text(950, 1000, str)





def loop(val):
    global i, startangle, endangle, cx, cy, a, b, running, x, y, flag, speed, ballposition

    if startangle < endangle:
        angle = i * math.pi / 180.0
        glClear(GL_COLOR_BUFFER_BIT)
        pitch()
        scoreboard()
        if running == 3:
            scoreinfo()
        info()
        batsman(x, y, flag)
        drawball(cx + a * math.cos(angle), cy + b * math.sin(angle), 13)
        ballposition = cy + b * math.sin(angle)
        glFlush()
        i += speed
        if i <= endangle:
            glutTimerFunc(time_interval[0], loop, 0)  # Reduced timer interval, frame rate enhancer
        elif running == 1:
            second_step()
        elif running == 2:
            hit()
    else:
        angle = i * math.pi / 180.0
        glClear(GL_COLOR_BUFFER_BIT)
        pitch()
        scoreboard()
        if running == 3:
            scoreinfo()
        info()
        batsman(x, y, flag)
        drawball(cx + a * math.cos(angle), cy + b * math.sin(angle), 13)
        ballposition = cy + b * math.sin(angle)
        glFlush()
        glutPostRedisplay()
        i -= speed
        if i >= endangle:
            glutTimerFunc(time_interval[0], loop, 0)  # Reduced timer interval
        elif running == 1:
            second_step()
        elif running == 2:
            hit()


def loop1(val):
    global u, running, x, y, flag, xone, xtwo, yone, ytwo, ballposition

    if u <= 1:
        glClear(GL_COLOR_BUFFER_BIT)
        pitch()
        scoreboard()
        if running == 3:
            scoreinfo()
        info()
        batsman(x, y, flag)
        drawball(xone + u * (xtwo - xone), yone + u * (ytwo - yone), 13)
        ballposition = yone + u * (ytwo - yone)
        glFlush()
        u += 0.05  # Increased step size for smoother animation
        glutTimerFunc(time_interval[0], loop1, 0)  # Reduced timer interval



def hit():
    global started, runcount, score, ballcount, running, flag, side, temp, x, y, u
    global xone, xtwo, yone, ytwo, cx, cy, a, b, startangle, endangle, i, ballposition
    global current_player, player1_score, player2_score

    runcount += score
    ballcount += 1
    running = 3
    flag = 1

    if ballcount >= total_balls:
        if current_player == 1:
            player1_score = runcount
            current_player = 2
            started = 0
            ballcount = 0
            runcount = 0
            side = -1  # Reset side
            
            def switch_to_player2():
                glClear(GL_COLOR_BUFFER_BIT)
                pitch()
                text(950, 1000, "Player 2, Press Left or Right Arrow Key to Start")
                glFlush()
                glutSpecialFunc(arrow1)
            
            # Schedule the switch to avoid state conflicts
            glutTimerFunc(1000, lambda _: switch_to_player2(), 0)
            return
        else:
            player2_score = runcount
            display_winner()
            return

    if side == -1:
        if score == 0:
            glClear(GL_COLOR_BUFFER_BIT)
            pitch()
            scoreboard()
            if running == 3:
                scoreinfo()
            info()
            batsman(x, y, flag)
            drawball(950 + temp, 1450, 13)
            ballposition = 1500
            glFlush()
        elif score < 4:
            xone = 950 + temp
            yone = 1500
            xtwo = 700 - (score * 150)
            ytwo = random.randint(500, 1000)
            u = 0
            loop1(0)
        elif score == 4:
            xone = 950 + temp
            yone = 1500
            xtwo = 0
            ytwo = random.randint(500, 1000)
            u = 0
            loop1(0)
        elif score == 6:
            cx = 950 + temp
            cy = 0
            a = 950 + temp + random.randint(0, 400)
            b = 1550
            startangle = 90
            endangle = 180
            i = startangle
            x = 950 + temp + 40
            y = 1500
            glutTimerFunc(time_interval[0], loop, 0)  # Reduced timer interval
    elif side == 1:
        if score == 0:
            glClear(GL_COLOR_BUFFER_BIT)
            pitch()
            scoreboard()
            if running == 3:
                scoreinfo()
            info()
            batsman(x, y, flag)
            drawball(950 + temp, 1450, 13)
            ballposition = 1500
            glFlush()
        elif score < 4:
            xone = 950 + temp
            yone = 1500
            xtwo = 1300 + (score * 150)
            ytwo = random.randint(500, 1000)
            u = 0
            loop1(0)
        elif score == 4:
            xone = 950 + temp
            yone = 1500
            xtwo = 2000
            ytwo = random.randint(500, 1000)
            u = 0
            loop1(0)
        elif score == 6:
            cx = 950 + temp
            cy = 0
            a = 2000 - (950 + temp) + random.randint(0, 400)
            b = 1550
            startangle = 90
            endangle = 0
            i = startangle
            x = 950 + temp + 40
            y = 1500
            glutTimerFunc(time_interval[0], loop, 0)  # Reduced timer interval




def myInit():
    glClearColor(71.0 / 256.0, 162.0 / 256.0, 13.0 / 256.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 2000.0, 0.0, 2000.0)

def second_step():
    global running, temp, cx, cy, a, b, startangle, endangle, i, x, y, flag, mid

    running = 2
    temp = random.randint(0, 99)
    if random.randint(0, 1):
        temp = -temp
        cx = 950 + temp
        cy = mid
        a = -temp
        b = 1550 - mid
        startangle = 0
        endangle = 90
        i = startangle
        x = 950 + temp + 40
        y = 1500
        flag = 0
        glutTimerFunc(time_interval[0], loop, 0)  # Reduced timer interval
    else:
        cx = 950 + temp
        cy = mid
        a = temp
        b = 1550 - mid
        startangle = 180
        endangle = 90
        i = startangle
        x = 950 + temp + 40
        y = 1500
        flag = 0
        glutTimerFunc(time_interval[0], loop, 0)  # Reduced timer interval



def cricket():
    global started, score, mid, speed, cx, cy, a, b, startangle, endangle, i, x, y, flag, ballposition, running

    started = 1
    score = 0
    random.seed(time.time())
    glClear(GL_COLOR_BUFFER_BIT)
    mid = random.randint(800, 1400)
    speed = random.randint(10, 15)   # ball throwing speed. !!!!!!!!
    cx = 950
    cy = 0
    a = 250
    b = mid
    startangle = 0
    endangle = 90
    i = startangle
    x = 1040
    y = 1500
    flag = 0
    ballposition = 0
    running = 1
    loop(0)

def arrow(key, p, q):
    global side, started

    if key == GLUT_KEY_LEFT:
        glClear(GL_COLOR_BUFFER_BIT)
        cricket()
        side = -1
        started = 1
    elif key == GLUT_KEY_RIGHT:
        glClear(GL_COLOR_BUFFER_BIT)
        cricket()
        side = 1
        started = 1

def intro():
    if started != 1:
        set_overs()
        glClear(GL_COLOR_BUFFER_BIT)
        text(950, 1000, "Press Left or Right Arrow Key to Start")
        glFlush()

#score calculation based on bat hitting position
# def keyboard(key, p, q):
#     global score, ballposition

#     if key == b' ':
#         if ballposition < 1000:
#             score = 0
#         elif ballposition < 1100:
#             score = 1
#         elif ballposition < 1200:
#             score = 2
#         elif ballposition < 1300:
#             score = 3
#         elif ballposition < 1400:
#             score = 4
#         elif ballposition < 1550:
#             score = 6

#socre calculation based on randomized probability
def keyboard(key, p, q):
    global score, ballposition

    if key == b' ':
        prob = random.random()  # Random float between 0.0 and 1.0
        if 0 < prob < 0.2:
            score = 0
        elif 0.21 < prob < 0.3:
            score = 1
        elif 0.31< prob < 0.4:
            score = 2
        elif 0.41 < prob < 0.5:
            score = 3
        elif 0.51 < prob < 0.7:
            score = 4
        else:
            score = 6


# Add this function at the module level (outside any other function)
def arrow1(key, x, y):
    global side, started
    if key == GLUT_KEY_LEFT or key == GLUT_KEY_RIGHT:
        glClear(GL_COLOR_BUFFER_BIT)
        side = -1 if key == GLUT_KEY_LEFT else 1
        started = 1
        cricket()  # Start the game for player 2



def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # glutInitWindowSize(glutGet(GLUT_SCREEN_WIDTH), glutGet(GLUT_SCREEN_HEIGHT))   #change window size
    glutInitWindowSize(1280, 720)   #change window size
    glutInitWindowPosition(200, 0)
    glutCreateWindow(b"cricket")
    glutSpecialFunc(arrow)
    glutKeyboardFunc(keyboard)
    myInit()
    glutDisplayFunc(intro)
    glutMainLoop()

if __name__ == "__main__":
    main()
