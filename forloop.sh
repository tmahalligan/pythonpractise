#!/bin/bash

for i in {1..3};
  do multipass launch -c 2 -m 2G -d 10G -n server$i
done
