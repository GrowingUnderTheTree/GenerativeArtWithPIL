import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()


def nft():
    print(xd)
xd = random.randint(800, 2969)
gg = random.randint(895, 2737)
image = Image.new('RGB', (xd, gg))
width, height = image.size

number_of_squares = random.randint(10, 650)
number_of_lines = random.randint(27, 913)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    a = random.randint(69, 164)
    b = random.randint(87, 135)
    x = random.randint(0, width)
    y = random.randint(0, height)
    c = random.randint(10, 15)

    rectangle_shape = [
        (x, y),
        (x + a, y + b)]
    circle_shape = [
        (x, y),
        (x + a, y + b)]
    line_shape = [
        (x, y),
        (x + a, y + b)]
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(8, 255),
            random.randint(76, 255)
        )
    )
    draw_image.ellipse(
        circle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(8, 255),
            random.randint(76, 255)
        )
    )
    draw_image.line(
        line_shape,
        fill=(
            random.randint(0, 255),
            random.randint(8, 255),
            random.randint(76, 255)
        ),
        width=c
    )

for i in range(number_of_lines):
    a = random.randint(69, 164)
    b = random.randint(87, 135)
    x = random.randint(0, width)
    y = random.randint(0, height)
    c = random.randint(10, 15)

    line_shape = [
        (x, y),
        (x + a, y + b)]
    draw_image.line(
        line_shape,
        fill=(
            random.randint(0, 255),
            random.randint(8, 255),
            random.randint(76, 255)
        ),
        width=c
    )

print(f'Processing run_id: {run_id}')
image.show("bapakkau hijau")
#image.save(f'{run_id}.png')
