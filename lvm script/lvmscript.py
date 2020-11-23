#!/usr/bin/python3
import os

while(True):
  print("""      LVM AUTOMATION
        --------------
        
        1. LIST DISKS AND PARTITIONS
        2. CREATE PV
        3. DISPLAY PV
        4. CREATE VG
        5. DISPLAY VG
        6. CREATE LV
        7. DISPLAY LV
        8. EXTEND VG
        9. EXTEND LV
        10. MOUNT LV
        11. REDUCE LV
        12. VIEW MOUNTPOINTS

        0. TO EXIT
        
        What do you want to do ?""")
  ch = int(input())
  if (ch == 0):
      exit()
  elif (ch == 1):
      os.system("fdisk -l")
  elif (ch == 2):
      d = input("Enter disk name: ")
      os.system("pvcreate {}".format(d))
  elif (ch == 3):
      d = input("Enter disk name: ")
      os.system("pvdisplay {}".format(d))
  elif (ch == 4):
      d = input("Enter PV name: ")
      v = input("Enter VG name: ")
      os.system("vgcreate {} {}".format(v,d))
  elif (ch == 5):
      v = input("Enter VG name: ")
      os.system("vgdisplay {}".format(v))
  elif (ch == 6):
      l = input("Enter LV name: ")
      s = input("Enter LV size in GiB: ")
      v = input("Enter VG name: ")
      os.system("lvcreate --size {}G --name {} {}".format(s,l,v))
      os.system("mkfs.ext4 /dev/{}/{}".format(v,l))
  elif (ch == 7):
      l = input("Enter LV name: ")
      v = input("Enter VG name: ")
      os.system("lvdisplay {}/{}".format(v,l))
  elif (ch == 8):
      p = input("Enter PV name: ")
      v = input("Enter VG name: ")
      os.system("vgextend {} {}".format(v,p))
  elif (ch == 9):
      l = input("Enter LV name: ")
      v = input("Enter VG name: ")
      s = input("Enter additional size in GiB: ")
      os.system("lvextend --size +{}G /dev/{}/{}".format(s,v,l))
      os.system("resize2fs /dev/{}/{} ".format(v,l))
  elif (ch == 10):
      l = input("Enter LV name: ")
      v = input("Enter VG name: ")
      m = input("Enter absolute path of mountpoint: ")
      os.system("mount /dev/{}/{} {}".format(v,l,m))
  elif (ch == 11):
      f = input("Enter absolute path of mountpoint: ")
      l = input("Enter LV name: ")
      v = input("Enter VG name: ")
      s = input("Reduce to what size? ")
      os.system("umount {}".format(f))
      os.system("e2fsck -f /dev/mapper/{}-{}".format(v,l))
      os.system("resize2fs /dev/mapper/{}-{} {}G".format(v,l,s))
      os.system("lvreduce --size {}G /dev/mapper/{}-{}".format(s,v,l))
      os.system("mount /dev/mapper/{}-{} {}".format(v,l,f))
  elif (ch == 12):
      os.system("df -h")
  else:
      print("Incorrect Option")
