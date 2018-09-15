##the script use for download kernel and auto update


#download latest kernel from kernel.org
import os
import sys
import re
import time
import urllib2
import commands
from bs4 import BeautifulSoup
from excepts import *

kernel_path = "/opt/kernel/"
kernelorg = "https://www.kernel.org/"
kernel_name = ""

def download_latest_kernel():
	html = urllib2.urlopen(kernelorg).read()
	soup = BeautifulSoup(html,'lxml')
	attr = soup.find('td',id="latest_link")
	download_link = attr.a['href']
	status,result = commands('wget link_address')
	time.sleep(600)
	if status != 0:
		try:
			raise DownloadException("kernel download failed, please check network.")
		except DownloadException as e:
			print e.message
			sys.exit(0)

def latest_kernel__chk():
	os.chdir(kernel_path)
	kernel_list = []
	latest_kernel = ""
	#remove dir from the floder
	for item in os.listdir(kernel_path):
		if os.path.isdir(item):
			os.system('rm -rf %s' %(item))
		else:
			pass
	#remove the file which is not kernel file
	for item in os.listdir(kernel_path):
		pattern = re.search('.tar.xz',item)
		if pattern:
			pass
		else:
			os.system('rm -rf %s' %(item))
	#modify the kernel file name uniformity
	kernel_list = os.listdir(kernel_path)
	kernel_list.sort()
	kernel_list.reverse()
	kernel_list = kernel[0:2:1]
	for item in os.listdir(kernel_path):
		if item not in kernel_list:
			os.system('rm -rf %s' %(item))
	latest_kernel = kernel_list[0]
	return latest_kernel

def kernel_install(kernel):
	kernel_name = kernel
	kernel_dir = 
	os.chdir(kernel_path)
	os.system('tar xvJf %s' %(kernel_name))
	kernel_dir = kernel_name.split('.tar.xz')[0] 
	os.chdir(kernel_dir)
	os.system('cp /boot/config-3.10.0-862.el7.x86_64 .config')
	os.system('cp /home/autotest/auto_kernel_update/build_kernel.sh ./')
	#judge the make kernel is successful or not, it's called a shell script
	status,result = commands.getstatusoutput('sh build_kernel.sh')
	if status != 0:
		try:
			raise BuildkernelException("kernel build failed, please try to build it manually.")
		except BuildkernelException as e:
			print e.message
			sys.exit(0)

	
	
			
		
	
	



			
		
		
	
	 

	
