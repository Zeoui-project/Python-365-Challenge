# %% [markdown]
# # Cred Logo using Python

# %%
%pip install turtle

# %%
import turtle
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.goto(-166, 100)
t.width(5)
t.color("white")
t.forward(256)
t.right(90)
t.forward(220)
t.right(60)
t.forward(150)
t.right(60)
t.forward(150)
t.right(60)
t.forward(220)

t.penup()
t.goto(-86, 50)
t.pendown()
t.right(90)
t.forward(136)
t.right(90)
t.forward(60)
t.color("black")
t.forward(40)
t.color("white")
t.forward(40)
t.right(60)

t.forward(104)
t.right(60)
t.forward(104)
t.right(60)
t.forward(106)
t.right(90)
t.forward(130)

t.penup()
t.goto(10, -75)
t.pendown()
t.right(150)
t.forward(57)
t.right(60)
t.forward(57)
t.right(60)
t.forward(30)
t.penup()
t.goto(-163, -300)
t.pendown()

t.write("CRED", font=("Sentic",75,"normal"))