import sys
from bs4 import BeautifulSoup

def get_av_fails(soup, check):
	results={'server':0,'workstation':0}
	client=''
	site=''
	for ods in soup.find_all("check_type"):
		if ods.string==check:
			chk_type_parent = ods.parent.parent.parent
			chk_type_of_machine = chk_type_parent.name
			results[chk_type_of_machine]+=1
	return results
		
	
if __name__ == "__main__":
	handler = open(sys.argv[1]).read()
	soup = BeautifulSoup(handler,"xml")
	'''
	List of checks:
	1001 - Failed Antivirus Checks
	1002 - Backup Fails
	1020 - CryptoLocker GPO Trip
	'''
	try:
		c = str(sys.argv[2])
	except:
		print "Missing check value!"
		exit()
	print get_av_fails(soup,c)
