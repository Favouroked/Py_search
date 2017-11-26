from threading import Thread
from queue import Queue
import os

SEARCH_NAME = 'fav'

NUMBER_OF_THREADS = 5
q = Queue(maxsize = 0)

def do_stuff(q):
    while True:
        x = q.get()
        search(x, SEARCH_NAME)
        q.task_done()

def search(the_dir, name):
    files_in_dir = os.listdir(the_dir)
    for i in files_in_dir:
        if name in i:
            print(os.path.join(the_dir, i))
        if os.path.isdir(os.path.join(the_dir, i)):
            q.put(os.path.join(the_dir, i))

for i in range(NUMBER_OF_THREADS):
    worker = Thread(target=do_stuff, args = (q,))
    worker.setDaemon(True)
    worker.start()

q.put('/home/favour')

q.join()
