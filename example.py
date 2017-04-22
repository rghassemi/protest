from display import ThreeLineDisplay
import time

if __name__ == "__main__":
    display = ThreeLineDisplay()
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    first_line = ['Life', 'Music', 'Friends', 'Love', 'BBQ']
    second_line = ['Before', 'Instead of', '>']
    third_line = ['Politics', 'Parties', 'Greed', 'Apathy']

    display.draw_the_line(line_number=0, queue=first_line, color=RED)
    display.draw_the_line(line_number=1, queue=second_line, start_column=15, color=GREEN)
    display.draw_the_line(line_number=2, queue=third_line, start_column=15,  color=BLUE)
    display.update()

    while True:
        time.sleep(0.05)
        #display.scroll_line(0)
        #display.scroll_line(1)
        display.scroll_line(2)
