class Relogio:
    def __init__(self, h=0, m=0, s=0):
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            print("Horário digitado inválido")
            self.h, self.m, self.s = 0, 0, 0
        else:
            self.h, self.m, self.s = h, m, s

    def __add__(self, hora):
        total_segundos = (self.h + hora.h) * 3600 + (self.m + hora.m) * 60 + self.s + hora.s
        h = (total_segundos // 3600) % 24
        m = (total_segundos % 3600) // 60
        s = total_segundos % 60
        return Relogio(h, m, s)

    def __sub__(self, hora):
        if self.h < hora.h or (self.h == hora.h and self.m < hora.m) or (self.h == hora.h and self.m == hora.m and self.s < hora.s):
            print("O primeiro horário deve ser maior que o segundo")
            return None
        total_segundos = (self.h - hora.h) * 3600 + (self.m - hora.m) * 60 + self.s - hora.s
        h = total_segundos // 3600
        m = (total_segundos % 3600) // 60
        s = total_segundos % 60
        return Relogio(h, m, s)

    def __eq__(self, hora):
        return self.h == hora.h and self.m == hora.m and self.s == hora.s

    def __gt__(self, hora):
        return (self.h > hora.h) or (self.h == hora.h and self.m > hora.m) or (self.h == hora.h and self.m == hora.m and self.s > hora.s)

    def __lt__(self, hora):
        return (self.h < hora.h) or (self.h == hora.h and self.m < hora.m) or (self.h == hora.h and self.m == hora.m and self.s < hora.s)

    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"


r1 = Relogio(18, 37, 32)
r2 = Relogio(20, 0, 30)
print(r1 + r2)  
print(r2 - r1)  
print(r1 == r2)  
print(r1 > r2)  
print(r1 < r2)  