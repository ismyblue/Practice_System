#！/usr/bin/python

import re,os

def getlikestr1(str):
	filenames = re.findall('"\./(.*?)"',str)
	for filename in filenames:
		str = re.sub('"\./('+filename+')"','\"{% static \'practice/' +filename+'\' %}\"', str)
	return str


def getlikestr2(str):
	str = re.sub('https://cdn.bootcss.com/Swiper/3.4.2/css/swiper.min.css','{% static \'practice/css/swiper.min.css\' %}', str)
	str = re.sub('https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js','{% static \'practice/js/jquery.min.js\' %}', str)
	str = re.sub('https://cdn.bootcss.com/Swiper/3.4.2/js/swiper.jquery.min.js','{% static \'practice/js/swiper.jquery.min.js\' %}', str)
	return str


if __name__ == '__main__':
	for file in os.listdir():
		if file.endswith('.html'):
			f = open(os.path.join('.', file),'r+', encoding='utf-8')			
			lines = f.readlines()
			f.seek(0)			
			for line in lines:
				line = getlikestr1(line)
				line = getlikestr2(line)
				f.write(line)
				if '<head>' in line:
					f.write('{% load static %}\n')
			f.close()
		print(file + 'done')
