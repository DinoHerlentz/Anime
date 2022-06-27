import animec

amount = 5

aninews = animec.Aninews(amount)
links = aninews.links
titles = aninews.titles
descriptions = aninews.description

for i in range(amount):
    print(f"{i + 1} {titles[i]}")