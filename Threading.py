import threading 

def worker(): 
    print('Hello world')

thread_list= []
for i in range(4):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    thread.start()
