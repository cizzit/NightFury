import sys
from bs4 import BeautifulSoup

def get_overdue(soup):
	results={}
	client=''
	site=''
	for ods in soup.find_all("overdue"):
		server = ods.parent
		server_name = server.find('name').string[:]
		site_name = server.parent.parent.find('name').string[:]
		client_name = server.parent.parent.parent.find('name').string[:]
		if client_name not in results:
			results[client_name] = {}
		if site_name not in results[client_name]:
			results[client_name][site_name] = []
		results[client_name][site_name].append(server_name)
	if not any(results):
		return None
	return results
		
if __name__ == "__main__":
	handler = open(sys.argv[1]).read()
	soup = BeautifulSoup(handler,"xml")
	print get_overdue(soup)
