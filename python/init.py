#!/usr/bin/env python3
import subprocess as subp
import sys
import termcolor
import re 
import shutil

def green(message):
    print(termcolor.colored(message, 'green'))

def yellow(message):
    print(termcolor.colored(message, 'yellow'))

# Software Install
def execDnf(func):
    def wrapper(*args):
        green("----- Start Package Install -----")
        func(*args)
        green("----- End  Package Install -----\n")
    return wrapper

@execDnf
def test(package):
    check = "rpm -q " + package
    dnf = "dnf install -y " + package
    checkcode = subp.run(check, shell=True, stdout=subp.PIPE, stderr=subp.STDOUT).returncode

    if checkcode != 0 :
        subp.call(dnf, shell=True)
    else:
        yellow("Already Installed : " + package)

test("epel-release")
test("git")
test("httpd")
test("nginx")

# SELinux
green("----- Disable SELinux -----")
conf = "/etc/sysconfig/selinux"
conf_bak = conf + ".bak"
pattern="(\nSELINUX=|^SELINUX=).*"
rep_str = "disabled"
add_str = "SELINUX=disabled"

## backup
shutil.copy2(conf, conf_bak)

sestatus = subp.run("getenforce", shell=True, stdout=subp.PIPE)

if str(sestatus.stdout) in "Disabled":
    yellow("SELINUX is Disabled")
else:
    subp.run("setenforce 0", shell=True)

with open(conf, encoding="cp932") as f:
    data_lines = f.read()

if re.search(pattern, data_lines):
    data_lines = re.sub(pattern, r"\1" + rep_str, data_lines)
    with open(conf, mode="w", encoding="cp932") as f:
        f.write(data_lines)
else:
    with open(conf, mode="a", encoding="cp932") as f:
        f.write(add_str)
with open(conf, encoding="cp932") as f:
    print(f.read())

# nftables
green("----- Start nftables -----")
nf = "nftables"
cmd = "systemctl status " + nf + " --no-pager"
if subp.run(cmd, shell=True).returncode !=0:
    cmd = "systemctl start " + nf
    subp.call(cmd, shell=True)

cmd = "systemctl is-enabled " + nf
if subp.run(cmd, shell=True).returncode !=0:
    cmd = "systemctl enable " + nf
    subp.cal(cmd, shell=True)

green("nftables backup")
cmd="nft list ruleset > /etc/nftables/org.nft"
subp.call(cmd, shell=True)



