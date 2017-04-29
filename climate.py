from display import ThreeLineDisplay
import time

if __name__ == "__main__":
    display = ThreeLineDisplay()
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)




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
        time.sleep(10)

        reset_all_lines()
        display.draw_the_line(line_number=0, text="Make Earth", color=YELLOW)
        display.draw_the_line(line_number=1, text="** Green **", color=GREEN)
        display.draw_the_line(line_number=2, text="!! Again !!",  color=(255,0,255))
        display.update()
        time.sleep(10)
