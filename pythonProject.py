import os
from colorama import Fore
def reset_color():
    "resets terminal font color"
    print(Fore.RESET)
def quit():
    print('see you later')
    exit()
banner = '''
                               _ . - = - . _
                           . "  \  \   /  /  " .
                         ,  \                 /  .
                       . \   _,.--~=~"~=~--.._   / .
                      ;  _.-"  / \ !   ! / \  "-._  .
                     / ,"     / ,` .---. `, \     ". \\
                    /.'   `~  |   /:::::\   |  ~`   '.\\
                    \`.  `~   |   \:::::/   | ~`  ~ .'/
                     \ `.  `~ \ `, `~~~' ,` /   ~`.' /
                      .  "-._  \ / !   ! \ /  _.-"  .
                       ./    "=~~.._  _..~~=`"    \.
                         ,/         ""          \,
                           . _/             \_ .
                              " - ./. .\. - "
                                                   
                ▀███▄   ▀███▀████▄     ▄███▀     ██     ▀███▀▀▀██▄ 
                  ███▄    █   ████    ████      ▄██▄      ██   ▀██▄
                  █ ███   █   █ ██   ▄█ ██     ▄█▀██▄     ██   ▄██ 
                  █  ▀██▄ █   █  ██  █▀ ██    ▄█  ▀██     ███████  
                  █   ▀██▄█   █  ██▄█▀  ██    ████████    ██       
                  █     ███   █  ▀██▀   ██   █▀      ██   ██       
                ▄███▄    ██ ▄███▄ ▀▀  ▄████▄███▄   ▄████▄████▄     
                                                   
An introduction to the finest network mapper in the land.
All explinations are from nmap.

Press q at any time to quit!
'''
print(Fore.MAGENTA)
print(banner)
print(Fore.RED + 'THIS SCRIPT REQUIRES SUDO PRIVILEGES')
reset_color()
print('Nmap (“Network Mapper”) is an open source tool for network exploration and security auditing. It was designed to rapidly scan large networks, although it works fine against single hosts.'
          '\nNmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, '
          '\nwhat type of packet filters/firewalls are in use, and dozens of other characteristics. '
          '\nWhile Nmap is commonly used for security audits, many systems and network administrators find it useful for routine tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime.\n')

def easy_scan():
    "this is the quickest scan"
    while True:
        ip = input('Enter an IP or domain WARNING! only scan domains you own proceed at your own risk: ')
        if ip == 'q':
            quit()
        print('your scan will be exported to a text file named "nmap_scan" \n')
        scan = input('would you like to scan using the default nmap scan (TCP scan of 1000 most used ports HTTP,SSH,FTP...ETC Y/N: ')

        if scan == 'y':
            exe_text = f'nmap {ip}'
            print(Fore.BLUE)
            print(f'your nmap scan is "{exe_text}"')
            reset_color()
            os.system(f'sudo nmap {ip} > nmap_scan.txt')
            os.system('cat nmap_scan.txt')
            another_scan = input('would you like to do another scan or return to main menu (R) Y/N/R: ')
            if another_scan == 'y':
                continue
            elif another_scan == 'n':
                print('Ok see you around hacker')
                exit()
            elif another_scan == 'r':
                break
            elif another_scan == 'q':
                print('see you later')
                exit()
        elif scan == 'q':
            quit()
        elif scan == 'n':
            break
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue
def moderate_scan():
    "this is a more in depth scan"
    while True:

        ip = input('Enter an IP or domain WARNING! only scan domains you own proceed at your own risk: ')
        if ip == 'q':
            print('see you later')
            exit()
        print('your scan will be exported to a text file named "nmap_scan" \n')
        start_port = input('what starting port would you like to scan say "all" for all ports or press ENTER for default 1000: ')
        if start_port == 'all':
            port_number = False
            port = '-p-'
            port_txt = '65535'
        elif start_port == '':
            port_number = False
            port = ''
            port_txt = 'default 1000'
        elif start_port == 'q':
            quit()
        else:
            port_number = True
            end_port = input('what is the ending port for your scan: ')

        tcp_udp = input('Would you like to scan UDP or TCP or both: ')
        if tcp_udp == 'udp':
            protocol = '-sU'
            protocol_txt = 'UDP'
        elif tcp_udp == '':
            protocol = '-sS'
            protocol_txt = 'TCP'
        elif tcp_udp == 'tcp':
            protocol = '-sS'
            protocol_txt = 'TCP'
        elif tcp_udp == 'both':
            protocol = '-sU -sS'
            protocol_txt = 'TCP and UDP'
        elif tcp_udp == 'q':
            quit()
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue

        if port_number == False:
           finalize = input(Fore.BLUE +f'You are preparring to scan {ip} on port/s {port_txt} scanning {protocol_txt} does that sound right Y/N: ')
           reset_color()
           if finalize == 'y':
              os.system(f'sudo nmap {port} {protocol} {ip} > nmap_scan.txt')
              os.system('cat nmap_scan.txt')
              another_scan = input('would you like to do another scan or return to main menu (R) Y/N/R: ')
              if another_scan == 'y':
                   continue
              elif another_scan == 'n':
                   print('Ok see you around hacker')
                   exit()
              elif another_scan == 'r':
                   break
              elif finalize == 'q':
                   quit()
           elif finalize == 'n':
                print('starting you over')
                continue
           elif finalize == 'q':
                quit()
           else:
                print(Fore.RED + 'ERROR:please enter a sufficient value')
                reset_color()
                continue
        else:
            finalize = input(Fore.BLUE +f'You are preparring to scan {ip} on port/s {start_port} - {end_port} scanning {protocol_txt} does that sound right Y/N: ')
            reset_color()
            if finalize == 'y':
                os.system(f'sudo nmap -p {start_port}-{end_port} {protocol} {ip}> nmap_scan.txt')
                os.system('cat nmap_scan.txt')
                another_scan = input('would you like to do another scan or return to main menu (R) Y/N/R: ')
                if another_scan == 'y':
                    continue
                elif another_scan == 'n':
                    print('Ok see you around hacker')
                    exit()
                elif another_scan == 'r':
                    break
                elif another_scan == 'q':
                    quit()
            elif finalize == 'n':
                print('starting you over')
                continue
            elif finalize == 'q':
                quit()
            else:
                print(Fore.RED + 'ERROR:please enter a sufficient value')
                reset_color()
                continue

