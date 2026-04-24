import datetime

def generate():
    print("\033[95m" + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\033[96m   🔑  V12 PRO - KEY GENERATOR (HWID LOCK)")
    print("\033[95m" + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    
    key_name = input("\nEnter Key Name (e.g. USER01): ")
    days = int(input("How many days?: "))
    
    expiry_time = datetime.datetime.now() + datetime.timedelta(days=days)
    expiry_str = expiry_time.strftime("%Y-%m-%d %H:%M")
    
    # Key|Expiry|HWID (NONE လို့ထားရင် ပထမဆုံးဝင်တဲ့သူနဲ့ Lock ကျမည်)
    with open("keys.txt", "a") as f:
        f.write(f"{key_name}|{expiry_str}|NONE\n")
    
    print(f"\n\033[92m[✓] Key Created: {key_name}")
    print(f"[✓] Expires on: {expiry_str}")
    print(f"[!] Status: Locked to first device only.\033[0m")

if __name__ == "__main__":
    generate()
