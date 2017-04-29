from display import ThreeLineDisplay
import time

if __name__ == "__main__":
    display = ThreeLineDisplay()
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)



    WAIT_TIME = 2

    def third(line):
        index = 0
        while True:
            yield line[index % len(line)]
            index += 1


    def reset_all_lines():
        for i in [0, 1, 2]:
            display.reset_line(i)
            display.clear_line(i)
    YELLOW = (255, 255, 0)
    PINK = (255, 0, 255)


    # Compassionate
    # Care
    # Love
    while True:

        # First one ###############################################
        #first_line = ['1 MarAlago']
        #second_line = ['Trip=$3.6M']
        #third_line = ['= 18 PhDs', '= 72 Jobs', '= 24 Homes', '=280k Meals', '= 1 Lab']
        #reset_all_lines()
        #cycle = third(third_line)
        #first_cycle = third(first_line)
        #text = cycle.next()
        reset_all_lines()
        display.draw_the_line(line_number=0, text="Make Earth", color=GREEN)
        display.draw_the_line(line_number=1, text="** Cool **", color=(255,255,0))
        display.draw_the_line(line_number=2, text="!! Again !!",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="Make Earth", color=YELLOW)
        display.draw_the_line(line_number=1, text="** Green **", color=GREEN)
        display.draw_the_line(line_number=2, text="!! Again !!",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="   Make", color=YELLOW)
        display.draw_the_line(line_number=1, text="  America", color=GREEN)
        display.draw_the_line(line_number=2, text="Smart Again",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="   Make", color=YELLOW)
        display.draw_the_line(line_number=1, text="  America", color=GREEN)
        display.draw_the_line(line_number=2, text="Love  Again",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="   Make", color=YELLOW)
        display.draw_the_line(line_number=1, text="  America", color=GREEN)
        display.draw_the_line(line_number=2, text="Care  Again",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="   Make", color=YELLOW)
        display.draw_the_line(line_number=1, text="  America", color=GREEN)
        display.draw_the_line(line_number=2, text="Think Again",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="All Species", color=YELLOW)
        display.draw_the_line(line_number=1, text="    Are    ", color=GREEN)
        display.draw_the_line(line_number=2, text="Endangered",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="  Ice Age", color=YELLOW)
        display.draw_the_line(line_number=1, text="  to 1850", color=GREEN)
        display.draw_the_line(line_number=2, text="  4\xb0 rise",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="   1850", color=YELLOW)
        display.draw_the_line(line_number=1, text="  to 2017", color=GREEN)
        display.draw_the_line(line_number=2, text="  2\xb0 rise",  color=(255,0,255))
        display.update()
        time.sleep(WAIT_TIME)
