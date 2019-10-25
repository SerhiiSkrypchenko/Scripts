from exchangeFunctions import cancelAllOpenSellOrderETH
import testNet2

while True:
    cancelAllOpenSellOrderETH(testNet2.exchange_peers)