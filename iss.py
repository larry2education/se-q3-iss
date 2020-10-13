#!/usr/bin/env python

__author__ = 'Larry Scott with help from Pete'

import requests
import time
import turtle


def main():
    get_astronaut()
    get_iss_pass()
    longi, lat = iss_now()
    risetime = find_time()
    handle_turtle(longi, lat, risetime)
    pass


def get_astronaut():
    r = requests.get("http://api.open-notify.org/astros.json")
    print(r.json())


def get_iss_pass():
    t = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=39.7684&lon=-86.1581&n=1")
    print(t.json())


def iss_now():
    n = requests.get("http://api.open-notify.org/iss-now.json")
    data = n.json()
    lat = float(data["iss_position"]["latitude"])
    longi = float(data["iss_position"]["longitude"])
    print(data["iss_position"]["latitude"])
    print(n.json())
    return longi, lat


def handle_turtle(x, y, risetime):
    iss = turtle.Turtle()
    screen = turtle.Screen()
    turtle.setup(width=720, height=360, startx=0, starty=0)
    turtle.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    iss.shape("iss.gif")
    iss.penup()
    iss.goto(-86.1581, 39.7684)
    iss.dot(15, "yellow")
    iss.color("white")
    iss.write(risetime, font=("Times New Roman", 18))
    iss.goto(x, y)

    turtle.done()


def find_time():
    t = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=39.7684&lon=-86.1581&n=1")
    print(t)
    t = t.json()

    rise = time.ctime(t["response"][0]["risetime"])
    return rise


if __name__ == '__main__':
    main()
