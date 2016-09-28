import os

# a sample graph
graph = {'B2': ['K1','K8','B4'],'B4': ['F0','B9','L0','B2','S4' ],'B8': ['L6'],'B9': ['D4','S9','B4'],'C3': ['T5'],'D1': ['J1'],'D3': ['S4'],'D4': ['B9'],'E9': ['S4','F1'],'F0': ['B4','O9'],'F1': ['E9']
        ,'G6': ['M3'],'H9': ['N5'],'I7': ['Y0'],'J1': ['D1'],'J2': ['R1'],'J4': ['K3'],'J9': ['L1','S4','P5','U6'],'K1': ['B2'],'K3': ['X5','J4'],'K8': ['B2'],'L0': ['B4'],'L1': ['T6','J9','N5','Y0'],
        'L6': ['B8'],'M3': ['G6'],'M4': ['W3'],'N5': ['H9','L1'],'O9': ['F0'],'P5': ['J9'],'R1': ['J2'],'R5': ['Y0'],'S4': ['E9','J9','B4','D3'],'S9': ['B9'],'T5': ['C3'],'T6': ['L1'],'U6': ['J9'],
        'W3': ['X5','Y0','M4'],'X5': ['W3','K3'],'Y0': ['L1','W3','I7','R5']}
  
class MyQUEUE: # just an implementation of a queue
	
	def __init__(self):
		self.holder = []
		
	def enqueue(self,val):
		self.holder.append(val)
		
	def dequeue(self):
		val = None
		try:
			val = self.holder[0]
			if len(self.holder) == 1:
				self.holder = []
			else:
				self.holder = self.holder[1:]	
		except:
			pass
			
		return val	
		
	def IsEmpty(self):
		result = False
		if len(self.holder) == 0:
			result = True
		return result

path_queue = MyQUEUE() # now we make a queue

def BFS(graph,start,end,q):
	
	temp_path = [start]

	q.enqueue(temp_path)

	while q.IsEmpty() == False:
		tmp_path = q.dequeue()
		last_node = tmp_path[len(tmp_path)-1]
		#print (tmp_path)
		if last_node == end:
			print ("VALID_PATH : ",tmp_path)
		for link_node in graph[last_node]:
			if link_node not in tmp_path:
				new_path = []
				new_path = tmp_path + [link_node]
				q.enqueue(new_path)
while True:
    try:
        in_node = input('\nEnter IN: ')      
        if in_node not in graph:
            print("Invalid start node.")
            continue
        else:
            ex_node = input('Enter EX: ')
            if ex_node not in graph:
                print("Invalid end node.")
                continue
            else:
                BFS(graph,in_node,ex_node,path_queue)        
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
input()