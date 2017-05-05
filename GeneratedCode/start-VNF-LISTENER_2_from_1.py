#---- Python VM startup for LISTENER_2_from_1 ---
import multiprocessing
import time
import LISTENER_2_from_1
import DECRYPT_2_from_1
import ENCRYPT_1_to_2
import WRITER_1_to_2

processes = []

if __name__ == '__main__':
	p = multiprocessing.Process(target=LISTENER_2_from_1.startLISTENER_2_from_1)
	processes.append(p)
	p.start()
	print "started LISTENER_2_from_1"
	time.sleep(5)
	p = multiprocessing.Process(target=DECRYPT_2_from_1.startDECRYPT_2_from_1)
	processes.append(p)
	p.start()
	print "started DECRYPT_2_from_1"
	time.sleep(5)
	p = multiprocessing.Process(target=ENCRYPT_1_to_2.startENCRYPT_1_to_2)
	processes.append(p)
	p.start()
	print "started ENCRYPT_1_to_2"
	time.sleep(5)
	p = multiprocessing.Process(target=WRITER_1_to_2.startWRITER_1_to_2)
	processes.append(p)
	p.start()
	print "started WRITER_1_to_2"
	time.sleep(5)

	for p in processes:
		p.join()
