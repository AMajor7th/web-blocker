host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
sites = ["www.facebook.com", "www.twitter.com", "www.youtube.com", "https://chat.zalo.me", "www.chess.com", "www.lazada.vn", "chat.zalo.me"]

def block_sites(on):
    with open(host_path, "r+") as f:
        if on != 0:
            content = f.read()
            for site in sites:
                if site not in content:
                    f.write(redirect + " " + site + "\n")
        else:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if not any(site in line for site in sites):
                    f.write(line)
            f.truncate()

if __name__ == "__main__":
    run = input("Bat ki so de bat, 0 de tat: ")
    block_sites(int(run))
