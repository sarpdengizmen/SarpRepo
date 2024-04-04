import cv2
import numpy as np
from vision_construct_arena import Virtual_game_arena as vga
import math

def show(img):
    '''
    A basic funstion to show images faster
    '''
    cv2.imshow("DEBUG", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

class Line:
    '''
    A class to represent a line in the form ax+by+c=0,
    Can reflect itself over another line object
    '''
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self.update_values()

    def update_values(self):
        self.abc = [self.end[1]-self.start[1], self.start[0]-self.end[0], self.end[0]*self.start[1]-self.start[0]*self.end[1]] #ax+by+c=0 line equation
    
    def inclusiveangles(self, point):
        startangle = math.degrees(math.atan2(self.start[1]-point[1], self.start[0]-point[0]))
        endangle = math.degrees(math.atan2(self.end[1]-point[1], self.end[0]-point[0]))
        return [startangle, endangle]

    def reflect(self, refline):
        a, b, c = refline.abc
        #calculate reflection of start and end points
        x, y = self.start
        self.start = (x - 2*a*(a*x+b*y+c)/(a**2+b**2), y - 2*b*(a*x+b*y+c)/(a**2+b**2)) #reflection of start point
        x, y = self.end
        self.end = (x - 2*a*(a*x+b*y+c)/(a**2+b**2), y - 2*b*(a*x+b*y+c)/(a**2+b**2)) #reflection of end point

    def doesintersect(self, otherline):
        '''
        Finds if finite lines intersect
        '''
        x1, y1 = self.start
        x2, y2 = self.end
        x3, y3 = otherline.start
        x4, y4 = otherline.end
        #Check if lines are parallel
        if (y2-y1)*(x4-x3) - (y4-y3)*(x2-x1) == 0:
            return False
        #Check if intersection point is within the finite lines
        t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4))/((y2-y1)*(x4-x3) - (y4-y3)*(x2-x1)) #parameter for self line equation
        u = -((x1-x3)*(y1-y2) - (y1-y3)*(x1-x2))/((y2-y1)*(x4-x3) - (y4-y3)*(x2-x1)) #parameter for other line equation
        if 0 <= t <= 1 and 0 <= u <= 1:
            return True
        return False
    
    def copy(self):
        return Line(self.start, self.end)


    #Properties of the line change when start or end points are changed
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, start):
        self._start = start
        self.update_values()
    @property
    def end(self):
        return self._end
    @end.setter
    def end(self, end):
        self._end = end
        self.update_values()

class Circle:
    '''
    A class to represent a circle
    '''
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.update_values()
    
    def reflect(self, refline):
        a, b, c = refline.abc
        #calculate reflection of center
        x, y = self.center
        self.center = (x - 2*a*(a*x+b*y+c)/(a**2+b**2), y - 2*b*(a*x+b*y+c)/(a**2+b**2))

    def doesintersect(self, otherline):
        '''
        Finds if line and circle intersect
        '''
        x1, y1 = otherline.start
        x2, y2 = otherline.end
        x3, y3 = self.center
        r = self.radius
        
        #Find intersection point of line and circle
        m = (y2-y1)/(x2-x1)
        c = y1 - m*x1
        a = 1 + m**2
        b = 2*(m*c - m*y3 - x3)
        c = x3**2 + y3**2 + c**2 - 2*y3*c - r**2
        #Check if intersection point is within the finite lines
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return False
        t1 = (-b + discriminant**0.5)/(2*a)
        t2 = (-b - discriminant**0.5)/(2*a)
        if 0 <= t1 <= 1 or 0 <= t2 <= 1:
            return True
        return False
    
    def copy(self):
        return Circle(self.center, self.radius)

        

class Arena:
    def __init__(self):
        
        

