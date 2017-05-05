#---- Python VM startup for LISTENER_1_from_2 ---
import multiprocessing
import time
import LISTENER_1_from_2
import DECRYPT_1_from_2
import ENCRYPT_2_to_1
import WRITER_2_to_1

processes = []

if __name__ == '__main__':
	p = multiprocessing.Process(target=LISTENER_1_from_2.startLISTENER_1_from_2)
	processes.append(p)
	p.start()
	print "started LISTENER_1_from_2"
	time.sleep(5)
	p = multiprocessing.Process(target=DECRYPT_1_from_2.startDECRYPT_1_from_2)
	processes.append(p)
	p.start()
	print "started DECRYPT_1_from_2"
	time.sleep(5)
	p = multiprocessing.Process(target=ENCRYPT_2_to_1.startENCRYPT_2_to_1)
	processes.append(p)
	p.start()
	print "started ENCRYPT_2_to_1"
	time.sleep(5)
	p = multiprocessing.Process(target=WRITER_2_to_1.startWRITER_2_to_1)
	processes.append(p)
	p.start()
	print "started WRITER_2_to_1"
	time.sleep(5)

	for p in processes:
		p.join()
