# ssh_honeypot
/cowrie/honeyfs/etc # cd ../
/cowrie/honeyfs # cd ../
/cowrie # ls
CHANGELOG.md             cowrie                   etc                      share
INSTALL.md               cowrie.cfg               honeyfs                  twistd.pid
LICENSE.md               data                     log                      twisted
README.md                dl                       requirements-output.txt  txtcmds
bin                      doc                      requirements.txt         var
/cowrie # cd bin/
/cowrie/bin # ls
asciinema  cowrie     createfs   fsctl      playlog
/cowrie/bin # ./fsctl data/fs.picle
data/fs.picle
File data/fs.picle does not exist.
/cowrie/bin # cd ../
/cowrie # bin/fsctl data/fs.pickle
data/fs.pickle

Kippo/Cowrie file system interactive editor
Donovan Hubbard, Douglas Hubbard, March 2013
Type 'help' for help

fs.pickle:/$ help

Documented commands (type help <topic>):
========================================
EOF  chgrp  chown  cp    file  ls     mv   rm     touch
cd   chmod  clear  exit  help  mkdir  pwd  rmdir

Miscellaneous help topics:
==========================
about

fs.pickle:/$ ls
bin/
boot/
dev/
etc/
home/
initrd.img
lib/
lost+found/
media/
mnt/
opt/
proc/
root/
run/
sbin/
selinux/
srv/
sys/
tmp/
usr/
var/
vmlinuz
fs.pickle:/$ cd etc
fs.pickle:/etc$ touch flag.txt
Added '/etc/flag.txt'
fs.pickle:/etc$ ()
