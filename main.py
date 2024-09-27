import os
from pystyle import *
import tls_client, requests
import ctypes
import random
import easygui
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class xyzraid:
    def __init__(self):
        try:
            self.tokens = self.load_tokens()
            self.nowtimer = datetime.today().strftime('%H:%M:%S')
            os.system("mode 80, 20")
            self.clear()
            self.setTitle("Pass Changer Tool → DisCodes")
            self.banner()

            useproxy =  Write.Input(f'{self.nowtimer} Use Proxies? (y/n): ', Colors.cyan_to_green, interval=0.03).lower()

            if useproxy == "y":
                Write.Print("~ Using Proxy", Colors.cyan_to_green, interval=0.03)
                proxy = self.get_proxy_list()

                self.session = tls_client.Session(client_identifier = "chrome_122", random_tls_extension_order=True)
                self.session.proxies = {
                    "http": proxy,
                    "https": proxy
                }
            else:
                Write.Print("~ Using Proxyless", Colors.cyan_to_green, interval=0.03)
                self.session = tls_client.Session(client_identifier = "chrome_122", random_tls_extension_order=True)
                
            self.xyz_main()
        except Exception as e:
            print(f"An error occurred during initialization: {e}")
    
    def load_tokens(self):
        try:
            with open("tokens.txt", "r", encoding="utf-8") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print("tokens.txt file not found.")
            return []
        except Exception as e:
            print(f"An error occurred while loading tokens: {e}")
            return []

    def banner(self):
        try:
            banner = f'''
    ____  _      ______          __         
   / __ \(_)____/ ____/___  ____/ /__  _____
  / / / / / ___/ /   / __ \/ __  / _ \/ ___/
 / /_/ / (__  ) /___/ /_/ / /_/ /  __(__  ) 
/_____/_/____/\____/\____/\__,_/\___/____/  

                                                     
Token loaded: {len(self.tokens)} | DisCodes

'''
            print(Colorate.Vertical(Colors.cyan_to_green, Center.XCenter(banner)))
        except Exception as e:
            print(f"An error occurred while displaying the banner: {e}")
    
    def clear(self):
        try:
            os.system("cls")
        except Exception as e:
            print(f"An error occurred while clearing the console: {e}")
    
    def setTitle(self, _str):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
        except Exception as e:
            print(f"An error occurred while setting the console title: {e}")
    
    def get_proxy_list(self):
        try:
            useproxy = Write.Input(f'\n{self.nowtimer} (y) Own Proxies or (n) Generate some ', Colors.cyan_to_green, interval=0.03).lower()

            if useproxy == "y":
                proxylist = easygui.fileopenbox(msg="Choose your Proxy List", title="Proxy List Opener", filetypes=".txt")
                proxies = open(proxylist, "r", encoding="utf-8").read().splitlines()
                return "http://" + random.choice(proxies) or "https://" + random.choice(proxies)
            else:
                try:
                    api = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text"
                    proxies = requests.get(api).text.splitlines()
                    return "http://" + cycle(proxies) or "https://" + cycle(proxies)
                except Exception as e:
                    print(f"An error occurred while generating proxies: {e}")
                    return None
        except Exception as e:
            print(f"An error occurred while getting proxy list: {e}")
            return None

    @staticmethod
    def get_cookie(): 
        try:
            response = requests.Session().get('https://discord.com/app')
            cookie = str(response.cookies)
            return cookie.split('dcfduid=')[1].split(' ')[0], cookie.split('sdcfduid=')[1].split(' ')[0], cookie.split('cfruid=')[1].split(' ')[0]
        except Exception as e:
            print(f"An error occurred while getting cookies: {e}")
            return None, None, None
    
    @staticmethod
    def get_headers(token):
        try:
            headers = {
                "authority": "discord.com",
                "method": "GET",
                "path": "/api/v9/users/@me",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Authorization": token,
                "Cache-Control": "no-cache",
                "cookie": "__dcfduid=%s; __sdcfduid=%s; locale=en-US; __cfruid=%s" % xyzraid.get_cookie(),
                "Dnt": "1",
                "Pragma": "no-cache",
                "Priority": "u=1, i",
                "Referer": "https://discord.com/channels/@me",
                "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-Debug-Options": "bugReporterEnabled",
                "X-Discord-Locale": "en-US",
                "X-Discord-Timezone": "Asia/Calcutta",
                "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzE3MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
            }

            return headers
        except Exception as e:
            print(f"An error occurred while getting headers: {e}")
            return None
    
    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "Success",
            201: "Success",
            204: "Success",
            400: "Detected Captcha",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method not allowed",
            429: "Too many Requests"
        }
        return status_messages.get(status_code, "Unknown Status")

    
    def xyz_main(self):
        try:
            self.clear()
            self.banner()

            new_pass = Write.Input(f'{self.nowtimer} New Password: ', Colors.cyan_to_green, interval=0.03)
            threads = float(Write.Input(f'{self.nowtimer} Threads: ', Colors.cyan_to_green, interval=0.03))

            def pwchanger(token, password, email, new_pass):
                url = 'https://discord.com/api/v9/users/@me'
                payload = {'password': password, 'new_password': new_pass}
                headerz = xyzraid.get_headers(token)
                
                tk = token[:32] + "*" * 3  # Initialize tk before try-except block
                try:
                    r = self.session.patch(url, json=payload, headers=headerz)
                    if r.status_code == 200:
                        new_token = r.json()['token']
                        tk = new_token[:32] + "*" * 3
                        print(Colorate.Vertical(Colors.cyan_to_green, f'{self.nowtimer} ({xyzraid.check_status(r.status_code)}) → {tk} [{new_pass}]'))
                        with open("new_tokens.txt", "a") as f:
                            f.write(f"{email}:{new_pass}:{new_token}\n")
                    else:
                        print(Colorate.Horizontal(Colors.red_to_yellow, f'{self.nowtimer} ({xyzraid.check_status(r.status_code)}) → {tk}'))
                except Exception as e:
                    print(f"An error occurred while changing password for {email}: {e}")

            tokens = list(set(self.tokens))

            with ThreadPoolExecutor(max_workers=threads) as executor:
                for account in tokens:
                    email, password, token = account.split(':')[:3]
                    executor.submit(pwchanger, token, password, email, new_pass)
        except Exception as e:
            print(f"An error occurred in the main function: {e}")

xyzraid()
input("")
