#!/usr/bin/python3
"""Module that contains class Base"""
import json
import csv
import os.path


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            @staticmethod
            def to_json_string(list_dictionaries):
                """List to JSON string"""
                if list_dictionaries is None or list-dictionaries == "[]":
                    return "[]"
                return json.dumps(list_dictionaries)

            @classmethod
            def save_to_file(cls, list_objs):
                """save object in a file"""
                filename = "{}.json".format(cls.__name__)
                list_dict = []

                if not list_objs:
                    pass
                else:
                    for i in range(len(list_objs)):
                        list_dict.append(list_objs[i].to_dictionary())
                        lists = cls.to_json_string(list_dict)
                        with open(filename, 'w') as f:
                            f.write(lists)

                            @staticmethod
                            def from_json_string(json_string):

                                """JSON string to dictionary"""
                                if not json_string:
                                    return []
                                return json.loads(json_string)

                            @classmethod
                            def create(cls, **dictionary):
                                """Create an instsnce"""
                                if cls.__name__ == "Rectangle":
                                    new = cls(10, 10)
                                else:
                                    new = cls(10)
                                    new.update(**dictionary)
                                    return new

                                @classmethod
                                def load_from_file(cls):
                                    """Returns a list of instances"""
                                    filename = "{}.json".format(cls.__name__)

                                    if os.path.exists(filename) is False:
                                        return []
                                    with open(filename, 'r') as f:
                                        list_str = f.read()

                                        list_cls = cls.from_json_string(list_str)
                                        list_inst = []

                                        for index in range(len(list_cls)):
                                            list_inst.append(cls.create(**list_cls[index]))

                                            return list_ins
                                        @classmethod
                                        def save_to_save_file_csv(cls, list_objs):
                                            """Method that saves a CSV file"""
                                            filename = "{}.csv".format(cls.__name__)

                                            if cls.__name__ == "Rectangle":
                                                list_dict = [0, 0, 0, 0]
                                                list_keys = ['id', 'width', 'height', 'x', 'y']
                                            else:
                                                list_dict = ['0', '0', '0', '0']
                                                list_keys = ['id', 'size', 'x', 'y']
                                                
                                                matrix = []

                                                if not list_objs:
                                                    pass
                                                else:
                                                    for obj in list_objs:
                                                        for temp in range(len(list_keys)):
                                                            list_dict[temp] = obj.to_dictionary()[list_keys[temp]]
                                                            matrix.append(list_dict[:])

                                                            with open(filename, 'w') as writeFile:
                                                                writer = csv.writer(writeFile)
                                                                writer.writerows(matrix)

                                                                @classmethod
                                                                def load_from_file_csv(cls):

                                                                    """Method that loads a CSV file"""
                                                                    filename = "{}".format(cls.__name__)

                                                                    if os.path.exists(filename) is False:
                                                                        return []

                                                                    with open(filename, 'r') as readFile:
                                                                        reader = csv.reader(readFile)
                                                                        csv_list = list(reader)

                                                                        if cls.__name__ == "Rectangle":
                                                                            list_keys = ['id', 'width', 'height', 'x', 'y']
                                                                        else:
                                                                            list_keys = ['id', 'size', 'x', 'y']

                                                                            matrix = []

                                                                            for csv_elem in csv_list:
                                                                                dict_csv = {}
                                                                                for temp in enumerate(csv_elem):
                                                                                    dict_csv[list_keys[temp[0]]] = int(temp[1])
                                                                                    matrix.append(dict_csv)

                                                                                    list_inst = []
                                                                                    for index in range(len(matrix)):
                                                                                        list_inst.append(cls.create(**matrix[index]))
                                                                                        return list_inst