def deep_scan():
    "this is a custom deep scan"
    while True:

        ip = input('Enter an IP or domain WARNING! only scan domains you own proceed at your own risk: ')
        if ip == 'q':
            quit()
        print('your scan will be exported to a text file named "nmap_scan" \n')

        start_port = input(
            'what starting port would you like to scan say "all" for all ports or press ENTER for default 1000: ')
        if start_port == 'all':
            port_number = False
            port = '-p-'
            port_txt = '65535'
        elif start_port == '':
            port_number = False
            port = ''
            port_txt = 'default 1000'
        elif start_port == 'q':
            quit()
        else:
            port_number = True
            end_port = input('what is the ending port for your scan: ')

        output = input('what style output would you like\n all (a)\n grepable (g)\n XML (x)\n default (d)\n Enter style a/g/x/d: ')
        if output == 'a':
            format_txt = 'all'
            format = '-oA'
        elif output == 'g':
            format_txt = 'grepable'
            format = '-oG'
        elif output == 'x':
            format_txt = 'XML'
            format = '-oX'
        elif output == 'd':
            format_txt = 'default'
            format = ''
        elif start_port == 'q':
            quit()
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue

        scan_speed = input('what would you like you scan speed to be\n slowest (s)\n IDS evader (i)\n timeley (t)\n default (d)\n aggressive (a)\n fastest (f)\n Enter your scan speed s/i/t/d/a/f: ')
        if scan_speed == 's':
            speed_text = 'slowest'
            speed = '-T0'
        elif scan_speed == 'i':
            speed_text = 'IDS evader'
            speed = '-T1'
        elif scan_speed == 't':
            speed_text = 'timely'
            speed = '-T2'
        elif scan_speed == 'd':
            speed_text = 'default'
            speed = '-T3'
        elif scan_speed == 'a':
            speed_text = 'aggressive'
            speed = '-T4'
        elif scan_speed == 'f':
            speed_text = 'fastest'
            speed = '-T5'
        elif scan_speed == 'q':
            quit()
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue

        scan_type = input('What will your scan type be\n SYN scan (s)\n ACK scan (a)\n FIN scan (f)\n XMAS (x)\n UDP (u)\nEnter your scan type s/a/f/x/u: ')
        if scan_type == 's':
            scan_txt = 'SYN'
            scan = '-sS'
        elif scan_type == 'a':
            scan_txt = 'ACK'
            scan = '-sA'
        elif scan_type == 'f':
            scan_txt = 'FIN'
            scan = '-sA'
        elif scan_type == 'x':
            scan_txt = 'XMSAS'
            scan = '-sA'
        elif scan_type == 'u':
            scan_txt = 'UDP'
            scan = '-sA'
        elif scan_type == 'q':
            quit()
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue

        version_intense = input('what will the version intensity be 1-9: ')
        if version_intense == '1':
            version_txt = 'level 1'
            intensity = '-sV'
        elif version_intense == '2':
            version_txt = 'level 2'
            intensity = '-sV --version-intensity 2'
        elif version_intense == '3':
            version_txt = 'level 3'
            intensity = '-sV --version-intensity 3'
        elif version_intense == '4':
            version_txt = 'level 4'
            intensity = '-sV --version-intensity 4'
        elif version_intense == '5':
            version_txt = 'level 5'
            intensity = '-sV --version-intensity 5'
        elif version_intense == '6':
            version_txt = 'level 6'
            intensity = '-sV --version-intensity 6'
        elif version_intense == '7':
            version_txt = 'level 7'
            intensity = '-sV --version-intensity 7'
        elif version_intense == '8':
            version_txt = 'level 8'
            intensity = '-sV --version-intensity 8'
        elif version_intense == '9':
            version_txt = 'level 9'
            intensity = '-sV --version-intensity 9'
        elif version_intense == 'q':
            quit()
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue

        os_detection = input(' would you like OS detection\n OS detection (o)\n all forms of detextion (a)\nEnter your OS detection o/a: ')
        if os_detection == 'o':
            detection_txt = 'default'
            detection = '-O'
        elif os_detection == 'a':
            detection_txt = 'all'
            detection = '-A'
        elif os_detection == 'q':
            quit()
        else:
            print(Fore.RED + 'ERROR:please enter a sufficient value')
            reset_color()
            continue



        if port_number == False:
            print(Fore.BLUE + f'here are your scan specifications:')
            finalize = input(Fore.RED + f'\n IP: {ip}\n ports: {port_txt}\n scan type: {scan_txt}\n file output: {format_txt}\n scan speed: {speed_text}\n version discovery level: {version_txt}\n OS detection: {detection_txt}\n Are these specifications correct y/n: ')
            reset_color()
            if finalize == 'y':
                os.system(f'sudo nmap {port} {scan} {ip} {speed} {intensity} {detection} {format} nmap_scan.txt')
                os.system('cat nmap_scan.txt')
                another_scan = input('would you like to do another scan or return to main menu (R) Y/N/R: ')
                if another_scan == 'y':
                    continue
                elif another_scan == 'n':
                    print('Ok see you around hacker')
                    exit()
                elif another_scan == 'r':
                    break
                elif finalize == 'q':
                    print('see you later')
                    exit()
            elif finalize == 'n':
                print('starting you over')
                continue
            elif finalize == 'q':
                print('see you later')
                exit()
            else:
                print(Fore.RED + 'ERROR:please enter a sufficient value')
                reset_color()
                continue
        else:
            print(Fore.BLUE + f'here are your scan specifications:')
            finalize = input(Fore.RED + f'\nIP: {ip}\n start port: {start_port}\n end port: {end_port}\n scan type: {scan_txt}\n file output: {format_txt}\n scan speed: {speed_text}\n version discovery level: {version_txt}\n OS detection: {detection_txt}\n Are these specifications correct y/n: ')
            reset_color()
            if finalize == 'y':
                if format == 'd':
                    os.system(f'sudo nmap -p {start_port}-{end_port} {scan} {ip} > nmap_scan')
                    os.system('cat nmap_scan.txt')
                else:
                    os.system(f'sudo nmap -p {start_port}-{end_port} {scan} {ip} {speed} {intensity} {detection} {format} nmap_scan.txt')
                    os.system('cat nmap_scan.txt')
                another_scan = input('would you like to do another scan or return to main menu (R) Y/N/R: ')
                if another_scan == 'y':
                    continue
                elif another_scan == 'n':
                    print('Ok see you around hacker')
                    exit()
                elif another_scan == 'r':
                    break
                elif another_scan == 'q':
                    print('see you later')
                    exit()
            elif finalize == 'n':
                print('starting you over')
                continue
            elif finalize == 'q':
                print('see you later')
                exit()
            else:
                print(Fore.RED + 'ERROR:please enter a sufficient value')
                reset_color()
                continue

print(Fore.BLUE + 'scanme.nmap.org is a testing domain provided by nmap Give it a try!')
reset_color()
while True:
    scan_level = input('What level scan would you like to do...\n tutorial (t)\n simple scan (s)\n medium scan (m)\n custom heavy scan (h)\n Enter scan type t/s/m/h: ')

    if scan_level == 's':
        easy_scan()
    elif scan_level == 'm':
        moderate_scan()
    elif scan_level == 'h':
        deep_scan()
    elif scan_level == 'q':
        exit()