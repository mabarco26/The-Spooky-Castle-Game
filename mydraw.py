from shapes import Paper ,Triangle , Rectangle , Oval

paper = Paper()

rect = Rectangle()
rect.set_width(20)
rect.set_height(15)
rect.set_color("green")
rect.draw()

olv = Oval()
olv.randomize(20,200)
olv.draw()


tri = Triangle(5, 40, 10, 10 , 100, 100)
tri.set_color("yellow")
tri.set_x(-160)
tri.set_y(60)
tri.draw()

paper.display()