class Path_Finder:
    def __init__(self, vir_arena):
        self.v_arena = vir_arena #Virtual game arena object
        self.v_arena_bin = cv2.inRange(cv2.cvtColor(self.v_arena.arena, cv2.COLOR_BGR2GRAY),1,255) #Binary image of arena
        self.arena_contour = self.v_arena.arena_contour #Array of 4 points of arena contour
        self.arena_contour = sorted(self.arena_contour, key=lambda x: x[0][0]) #Sort by ascending x
        #Find the center of the two points on the left and right of the arena,corresponds to player positions
        self.p1_pos = (int((self.arena_contour[0][0][0] + self.arena_contour[1][0][0])/2), int((self.arena_contour[0][0][1] + self.arena_contour[1][0][1])/2))
        self.p2_pos = (int((self.arena_contour[2][0][0] + self.arena_contour[3][0][0])/2), int((self.arena_contour[2][0][1] + self.arena_contour[3][0][1])/2))
        self.path = self.Path(self.p1_pos, 25, self.v_arena)
        inter, angle = self.path.cast_ray(self.p1_pos, 25)
        for i in range(30):
            inter, angle = self.path.cast_ray(inter, angle)
        cv2.imshow("arena", self.v_arena.arena)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        self.colordict = {"wall": (0,255,0), "obstacle": (255,0,0), "goal": (0,0,255)}
    
    def generate_lines(self, contour):
        '''
        Generates the lines of a given cv2 contour
        '''
        self.lines = []
        for i in range(len(contour)):
            self.lines.append(Line(contour[i][0], contour[(i+1)%len(contour)][0]))
    
    class Node:
        """
        A class to represent a node in the pathfinding algorithm, each node is a arena represented by coordinate system
        """
        def __init__(self, symline=None, parent=None):
            if parent == None:
                #Inital node
                

        def add_child(self, child):
            self.children.append(child)
    class Path:
        def __init__(self, start, angle, v_arena, goal=None):
            self.v_arena = v_arena
            self.v_arena_bin = cv2.inRange(cv2.cvtColor(v_arena.arena, cv2.COLOR_BGR2GRAY),1,255)
            self.x = start[0]
            self.y = start[1]
            self.angle = angle
            self.path = []
            self.path.append(((self.x, self.y), self.angle))
            

        def cast_ray(self, start, angle):
            #point is starting point of ray in pixel coordinates
            #angle is angle of ray in degrees
            blank = np.zeros(self.v_arena_bin.shape, dtype=np.uint8)
            cv2.line(blank, (int(start[0]+8*math.cos(math.radians(angle))), int(start[1]+8*math.sin(math.radians(angle)))), (int(start[0]+1000*math.cos(math.radians(angle))), int(start[1]+1000*math.sin(math.radians(angle)))), (255,255,255), 2)
            
            #Finding the intersection of the ray with the arena
            intersection = cv2.bitwise_and(blank, self.v_arena_bin)
            intersection = cv2.findNonZero(intersection)
            intersection = sorted(intersection, key=lambda x: np.linalg.norm(x[0]-start))
            intersection = intersection[0][0] #Collision occurs with the first pixel after the starting point

            #Search along the intersected line for adjacent pixels
            mask = np.zeros(self.v_arena_bin.shape, dtype=np.uint8)
            cv2.circle(mask, (intersection[0], intersection[1]), 8, (255,255,255), -1)
            portion_of_line = cv2.bitwise_and(mask, self.v_arena_bin)
            portion_of_line = cv2.findNonZero(portion_of_line)
            portion_of_line = sorted(portion_of_line, key=lambda x: np.linalg.norm(x[0]-intersection), reverse=True)
            lineangle = math.degrees(math.atan2(portion_of_line[0][0][1]-intersection[1], portion_of_line[0][0][0]-intersection[0]))
            bounceangle = 2*lineangle - angle
            self.path.append((intersection, bounceangle))
            cv2.line(self.v_arena.arena, start, (intersection[0], intersection[1]), (0,0,255), 2)
            show(self.v_arena.arena)
            return intersection, bounceangle
        
        
        
        
        

        

#import image from ./DataSet/img1_1.jpg
arenaimg = cv2.imread("./DataSet/img1_1.jpg")
#resize the image to 900x500
arenaimg = cv2.resize(arenaimg, (800,600))
#arenaimg = ga.Game_arena()
arena = vga(arenaimg,1, 1, 1, DEBUG=False)
#Path_Finder(arena)
