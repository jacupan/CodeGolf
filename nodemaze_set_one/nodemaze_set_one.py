import os


#in_node = input('Enter IN: ')
#ex_node = input('Enter EX: ')

# a sample graph
graph = {'R2': ['D2','I9'],
             'C3': ['I9','P0'],
             'P0': ['C3'],
             'K9': ['X3'],
             'A3': ['B9','G8'],
             'F1': ['E6'],
             'I9': ['C3','T2'],
             'C1': ['X5'],
             'B9': ['A3','L1','Z2'],
             'T2': ['E6','I9','X3','Z2'],
             'L1': ['B9','N1','X5'],
             'B7': ['Q5','W0','Z2'],
             'W0': ['B7'],
             'G8': ['A3'],
             'X3': ['B4','K9','T2'],
             'B4': ['X3'],
             'N1': ['L1'],
             'E6': ['F1','R9','T2'],
             'Z2': ['B7','B9','T2'],
             'Q5': ['B7'],
             'R9': ['E6'],
             'X5': ['C1','L1']}
  
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

#BFS(graph,"X5","I9",path_queue)

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

#os.system("pause")
input()