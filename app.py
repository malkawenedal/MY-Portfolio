# Import libraries and dependencies
from sys import platform
import pandas as pd
import ccxt
import csv
import os
from pathlib import Path
# from dotenv import load_dotenv
import json
from pytz import timezone
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta
import warnings
from pytz import timezone # set timezone
from io import StringIO
warnings.filterwarnings("ignore")
import streamlit as st
########################################################################3
st.title('Welcome to My PortFolio :sunglasses:')

from PIL import Image
image = Image.open('btc.png')
st.image(image,use_column_width="always")


# st.title('Welcome to My PortFolio :sunglasses:')

\

st.title("One Stop Shop")
st.markdown(" #### This software built to give you an access to multiple Cryptocurrency Exchange\Trading Platform to Retrive a Historical and live Crypto OHLCV for both Spot Exchanges &Derivatives Exchanges ")
st.write("The List of Platforms")


DF= {
        "Platform":["FTX","Kraken","Kucoin","MEXC"],
        "website":["https://ftx.com","https://www.kraken.com/","https://www.kucoin.com/","https://www.mexc.com/"]}
Platforms=pd.DataFrame(DF)
st.table(Platforms)  
##################################################################
st.title("Bitcoin")
st.subheader("Give it a Try ")

############
KUCOIN_KEY=" mx0UiKipmZ54cpPdaH"
KUCOIN_SECRET="796c447a500f4731be86a7a48b2b60a5" 
FTX_KEY="iGAAXnLAx1wm-fmxUtldFNf19SPrNlsPIRcZGlBm"
FTX_SECRET="l936V6xmk7zcT6EtIQCrcbBN7yS1AUa9HhEdozZo"
KRAYKEN_KEY="ct20T7CteNCqKeqNalaMOtROv+wgcm4Owv2CJY2eS4vBbBmDy5wcNp4/"
KRAKEN_SECRET="F8LahS0trnZqOCfqvFjEjH2hicLuRNFYe94ta7Vfct+jE/Gzpj75/sMbiq16+I0p2yzISR6myYGMOpEondSrCQ== "
MEXC_KEY="mx0qYb0mZjFJgCtxZX"
MEXC_SECRET="66f259628b8141d286909a2b245d59c1"
###########
ftx_key = FTX_KEY         #os.getenv('FTX_KEY')
ftx_secret =FTX_SECRET       #os.getenv('FTX_SECRET')

krayken_key =KRAYKEN_KEY    #os.getenv('KRAYKEN_KEY')
krayken_secret =KRAKEN_SECRET   #os.getenv('KRAKEN_SECRET')

mexc_key=MEXC_KEY          #os.getenv('MEXC_KEY')
mexc_secret=MEXC_SECRET           #os.getenv('MEXC_SECRET')

kucoin_key = KUCOIN_KEY      #os.getenv('KUCOIN_KEY')
kucoin_secret =KUCOIN_SECRET     #os.getenv('KUCOIN_SECRET')
#################################################################################


ex1 = "ftx"
ex2 = "kraken"
ex3 = "mexc"
ex4 = "kucoin"
####################################################################################
###################################################################################

exchange_class1 = getattr(ccxt,ex1)
exchange = exchange_class1({'verbose': True})
ftx = exchange_class1({
    'apiKey': ftx_key,
    'secret': ftx_secret,
})

exchange_class2 = getattr(ccxt,ex2)
kraken = exchange_class2({'verbose': True})
kraken = exchange_class2({
    'apiKey': krayken_key,
    'secret': krayken_secret,
})

exchange_class3 = getattr(ccxt,ex3)
exchange = exchange_class3({'verbose': True})
mexc = exchange_class3({
    'apiKey': mexc_key,
    'secret': mexc_secret,
})

exchange_class4 = getattr(ccxt,ex4)
exchange = exchange_class4({'verbose': True})
kucoin = exchange_class4({
    'apiKey': kucoin_key,
    'secret': kucoin_secret,
})
###################################################################################
import numpy as np
option = st.selectbox('Pick a Platfrom!!',(' ',"FTX","KRAKEN","KUCOIN","MEXC"))

