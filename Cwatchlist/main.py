# ====================== Packages =============================== #
import requests
import json
from tkinter import *
from tkinter import messagebox
import sqlite3


# Function that switch color between red or green depending on profit or loss
def pl_color(value):
    if value < 0:
        return 'red'
    elif value > 0:
        return 'green'
    else:
        return 'black'


# Function that helps in alternating color swaps.
def color_swap(num):
    if num % 2 == 0:
        return ''
    else:
        return ''


# ====================== API =============================== #
def api_pull():
    # Putting together my URL for http request for the API
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    # My key from coinmarketcap.com
    my_key = "&CMC_PRO_API_KEY=" + "8405bc70-46f5-49e2-a3c1-c15ec1403471"

    # Filters that are being applied on the request with compliance to the API documentation.
    parameters = [
                'start=1',
                'limit=100',
                'convert=USD'
                ]

    # Used requests.get module to fetch data from Coin Market Cap's API with my personal key.
    api_data = requests.get(url + "?" + "&".join(parameters) + my_key)

    # The result of the http request to the API is converted to a more parsable format stored in a dictionary.
    data = json.loads(api_data.content)
    return data


# ====================== Windows =============================== #
def c_header():
    si_no = Label(crypto_port, text='SI No.', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    si_no.grid(row=0, column=0, sticky=N + S + E + W)

    c_name = Label(crypto_port, text='Currency Name', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_name.grid(row=0, column=1, sticky=N + S + E + W)

    c_code = Label(crypto_port, text='Acronym', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_code.grid(row=0, column=2, sticky=N + S + E + W)

    cur_price = Label(crypto_port, text='Current Price', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    cur_price.grid(row=0, column=3, sticky=N + S + E + W)

    c_quant = Label(crypto_port, text='Quantity', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_quant.grid(row=0, column=4, sticky=N + S + E + W)

    pur_price = Label(crypto_port, text='Purchased Price', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    pur_price.grid(row=0, column=5, sticky=N + S + E + W)

    c_pos = Label(crypto_port, text='Profit / Loss', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_pos.grid(row=0, column=6, sticky=N + S + E + W)

    c_net = Label(crypto_port, text='Net Amount', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_net.grid(row=0, column=7, sticky=N + S + E + W)


def c_populate(data):
    cnt = 0
    total = 0

    cur_obj.execute('SELECT * FROM cryptoholding')
    watchlist = cur_obj.fetchall()

    for i in range(10):
        for item in watchlist:
            if data['data'][i]['symbol'] in item[1]:
                cnt += 1
                total += (item[3] * item[2])

                si_no = Label(crypto_port, text=str(cnt), font='Lago 10 bold', fg='blue', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                si_no.grid(row=cnt, column=0, sticky=N+S+E+W)

                c_name = Label(crypto_port, text=data['data'][i]['name'], font='Lago 10 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                c_name.grid(row=cnt, column=1, sticky=N+S+E+W)

                c_code = Label(crypto_port, text=data['data'][i]['symbol'], font='Lago 10 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                c_code.grid(row=cnt, column=2, sticky=N+S+E+W)

                cur_price = Label(crypto_port, text='$ {0:.2f}'.format(data['data'][i]['quote']['USD']['price']), font='Lago 10 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                cur_price.grid(row=cnt, column=3, sticky=N+S+E+W)

                c_quant = Label(crypto_port, text=item[2], font='Lago 10 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                c_quant.grid(row=cnt, column=4, sticky=N+S+E+W)

                pur_price = Label(crypto_port, text='$ {0:.2f}'.format(item[3]), font='Lago 10 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                pur_price.grid(row=cnt, column=5, sticky=N+S+E+W)

                c_pos = Label(crypto_port, text='x{0:.2f}'.format((data['data'][i]['quote']['USD']['price']) / item[3]), font='Lago 10 bold', fg=pl_color((data['data'][i]['quote']['USD']['price'] - item[3])), bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                c_pos.grid(row=cnt, column=6, sticky=N+S+E+W)

                c_net = Label(crypto_port, text=(item[3] * item[2]), font='Lago 10 bold', fg=pl_color((data['data'][i]['quote']['USD']['price'] - item[3])), bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
                c_net.grid(row=cnt, column=7, sticky=N+S+E+W)

    tl = Label(crypto_port, text='TOTAL:', font='Lago 12 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
    tl.grid(row=cnt+1, column=6, sticky=N + S + E + W)

    t_pos = Label(crypto_port, text=total, font='Lago 12 bold', fg='white', bg='grey', relief='ridge', borderwidth='3', padx='5', pady='5')
    t_pos.grid(row=cnt+1, column=7, sticky=N + S + E + W)

    bt_addup = Button(crypto_port, text='Add/Update', font='Verdana 14 bold', command=c_addup, fg='white', bg='green', relief='raised', borderwidth='3', padx='5', pady='5')
    bt_addup.grid(row=cnt + 1, column=1, sticky=N + S + E + W)

    bt_del = Button(crypto_port, text='Delete', font='Verdana 14 bold', command=c_del, fg='yellow', bg='red', relief='raised', borderwidth='3', padx='5', pady='5')
    bt_del.grid(row=cnt + 1, column=3, sticky=N + S + E + W)

    # Clearing the all data for refresh to take effect
    data = ''

    bt_refresh = Button(crypto_port, text='Refresh', font='Verdana 14 bold', command=refresh, fg='black', bg='orange', relief='raised', borderwidth='3', padx='5', pady='5')
    bt_refresh.grid(row=cnt + 1, column=5, sticky=N + S + E + W)


def c_addup():
    crypto_addup = Toplevel()
    crypto_addup.title("Add or Update")

    c_code = Label(crypto_addup, text='Acronym: ', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_code.grid(row=0, column=0, sticky=N + S + E + W)
    txt_code = Entry(crypto_addup, relief='ridge', borderwidth='3')
    txt_code.grid(row=0, column=1)

    c_quant = Label(crypto_addup, text='Quantity: ', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_quant.grid(row=0, column=2, sticky=N + S + E + W)
    txt_quant = Entry(crypto_addup, relief='ridge', borderwidth='3')
    txt_quant.grid(row=0, column=3)

    pur_price = Label(crypto_addup, text='Price(USD): ', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    pur_price.grid(row=0, column=4, sticky=N + S + E + W)
    txt_price = Entry(crypto_addup, relief='ridge', borderwidth='3')
    txt_price.grid(row=0, column=5)

    bt_addup = Button(crypto_addup, text='Add/Update', font='Verdana 14 bold', command=lambda: db_write(txt_code.get(), txt_quant.get(), txt_price.get()), fg='white', bg='green', relief='raised', borderwidth='3', padx='5', pady='5')
    bt_addup.grid(row=0, column=6, sticky=N + S + E + W)


def c_del():
    crypto_del = Toplevel()
    crypto_del.title("Coin to be deleted!")

    c_code = Label(crypto_del, text='Acronym: ', font='Lago 12 bold italic', fg='white', bg='black', relief='groove', borderwidth='3', padx='5', pady='5')
    c_code.grid(row=0, column=0, sticky=N + S + E + W)
    txt_code = Entry(crypto_del, relief='ridge', borderwidth='3')
    txt_code.grid(row=0, column=1)

    bt_del = Button(crypto_del, text='DELETE', font='Verdana 14 bold', command=lambda: delete_entry(txt_code.get()), fg='white', bg='green', relief='raised', borderwidth='3', padx='5', pady='5')
    bt_del.grid(row=0, column=4, sticky=N + S + E + W)


# Function that helps to clear everything from the main window & repopulate it.
def refresh():
    for element in crypto_port.winfo_children():
        element.destroy()
    c_populate(api_pull())
    c_header()


# ====================== Database Functions=============================== #
# Function that carries out add & update entries into the database
def db_write(symbol, quantity, position):
    temp = db_read(symbol)
    if symbol in [i[1] for i in temp]:
        cur_obj.execute('UPDATE cryptoholding SET quantity=?, position=? WHERE symbol=?', (int(quantity) + temp[0][2], ((float(position) * int(quantity)) + (temp[0][2] * temp[0][3]))/(int(quantity) + temp[0][2]), symbol))
        con_obj.commit()
        messagebox.showinfo('Attention!', 'Existing coin info has been updated.')
    else:
        cur_obj.execute('INSERT INTO cryptoholding(id, symbol, quantity, position) VALUES(?, ?, ?, ?)', (idgen(), symbol, int(quantity), float(position)))
        con_obj.commit()
        messagebox.showinfo('Attention!', 'A new coin has been added to your portfolio!')
    refresh()


# Function to remove an entire row from the database, corresponding to the given key.
def delete_entry(symbol):
    cur_obj.execute('DELETE FROM cryptoholding WHERE symbol=?', (symbol, ))
    con_obj.commit()
    messagebox.showinfo('Attention!', 'Coin info has been deleted!')
    refresh()


# Function that reads & returns entire row of data corresponding to the given key.
def db_read(symbol):
    cur_obj.execute('SELECT * FROM cryptoholding WHERE symbol=?', (symbol, ))
    return cur_obj.fetchall()


# Function that generates a unique id for each entry when required.
def idgen():
    i = 1
    cur_obj.execute('SELECT id FROM cryptoholding')
    temp = cur_obj.fetchall()
    while i in [j[0] for j in temp]:
        i += 1
    return i


# ====================== Database Connect=============================== #
con_obj = sqlite3.connect('cryptoport.db')
cur_obj = con_obj.cursor()

# Creating a database if it doesn't already exist.
cur_obj.execute('CREATE TABLE IF NOT EXISTS cryptoholding(id INTEGER PRIMARY KEY, symbol TEXT, quantity INTEGER, position REAL)')
con_obj.commit()

# ====================== Main Window =============================== #
crypto_port = Tk()
crypto_port.title("Crypto Currency Portfolio")

# ====================== Main loop =============================== #
c_populate(api_pull())
c_header()
crypto_port.mainloop()

cur_obj.close()
con_obj.close()
