#!/usr/bin/python3

import re
import os
import sys

lines = sys.stdin.readlines()

l1 = []
l2 = []
l3 = []
l4 = []

lemma = sys.argv[1]
print(lemma)
if (lemma == 'AsymmetricNeedsCompromiseBefore'):

  for line in lines:
    num = line.split(':')[0]
    if re.match('.*!KU\(\s\~rk.*', line) or re.match('.*!KU\(.*h\(\~rk.*', line) or re.match('.*rk.* \u228F h\(~rk.*', line) or re.match('.*!KU\( \~new\_rk.*', line) or re.match('.*!KU\(.*h\(\~new\_rk.*', line) or re.match('.*!KU\(.*h\(pck.*', line):
      l1.append(num)
    elif re.match('.*!KU\(\s\~sck.*', line) or re.match('.*!KU\(.*h\(sck.*', line) or re.match('.*rk.* \u228F h\(sck.*', line):
      l2.append(num)
    elif re.match('.*GlobalSendChainKey\(.*\#v.*', line) or re.match('.*CompromisePartie\(.*\#vk.*', line):
      l3.append(num)
    elif re.match('.*StartChainRk\(.*\#j.*', line) or re.match('.*CompromisePartie\(.*\#j.*', line):
      l3.append(num)
    else :
      l4.append(num)

elif (lemma == 'rkImpo'):
  for line in lines:
      num = line.split(':')[0]
      if re.match('.*StartChainRk\(.*\#l.*', line) or re.match('.*KeyUpdate\(.*\#l.*', line):
        l1.append(num)  
      elif re.match('.*StartChainRk\(.*\#i.*', line):
        l2.append(num)  
      elif re.match('.*BookKeppingRootKeys\(.*\#l.*', line): 
        l2.append(num) 
      elif re.match('.*StartChainRk\(.*\#j.*', line):
        l3.append(num)  
      else :
       l4.append(num) 

elif (lemma == 'rkImpoBis'):
  for line in lines:
      num = line.split(':')[0]
      if re.match('.*StartChainRk\(.*\#l.*', line):
        l1.append(num)  
      elif re.match('.*StartChainRk\(.*\#i.*', line):
        l2.append(num)  
      elif re.match('.*GlovalSendChainKey\(.*\#j.*', line):
        l2.append(num) 
      elif re.match('.*BookKeppingGlobalRootKeys\(.*\#j.*', line): 
        l1.append(num)  
      else :
       l4.append(num)  

elif (lemma == 'NoDoubleRole'):
  for line in lines:
      num = line.split(':')[0]
      if re.match('.*GlobalSendChainKey\(.*\#i.*', line) or re.match('.*SendingChainKey\(.*\#i.*', line) :
        l1.append(num)  
      elif re.match('.*ReceivingChainKey\(.*\#j.*', line) or re.match('.*ReceiverChain\(.*\#j.*', line) :
        l2.append(num)  
      elif re.match('.*SendingChainKey\(.*\#vr.*', line):
        l3.append(num)
      else :
       l4.append(num)
       
elif (lemma == 'NoDoubleRoleSt2'):
  for line in lines:
      num = line.split(':')[0]
      if re.match('.*ReceiverChain\(.*\#j.*', line):
        l1.append(num)  
      elif re.match('.*ReceivingChainKey\(.*\#j.*', line):
        l2.append(num)  
      elif re.match('.*StartChainRkSnd\(.*\#i.*', line):
        l3.append(num) 
      else :
       l4.append(num)

elif (lemma == 'StartChainPreceededByAssociate'):
  for line in lines:
      num = line.split(':')[0]
      if re.match('.*StartChainRk\(.*\#i.*', line) or re.match('.*ReceivingChainKey\(.*\#i.*', line) or re.match('.*SendingChainKey\(.*\#i.*', line):
        l1.append(num)  
      elif re.match('.*: InitKeyExchange\(.*\#j.*', line) : 
        l2.append(num)  
      else :
       l4.append(num) 

elif (lemma == 'MonotonousAfterSend'):
  for line in lines:
      num = line.split(':')[0]
      if re.match('.*GlobalSendChainKey\(.*\#i.*', line)  :
        l1.append(num)  
      elif re.match('.*StartChainKey\(.*\#j.1.*', line) :
        l2.append(num)  
      elif re.match('.*SendingChainKey\(.*\#i.*', line) :
        l2.append(num)  
      else :
       l4.append(num)
else:
  pass

ranked = l1 + l2 + l3

for i in ranked:
  print(i)
