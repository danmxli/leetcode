#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <cpp_file>"
    exit 1
fi

if [[ ! $1 =~ \.cpp$ ]]; then
    echo "Error: File must be a .cpp file"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File $1 does not exist"
    exit 1
fi

# Get filename without extension
filename="${1%.*}"

# Compile
g++ -std=c++17 "$1" -o "$filename"

if [ $? -eq 0 ]; then
    # Run the program
    echo "Running $filename..."
    ./"$filename"
    
    # Clean up
    rm "$filename"
else
    echo "Compilation failed"
    exit 1
fi