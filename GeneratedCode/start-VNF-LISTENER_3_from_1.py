#---- Python VM startup for LISTENER_3_from_1 ---
import multiprocessing
import time
import LISTENER_3_from_1
import DECRYPT_3_from_1
import ENCRYPT_1_to_3
import WRITER_1_to_3

processes = []

if __name__ == '__main__':
	p = multiprocessing.Process(target=LISTENER_3_from_1.startLISTENER_3_from_1)
	processes.append(p)
	p.start()
	print "started LISTENER_3_from_1"
	time.sleep(5)
	p = multiprocessing.Process(target=DECRYPT_3_from_1.startDECRYPT_3_from_1)
	processes.append(p)
	p.start()
	print "started DECRYPT_3_from_1"
	time.sleep(5)
	p = multiprocessing.Process(target=ENCRYPT_1_to_3.startENCRYPT_1_to_3)
	processes.append(p)
	p.start()
	print "started ENCRYPT_1_to_3"
	time.sleep(5)
	p = multiprocessing.Process(target=WRITER_1_to_3.startWRITER_1_to_3)
	processes.append(p)
	p.start()
	print "started WRITER_1_to_3"
	time.sleep(5)

	for p in processes:
		p.join()
