import os
import time as t
def program1():
	os.system("export TERM=xterm;clear")
	print("\t\t\t\t\t--------------WELCOME TO REMOTE-SERVER-----------------")
	print("""
		1) Press 1 for HADOOP SERVICES with LVM SERVICE
		2) Press 2 for WEB SERVICES
		3) Press 3 DOCKER WORLD
		4) Press 4 LVM SERVICES
		5) Press 5 Exit""")
	x = int(input("\nENTER YOUR CHOICE:"))
	if x==1:
		def hadoop():
			os.system("export TERM=xterm;clear")
			print("\t\t\t\tWELCOME TO HADOOP WORLD")
			print("""
				A) Press 1 For Starting Datanode Services
				B) Press 2 For Starting Namenode Services
				C) Press 3 For Client Services
				D) Press 4 To Check Cluster Report
				E) Press 5 To Stop Datanode
				F) Press 6 To Stop Namenode 
				G) Press 7 Back""")
			y=int(input("ENTER YOUR CHOICE : "))
			if y==1:
				os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
				print("\n\n--------jdk installed now hadoop installing-----------")
				t.sleep(1)
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				print("\n\n----HADOOP SUCCESSFULLY INSTALLED----")
				os.system("jps;hadoop version")
				disk_name=input("\nENTER THE DEVICE NAME FOR SHARING STORAGE : ")
				storage_size=int(input("\nENTER THE STORAGE SIZE YOU WANT TO SHARE : "))
				os.system(f"pvcreate {disk_name};vgcreate user_vg {disk_name};lvcreate --size +{storage_size}G ---name user_LVM user_vg;mkfs.ext4 /dev/user_vg/user_LVM")
				print("\n\n--------CONFIGURING DATANODE---------")
				t.sleep(1)
				os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
				dataip=input("\nENTER THE IP ADDRESS OF NAMENODE : ")
				dataport=int(input("\nENTER THE PORT NO :"))
				datadir=input("\nENTER THE DIRECTORY NAME YOU WANT : ")
				os.system(f"rm -rf /{datadir};mkdir /{datadir};mount /dev/user_vg/user_LVM /{datadir};df -h;echo 3 >/proc/sys/vm/drop_caches")  
				datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
				datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{datadir}</value>
</property>
</configuration>''')
				datafile.close()
				datafile1=open("/etc/hadoop/core-site.xml", 'w')
				datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
				datafile1.close()
				os.system("hadoop-daemon.sh start datanode;hadoop-daemon.sh stop datanode;hadoop-daemon.sh start datanode;jps")			
				os.system("systemctl stop firewalld;setenforce 0")			
				print("\n\n------------------Datanode Is Started--------------")
			elif y==2: 
				os.system("rpm -ivh jdk-8u171-linux-x64.rpm;rpm -ivh hadoop-1.2.1-1.x86_64.rpm  --force;jps;hadoop version")
				print("\n\n---------jdk installed and hadoop installed------")
				t.sleep(1)
				print("\n\n--------------CONFIGURING NAMENODE-----------")
				t.sleep(1)
				os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
				dataip=input("\nENTER THE IP ADDRESS TO GIVE MASTER : ")
				dataport=int(input("\nENTER THE PORT NO :"))
				datadir=input("\nENTER THE DIRECTORY NAME YOU WANT : ")
				os.system(f"rm -rf /{datadir};mkdir /{datadir}")  
				datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
				datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{datadir}</value>
</property>
</configuration>''')
				datafile.close()
				datafile1=open("/etc/hadoop/core-site.xml", 'w')
				datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
				datafile1.close()
				os.system("hadoop namenode -format;echo 3>/proc/sys/vm/drop_caches;systemctl stop firewalld;setenforce 0;hadoop-daemon.sh start namenode;jps")						
				print("\n\n--------------Namenode Is Started----------")
			elif y==3:
				os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
				print("\n\n---------jdk install now hadoop installing------")
				t.sleep(1)
				os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
				print("\n\n----------HADOOP SUCCESSFULLY INSTALLED---------")
				os.system("jps;hadoop version")
				print("\n\n--------------CONFIGURING CLIENT-----------")
				t.sleep(1)
				os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
				dataip=input("\nENTER THE IP ADDRESS OF NAMENODE : ")
				dataport=int(input("\nENTER THE PORT NO :"))
				datafile1=open("/etc/hadoop/core-site.xml", 'w')
				datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{dataip}:{dataport}</value>
