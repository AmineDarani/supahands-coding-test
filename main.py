from collections import deque

def main():



# Due to time constraint I wasnt able to add the 2 hunters funcionality and decided to opt
# for only one hunter Choosing the path that would generate the most boars in the least
# amout of time traveled


  hunting_map = {
    'A':['B','C','K'],
    'B':['D','E'],
    'C':['E','G','H'],
    'D':['E','F'],
    'E':['G','I','F'],
    'F':['I','J'],
    'G':['I','K'],
    'H':['I','F'],
    'I':['K'],
    'J':['K'],
    'K':[]
  }
  prey = 0
  stamina = 3
  path="The path taken :"
  patharr=[]
  result=optimal_path(hunting_map,'A','K')
  for a in result[0]:
      path = path+"  "+a
      patharr.append([a,3])


  print(hunting_map)

  print(path)
  print("Nodes visited  : ",result[1]+1)
  prey = startAdventure(patharr,stamina,prey)

  print("Total prey     : ",prey)




def startAdventure(patharr,stamina,prey):
    for node in patharr:
        boars = node[1]
        while boars !=0:
            stats = restorhunt(boars,stamina,prey)
            boars = stats[1]
            stamina =stats[2]
            prey= stats[0]

        if(stamina>0):
            stamina = moveonce(stamina)
        else :
            rest(stamina)



    return prey


    # Used to find out if the hunters should rest or hunt this round
def restorhunt(boars,stamina,prey):
    if(stamina>0):
        if(boars>0):
            prey = prey +1
            boars = boars -1
            stamina=stamina-1
            return prey,boars,stamina
        if(boars==0):
            return prey,boars,stamina
    if(stamina==0):
        stamina =rest(stamina)
        return prey,boars,stamina

def moveonce(stamina):
    return stamina-1

def rest(stamina):
    stamina=stamina+2
    return stamina




# This Method is used to find the most optimal path for the most boars the hunters can harvest
# I am using a modified version of dijkstra algorithm
def optimal_path(map,start,finish):
    notvisited = list(map.copy().keys())
    distance_from_start = {
        node: (0 if node == start else -10000) for node in map.keys()
    }
    previous_node = {node: None for node in map.keys()}
    while notvisited:
        current_node = notvisited[0]
        notvisited.remove(current_node)
        for neighbor in map[current_node]:
            new_path = distance_from_start[current_node] + 1
            if new_path > distance_from_start[neighbor]:
                distance_from_start[neighbor] = new_path
                previous_node[neighbor] = current_node

    path = deque()
    current_node = finish
    while previous_node[current_node] is not None:
        path.appendleft(current_node)
        current_node = previous_node[current_node]
    path.appendleft(start)
    return (path,distance_from_start[finish])

main()
