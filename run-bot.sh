#!/bin/bash

python get_device_indices.py
cd MED || exit
python local_try.py
