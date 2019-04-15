class Coordinate:
    x = 0
    y = 0
f=open('xy.dat','r')
def get_maxmin_mag(f):
    rows=[]
    for line in f:
    	rows.append(line)
    x_min=float(rows[0].split()[0])
    y_min=float(rows[0].split()[1])
    x_max=float(rows[0].split()[0])
    y_max=float(rows[0].split()[1])
    distance_min=(x_min**2+y_min**2)**0.5
    distance_max=(x_max**2+y_max**2)**0.5
    for row in rows:
    	distance_new=( float(row.split()[0])**2 + float(row.split()[1])**2 )**0.5
    	if distance_new >distance_max:
    		distance_max=distance_new
    		x_max=row.split()[0]
    		y_max=row.split()[1]
    	if distance_new<distance_min:
    		distance_min=distance_new
    		x_min=row.split()[0]
    		y_min=row.split()[1]
    min_point=Coordinate()
    min_point.x=round(float(x_min),6)
    min_point.y=round(float(y_min),6)
    max_point=Coordinate()
    max_point.x=round(x_max,6)
    max_point.y=round(y_max,6)
    return max_point,min_point


'''
class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    points = {}
    for i in f.readlines():
        i = i[:-1]
        x,y = i.split()
        point = Coordinate()
        point.x,point.y = float(x),float(y)
        magnitude = (point.x**2 + point.y**2)**0.5
        points[magnitude] = point
    return points[max(points.keys())],points[min(points.keys())]
'''