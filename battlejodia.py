def port(adresIP):
	adresIP_port = adresIP.split(".")
	nimewo_adresIP= [int(nimewo) for nimewo in adresIP_port]
	total= sum(nimewo_adresIP)
	ouve_port= total * nimewo_adresIP[0]
	return ouve_port


if __name__ == '__main__':
	
	adresIP= input('antre adres IP w :')
	ouve_port= find_ouve_port(adresIP)
	print("Port a ouve :", ouve_port)
