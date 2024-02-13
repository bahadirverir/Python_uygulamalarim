import tkinter as tk
from tkinter import messagebox

# <<<FONKSİYONUN OLUŞTURULMASI VE HATA KONTROLÜ TAMAMLANDI>>>#
def endeks_hesaplama():
    try:
        kilo = float(kilo_entry.get())
        boy = float(boy_entry.get())
        boy = (boy / 100)**2
        endeks = (kilo / boy)

        if (endeks) <= 18.4:
            fiziki_durum = "Zayıf"
        elif (endeks) > 18.4 and (endeks) <= 24.9:
            fiziki_durum = "Normal"
        elif (endeks) > 25.0 and (endeks) <= 29.9:
            fiziki_durum = "Fazla Kilolu"
        elif (endeks) > 30.0 and (endeks) <= 34.9:
            fiziki_durum= "OBEZ"
        else:
            fiziki_durum = "OBEZ"

        sonuç_label.config(text="Beden Kitle İndeksi: {:.2f} olarak hesaplandı\nDurum: {}".format(endeks, fiziki_durum))

    except ValueError:
        messagebox.showerror(title="Hata",message="Lütfen geçersiz değerler girmeyin.")
    except ZeroDivisionError:
        messagebox.showerror(title="Hata",message="Lütfen boyunuzu 0'dan farklı girin.")
#<<------------------------------------------------------------------------------------------->>#
# Tkinter arayüzü kodları#

#arayüz adında bir pencere oluşturuldu ve bu pencerenin üst ana başlığı(title) belirlendi#
arayüz = tk.Tk()
arayüz.title("<<Beden Kitle Endeksi Hesaplama>>")
arayüz.minsize(width=500 , height=275)
arayüz.config(bg="black")

#arayüze kenarlık(frame) ekledi ve kenar boşlukları x,y girildi#
kenarlık = tk.Frame(arayüz)
kenarlık.pack(padx=100, pady=60)
kenarlık.config(bg="black")

# bir etiket(label) oluşturulur ve kenarlık(frame) isimli çerçeveye eklenir.
#içinde kilonuz yazan bir etiket oluşturulur konumu ve boyutu belirlenir
#entry komutu kullanılarak kullanıcıya bir giriş alanı oluşturulur
kilo_label = tk.Label(kenarlık, text="Kilonuz (kg):",fg="black")
kilo_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
kilo_entry = tk.Entry(kenarlık)
kilo_entry.grid(row=0, column=1, padx=5, pady=5)
kilo_label.config(bg="black",fg="lightgreen")
kilo_label.config(font=("Arial",16))

boy_label = tk.Label(kenarlık, text="Boyunuz (cm):",fg="black")
boy_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
boy_entry = tk.Entry(kenarlık)
boy_entry.grid(row=1, column=1, padx=5, pady=5)
boy_label.config(bg="black",fg="lightgreen")
boy_label.config(font=("Arial",16))
#Hesapla isminde bir buton oluşturlur ve butona tıklandığında endeks_hesaplama fonksiyonu çağırılır
hesapla_button = tk.Button(kenarlık, text="Hesapla", command=endeks_hesaplama)
hesapla_button.grid(row=2, columnspan=2, padx=5, pady=5)

#sonuçların gösterileceği alan olusturuldu#
sonuç_label = tk.Label(kenarlık, text="",bg="black",fg="white")
sonuç_label.grid(row=3, columnspan=2, padx=5, pady=5)
sonuç_label.config(font=("Arial", 16))
sonuç_label.config(bg="black",fg="lightgreen")

#arayüzün döngüsel olarak başlamasını ve çıkış işlemine kadar aktif olmasını sağlar#
arayüz.mainloop()