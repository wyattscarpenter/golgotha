#!/usr/bin/env python3

import sys
import re
try:
  import regex
except:
  pass #TODO: I'm debating doing a shell command to install the regex package here
def eprint(*args, **kwargs):
  print(f"line {line_index}:",*args, file=sys.stderr, **kwargs)

debug = True #False #True

def dprint(*args, **kwargs):
  if debug: eprint(*args, **kwargs)

source_string = ""
line_index = 1
operator_rules = []
def main():
  global line_index
  global source_string
  if len(sys.argv) <= 1:
    print("USAGE: golgotha filenames_to_tranform...")
  else:
    for filename in sys.argv[1:]:
      with open("golgotha."+filename,"w",encoding='utf-8') as outfile:
        with open(filename,"r",encoding='utf-8') as infile:
          for line in infile:
            line_index += 1
            if line[0] == '🔣':
              #WARNING: this code contains regex operations on text that will be used for regex operations later. So, be wary of that.
              dprint("operator rule line encountered")
              rule = line[1:].strip('\n').split('🔜')
              dprint(rule)
              rule[0] = re.escape(rule[0]) # first, we escape
              dprint(rule[0])
              rule[0] = regex.sub("(\d)", r"[^\\S\\r\\n]*(?P<arg\1>\\w+|\(.*\))[^\\S\\r\\n]*", rule[0]) #now, we massage the string to be the regex we want #TODO: real nesting parens, using the "regex" package and something like \(([^()]|(?R))*\). Also for [] and {}.
              dprint(rule[0])
              rule[1] = re.sub("(\d)", r"\\g<arg\1>", rule[1]) #rhs of rule uses proper subs, using \g form for maximum disambiguation
              dprint(rule)
              operator_rules.append(rule)
              
            else:
              source_string += line #I don't remember if string += is valid in python
          for rule in operator_rules:
                source_string = regex.sub(rule[0], rule[1], source_string) #TODO: figure out if this works or if I need a global tag or whatever
          outfile.write(source_string)
main()