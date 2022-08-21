from turtle import Turtle
from brick import Brick

# TODO build a wall that is 13 by 8
# The wall has 3 rows of two
# When


class Wall():

    def __init__(self, screen_width):
        self.bricks = []
        self.bricks_per_row = 13
        self.segment_width = int(screen_width / self.bricks_per_row)
        self.bricks_width = int(self.segment_width / 20)
        self.start_position = int(screen_width / 2) - int(self.segment_width / 2)
        self.brick_bin = (screen_width + 100, 0)
        self.bin_count = 0

    def build_board(self):
        levels = [{
            'y_pos': 20,
            'color': 'green',
            'value': 1,
        }, {
            'y_pos': 45,
            'color': 'green',
            'value': 1,
        }, {
            'y_pos': 70,
            'color': 'yellow',
            'value': 3,
        }, {
            'y_pos': 95,
            'color': 'yellow',
            'value': 3,
        }, {
            'y_pos': 120,
            'color': 'orange',
            'value': 5,
        }, {
            'y_pos': 145,
            'color': 'orange',
            'value': 5,
        }, {
            'y_pos': 170,
            'color': 'red',
            'value': 7,
        }, {
            'y_pos': 195,
            'color': 'red',
            'value': 7,
        }]
        for level in levels:
            for x in range(self.bricks_per_row):
                x_pos = x * self.segment_width - self.start_position
                position = (x_pos, level['y_pos'])
                self.add_brick(color=level['color'], value=level['value'], position=position)

    def add_brick(self, color, value, position):
        new_brick = Brick(color=color, value=value, position=position)
        self.bricks.append(new_brick)

    def destroy_brick(self, index):
        des_brick = self.bricks[index]
        des_brick.reset()
        des_brick.goto(self.brick_bin)
        self.bin_count += 1
        print("delete called from wall.")

    def all_bricks_destroyed(self):
        result = False
        if self.bin_count >= 104:
            result = True
        return result