if option== "FTX":

    ticker = "BTC"
    ticker = ticker+"/USDT"
    df1 = pd.DataFrame(ftx .fetch_ohlcv("BTC/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    df1["timestamp"] = pd.to_datetime(df1["timestamp"], unit = "ms").apply(lambda x:x.tz_localize('UTC').tz_convert('US/Eastern'))
    df1["ticker"] = ticker
    df1["exchange"] = np.nan
    x = df1["timestamp"].max()
    x = pd.to_datetime(x.value, unit="ns")
    ftx_data=df1["timestamp"].min(), df1["timestamp"].max(), len(df1)
    st.write(ftx_data)
    st.write(df1)



elif option== "KRAKEN":
       
    ticker = "BTC"
    ticker = ticker+"/USDT"
    df2 = pd.DataFrame(kraken .fetch_ohlcv("BTC/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    df2["timestamp"] = pd.to_datetime(df2["timestamp"], unit = "ms").apply(lambda y:y.tz_localize('UTC').tz_convert('US/Eastern'))
    df2["ticker"] = ticker
    df2["exchange"] = np.nan
    y = df2["timestamp"].max()
    y = pd.to_datetime(y.value, unit="ns")
    kraken_data=df2["timestamp"].min(), df2["timestamp"].max(), len(df2)
    st.write(kraken_data)
    st.write(df2)

elif option == "KUCOIN" :
    ticker = "BTC"
    ticker = ticker+"/USDT"
    df3 = pd.DataFrame(kucoin .fetch_ohlcv("BTC/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    df3["timestamp"] = pd.to_datetime(df3["timestamp"], unit = "ms").apply(lambda z:z.tz_localize('UTC').tz_convert('US/Eastern'))
    df3["ticker"] = ticker
    df3["exchange"] = np.nan
    z = df3["timestamp"].max()
    z = pd.to_datetime(z.value, unit="ns")
    kucoin_data=df3["timestamp"].min(), df3["timestamp"].max(), len(df3)
    st.write(kucoin_data)
    st.write(df3)

elif option== "MEXC":
    ticker = "BTC"
    ticker = ticker+"/USDT"
    df4 = pd.DataFrame(mexc .fetch_ohlcv("BTC/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    df4["timestamp"] = pd.to_datetime(df4["timestamp"], unit = "ms").apply(lambda zz:zz.tz_localize('UTC').tz_convert('US/Eastern'))
    df4["ticker"] = ticker
    df4["exchange"] = np.nan
    zz = df4["timestamp"].max()
    zz= pd.to_datetime(zz.value, unit="ns")
    mexc_data=df4["timestamp"].min(), df4["timestamp"].max(), len(df4)
    st.write(mexc_data)
    st.write(df4)

else:
    st.write('Please choose from the above options \u2191')

################################################################################################################################
## Etherum Block
#############################################################################################################################

st.title("Etherum")

option2 = st.selectbox(' Pick a Platfrom!!',(' ',"FtX","KrAKEN","KuCOIN","MeXC"))

if option2== "FtX":

    ticker2 = "ETH"
    ticker2 = ticker2+"/USDT"
    Df1 = pd.DataFrame(ftx .fetch_ohlcv("ETH/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    Df1["timestamp"] = pd.to_datetime(Df1["timestamp"], unit = "ms").apply(lambda X:X.tz_localize('UTC').tz_convert('US/Eastern'))
    Df1["ticker"] = ticker2
    Df1["exchange"] = np.nan
    X = Df1["timestamp"].max()
    X= pd.to_datetime(X.value, unit="ns")
    Ftx_data=Df1["timestamp"].min(), Df1["timestamp"].max(), len(Df1)
    st.write(Ftx_data)
    st.write(Df1)

# x = pd.to_datetime(x.value, unit="ns")
# str(int((end - datetime.datetime(1970,1,1)).total_seconds()))

elif option2== "KrAKEN":
       
    ticker2 = "ETH"
    ticker2 = ticker2+"/USDT"
    Df2 = pd.DataFrame(kraken .fetch_ohlcv("ETH/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    Df2["timestamp"] = pd.to_datetime(Df2["timestamp"], unit = "ms").apply(lambda Y:Y.tz_localize('UTC').tz_convert('US/Eastern'))
    Df2["ticker"] = ticker2
    Df2["exchange"] = np.nan
    Y = Df2["timestamp"].max()
    Y= pd.to_datetime(Y.value, unit="ns")
    Kraken_data=Df2["timestamp"].min(), Df2["timestamp"].max(), len(Df2)
    st.write(Kraken_data)
    st.write(Df2)

elif option2 == "KuCOIN" :
    ticker2 = "BTC"
    ticker2 = ticker2+"/USDT"
    Df3 = pd.DataFrame(kucoin .fetch_ohlcv("BTC/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    Df3["timestamp"] = pd.to_datetime(Df3["timestamp"], unit = "ms").apply(lambda Z:Z.tz_localize('UTC').tz_convert('US/Eastern'))
    Df3["ticker"] = ticker2
    Df3["exchange"] = np.nan
    Z = Df3["timestamp"].max()
    Z= pd.to_datetime(Z.value, unit="ns")
    Kucoin_data=Df3["timestamp"].min(), Df3["timestamp"].max(), len(Df3)
    st.write(Kucoin_data)
    st.write(Df3)

elif option2== "MeXC":
    ticker2 = "ETH"
    ticker2 = ticker2+"/USDT"
    Df4 = pd.DataFrame(mexc .fetch_ohlcv("ETH/USDT", limit= 1000, timeframe = "1m"), columns = ["timestamp", "Open","High", "Low", "Close", "Volume"])
    Df4["timestamp"] = pd.to_datetime(Df4["timestamp"], unit = "ms").apply(lambda ZZ:ZZ.tz_localize('UTC').tz_convert('US/Eastern'))
    Df4["ticker"] = ticker2
    Df4["exchange"] = np.nan
    ZZ = Df4["timestamp"].max()
    ZZ= pd.to_datetime(ZZ.value, unit="ns")
    Mexc_data=Df4["timestamp"].min(), Df4["timestamp"].max(), len(Df4)
    st.write(Mexc_data)
    st.write(Df4)

else:
    st.write('Please choose from the above options \u2191')

#########################################################################
## Contact Information 
###################################################################


# Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )





dict_info = {"":"","Email": "Malkawenedal@Gmail.com", "Mobile phone": "647-381-2020","Github":"https://github.com/malkawenedal",
"Linkedin":"www.linkedin.com/in/nedal1995",
"Resume":"https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:b29f449d-10fb-3da1-80ef-cba882cb0921"}


with st.sidebar:
    st.title("Nedal Mahanweh :sunglasses: ")
    st.title("Please find my contact information    \u21CA ")
    
option = st.sidebar.selectbox(
     'How would you like to contact me ?',
     ('','Email', 'Mobile phone','Github','Linkedin', "Resume"))

with st.sidebar:
    if option=="Email":
        st.write('## Its my Pleasure to provide you with my %s: %s' % (option, dict_info[option]))
        st.balloons()
    elif option=="Mobile phone":
        st.write('## Its my Pleasure to provide you with my %s: %s' % (option, dict_info[option]))
        st.balloons()
    elif option=="Github":
        st.write('## Its my Pleasure to provide you with my %s: %s' % (option, dict_info[option]))
        st.balloons()
    elif option=="Linkedin":
        st.write('## Its my Pleasure to provide you with my %s: %s' % (option, dict_info[option]))
        st.balloons()
    elif option=="Resume":
        st.write('## Its my Pleasure to provide you with my %s: %s' % (option, dict_info[option]))
        st.balloons()
    else:
        st.write('Please choose from the above options \u2191')
        
        