#!/bin/bash
curl -IL $1| grep  -A5 "^HTTP/2 302" | grep "location:"  | cut -d ' ' -f2

#-A20 ==  first occurence of HTTP302 display  5 line after it
#cut -d ' '  -f2 == split the line and space and extract the second field