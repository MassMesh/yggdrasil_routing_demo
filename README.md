# Yggdrasil Routing Demo
Blink some lights on some raspberry pis... gaze into the mesh.

# Ingredients

* Some Raspberry Pis... 4 or 3b will do, but 3 and lower will have pretty slow speed on Yggdrasil network (encryption requires CPU.)
* Some SD cards... one to a pi.
* USB -> Ethernet adapters. The pi only comes with one port, and that's not going to cut it for the demo. Pick up a few converters so that you can make multiple links on a single device.
* Cases... Hit us up in Riot and we can connect you with them on the cheap. We've got the means of 3D print production at our disposal.

# Prep Work

Flash the SD cards with Raspbian headless.
* We use [Etcher](https://www.balena.io/etcher/)
* You can download Raspbian [here](https://www.raspberrypi.org/downloads/raspbian/)

Raspbian comes with ssh access [disabled by default.](https://www.raspberrypi.org/documentation/remote-access/ssh/) We will now enable it by placing a file called `ssh` in the boot partition of the SD card.

`mount /dev/mmcblk0p1 /mnt/acab`

`touch /mnt/acab/ssh`

Once you've enabled ssh access, go ahead and unmount the SD card.

`umount /mnt/acab/`

Now, we will load the SD card with the source files for our demo.

`mount /dev/mmblk0p2 /mnt/acab/`

`sudo ./prep.sh`

## Running The Demo

First, you'll need to log into the pi. Do so by following the instructions [here.](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)

Once you're logged in, install Yggdrasil by following the instructions [here.](https://yggdrasil-network.github.io/installation-linux-deb.html)

Finally, you'll need to install the dependencies for the python demo.

`cd ~/blink_ident/ && pip install gpiozero psutil`

Once the dependencies are installed, start the demo service.

`sudo systemctl start demo`

If you would like the demo to start on boot

`sudo systemctl enable demo`
