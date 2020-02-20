class Graph:
    #link_dict ={}
    #node_dict = {} 
    Node_number = 0 
class Nodes(Graph):  
    node_dict = {}
    def add_nodes(self,location):  
        Graph.Node_number +=1 
        self.Location = location
        self.Node_ID = Graph.Node_number  
        Nodes.node_dict[self.Node_ID] = self.Location
    def get_node_dict(self):
        print(Nodes.node_dict)
class Links(Nodes): 
    link_dict = {}
    def add_links(self,Source,Destination,Distance):  
        if Source  not in Nodes.node_dict.keys(): 
            print("Source_Error") 
        if Destination not in  Nodes.node_dict.keys(): 
            print("Destination_Error")   
        else:  
            self.Distance = Distance
            self.Source_ID = Source 
            self.Destination_ID = Destination 
            self.link_tuple = (self.Source_ID,self.Destination_ID ) 
            #Graph.node_dict[self.Source_ID] = self.link_tuple 
            #Graph.node_dict[self.Destination_ID] = self.link_tuple 
            Links.link_dict[self.link_tuple] = self.Distance 
    #ef get_link_dict(self):         
    def del_links(self,source,destination): 
        if source  not in Nodes.node_dict.keys(): 
            print("Source_Error") 
        if destination not in  Nodes.node_dict.keys(): 
            print("Destination_Error")  
        else: 
            del_tuple=(source,destination)      
            del Links.link_dict[del_tuple]  
    def del_nodes(self,id1): 
        if id1  not in Nodes.node_dict.keys(): 
            print("not fonnd such a node")     
        else:  
           
         i=0 
         b = {}
         for possible_ID in Nodes.node_dict.keys():   
             b[i] = (id1 , possible_ID)   
             #print(b[i]) 
             #print(tuple(Links.link_dict.keys()))
             for keys in  tuple(Links.link_dict.keys()): 
               if b[i]== keys: 
                  del Links.link_dict[b[i]]
             i =i+1   
         del Nodes.node_dict[id1]      
              
    def get_link_dict(self): 
        print(Links.link_dict)      
a = Nodes() 
a.add_nodes([100,200]) 
b = Nodes() 
b.add_nodes([100,299])  
#b.get_node_dict()
c = Links() 
c.add_links(1,2,100) 
#.del_links(1,2) 
c.del_nodes(1) 
c.get_link_dict()
c.get_node_dict()

