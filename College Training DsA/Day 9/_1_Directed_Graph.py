import sys
class Graph:
    def __init__(self):
        self.nodes=[]  #declared variable
        self.graph=[]
        self.nodeCount=0

    def addNode(self):
        if v in self.nodes:
            print(v,"is already present")
        else:
            self.nodeCount+=1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp=[]
            for x in range(self.nodeCount):
                temp.append(0)
            self.graph.append(temp)
            print(v,"is added.") 
        

    def addEdge_Undirected_Unweighted(self):
        if v1 not in self.nodes:
            print(v1,"not present")
            return
        if v2 not in self.nodes:
            print(v2," not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1
    def addEdge_Undirected_Weightef(self):
        if v1 not in self.nodes:
            print(v1,"not present")
            return
        if v2 not in self.nodes:
            print(v2," not present")
            return
        index1=self.nodes.index(v1)
        index2=self.nodes.index(v2)
        self.graph[index1][index2]=1
        self.graph[index2][index1]=1

    def addEdge_Directed_Weighted(self):
        pass
    def printGraph(self):
        for i in range(self.nodeCount):
            for j in range(self.nodeCount):
                print(self.graph[i][j],end=" ")
    def deleteGraph(self):
        if v not in self.nodes:
            print(v,"not present")
        else:
            nodeCount-=1
            index1 = self.nodes.index(v)
            self.nodes.pop(index1)
            self. graph.pop(index1)
            for x in self.graph:
                x.pop(index1)
            print(v,"is deleted")


if __name__=='__main__':
    obj=Graph(   )
    print("\n 1. (Insetion)add a node using adjaceny matrix represent")
    print("2. (Insertion) add a edge using adjaceny matrix representation")
    print("3. (Insertion) add a edge undirected weighted graph")
    print("4. (Insertion) add a edge directed weighted grpah")
    print("5. Print Graph")
    print("6. Delete Graph ")
    print("0. Exit ")
    n=int(input("Enter any choice:"))
    if n==1:
        v=str(input("Enter Node: "))
        obj.addNode()
    elif n==2:
        v1=str(input("Enter vertex1: "))
        v2=str(input("Enter vertex2: "))
        obj.addEdge_Undirected_Unweighted()

    elif n==3:
        v1=str(input("Enter vertex1: "))
        v2=str(input("Enter vertex2: "))
        obj.addEdge_Undirected_Weighted()
    elif n==4:
        v1=str(input("Enter vertex1: "))
        v2=str(input("Enter vertex2: "))
        obj.addEdge_Directed_Weighted()
    elif n==5:
        obj.printGraph()
    elif n==6:
        obj.deleteGraph()
    elif n==0:
        sys.exit(0)