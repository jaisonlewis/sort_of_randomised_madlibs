from elements import *

name = input("Name (type r to randomise): ")
if name == ("r"):
   name = namer()

noun2 = input("Enter an enchanted object here (type r to randomise)")
if noun2 == ("r"):
   noun2 = nounb()



madlib = (f"Once upon a time, in a {adjective()} kingdom far away, there lived a peasant named \
{name}. One day, {name} decided to embark on a(n) {adjective()} adventure to find \
a legendary {noun2}. Along the way, {name} encountered a {adjective()} {animal()} who became \
their loyal companion. Together, they traversed {adjective()} landscapes, braving {noun()} \
and overcoming {adjective()} obstacles. Finally, after much perseverance, {name} reached the \
enchanted {noun2} and discovered its {adjective()} powers. With great excitement, {name} \
returned to the kingdom and used the {noun2}'s powers to bring {adjective()} prosperity \
and joy to all. And they all lived {adverb()} ever after.")

print(madlib)