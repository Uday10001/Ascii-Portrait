class Skeleton:
    def __init__(self, scale: float=1):
        self.scale = scale
        self.width = int(48)
        self.height = int(65)
        self.portrait = [["," for j in range(self.width)] for i in range(self.height)]
    
    def draw_hair(self):
        for x in range(0, int(22  )):
            for y in range(int(5  ), int(44  )):
                center_x = int(23  )
                center_y = int(20  )
                radius = int(22  )
                if ((x - center_x) * (x - center_x)) + ((y - center_y) * (y - center_y)) <= radius * radius:
                    self.portrait[x][y] = "S"
    
    def draw_face(self):
        # Upper face
        for x in range(int(10  ), int(22  )):
            for y in range(int(3  ), int(40  )):
                center_x = int(19  )
                center_y = int(21  )
                if ((x - center_x) * (x - center_x)) // (0.7  ) + ((y - center_y) * (y - center_y)) // (2.7  ) < (90    ):
                    self.portrait[x][y] = ';'
        
        # Chin
        for x in range(int(22  ), int(45  )):
            for y in range(int(4  ), int(38  )):
                center_x = int(19  )
                center_y = int(21  )
                if (((x - center_x) * (x - center_x)) // (8  )) + (((y - center_y) * (y - center_y)) // (2.7  )) < (90    ):
                    self.portrait[x][y] = ';'
        
        # Ear
        for x in range(int(20  ), int(50  )):
            for y in range(int(30  ), int(45  )):
                center_x = int(25  )
                center_y = int(35  )
                if (((x - center_x) * (x - center_x)) // (1  )) + (((y - center_y) * (y - center_y)) // (0.7  )) < (40    ) and self.portrait[x][y] != ';':
                    self.portrait[x][y] = '*'    
    def draw_robe(self):
        for y in range(44, 65):
            for x in range(0, 48):
                if ((x-22)*(x-22)//20) + ((y-74) * (y-74)/10)  < 90:
                    self.portrait[y][x] = '#'


    def render(self):
        for i in range(len(self.portrait)):
            for j in range(len(self.portrait[0])):
                print(self.portrait[i][j], end='')
            print()
    
    def generate(self):
        self.draw_hair()
        self.draw_face()
        self.draw_robe()

        return self.portrait
structure = Skeleton(scale=1.0)
structure.generate()
structure.render()
