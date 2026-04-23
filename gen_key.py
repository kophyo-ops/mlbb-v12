import datetime

def generate():
    key_name = input("Enter Key Name (e.g. USER01): ")
    days = int(input("How many days?: "))
    
    # လက်ရှိအချိန်ကနေ သတ်မှတ်ရက်ကို ပေါင်းထည့်ခြင်း
    expiry_time = datetime.datetime.now() + datetime.timedelta(days=days)
    expiry_str = expiry_time.strftime("%Y-%m-%d %H:%M")
    
    # Key ကို keys.txt ထဲမှာ သိမ်းဆည်းခြင်း
    with open("keys.txt", "a") as f:
        f.write(f"{key_name}|{expiry_str}\n")
    
    print(f"\n[✓] Key Created: {key_name}")
    print(f"[✓] Expires on: {expiry_str}")

if __name__ == "__main__":
    generate()