</property>
</configuration>''')
				datafile1.close()			
				os.system("systemctl stop firewalld;setenforce 0")			
				print("\n\n--------------Client Service Started----------")
			elif y==4:			
				os.system("hadoop dfsadmin -report")
			elif y==5:
				os.system("hadoop-daemon.sh stop datanode;jps")
			elif y==6:
				os.system("hadoop-daemon.sh start namenode;jps")
			elif y==7:
				os.system("export TERM=xterm;clear")
				program1()
		hadoop()
	elif x==2:
		os.system("export TERM=xterm;clear;cd /etc/yum.repos.d/;wget https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm;wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm;wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm;wget https://www.elrepo.org/RPM-GPG-KEY-elrepo.org;wget http://repo.webtatic.com/yum/el7/webtatic-release.rpm")
		file1=open("/etc/yum.repos.d/soft.repo", 'w')
		file1.write("""[DVD1]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/AppStream
gpgcheck=0

[DVD2]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/BaseOS
gpgcheck=0""")
		file1.close()
		print("\n---------------INSTALLING HTTPD----------------------------------------------")
		os.system("yum install httpd")
		os.system("systemctl stop firewalld;setenforce 0")
		print("------------------------------YOUR WEB SERVICE HAS STARTED----------------------")
	elif x==3:
		def docker():
			os.system("export TERM=xterm;clear")
			print("\t\t\t\tWELCOME TO WORLD OF DOCKER")
			print("""
				A) Press 1 For Installing Docker
				B) Press 2 For Start docker service 
				C) Press 3 For Launch Container 
				D) Press 4 For Start Container
				E) Press 5 For Stop Container
				F) Press 6 For Status Of Containers
				G) Press 7 FOR Delete Containers
				H) Press 8 For Delete Image 
				I) Press 9 For Stop docker service
				J) Press 10 For Status docker service
				K) Press 11 Back""")
			y=int(input("ENTER YOUR CHOICE : "))
			if y==1:
				os.system("cd /etc/yum.repos.d/;wget https://download.docker.com/linux/centos/docker-ce.repo;yum install docker-ce --nobest")
				print("\n\-------------------docker has been installed---------------")
			elif y==3:
				image = input("\nGIVE THE IMAGE NAME : ")
				version = input("\nENTER VERSION : ")
				os_name = input("\nENTER YOUR OS NAME : ")
				os.system(f"docker pull {image}:{version};clear;docker run -it --name {os_name} {image}:{version} ")
			elif y==4:
				os_name = input("ENTER YOUR OS NAME TO START: ")
				os.system(f"docker start {os_name}")
			elif y==5:
				os_name = input("ENTER YOUR OS NAME TO STOP: ")
				os.system(f"docker stop {os_name}")
			elif y==6:
				os.system("docker ps -a")
			elif y==7:
				os_name = input("ENTER YOUR OS NAME TO DELETE: ")
				os.system(f"docker rm {os_name}")
			elif y==8:
				image_name = input("\nENTER YOUR IMAGE NAME TO DELETE: ")
				version = int(input("\nENTER VERSION : "))
				os.system(f"docker rmi {image_name}:{version}")
			elif y==9:
				os.system("systemctl stop docker;tput setaf 3;echo '---------------YOUR DOCKER SERVICE STOPPED ---------'")
			elif y==10:
				os.system("systemctl status docker")
			elif y==2:
				os.system("systemctl start docker;tput setaf 3;echo '---------------YOUR DOCKER SERVICE STARTED --------'")
			elif y==11:
				os.system("export TERM=xterm;clear")
				program1()
		docker()
	elif x==4:
		def lvm():
			os.system("export TERM=xterm;clear")
			print("\t\t\t\tWELCOME FOR LVM SERVICES")
			print("""
				A) Press 1 For Static To Dynamic
				B) Press 2 For Extend Your LVM Size  
				C) Press 3 For Reduce Your LVM Size
				D) Press 4 FOr Extend Your Volume Group Size 
				E) Press 5 For Remove LVM
				F) Press 6 For Remove Volume Group
				G) Press 7 For Remove Physical Volume
				H) Press 8 Back""")
			y=int(input("ENTER YOUR CHOICE : "))
			print()
			if y==1:
				static_volume=input("GIVE THE PATH OF YOUR STATIC VOLUME: ")
				print()
				dynamic_size =int(input("ENTER THE SIZE YOU WANT TO CREATE : "))
				print()
				user_vg=input("ENTER THE VOLUME GROUP NAME : ")
				print()
				user_lv=input("ENTER THE LOGICAL VOLUME NAME : ")
				print()
				os.system(f"pvcreate {static_volume};vgcreate {user_vg} {static_volume};lvcreate --size +{dynamic_size}G --name {user_lv} {user_vg};mkfs.ext4 /dev/{user_vg}/{user_lv};mkdir /user_dir;mount /dev/{user_vg}/{user_lv} /user_dir;df -h")
				print("\n\n------------------YOUR STATIC VOLUME CONVERTED TO DYNAMIC ---------------")
			elif y==2:
				lv_name=input("Give Your LV Path : ")
				print()
				lv_extend_size=int(input("How much You Want To Extend In GB : "))
				print()
				os.system(f"e2fsck -ff {lv_name};lvextend --size +{lv_extend_size}G {lv_name};fsadm resize {lv_name}")
			elif y==3:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print()
				lv_reduce_size=int(input("How much You Want To Reduce In GB : "))
				print()
				final_size=int(input("How Much Size DO You Want After Reducing :"))
				print() 
				os.system(f"umount -v {mounting_point};e2fsck -ff {lv_name};resize2fs {lv_name} {final_size}G;lvreduce --size -{lv_reduce_size}G {lv_name};resize2fs {lv_name};mount {lv_name} {mounting_point}")
			elif y==4: 
				device_name=input("Give Your Deivce Name : ")
				print()
				vg_name=input("Give Your Volume Group Name : ")
				print() 
				os.system(f"pvcreate {device_name};vgextend {vg_name} {device_name}")
			elif y==5:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print() 
				os.system(f"umount -v {mounting_point};lvremove {lv_name}")
			elif y==6:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print() 
				vg_name=input("Give Your VG Name : ")
				print()
				os.system(f"umount -v {mounting_point};lvremove {lv_name};vgremove {vg_name}")
			elif y==7:
				mounting_point=input("Give Your LVM Mount Point: ")
				print()
				lv_name=input("Give Your LV Path : ")
				print() 
				vg_name=input("Give Your VG Name : ")
				print()
				pv_name=input("Give Your PV Name : ")
				print()
				os.system(f"umount -v {mounting_point};lvremove {lv_name};vgremove {vg_name};pvremove {pv_name}")
			elif y==8:
				os.system("export TERM=xterm;clear")
				program1()
		lvm()
	elif x==5:
		exit()
	print()
	xit=input("WANT TO RUN AGAIN SERVER SIDE[Y/N] : ").upper()
	if xit == "Y":
		program1()
	else:
		exit()
program1()	
