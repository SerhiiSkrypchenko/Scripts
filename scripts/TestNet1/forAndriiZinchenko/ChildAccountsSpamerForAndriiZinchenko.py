import requests
import random
import time

sec_str = input("Введите задержку в секундах после каждой отправленной транзакции: ")
node = input("Введите ноду на которую отправлять транзакции (например, localhost:7876 или apl-tap-0.testnet-ap.apollowallet.org: ")

#node = "localhost:7876"
#node = "apl-tap-0.testnet-ap.apollowallet.org"
#apl-t2-1.testnet2.apollowallet.org

sec = int(sec_str)

parentAccount =  "APL-X5JH-TJKJ-DVGC-5T2V8"
psecret = "1"

headers = {
            'Content-Type': "application/json"
        }
#creating child accounts from 100000 to 100999
data = {
        'parent': parentAccount,
        'secret': psecret,
        'child_secret_list': ["100000","100001","100002","100003","100004","100005","100006","100007","100008","100009","100010","100011","100012","100013","100014","100015","100016","100017","100018","100019","100020","100021","100022","100023","100024","100025","100026","100027","100028","100029","100030","100031","100032","100033","100034","100035","100036","100037","100038","100039","100040","100041","100042","100043","100044","100045","100046","100047","100048","100049","100050","100051","100052","100053","100054","100055","100056","100057","100058","100059","100060","100061","100062","100063","100064","100065","100066","100067","100068","100069","100070","100071","100072","100073","100074","100075","100076","100077","100078","100079","100080","100081","100082","100083","100084","100085","100086","100087","100088","100089","100090","100091","100092","100093","100094","100095","100096","100097","100098","100099","100100","100101","100102","100103","100104","100105","100106","100107","100108","100109","100110","100111","100112","100113","100114","100115","100116","100117","100118","100119","100120","100121","100122","100123","100124","100125","100126","100127","100128","100129","100130","100131","100132","100133","100134","100135","100136","100137","100138","100139","100140","100141","100142","100143","100144","100145","100146","100147","100148","100149","100150","100151","100152","100153","100154","100155","100156","100157","100158","100159","100160","100161","100162","100163","100164","100165","100166","100167","100168","100169","100170","100171","100172","100173","100174","100175","100176","100177","100178","100179","100180","100181","100182","100183","100184","100185","100186","100187","100188","100189","100190","100191","100192","100193","100194","100195","100196","100197","100198","100199","100200","100201","100202","100203","100204","100205","100206","100207","100208","100209","100210","100211","100212","100213","100214","100215","100216","100217","100218","100219","100220","100221","100222","100223","100224","100225","100226","100227","100228","100229","100230","100231","100232","100233","100234","100235","100236","100237","100238","100239","100240","100241","100242","100243","100244","100245","100246","100247","100248","100249","100250","100251","100252","100253","100254","100255","100256","100257","100258","100259","100260","100261","100262","100263","100264","100265","100266","100267","100268","100269","100270","100271","100272","100273","100274","100275","100276","100277","100278","100279","100280","100281","100282","100283","100284","100285","100286","100287","100288","100289","100290","100291","100292","100293","100294","100295","100296","100297","100298","100299","100300","100301","100302","100303","100304","100305","100306","100307","100308","100309","100310","100311","100312","100313","100314","100315","100316","100317","100318","100319","100320","100321","100322","100323","100324","100325","100326","100327","100328","100329","100330","100331","100332","100333","100334","100335","100336","100337","100338","100339","100340","100341","100342","100343","100344","100345","100346","100347","100348","100349","100350","100351","100352","100353","100354","100355","100356","100357","100358","100359","100360","100361","100362","100363","100364","100365","100366","100367","100368","100369","100370","100371","100372","100373","100374","100375","100376","100377","100378","100379","100380","100381","100382","100383","100384","100385","100386","100387","100388","100389","100390","100391","100392","100393","100394","100395","100396","100397","100398","100399","100400","100401","100402","100403","100404","100405","100406","100407","100408","100409","100410","100411","100412","100413","100414","100415","100416","100417","100418","100419","100420","100421","100422","100423","100424","100425","100426","100427","100428","100429","100430","100431","100432","100433","100434","100435","100436","100437","100438","100439","100440","100441","100442","100443","100444","100445","100446","100447","100448","100449","100450","100451","100452","100453","100454","100455","100456","100457","100458","100459","100460","100461","100462","100463","100464","100465","100466","100467","100468","100469","100470","100471","100472","100473","100474","100475","100476","100477","100478","100479","100480","100481","100482","100483","100484","100485","100486","100487","100488","100489","100490","100491","100492","100493","100494","100495","100496","100497","100498","100499","100500","100501","100502","100503","100504","100505","100506","100507","100508","100509","100510","100511","100512","100513","100514","100515","100516","100517","100518","100519","100520","100521","100522","100523","100524","100525","100526","100527","100528","100529","100530","100531","100532","100533","100534","100535","100536","100537","100538","100539","100540","100541","100542","100543","100544","100545","100546","100547","100548","100549","100550","100551","100552","100553","100554","100555","100556","100557","100558","100559","100560","100561","100562","100563","100564","100565","100566","100567","100568","100569","100570","100571","100572","100573","100574","100575","100576","100577","100578","100579","100580","100581","100582","100583","100584","100585","100586","100587","100588","100589","100590","100591","100592","100593","100594","100595","100596","100597","100598","100599","100600","100601","100602","100603","100604","100605","100606","100607","100608","100609","100610","100611","100612","100613","100614","100615","100616","100617","100618","100619","100620","100621","100622","100623","100624","100625","100626","100627","100628","100629","100630","100631","100632","100633","100634","100635","100636","100637","100638","100639","100640","100641","100642","100643","100644","100645","100646","100647","100648","100649","100650","100651","100652","100653","100654","100655","100656","100657","100658","100659","100660","100661","100662","100663","100664","100665","100666","100667","100668","100669","100670","100671","100672","100673","100674","100675","100676","100677","100678","100679","100680","100681","100682","100683","100684","100685","100686","100687","100688","100689","100690","100691","100692","100693","100694","100695","100696","100697","100698","100699","100700","100701","100702","100703","100704","100705","100706","100707","100708","100709","100710","100711","100712","100713","100714","100715","100716","100717","100718","100719","100720","100721","100722","100723","100724","100725","100726","100727","100728","100729","100730","100731","100732","100733","100734","100735","100736","100737","100738","100739","100740","100741","100742","100743","100744","100745","100746","100747","100748","100749","100750","100751","100752","100753","100754","100755","100756","100757","100758","100759","100760","100761","100762","100763","100764","100765","100766","100767","100768","100769","100770","100771","100772","100773","100774","100775","100776","100777","100778","100779","100780","100781","100782","100783","100784","100785","100786","100787","100788","100789","100790","100791","100792","100793","100794","100795","100796","100797","100798","100799","100800","100801","100802","100803","100804","100805","100806","100807","100808","100809","100810","100811","100812","100813","100814","100815","100816","100817","100818","100819","100820","100821","100822","100823","100824","100825","100826","100827","100828","100829","100830","100831","100832","100833","100834","100835","100836","100837","100838","100839","100840","100841","100842","100843","100844","100845","100846","100847","100848","100849","100850","100851","100852","100853","100854","100855","100856","100857","100858","100859","100860","100861","100862","100863","100864","100865","100866","100867","100868","100869","100870","100871","100872","100873","100874","100875","100876","100877","100878","100879","100880","100881","100882","100883","100884","100885","100886","100887","100888","100889","100890","100891","100892","100893","100894","100895","100896","100897","100898","100899","100900","100901","100902","100903","100904","100905","100906","100907","100908","100909","100910","100911","100912","100913","100914","100915","100916","100917","100918","100919","100920","100921","100922","100923","100924","100925","100926","100927","100928","100929","100930","100931","100932","100933","100934","100935","100936","100937","100938","100939","100940","100941","100942","100943","100944","100945","100946","100947","100948","100949","100950","100951","100952","100953","100954","100955","100956","100957","100958","100959","100960","100961","100962","100963","100964","100965","100966","100967","100968","100969","100970","100971","100972","100973","100974","100975","100976","100977","100978","100979","100980","100981","100982","100983","100984","100985","100986","100987","100988","100989","100990","100991","100992","100993","100994","100995","100996","100997","100998","100999"]
        }
