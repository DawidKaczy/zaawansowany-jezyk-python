from vector.vector2D import Vector2D

if __name__ == '__main__':
    ob1 = Vector2D(1, 0)
    ob2 = Vector2D(0, 1)
    print(Vector2D.length(ob1))
    print(Vector2D.dot_product(ob1, ob2))
    print(Vector2D.angle_between(ob1, ob2))