import os
import subprocess
import time as t
def program1():
    os.system("export TERM=xterm;clear")
    print("\t\t\t\t\tWELCOME TO REMOTE-SIDE") 
    print("""
            1) Press 1 for HADOOP SERVICES with LVM SERVICE
            2) Press 2 for WEB SERVICES
            3) Press 3 DOCKER WORLD
            4) Press 4 LVM SERVICES
            5) Press 5 for AWS services
            6) Press 6 for Linux basic commands
            7) Press 7 Exit""")
    x = int(input("ENTER YOUR CHOICE:"))
    if x==1:
       def hadoop():
          os.system("export TERM=xterm;clear")
          jdk=subprocess.getstatusoutput("jps")
          if jdk[0]==127:			
             print("\n\n--------jdk installing---------")
             subprocess.getstatusoutput("rpm -ivh jdk-8u171-linux-x64.rpm")
             print("Installation Completed")
          else:             
             print("JDK requirement  already satisfied")
          hadoop=subprocess.getstatusoutput("hadoop version")
          if hadoop[0]==127:
             print("------------Hadoop installing-----------")
             subprocess.getoutput("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
             print("\n\n----HADOOP SUCCESSFULLY INSTALLED----")
          else:
               print("Hadoop requirement already satisfied")
               t.sleep(1)
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
                    os.system("hadoop-daemon.sh stop namenode;jps")
          elif y==7:
                    os.system("export TERM=xterm;clear")
                    program1()
                    
       hadoop()
    elif x==2:
        os.system("tput setaf 6;cd /etc/yum.repos.d/;wget https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm;wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm;wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm;wget https://www.elrepo.org/RPM-GPG-KEY-elrepo.org;wget http://repo.webtatic.com/yum/el7/webtatic-release.rpm")
        file1=open("/etc/yum.repos.d/soft.repo", 'w')
        file1.write("""[DVD1]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/AppStream
gpgcheck=0

[DVD2]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/BaseOS
gpgcheck=0""")
        file1.close()
        os.system("yum install httpd")
        os.system("systemctl stop firewalld;setenforce 0;systemctl start httpd")
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
               dynamic_size =int(input("ENTER THE SIZE YOU WANT TO CREATE: "))
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
                  os.system(f"umount {lv_name} {mounting_point};e2fsck -ff {lv_name};resize2fs {lv_name} {final_size}G;lvreduce --size -{lv_reduce_size}G {lv_name};resize2fs {lv_name};mount {lv_name} {mounting_point}")
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
         def ec2():
             os.system("export TERM=xterm;clear")
             x=subprocess.getstatusoutput("aws")
             if x[0]==252:
                print("already installed")
             else:
                os.system("curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip;unzip awscliv2.zip;sudo ./aws/install;aws configure")

             print("\t\t\t\tWELCOME TO WORLD OF AWS")
             print("""
                                    A) Press 1 For Linux SERVER
                                    B) Press 2 For RHEL8 SERVER
                                    C) Press 3 For SUSE SERVER
                                    D) Press 4 FOR Ubuntu SERVER
                                    E) Press 5 For Window SERVER
                                    F) Press 6 For Window SERVER with Container
                                    G) Press 7 For Cloud Front Service
				    F) Press 8 For S3 Service 
				    H) Press 9 For EBS Volume
                                    I) Press 10 Back """)
             y=int(input("ENTER YOUR CHOICE : "))
             if y==1:
                os.system("aws ec2 run-instances --image-id  ami-0e306788ff2473ccb  --count 1 --instance-type t2.micro --key-name  Mykeyn  --security-groups MySecurityGroupn")
                print("\n\-------------------Instance has been Launched---------------")
             elif y==3:
                os.system("aws configure;aws ec2 run-instances --image-id ami-0d0522ed4db1debd6  --count 1 --instance-type t2.micro --key-name  Mykeyn  --security-groups MySecurityGroupn")
             elif y==4:
                os.system("aws configure;aws ec2 run-instances --image-id  ami-0cda377a1b884a1bc  --count 1 --instance-type t2.micro --key-name  Mykeyn  --security-groups MySecurityGroupn")
                print("\n\-------------------Your Ubuntu Instance has been launched---------------")
             elif y==5:
                os.system("aws configure;aws ec2 run-instances --image-id  ami-0b2f6494ff0b07a0e  --count 1 --instance-type t2.micro --key-name  Mykeyn  --security-groups MySecurityGroupn")
                print("\n\-------------------Your Window Server has been launched---------------")
             elif y==6:
                os.system("aws configure;aws ec2 run-instances --image-id  ami-0295b81b270caa9d2 --count 1 --instance-type t2.micro --key-name  Mykeyn  --security-groups MySecurityGroupn")
                print("\n\-------------------Your Window Server With Containers has been launched---------------")
             elif y==2:
                os.system("aws configure;aws ec2 run-instances --image-id ami-052c08d70def0ac62  --count 1 --instance-type t2.micro --key-name  Mykeyn  --security-groups MySecurityGroupn;tput setaf 3;echo '---------------RHEL8 MACHINE HAS BEEN LAUNCHED --------'")
             elif y==7:
                origin_domain_name =input("Give Your S3 Bucket Name : ")
                os.system(f"aws cloudfront create-distribution --origin-domain-name {origin_domain_name}.s3.amazonaws.com")
             elif y==8:
                bucket_name =input("Enter Your Bucket Name : ")
                os.system(f"aws s3 mb s3://{bucket_name}")
             elif y==9:
                      def  ebs():
                         os.system("export TERM=xterm;clear;aws configure")
                         print("\t\t\t\tWELCOME TO WORLD OF AWS")
                         print("""
                                 A) Press 1 For Create Volume
                                 B) Press 2 For Attach Volume In Ec2
                                 C) Press 3 For Create Snapshot/Backup of your Volume
                                 D) Press 4 For Detach volume
                                 E) Press 5 For Modify Volume
                                 F) Press 6 For Describe the Volume
                                 G) Press 7 Back""")
                         y=int(input("ENTER YOUR CHOICE : "))
                         if y==1:
                                Volume_type=input("\n Enter Volume Type : ")
                                Availability_zone=input("\n Enter Availabilty Zone : ")
                                size=input("\n Enter Volume Size : ")
                                os.system(f"aws ec2 create-volume --volume-type {Volume_type} --availability-zone {Availability_zone} --size {size}")
                                print("\n\-------------------Volume has been Created---------------")
                         elif y==2:
                                  Voulme_id=input("\n Enter Volume id: ")
                                  Instance_id=input("\n Enter Instance Id: ")
                                  os.system(f"aws ec2 attach-volume --volume-id {Volume_id} --instance-id {Instance_id} --device /dev/sdf")
                                  print("\n\--------------------------Volume has been Attached------------------------------")
                         elif y==3:
                                  Voulme_id=input("\n Enter Volume id: ")
                                  Description=input("\n Enter Description")
                                  os.system(f"aws ec2 ceate-snapshot --voulme-id {Voulme_id} --description  {' Description '} ")
                                  print("\n\-------------------------- Snapshot of your voulme has been created------------------------------")
                         elif y==4:
                                  Voulme_id=input("\n Enter Volume id: ")
                                  os.system(f"aws ec2 detach-voulme --voulme-id {Voulme_id} ")
                                  print("\n\-------------------------your voulme has been detachted------------------------------")
                         elif y==5:
                                  Voulme_id=input("\n Enter Volume id: ")
                                  size=input("\n Enter Size : ")
                                  os.system(f"aws ec2 modify-voulme --size {size}  --voulme-id {Voulme_id} ")
                                  print("\n\-------------------------Volume has been modified------------------------------")
                         elif y==6:
                                 Voulme_id=input("\n Enter Volume id: ")
                                 os.system(f"aws ec2  describe-volumes   --voulme-ids {Voulme_id} ")
                                 print("\n\-------------------------Above are the details of Volume------------------------------")
                         elif y==7:
                                 os.system("export TERM=xterm;clear")
                                 ec2()
                      ebs()
             elif y==10:
                       os.system("export TERM=xterm;clear")
                       program1()		  
         ec2()
    elif x==6:
         def linux_commands():
             os.system("export TERM=xterm;clear")
             print("\t\t\t\tWELCOME TO WORLD OF LINUX")
             print("""
                    A) Press 1 For Calender
                    B) Press 2 For Date 
                    C) Press 3 For Making Directory
                    D) Press 4 For Deleting Directory
                    E) Press 5 For Ping
                    F) Press 6 For For Checking System IP
                    G) Press 7 FOR Listing Files in a Director
                    H) Press 8 For Calculator
                    I) Press 9 For reading a file content
                    J) Press 10 For creating a file 
                    K) Press 11 For View all Disk Partitions in Linux
                    L) Press 12 For View Specific Disk Partition in Linux
                    M) Press 13 For Checking File System Disk Space Usage
                    N) Press 14 For Checking The Software Exists Or Not
                    O) Press 15 For Finding Path Of Software Installed In Linux
                    P) Press 16 For Back""")
                
             y=int(input("ENTER YOUR CHOICE : "))
             if y==1:
                os.system("cal")
             elif y==3:
                   dir1 = input("\n GIVE NAME OF YOUR DIRECTORY WITH PATH ")
                   os.system(f"mkdir {dir1}")
             elif y==4:
                   dir1 = input("ENTER YOUR DIRECTORY NAME TO DELETE: ")
                   os.system(f"rmdir {dir1}")
             elif y==5:
                   pong = input("ENTER THE IP OR HOSTNAME YOU WANT TO PING: ")
                   os.system(f"ping -c 7 {pong}")
             elif y==6:
                   os.system("ifconfig")
             elif y==7:
                   list1 = input("TO LIST ENTER THE DIRECTORY PATH AS /root/.../...")
                   os.system(f"ls {list1}")
             elif y==8:
                  os.system("bc")
             elif y==2:
                  os.system("date")
             elif y==9:
                  filename = input("ENTER THE FILE PATH YOU WANT TO READ")
                  os.system(f"cat {filename}")
             elif y==10:
                   filename = input("ENTER THE FILE PATH YOU WANT TO CREATE")
                   os.system(f"vi {filename}")
             elif y==11:
                   os.system("fdisk -l")
             elif y==12:
                   diskName = input("ENTER DISK NAME LIKE /dev/sdb")
                   os.system(f"fdisk -l {diskName}")
             elif y==13:
                   os.system("df -h")
             elif y==15:
                   software_name =  input("ENTER THE SOFTWARE NAME OF WHICH LOCATION YOU WANT")
                   os.system(f"which {software_name}")
             elif y==14:
                   software_name =  input("ENTER THE SOFTWARE NAME ")
                   os.system(f"rpm -q {software_name}")
             elif y==16:
                   os.system("clear")
                   program1()
         linux_commands()
    elif x==7:
         os.system("export TERM=xterm;clear")
         exit()
    
    xit = input("WANT TO CONTINUE FROM SERVER MENU[Y/N] : ").upper()
    if xit =="Y":
       program1()
    else:
       exit()
program1()
