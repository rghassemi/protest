from display import ThreeLineDisplay
import time

if __name__ == "__main__":
    display = ThreeLineDisplay()
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    first_line = ['GOVERNMENT']
    second_line = ['+ SCIENCE =']
    third_line = [('Safer Roads', RED),
                  ('Healthier Kids', GREEN),
                  ('Stronger Babies', BLUE),
                  ('Clearer Skies', RED),
                  ('The Bald Eagle Thrives', GREEN),
                  ('Goodbye, Acid Rain', BLUE),
                  ('Ozone Layer Remains', RED),
                  ('Better Weather Prediction', GREEN),
                  ('Earthquake Safety', BLUE),
                  ('Fire Prevention', RED),
                  ('Treating Cancer', GREEN),
                  ('The Internet', BLUE),
                  ('GPS', RED),
                  ('Tang', GREEN),
                  ('Less Lead Poisoning', BLUE)]
    index=-1
    def third():
        index = 0
        while True:
            yield third_line[index % len(third_line)]
            index += 1

    cycle = third()
    (text, color) = cycle.next()
    display.draw_the_line(line_number=0, queue=first_line, color=RED)
    display.draw_the_line(line_number=1, queue=second_line, start_column=0, color=GREEN)
    display.draw_the_line(line_number=2, queue=text, start_column=0,  color=color)
    display.update()
    cycle = third()

    while True:
        time.sleep(1)
        #display.scroll_line(0)
        #display.scroll_line(1)
        #display.scroll_line(2)
        display.clear_line(2)
        (text, color) = cycle.next()
        print text, color
        display.draw_the_line(line_number=2, text=text, start_column=0,  color=color)


