#---- Python VM startup for LISTENER_1_from_3 ---
import multiprocessing
import time
import LISTENER_1_from_3
import DECRYPT_1_from_3
import ENCRYPT_3_to_1
import WRITER_3_to_1

processes = []

if __name__ == '__main__':
	p = multiprocessing.Process(target=LISTENER_1_from_3.startLISTENER_1_from_3)
	processes.append(p)
	p.start()
	print "started LISTENER_1_from_3"
	time.sleep(5)
	p = multiprocessing.Process(target=DECRYPT_1_from_3.startDECRYPT_1_from_3)
	processes.append(p)
	p.start()
	print "started DECRYPT_1_from_3"
	time.sleep(5)
	p = multiprocessing.Process(target=ENCRYPT_3_to_1.startENCRYPT_3_to_1)
	processes.append(p)
	p.start()
	print "started ENCRYPT_3_to_1"
	time.sleep(5)
	p = multiprocessing.Process(target=WRITER_3_to_1.startWRITER_3_to_1)
	processes.append(p)
	p.start()
	print "started WRITER_3_to_1"
	time.sleep(5)

	for p in processes:
		p.join()
