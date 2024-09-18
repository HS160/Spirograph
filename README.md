# Spirograph Project

A Python-based Spirograph visualization using the turtle graphics library. This project creates an artistic representation of a spirograph, drawing colorful patterns with two turtles moving in opposite directions.

## Creator

HS160

## Features

- Generates a spirograph pattern with two turtles
- Uses random RGB colors for each circle
- Creates a visually appealing design
- Customizable number of iterations, circle size, and rotation angle

## Requirements

- Python 3.x
- turtle module (typically comes pre-installed with Python)

## How to Run

1. Save the code in a file named `spirograph.py`
2. Open a terminal or command prompt
3. Navigate to the directory containing the file
4. Run the command: `python spirograph.py`

## Customization

You can easily customize the Spirograph by modifying the following parameters in the code:

- `t.pensize(2)` and `t1.pensize(2)`: Adjust the number to change the line thickness
- `t.speed('fastest')` and `t1.speed('fastest')`: Change the drawing speed (e.g., 'slow', 'normal', 'fast')
- `range(36)`: Modify the range to increase or decrease the number of iterations
- `t.circle(100)` and `t1.circle(100)`: Change the number to adjust the circle size
- `t.left(20)` and `t1.right(20)`: Modify the angle to change the rotation after each circle

## How It Works

1. The program sets up the screen and creates two turtle objects.
2. It defines a function `random_color()` to generate random RGB colors.
3. The program then enters a loop that runs 36 times, creating a full spirograph:
   - For each iteration, it sets a random color for both turtles
   - Both turtles draw a circle with a radius of 100 units
   - After each circle, one turtle rotates 20 degrees left, and the other 20 degrees right
4. This process creates two interwoven spirograph patterns
5. The program waits for a click on the screen to exit

## Extending the Project

Here are some ideas to extend the functionality of your Spirograph project:

1. Add user input for the number of iterations, circle size, or rotation angle
2. Implement different shapes instead of circles (e.g., squares, triangles)
3. Create a GUI to adjust parameters in real-time
4. Add a feature to save the generated artwork as an image file

Feel free to experiment and make the project your own!

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
