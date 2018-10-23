
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
    return DFS_Loop(graph)

def DFS_Loop(G):
    explored = [False for i in range(len(G))]
    group = []
    friend_groups = []
    for i in range(len(explored)):
        if not explored[i]:
           friend_groups.append(DFS(G,i,explored,group))
           
    return len(friend_groups)
        

def DFS(G,s,explored,group):
    explored[s] = True
    for j in range(0,len(G[s])):
        if explored[G[s][j]] == False:
            group.append(G[s][j])
            DFS(G,G[s][j],explored,group)
    return group
    

if __name__ == '__main__':

    matrix_filename = input('Please provide a filename containing a friends matrix:\n')
    with open(matrix_filename, 'r') as matrix_file:
        friends = [line.strip() for line in matrix_file.readlines()]
    num_circles = count_friend_circles(friends)
    print('Number of friend circles: ' + str(num_circles))