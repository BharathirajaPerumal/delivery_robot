class delivery_robot(object):

    left_rotation = {
        'N' : 'W',
        'E' : 'N',
        'W' : 'S',
        'S' : 'E'
    }

    right_rotation = {
        'N' : 'E',
        'E' : 'S',
        'W' : 'N',
        'S' : 'W'
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y = self.y + 1
        elif self.direction == 'E':
            self.x = self.x + 1
        elif self.direction == 'W':
            self.x = self.x - 1
        elif self.direction == 'S':
            self.y = self.y - 1

    def rotate(self,orientation):
        if orientation == 'L':
            self.direction = self.left_rotation[self.direction]
        else:
            self.direction = self.right_rotation[self.direction]

    def __str__(self):
        return '%d %d %c' % (self.x, self.y, self.direction)

class Plateau(object):
    def __init__(self, plateau_size):
        self.plateau_size = plateau_size

    def set_delivery_robot(self, delivery_robot):
        self.delivery_robot = delivery_robot

    def move_delivery_robot(self, moves):
        for move in moves:
            if move == 'L' or move == 'R':
                self.delivery_robot.rotate(move)
            else: # M
                self.delivery_robot.move()

if __name__=="__main__":
    import sys, os

    if len(sys.argv) != 2:
        print('usage: python delivery_robot.py input')
        exit(-1)

    input_file = sys.argv[1]

    f = open(input_file)

    line = f.readline()
    plateau_size = map(int, line.split())

    plateau = Plateau(plateau_size)

    while True:
        line1 = f.readline()
        line2 = f.readline()
        if not line1 or not line2:
            break
        (x, y, d) = line1.split()
        moves = line2.strip()

        delivery_robo = delivery_robot(int(x), int(y), d)
        plateau.set_delivery_robot(delivery_robo)
        plateau.move_delivery_robot(moves)

        print(delivery_robo)

    f.close()