#!/bin/bash
python storage.py

for i in {1..100}
do
	python indexer.py
done
