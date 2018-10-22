import queue

def count_friend_circles(friends):
    graph = {}
    connections = []
    for friend in friends:
        friend_connection = []
        for i in range(len(friend)):
            if friend[i] == 'Y':
                friend_connection.append(i)
        connections.append(friend_connection)

    for i in range(len(connections)):
        graph.update({i:connections[i]})
    
    return breadth_first_search(graph)

def breadth_first_search(G):
    num_friend_groups = 1
    first_end = BFS(G,0)
    if first_end < len(G):
        for i in range(first_end,len(G)):
            if BFS(G,i) < len(G):
                num_friend_groups += 1
    return num_friend_groups
        

def BFS(G,s):
    last_node = 0
    explored = [0 for i in range(len(G))]
    explored[s] = 1
    Q = queue.Queue()
    Q.put(s)
    while Q.qsize() > 0:
        Q.get()
        for node in G[s]:
            if node not in explored:
                explored.append(node)
                Q.put(node)
                last_node += 1
    print(last_node)
    return last_node

if __name__ == '__main__':

    matrix_filename = input('Please provide the name of a file that contains a friends matrix:\n')

    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]
    num_circles = count_friend_circles(friends)
    print(friends)
    print(f'Number of friend circles: {num_circles}')