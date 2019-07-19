#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import logging
import subprocess


class SubprocessUser:
    def __init__(self):
        self.host = '127.0.0.1'
        self.output = None
        self.command = list()
        self.data = None
        self.interface_state = None
        self.model = list()

    def check_output(self, arg):
        for i in arg:
            self.command.append(i)
        try:
            self.output = subprocess.check_output(arg, shell=True)
            if self.output is not None:
                logging.debug("System output is {}".format(self.output))
            else:
                logging.info("There are no output for command {}".format(self.command))
        finally:
            return self.output

    def byte_parser(self, byte_code):
        data = (byte_code.decode(encoding="ISO-8859-1"))
        self.data = data.split()
        logging.info("Converted byte_code looks like: {}".format(self.data))
        return self.data

    def interface_state_parser(self):
        counter = 0
        for i in self.data:
            counter += 1
            if i == 'state':
                self.interface_state = self.data[counter]
        if self.interface_state is not None:
            logging.info("Interface state is: {}".format(self.interface_state))
        else:
            logging.error("Can't parse interface state!")
        return self.interface_state

    def interface_status_checker(self):
        if self.interface_state == "UP":
            logging.info("Status successfully checked")
        else:
            raise AttributeError("Interface is not UP!")

    def default_route_checker(self, default_method, default_ip):
        if default_method and default_ip in self.data:
            logging.info("Default route ip is: {} and protocol: {}".format(default_ip, default_method))
        else:
            raise AttributeError("Default route doesn't corresponds to inputed")

    def cpu_info_model_parser(self):
        counter = 0
        for i in self.data:
            counter += 1
            if i == "model" and self.data[counter] == "name":
                for j in range(4):
                    counter += 1
                    self.model.append(self.data[counter])
        self.model.remove(':')
        return self.model

    def cpu_info_checker(self, *cpu_parameters):
        for par in cpu_parameters:
            if par not in self.model:
                raise AttributeError("Parameter {} not in cpu information".format(par))
            else:
                continue

    def temperature_checker(self):
        for i in self.data:
            temp = int(i[1:3])
            if temp > 80:
                raise ArithmeticError("Temperature of cpu more than 80 degrees!!!")
            else:
                continue

    @staticmethod
    def process_coast_checker(parsed_coast):
        for i in parsed_coast:
            if float(i) > float(50):
                raise ArithmeticError("Cpu coast of process is much then 50%!!!")
            else:
                continue

    def service_status_checker(self):
        if self.data[1] != 'active':
            logging.info("Service status is {}!".format(self.data[1]))
        else:
            logging.info("Service is active...")
