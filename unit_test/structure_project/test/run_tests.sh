#!/bin/bash
# to run the unittest defined in the test folder, you need to run in the project folder
#source: https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
# you can test one unit test or all unit tests

cd ..
python -m unittest test.test_prime
python -m unittest discover
