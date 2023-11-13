#!/usr/bin/python3
"""base class"""
import json
import os
import turtle


class Base:
    """Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__.

            :param id: the id.
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string.

        :param list_dictionaries:
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @staticmethod
    def from_json_string(json_string):
        """from_json_string.

        :param json_string:
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file.

        :param list_objs:
        """
        f_name = cls.__name__ + ".json"
        with open(f_name, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                l_dic = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(l_dic)
                f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create.

        :param dictionary:
        """
        dummy = cls(*dictionary.values())
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file."""
        f_name = f"{cls.__name__}.json"
        try:
            with open(f_name, "r") as f:
                l_dic = Base.from_json_string(f.read())
                return [cls.create(**dic) for dic in l_dic]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv.

        :param list_objs:
        """
        f_name = f'{cls.__name__}.csv'
        csv_data = []
        if list_objs is None or list_objs == []:
            csv_data.append("[]")
        else:
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_data.append(
                        f"{obj.id},{obj.width},{obj.height},{obj.x},{obj.y}")
                elif cls.__name__ == "Square":
                    csv_data.append(f"{obj.id},{obj.size},{obj.x},{obj.y}")

        with open(f_name, "w") as csvfile:
            csvfile.write("\n".join(csv_data))

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv."""
        f_name = cls.__name__ + ".csv"

        if not os.path.exists(f_name):
            return []

        list_of_instances = []
        with open(f_name, "r") as csvfile:
            csv_data = csvfile.read().splitlines()
            for line in csv_data:
                data = line.split(",")
                if cls.__name__ == "Rectangle":
                    instance = cls.create(id=int(data[0]), width=int(
                        data[1]), height=int(data[2]),
                        x=int(data[3]), y=int(data[4]))
                elif cls.__name__ == "Square":
                    instance = cls.create(id=int(data[0]), size=int(
                        data[1]), x=int(data[2]), y=int(data[3]))
                list_of_instances.append(instance)
        return list_of_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw.

        :param list_rectangles:
        :param list_squares:
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        t = turtle.Turtle()
        t.pensize(3)
        t.screen.bgcolor("black")
        t.color("white")

        def draw_rectangle(rect):
            """draw_rectangle.

            :param rect:
            """
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        def draw_square(square):
            """draw_square.

            :param square:
            """
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        for rect in list_rectangles:
            draw_rectangle(rect)

        for square in list_squares:
            draw_square(square)

        turtle.done()
