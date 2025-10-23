class IPAddress:
    def __init__(self, ip_str, mask_str):
        self.ip_str = ip_str
        self.mask_str = mask_str
        self.ip_int = self.ip_to_int(ip_str)
        self.mask_int = self.ip_to_int(mask_str)

        rede_int = self.ip_int & self.mask_int
        broadcast_int = rede_int | (~self.mask_int & 0xFFFFFFFF)

        self.rede = self.int_to_ip(rede_int)
        self.broadcast =self.int_to_ip(broadcast_int)
    
    def ip_to_int(self,ip):
        partes = ip.split(".")
        n = 0
        for p in partes:
            n = (n << 8) | int(p)
        return n
    
    def int_to_ip(self,n):
        return f"{( n >> 24 ) & 0xFF}.{( n >> 16 ) & 0xFF}.{( n >> 8 ) & 0xFF}.{( n ) & 0xFF}"

    def mask_to_cidr(self):
        return bin(self.mask_int).count("1")
    
    def pertence_a_rede(self,ip_str):
        ip_int = self.ip_to_int(ip_str)
        rede_ip = ip_int & self.mask_int
        return rede_ip == (self.ip_int & self.mask_int)
    
    def __str__(self):
        return f"{self.ip_str}/{self.mask_to_cidr()}"

#Teste de conversão
print(IPAddress("0.0.0.0", "0.0.0.0").ip_to_int("192.168.1.10")) # 3232235786
print(IPAddress("0.0.0.0", "0.0.0.0").int_to_ip(3232235786)) # "192.168.1.10"


if __name__ == "__main__":
    ip = IPAddress("192.168.1.10", "255.255.255.0")
    print(ip)                           # 192.168.1.10/24
    print(ip.rede)                      # 192.168.1.0
    print(ip.broadcast)                 # 192.168.1.255
    print(ip.pertence_a_rede("192.168.1.55"))  # True
    print(ip.pertence_a_rede("192.168.2.1"))   # False
