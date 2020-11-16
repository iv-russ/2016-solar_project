# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import matplotlib.pyplot as plt


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    
    par = line.split()
    star.R = int(par[1])
    star.color = par[2]
    star.m = float(par[3])
    star.x = float(par[4])
    star.y = float(par[5])
    star.Vx = float(par[6])
    star.Vy = float(par[7])

    
def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    par = line.split()
    planet.R = int(par[1])
    planet.color = par[2]
    planet.m = float(par[3])
    planet.x = float(par[4])
    planet.y = float(par[5])
    planet.Vx = float(par[6])
    planet.Vy = float(par[7])

    
def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            l = obj.type+' '+str(obj.R)+' '+obj.color+' '+str(obj.m)+' '+str(obj.x)+' '+str(obj.y)+' '+ str(obj.Vx)+' '+str(obj.Vy) + '\n'
            out_file.write(l)
            

def collect_statistics(body, time, statistics_list):
    distance = int((body.x**2 + body.y**2)**0.5)
    velocity = int((body.Vy ** 2 + body.Vx ** 2)**0.5)
    statistics_list.append([distance, velocity, int(time)])


def write_data_to_file(output_filename, statistics_list, objects):
    number_of_bodies = 0
    S = ''
    for body in objects:
        if(body.type == 'planet'):
            number_of_bodies += 1
    if(number_of_bodies == 1):
        for i in statistics_list:
            for j in i:
                S += str(j) + ' '
        with open(output_filename, 'w') as out_file:
            out_file.write(S) 
    else:
        pass

def draw_graph_from_file(output_filename):
    with open(output_filename, 'r') as out_file:
        Lst = list(out_file)[0].split()
        dist_list = Lst[0::3]
        vel_list = Lst[1::3]
        time_list = Lst[2::3]
        dist_list = list(map(int, dist_list))
        time_list = list(map(int, time_list))
        vel_list = list(map(int, vel_list))
        plt.plot(time_list, vel_list)
        plt.show()
        plt.plot(time_list, dist_list)
        plt.show()
        plt.plot(vel_list, dist_list)
        plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")
