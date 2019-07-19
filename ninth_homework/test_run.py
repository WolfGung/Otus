#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import pytest
import allure
import logging
from ninth_homework.subprocess_user import SubprocessUser


@allure.title("001 Critical: Looking for eth0 status")
@allure.severity("critical")
@pytest.mark.test001
def test001():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "ip a | grep eth0"
        output = process.check_output(command)
    with allure.step("Parse main interface state"):
        process.byte_parser(output)
        process.interface_state_parser()
    with allure.step("Checking that main interface is UP"):
        process.interface_status_checker()


@allure.title("002 Critical: Looking for default route")
@allure.severity("critical")
@pytest.mark.test002
def test002():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "ip r | grep default"
        output = process.check_output(command)
    with allure.step("Parse default route data"):
        process.byte_parser(output)
    with allure.step("Checking default route state"):
        process.default_route_checker(default_ip='172.17.0.1', default_method='dev')


@allure.title("003 Critical: Looking for cpu workload")
@allure.severity("critical")
@pytest.mark.test003
def test003():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "sensors | grep Core | awk '{print $3}'"
        output = process.check_output(command)
    with allure.step("Parse cpu temperature"):
        process.byte_parser(output)
    with allure.step("Checking temperature"):
        process.temperature_checker()


@allure.title("004 Critical: Looking for cpu info")
@allure.severity("critical")
@pytest.mark.test004
def test004():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "cat /proc/cpuinfo"
        output = process.check_output(command)
    with allure.step("Parse cpu information"):
        process.byte_parser(output)
        process.cpu_info_model_parser()
    with allure.step("Checking cpu information"):
        cpu_parameters = ['Intel(R)', 'Core(TM)', 'i3-7100']
        process.cpu_info_checker(*cpu_parameters)


@allure.title("005 Critical: Looking for process resource costs")
@allure.severity("critical")
@pytest.mark.test005
def test005():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "ps aux | awk '{print $3}'"
        output = process.check_output(command)
    with allure.step("Parse process information"):
        coast = process.byte_parser(output)
        parsed_coast = coast[1:]
    with allure.step("Checking resource costs"):
        process.process_coast_checker(parsed_coast)


@allure.title("006 Critical: Looking for web interfaces statistic")
@allure.severity("critical")
@pytest.mark.test006
def test006():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "ifconfig"
        output = process.check_output(command)
    with allure.step("Parse ifconfig statistic"):
        ifconfig = process.byte_parser(output)
    with allure.step("Print and logging statistic"):
        print(ifconfig)
        logging.info("Interface statistic: {}".format(ifconfig))


# @allure.title("007 Critical: Looking for service status")
# @allure.severity("critical")
# @pytest.mark.test007
# def test007():
#     with allure.step("Input command and take output"):
#         service_name = "ssh"
#         process = SubprocessUser()
#         command = "service {} status | grep Active".format(service_name)
#         output = process.check_output(command)
#     with allure.step("Parse ifconfig statistic"):
#         process.byte_parser(output)
#     with allure.step("Checking service status"):
#         process.service_status_checker()


@allure.title("008 Critical: Looking for tcp/udp port status")
@allure.severity("critical")
@pytest.mark.test008
def test008():
    with allure.step("Input command and take output"):
        process = SubprocessUser()
        command = "netstat -ntlp | grep LISTEN | awk '{print $4}'"
        output = process.check_output(command)
    with allure.step("Parse port statistic"):
        port_statistic = process.byte_parser(output)
    with allure.step("Printing and logging udp/tcp ports with LISTEN status"):
        print(port_statistic)
        logging.info("UDP/TCP ports with LISTEN status: {}".format(port_statistic))


@allure.title("009 Critical: Looking for package version")
@allure.severity("critical")
@pytest.mark.test009
def test009():
    with allure.step("Input command and take output"):
        package_name = "php-curl"
        process = SubprocessUser()
        command = "dpkg --list | grep {} | awk '{{print $3}}'".format(package_name)
        output = process.check_output(command)
    with allure.step("Parse package version"):
        package_version = process.byte_parser(output)
    with allure.step("Printing and logging package version"):
        print(package_version)
        logging.info("Package {} has version {}".format(package_name, package_version))


@allure.title("010 Critical: Looking for files in directory")
@allure.severity("critical")
@pytest.mark.test010
def test010():
    with allure.step("Input command and take output"):
        directory = "/home/zhukov/Documents"
        command = "cd {}; ls -l".format(directory)
        process = SubprocessUser()
        output = process.check_output(command)
    with allure.step("Parse directory content"):
        content = process.byte_parser(output)
    with allure.step("Printing and logging directory content"):
        print(content)
        logging.info("Directory with path '{}' has content '{}'".format(directory, content))


@allure.title("011 Critical: Looking for current directory")
@allure.severity("critical")
@pytest.mark.test011
def test011():
    with allure.step("Input command and take output"):
        command = "echo $PWD"
        process = SubprocessUser()
        output = process.check_output(command)
    with allure.step("Parse current directory information"):
        dir_info = process.byte_parser(output)
    with allure.step("Printing and logging current directory path"):
        print(dir_info)
        logging.info("Current directory path: {}".format(dir_info))


@allure.title("012 Critical: Looking for core version")
@allure.severity("critical")
@pytest.mark.test012
def test012():
    with allure.step("Input command and take output"):
        command = "uname -a"
        process = SubprocessUser()
        output = process.check_output(command)
    with allure.step("Parse core information"):
        core_info = process.byte_parser(output)[2]
    with allure.step("Printing and logging core info"):
        print(core_info)
        logging.info("Core version is: {}".format(core_info))


@allure.title("013 Critical: Looking for operation system version")
@allure.severity("critical")
@pytest.mark.test013
def test013():
    with allure.step("Input command and take output"):
        command = " lsb_release -a | grep Description | awk '{print $2 $3 $4}'"
        process = SubprocessUser()
        output = process.check_output(command)
    with allure.step("Parse operation system information"):
        os_info = process.byte_parser(output)
    with allure.step("Printing and logging operation system info"):
        print(os_info)
        logging.info("Core version is: {}".format(os_info))
