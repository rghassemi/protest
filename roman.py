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

    while True:
        # First one ###############################################
        first_line = ['1 MarAlago']
        second_line = ['Trip=$3.6M']
        third_line = ['= 18 PhDs', '= 72 Jobs', '= 24 Homes', '=280k Meals', '= 1 Lab']
        reset_all_lines()
        cycle = third(third_line)
        first_cycle = third(first_line)
        text = cycle.next()
        display.draw_the_line(line_number=0, queue=first_line, color=RED)
        display.draw_the_line(line_number=1, queue=second_line, color=GREEN)
        display.draw_the_line(line_number=2, text=text,  color=BLUE)
        display.update()

        for i in range(8):
            time.sleep(1)
            #display.scroll_line(0)
            #display.scroll_line(1)
            #display.scroll_line(2)
            display.clear_line(2)
            display.reset_line(2)
            display.draw_the_line(line_number=2, text=cycle.next(),  color=BLUE)

        reset_all_lines()

        # Second one ###############################################
        first_line = ['GOVERNMENT']
        second_line = ['+ SCIENCE =']
        third_line = [('Safe Roads', BLUE),
                      ('Fit Kids', BLUE),
                      ('Clear Skies', BLUE),
                      ('Safer Cars', BLUE),
                      ('Progress', BLUE),
                      ('Competition', BLUE),
                      ('Inspiration', BLUE),
                      ('GPS', BLUE)]

        cycle = third(third_line)
        (text, color) = cycle.next()
        display.draw_the_line(line_number=0, queue=first_line, color=RED)
        display.draw_the_line(line_number=1, queue=second_line, start_column=0, color=GREEN)
        display.draw_the_line(line_number=2, text=text, start_column=0,  color=color)
        display.update()

        for i in range(8):

            
            time.sleep(1)
            display.clear_line(2)
            display.reset_line(2)
            (text, color) = cycle.next()
            print text, color
            display.draw_the_line(line_number=2, text=text, start_column=0,  color=color)
        # Third one ###############################################
        reset_all_lines()
        first_line = ['Country', 'Science', 'Life']
        second_line = ['Before']
        third_line = ['Party']

        cycle = third(first_line)
        display.draw_the_line(line_number=0, text=cycle.next(), color=RED)
        display.draw_the_line(line_number=1, queue=second_line, start_column=0, color=GREEN)
        display.draw_the_line(line_number=2, queue=third_line, start_column=0,  color=color)
        display.update()

        for i in range(len(first_line)):
            display.clear_line(0)
            display.reset_line(0)
            display.draw_the_line(line_number=0, text=cycle.next(), color=RED)

            time.sleep(1)




