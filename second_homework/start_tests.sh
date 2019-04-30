#!/bin/bash

cd `dirname $0`

run_suite_one()
{
pytest -s ./test_suites/test_suite_1.py
}

run_suite_two()
{
pytest -s ./test_suites/test_suite_2.py
}

run_suite_three()
{
pytest -s ./test_suites/test_suite_3.py
}

run_all_suites()
{
pytest -s ./test_suites/
}

usage ()
{
echo "-1 - run first site test suite"
echo "-2 - run second site test suite"
echo "-3 - run third site test suite"
echo "-4 - run all suites"
}

if [ -z $* ]
then
usage
exit 1
fi


while getopts "1234" opt
do
case $opt in
1) run_suite_one;;
2) run_suite_two;;
3) run_suite_three;;
4) run_all_suites;;

esac
done
