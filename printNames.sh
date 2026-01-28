#!/bin/bash

read -p "Enter your name: " name
read -p "Enter how many times to print: " n

for ((i=1; i<=n; i++))
do
    echo "$i. $name"
done