response = requests.request("POST",
                                    "https://" + node + "/rest/v2/account/test",
                                    headers=headers, json = data)
print(response.json())
tx = response.json()["tx"]
print(tx)
data = {"tx": str(tx)}
response = requests.request("POST",
                                    "https://" + node + "/rest/v2/transaction", headers = headers,
                                    json =  data
                                    )
print(response.json())

#creating transactions between child accounts
alive = True
while alive:
        p = random.randint(100000, 100099)
        i = random.randint(100000, 100099)
        print(" <<<< --- START ---- >>>> ")
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET", "http://" + node + "/apl",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        print(str("accountReceive = " + accountReceive))
        print("secretPhrase of account Receiver = " + str(i))
        account = response.json()["account"]
        print("accountId of accountReceive = " + account)

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    "http://" + node + "/apl",
                                    params=getAccountId)

        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("sender secret phrase = " + str(p))
        print("accountSender = " + accountSender)
        amountATM = random.choice(["200000000", "300000000", "400000000", "500000000", "600000000", "700000000", "800000000"])
        print("amountATM = " + amountATM)

        data = {'parent': parentAccount, 'psecret': psecret, 'sender': str(accountSender), 'csecret': str(p),'recipient':str(accountReceive), 'amount':amountATM}
        response = requests.request("POST",
                                    "https://" + node + "/rest/v2/account/money",
                                    headers=headers, json = data)
        print(response.json())
        tx = response.json()["tx"]
        print(tx)
        data = {"tx": str(tx)}
        response = requests.request("POST",
                                    "https://" + node + "/rest/v2/transaction", headers = headers,
                                    json =  data
                                    )
        print(response.json())
        print("recipient = " + response.json()["recipient"])
        print("sender = " + response.json()["sender"])
        print("----------- END -------------")
        print()
        time.sleep(sec)










