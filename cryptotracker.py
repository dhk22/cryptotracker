from flask import Flask
from flask import render_template, redirect, url_for, flash, send_file, request
import requests

# Flask app defined
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def ticker():
    rbtc = requests.get('https://api.gdax.com/products/BTC-USD/ticker')
    btc = float(rbtc.json()['price'])
    reth = requests.get('https://api.gdax.com/products/ETH-USD/ticker')
    eth = float(reth.json()['price'])
    rltc = requests.get('https://api.gdax.com/products/LTC-USD/ticker')
    ltc = float(rltc.json()['price'])
    ricx = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=ICXBTC')
    icx = float(ricx.json()['price'])*btc
    rven = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=VENBTC')
    ven = float(rven.json()['price'])*btc
    rbnb = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=BNBBTC')
    bnb = float(rbnb.json()['price'])*btc
    riota = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=IOTABTC')
    iota = float(riota.json()['price'])*btc
    rxrp = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=XRPBTC')
    xrp = float(rxrp.json()['price'])*btc
    rreq = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=REQBTC')
    req = float(rreq.json()['price'])*btc
    rxrb = requests.get('https://api.kucoin.com/v1/open/tick?symbol=XRB-BTC')
    xrb = float(rxrb.json()['data']['lastDealPrice']) * btc
    rdbc = requests.get('https://api.kucoin.com/v1/open/tick?symbol=DBC-BTC')
    dbc = float(rdbc.json()['data']['lastDealPrice']) * btc
    rprl = requests.get('https://api.kucoin.com/v1/open/tick?symbol=PRL-BTC')
    prl = float(rprl.json()['data']['lastDealPrice']) * btc
    # rbittrex = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=btc-eth')
    # bittrex = rether.json()['result']['Last']

    amountbtc = 0.00007259
    amounteth = 1.8669022
    amountltc = 2.55734
    amountbnb = 1.97999570
    amounticx = 63.20078000
    amountven = 27.273186499999998
    amountiota = 0.93000000
    amountxrp = 0.82900000
    amountreq = 0.78500000
    amountprl = 29.0083626
    amountxrb = 93.62020873
    amountdbc = 3099.0713545

    valuebtc = btc*amountbtc
    valueeth = eth * amounteth
    valueltc = ltc * amountltc
    valuebnb = bnb * amountbnb
    valueicx = icx * amounticx
    valueven = ven * amountven
    valueiota = iota * amountiota
    valuexrp = xrp * amountxrp
    valuereq = req * amountreq
    valuexrb = xrb * amountxrb
    valueprl = prl * amountprl
    valuedbc = dbc * amountdbc

    valuetotal = valuebtc + valueeth + valueltc + valuebnb + valueicx + valueven + valueiota + valuexrp + valuereq + valuexrb + valueprl + valuedbc
    profittotal = valuetotal - 5578.32

    return render_template('ticker.html', btc=btc, eth=eth, ltc=ltc, icx=icx, ven=ven, bnb=bnb, iota=iota, xrp=xrp, req=req, xrb=xrb, dbc=dbc, prl=prl,
                           amountbtc=amountbtc, amounteth=amounteth, amountltc=amountltc, amounticx=amounticx, amountven=amountven, amountbnb=amountbnb, amountiota=amountiota, amountxrp=amountxrp, amountreq=amountreq, amountxrb=amountxrb, amountdbc=amountdbc, amountprl=amountprl,
                           valuebtc=valuebtc, valueeth=valueeth, valueltc=valueltc, valueicx=valueicx, valueven=valueven, valuebnb=valuebnb, valueiota=valueiota, valuexrp=valuexrp, valuereq=valuereq, valuexrb=valuexrb, valuedbc=valuedbc, valueprl=valueprl,
                           valuetotal=valuetotal, profittotal=profittotal)


# Flask app initialized
if __name__ == '__main__':
    app.run()