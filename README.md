# reverse_shell
(ENG) Very simple reverse shell, written using the python socket and subprocess libraries, to use in LAN.

It allows the client, the machine running the client.py file, to write and send commands to the "victim" machine running the server.py file, which will then be interpreted by that machine. The client will then receive, from the "attacked" machine, the output of the previously sent command.

These are very simple scripts that work exclusively on LAN, but allow you to execute any type of command and receive its output even if it doesn't support UTF-8 encoding.

You can watch the speed coding of this script (ita version) at this link: https://youtu.be/36bqbftsU7Y
