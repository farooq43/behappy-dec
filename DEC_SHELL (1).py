# author : @Exa21
# -*- coding: utf-8 -*-


import os
import sys
import fileinput
os.system("clear")

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'
wait = Y + '[' + W + "Wait" + Y + ']' + W
banner = """
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{}ᴍᴀᴅᴇ ʙʏ{} : {}💎 @Exa21 💎
{}ᴍᴏᴅɪғɪᴇᴅ ʙʏ{} : {}💮 @makimmm 💮
{}ʏᴏᴜᴛᴜʙᴇ{} : {} makim Channel
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""".format(G,Y,W,B,Y,W,B,Y,W,B,G)
banner2 = """
   {}[{}1{}]{} [ᎠᎬᏟ]ʟᴏɴɢ ᴇɴᴄʀʏᴘᴛ      
   {}[{}2{}]{} [ᎠᎬᏟ]ᴛᴇʀᴍᴜx ᴇɴᴄʀʏᴘᴛ
   
   
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""".format(G,W,G,W,G,W,G,W,G)

print banner
print banner2

def darkingenc():
   try:
        sc = raw_input(ask + W + "ɴᴀᴍᴇ sʜ " + G + "> " + W)
        f = open(sc,'r')
        filedata = f.read()
        f.close()
        
        newdata = filedata.replace("eval $@","echo $@")
        renameback = filedata.replace("echo $@","eval $@")

        f = open(sc,'w')
        f.write(newdata)
        f.close()
       
        print (wait + "Proccecing")
        
        os.system("touch makim_Tools.sh")
        os.system("bash " + sc)
        os.system("clear")
        print "ᴡᴀɪᴛɪɴɢ ғɪʟᴇ ᴛᴏ sᴀᴠᴇ"
        os.system("bash " + sc + " > makim_Tools.sh")
        os.rename("makim_Tools.sh","[woa].)" + sc)
        
        f = open(sc,'w')
        f.write(renameback)
        f.close()
        
        print (sukses + "ᴅᴏɴᴇ ᴅᴇᴄʀʏᴘᴛ sʜᴇʟʟ,ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ғᴏʟᴅᴇʀ ᴀɢᴀɪɴ")

   except KeyboardInterrupt:
       print (eror + " sᴛᴏᴘᴘᴇᴅ!")
   except IOError:
       print (eror + " ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ!")
       
def simpleenc():
   try:
       sc = raw_input(ask + W + "ɴᴀᴍᴇ sʜ " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")
       renameback = filedata.replace("echo","eval")
       
       f = open(sc,'w')
       f.write(newdata)
       f.close()

       os.system("touch makim_Proccecing.sh")
       os.system("bash " + sc)
       os.system("clear")
       print "ᴡᴀɪᴛɴɢ ғɪʟᴇ ᴛᴏ sᴀᴠᴇ"
       os.system("bash " + sc + " > ᴍᴀᴋɪᴍ_ᴘʀᴏᴄᴇss.sh")
       
       f = open(sc,'w')
       f.write(renameback)
       f.close()
       
       os.rename("ᴍᴀᴋɪᴍ_ᴘʀᴏᴄᴇss.sh","[woa]" + sc)
       print (sukses + "ᴅᴏɴᴇ ᴅᴇᴄʀʏᴘᴛ sʜᴇʟʟ,ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ғᴏʟᴅᴇʀ ᴀɢᴀɪɴ")

   except KeyboardInterrupt:
       print (eror + " sᴛᴏᴘᴘᴇᴅ!")
   except IOError:
       print (eror + " ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ!")

makim = raw_input(W + "ᴄʜᴏᴏsᴇ" + G + " > ")
if makim == "1" or makim == "01":
   darkingenc()
elif makim == "2" or makim == "02":
   simpleenc()
else:
        print (eror + " ᴡʀᴏɴɢ ɪɴᴘᴜᴛ !")