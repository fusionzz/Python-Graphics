import sys, math, pygame

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, 1)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Wireframe Cube Simulation (http://codeNtronix.com)")

        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,-1,-1),
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
            ]

        self.vertices2 = [
            Point3D(-1,-1,-1),
            Point3D(-1,0,-1),
            Point3D(0,0,-1),
            Point3D(0,-1,-1),
            Point3D(-1,0,0),
            Point3D(0,0,0),
            Point3D(0,-1,0),
            Point3D(-1,-1,0)
            ]


        self.vertices3 = [
            Point3D(0,-1,-1),
            Point3D(0,0,-1),
            Point3D(1,0,-1),
            Point3D(1,-1,-1),
            Point3D(0,0,0),
            Point3D(1,0,0),
            Point3D(1,-1,0),
            Point3D(0,-1,0)
            ]

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces = [(0,1,2,3),(0,1,4,7),(4,5,6,7),(7,6,3,0),(5,6,3,2)]
        self.faces2 = [(0,1,2,3),(0,1,4,7),(4,5,6,7),(7,6,3,0),(5,6,3,2)]


        self.angleX, self.angleY, self.angleZ = 0, 0, 0

    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0,0,0))

            # Will hold transformed vertices.
            t = []
            t1 = []  

            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)
                x, y = int(p.x), int(p.y)
                self.screen.fill((255,0,0),(x,y,2,2))


            for v1 in self.vertices2:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r1 = v1.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                # Transform the point from 3D to 2D
                p1 = r1.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t1.append(p1)
                x, y = int(p1.x), int(p1.y)
                self.screen.fill((255,0,0),(x,y,3,3)) 

            for f in self.faces:
                pygame.draw.line(self.screen, (255,255,255), (t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y))


            for f1 in self.faces2:
                pygame.draw.line(self.screen, (255,255,255), (t1[f1[0]].x, t1[f1[0]].y), (t1[f1[1]].x, t1[f1[1]].y))
                pygame.draw.line(self.screen, (255,255,255), (t1[f1[1]].x, t1[f1[1]].y), (t1[f1[2]].x, t1[f1[2]].y))
                pygame.draw.line(self.screen, (255,255,255), (t1[f1[2]].x, t1[f1[2]].y), (t1[f1[3]].x, t1[f1[3]].y))
                pygame.draw.line(self.screen, (255,255,255), (t1[f1[3]].x, t1[f1[3]].y), (t1[f1[0]].x, t1[f1[0]].y))

            self.angleX += 1
            self.angleY += 1
            self.angleZ += 1

            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()