from exchangeFunctions import cancelAllOpenBuyOrderETH
import testNet2

while True:
    cancelAllOpenBuyOrderETH(testNet2.exchange_peers)