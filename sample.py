import tkinter as tk
 
# メインウィンドウを作成
baseGround = tk.Tk()
# ウィンドウのサイズを設定
baseGround.geometry('500x300')
# 画面タイトル
baseGround.title('テキストボックス')
 
# ラベル
label1 = tk.Label(text='テキストボックス1')
label1.place(x=30, y=70)
 
label2 = tk.Label(text='テキストボックス2')
label2.place(x=30, y=120)
 
# テキストボックス
textBox1 = tk.Entry(width=40)
textBox1.place(x=30, y=90)
 
textBox2 = tk.Entry()
textBox2.place(x=30, y=150)
 
baseGround.mainloop()
