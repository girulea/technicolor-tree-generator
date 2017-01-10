from node import Node
from tree import Tree
from writer import Writer
from itertools import groupby
import threading
import sys
import re

class Pruner(threading.Thread):

  def __init__(self, node, w):
    threading.Thread.__init__(self)
    self.node = node;  
    self.writer_queue = w

  def run(self):
  	self.develop_node(self.node)

  def develop_node(self, n):
     if len( n.get_data()) < 10:
      self.add_node_child(n)
      self.prunes_nodes(n)
      nodes = n.get_child()
      for nds in nodes:
       self.develop_node(nds)
       n.remove_child(nds)  
     else:
      if self.check_key(n):
        self.writer_queue.add(n.get_data()+'\n')
        #n.get_dad().remove_child_lm(n)

  def add_node_child(self, n):
  	pre = n.get_data()
  	for c in charset:
  		n_node = Node( pre + c , n)
  		n.add_child(n_node)

  def check_key(self,n):
    cond = True
    if self.control_rules1(n,1,5) == False or self.control_rules2(n)== False or self.control_rules3(n) == False or self.control_rules4(n) == False:
      cond = False
    return cond

  def check_node(self,n):
    cond = True
    if self.control_rules1(n,0,5) == False or self.control_rules2(n)== False or self.control_rules3(n) == False or self.control_rules4(n) == False:
      cond = False
    return cond

  def prune_node(self,n):
    if not self.check_node(n):
      n.get_dad().remove_child(n)

  def prunes_nodes(self, n):
   nodes = n.get_child()
   for node in nodes:
    self.prune_node(node)

  def control_rules1(self, n, mn, mx):
   tmp_charset = list('ABCDEF')
   data = n.get_data()
   condiction = True
   num = 0
   for c in tmp_charset:
    num += data.count(c)
   if num > mx or num < mn:
    condiction = False
   return condiction


  def control_rules2(self, n):
   condiction = True
   search = re.search(r"(\w)\1{2,}", n.get_data())
   if search:
    condiction = False
   return condiction

  def control_rules3(self, n):
    condiction = True
    search = re.search(r"([0-9]).*\1.*\1", n.get_data())
    if search:
      condiction = False
    return condiction

  def control_rules4(self, n):
    condiction = True
    search = re.search(r"([A-Z]).*\1.*\1.*\1", n.get_data())
    if search:
      condiction = False
    return condiction


   

  def find(self,strng, char):
  	num = 0
  	index = 0
  	while index < len(strng):
  		index = strng.find(char, index)
  		if index == -1:
  			break
  		num += 1
  		index += 1
  	return num

charset = list('0123456789ABCDEF')
tree = Tree()
root = Node('', None)
tree.add_root(root)
w = Writer('/root/dict2.txt')
w.start()
#prnr = Pruner(root, w)
#prnr.start()
for c in charset:
  node = Node(c,root)
  prnr = Pruner(node, w)
  root.add_child(node)
  prnr.start()
