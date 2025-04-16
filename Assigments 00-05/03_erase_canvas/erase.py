from graphics import Canvas
import time

# Canvas size
WIDTH = 400
HEIGHT = 400

# Cell/grid settings
CELL_SIZE = 40
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

def main():
    canvas = Canvas(WIDTH, HEIGHT)
    
    # Store all cell rectangles
    cells = []
    for row in range(ROWS):
        row_cells = []
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            rect = canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, 'blue')
            row_cells.append(rect)
        cells.append(row_cells)

    # Initial position of eraser
    eraser = canvas.create_rectangle(0, 0, CELL_SIZE, CELL_SIZE, 'gray')

    while True:
        if canvas.get_mouse_pressed():
            x, y = canvas.get_mouse_x(), canvas.get_mouse_y()
            eraser_x = x - CELL_SIZE // 2
            eraser_y = y - CELL_SIZE // 2

            canvas.moveto(eraser, eraser_x, eraser_y)

            # Collision detection: check which cells overlap
            for row in range(ROWS):
                for col in range(COLS):
                    cell_x = col * CELL_SIZE
                    cell_y = row * CELL_SIZE
                    if (eraser_x < cell_x + CELL_SIZE and
                        eraser_x + CELL_SIZE > cell_x and
                        eraser_y < cell_y + CELL_SIZE and
                        eraser_y + CELL_SIZE > cell_y):
                        canvas.set_color(cells[row][col], 'white')

        canvas.update()
        time.sleep(0.01)

main()
