from forex_python.converter import CurrencyRates # to reach currency rates and their symbols
from forex_python.converter import CurrencyCodes # to reach codes of currencies rates
from forex_python.bitcoin import BtcConverter # to reach Bitcoin rates
import time

c = CurrencyRates() # currency rates 
# eğer decimal kullanımına zorlarsan ondalıklı sayı sisteminde veri aktarır

b = BtcConverter() # write down force_decimal=True in the bracket to bring datas of decimal rate

c_codes = CurrencyCodes()
print(c.get_symbol('USD')) # to get symbols of currencies


def choose_process():
    print()
    print("1) Forex Rates")
    print("2) Bitcoin Rates")
    print("3) Quit the Program")
    print("")
    return    
choose_process()
process_type = int(input("Choose the section what you want: \n"))

# now desinging logical functions that be conditioned to if statement
if process_type == 1:
    print("")
    print("Type Currencies that you want to learn their rates:")

    cur_rates_1 = str(input("First one; "))
    cur_rates_2 = str(input("Second one; "))
    print("")
    cur_rates_price = input("Type the amount what you want to convert: ")
    cur_rates_price = float(cur_rates_price) # tam sayı veya virgüllü sayının da girdi olarak alınabilmesi için yaptım bunu

    print() # boşluk ekliyorum ki çıktı alırken konsol teimz ve anlaşılır görünsün

    print(c.convert(cur_rates_1, cur_rates_2, cur_rates_price))

elif process_type == 2:
    btc_latest_price = input("Type the amount what you want to convert: ")
    btc_latest_price = float(btc_latest_price)
    print(f"{btc_latest_price} USD to BTC equals ", b.convert_to_btc(btc_latest_price, 'USD'))

elif process_type == 3:
    print("Program is closing...")
    time.sleep(0.5)
    exit()

else:
    print("Please restart the program and type a defined number, from 1 up to 3...")
    exit()
