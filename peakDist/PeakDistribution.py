# -*- coding: utf-8 -*-
"""
 Created by  on 14:37 12/14/14.
 
 @author: Edward
 
 Baylor College of Medicine
 Houston, TX 77030

"""


def distribution(indata1,indata2):
	chrD={'CHR1':[],'CHR2':[],'CHR3':[],'CHR4':[],'CHR5':[],'CHR6':[],'CHR7':[],'CHR8':[],'CHR9':[],'CHR10':[],'CHR11':[],'CHR12':[],'CHR13':[],'CHR14':[],'CHR15':[],'CHR16':[],'CHR17':[],'CHR18':[],'CHR19':[],'CHR20':[],'CHR21':[],'CHR22':[],'CHRX':[],'CHRY':[]}
	for keys in chrD.keys():
		for d1 in indata1[keys]:
			for d2 in indata2[keys]:
				ds=int(d1.split(':')[0])-int(d2.split(':')[0])
				if ds>=-2000 and ds<2000:
					chrD[keys].append(ds)
	return chrD

def getChrom(infdata):
	chrs={'CHR1':[],'CHR2':[],'CHR3':[],'CHR4':[],'CHR5':[],'CHR6':[],'CHR7':[],'CHR8':[],'CHR9':[],'CHR10':[],'CHR11':[],'CHR12':[],'CHR13':[],'CHR14':[],'CHR15':[],'CHR16':[],'CHR17':[],'CHR18':[],'CHR19':[],'CHR20':[],'CHR21':[],'CHR22':[],'CHRX':[],'CHRY':[]}
	for line in infdata:
		chrs_key=line.split()[0].upper()
		chrs_data=line.split()[1]+':'+line.split()[2]
		chrs[chrs_key].append(chrs_data)
	return chrs

def getlines(f):
	fs=[]
	for line in open(f):
		if ('chr' in line) and ('name' not in line):
			fs.append(line)
	return fs

def peaks(inf1, inf2):
	geneF1=getlines(inf1)
	geneF2=getlines(inf2)
	geneF1Data1=getChrom(geneF1)
	geneF1Data2=getChrom(geneF2)
	Distribution=distribution(geneF1Data1,geneF1Data2)
	return Distribution

def writeXLS(data,ofs):
	return

if __name__=='__main__':
	import argparse
	parser=argparse.ArgumentParser(description='Process peak cover distribution.')
	parser.add_argument('-p1',  type=str, required=True, help='first Gene peak bed file ')
	parser.add_argument('-p2', type=str, required=True, help='second Gene peak bed file ')
	parser.add_argument('-o',  type=str, required=True, help='Output data file ')
	args=parser.parse_args()
	data=peaks(args.p1, args.p2)
	opf=open(args.o, 'w')
	#data=peaks('AR_only.bed','spop.bed')
	#opf=open('AR_SPOP2k.txt','w')
	for keys in data.keys():
		for d in data[keys]:
			opf.write(str(d)+'\t')
	opf.close()