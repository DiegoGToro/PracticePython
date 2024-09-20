import dns.reseolver

def main():
	try: 
		objetivo = dns.reseolver.query("achirou.com","NS")
		for x in objetivo:
			print(x)
	except:
		print("No se pudo conseguir informaciòn")

if __name__ == '__main__':
    try:
	