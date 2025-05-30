#You need  a long text to make sure that the statistical distribution of letters in the English language is respected

plaintext = "ITWASTHEBESTOFTIMESITWASTHEWORSTOFTIMESITWASTHEAGEOFWISDOMITWASTHEAGEOFFOOLISHNESSITWASTHEEPOCHOFBELIEFITWASTHEEPOCHOFINCREDULITYITWASTHESEASONOFLIGHTITWASTHESEASONOFDARKNESSITWASTHESPRINGOFHOPEITWASTHEWINTEROFDESPAIRWEHADEVERYTHINGBEFOREUSWEHADNOTHINGBEFOREUSWEWEREALLGOINGDIRECTTOHEAVENWEWEREALLGOINGDIRECTTHEOTHERWAYINSHORTTHEPERIODWASSOFARLIKETHEPRESENTPERIODTHATSOMEOFITSNOISIESTAUTHORITIESINSISTEDONITSBEINGRECEIVEDFORGOODORFOREVILINTHESUPERLATIVEDEGREEOFCOMPARISONONLYTHEREWEREAKINGWITHALARGEJAWANDAQUEENWITHAPLAINFACEONTHETHRONEOFENGLANDTHEREWEREAKINGWITHALARGEJAWANDAQUEENWITHAFAIRFACEONTHETHRONEOFFRANCEINBOTHCOUNTRIESITWASCLEARERTHANCRYSTALTOTHELORDSOFTHESTATEPRESERVESOFLOAVESANDFISHESTHATTHINGSINGENERALWERESETTLEDFOREVERITWASTHEYEAROFOURLORDONETHOUSANDSEVENHUNDREDANDSEVENTYFIVESPIRITUALREVELATIONSWERECONCEDEDTOENGLANDATTHATFAVOUREDPERIODASATTHISMRSSOUTHCOTTHADRECENTLYATTAINEDHERFIVEANDTWENTIETHBLESSEDBIRTHDAYOFWHOMAPROPHETICPRIVATEINTHELIFEGUARDSHADHERALDEDTHESUBLIMEAPPEARANCEBYANNOUNCINGTHATARRANGEMENTSWEREMADEFORTHESWALLOWINGUPOFLONDONANDWESTMINSTEREVENTHECOCKLANEGHOSTHADBEENLAIDONLYAROUNDDOZENOFYEARSAFTERRAPPINGOUTITSMESSAGESASTHESPIRITSOFTHISVERYYEARLASTPASTSUPERNATURALLYDEFICIENTINORIGINALITYRAPPEDOUTTHEIRSMEREMESSAGESINTHEEARTHLYORDEROFEVENTSHADLATELYCOMETOTHEENGLISHCROWNANDPEOPLEFROMACONGRESSOFBRITISHSUBJECTSINAMERICAWHICHSTRANGETORELATEHAVEPROVEDMOREIMPORTANTTOTHEHUMANRACETHANANYCOMMUNICATIONSYETRECEIVEDTHROUGHANYOFTHECHICKENSOFTHECOCKLANEBROODFRANCELESSFAVOUREDONTHEWHOLEASTOMATTERSSPIRITUALTHANHERSISTEROFTHESHIELDANDTRIDENTROLLEDWITHEXCEEDINGSMOOTHNESSDOWNHILLMAKINGPAPERMONEYANDSPENDINGITUNDERTHEGUIDANCEOFHERCHRISTIANPASTORSSHEENTERTAINEDHERSELFBESIDESWITHSUCHHUMANEACHIEVEMENTSASSENTENCINGAYOUTHTOHAVEHISHANDSCUTOFFHISTONGUETORNOUTWITHPINCERSANDHISBODYBURNEDALIVEBECAUSEHEHADNOTKNEELEDDOWNINTHERAINTODOHONOURTOADIRTYPROCESSIONOFMONKSWHICHPASSEDWITHINHISVIEWATADISTANCEOFSOMEFIFTYORSIXTYYARDSITISLIKELYENOUGHTHATROOTEDINTHEWOODSOFFRANCEANDNORWAYTHEREWEREGROWINGTREESWHENTHATSUFFERERWASPUTTODEATHALREADYMARKEDBYTHEWOODMANFATETOCOMEDOWNANDBESAWNINTOBOARDSTOMAKEACERTAINMOVABLEFRAMEWORKWITHASACKANDAKNIFEINITTERRIBLEINHISTORYITISLIKELYENOUGHTHATINTHEROUGHOUTHOUSESOFSOMETILLERSOFTHEHEAVYLANDSADJACENTTOPARISTHEREWERESHELTEREDFROMTHEWEATHERTHATVERYDAYRUDECARTSBESPATTEREDWITHRUSTICMIRESNUFFEDABOUTBYPIGSANDROOSTEDINBYPOULTRYWHICHTHEFARMERDEATHHADALREADYSETAPARTTOBEHISTUMBRILSOFTHEREVOLUTIONBUTTHATWOODMANANDTHATFARMERTHOUGHTHEYWORKUNCEASINGLYWORKSILENTLYANDNOONEHEARDTHEMASTHEYWENTABOUTWITHMUFFLEDTREADTHERATHERFORASMUCHASTOENTERTAINANYSUSPICIONTHATTHEYWEREAWAKEWASTOBEATHEISTICALANDTRAITOROUSINENGLANDTHEREWASSCARCELYANAMOUNTOFORDERANDPROTECTIONTOJUSTIFYMUCHNATIONALBOASTINGDARINGBURGLARIESBYARMEDMENANDHIGHWAYROBBERIESTOOKPLACEINTHECAPITALITSELFEVERYNIGHTFAMILIESWEREPUBLICLYCAUTIONEDNOTTOGOOUTOFTOWNWITHOUTREMOVINGTHEIRFURNITURETOUPHOLSTERERSWAREHOUSESFORSECURITYTHEHIGHWAYMANINTHEDARKWASACITYTRADESMANINTHELIGHTANDBEINGRECOGNISEDANDCHALLENGEDBYHISFELLOWTRADESMANWHOMHESTOPPEDINHISCHARACTEROFTHECAPTAINGALLANTLYSHOTHIMTHROUGHTHEHEADANDRODEAWAYTHEMAILWASWAYLAIDBYSEVENROBBERSANDTHEGUARDSHOTTHREEDEADANDTHENGOTSHOTDEADHIMSELFBYTHEOTHERFOURINCONSEQUENCEOFTHEFAILUREOFHISAMMUNITIONAFTERWHICHTHEMAILWASROBBEDINPEACETHATMAGNIFICENTPOTENTATETHELORDMAYOROFLONDONWASMADETOSTANDANDDELIVERONTURNHAMGREENBYONEHIGHWAYMANWHODESPOILEDTHEILLUSTRIOUSCREATUREINSIGHTOFALLHISRETINUEPRISONERSINLONDONGAOLSFOUGHTBATTLESWITHTHEIRTURNKEYSANDTHEMAJESTYOFTHELAWFIREDBLUNDERBUSSESINAMONGTHEMLOADEDWITHROUNDSOFSHOTANDBALLTHIEVESSNIPPEDOFFDIAMONDCROSSESFROMTHENECKSOFNOBLELORDSATCOURTDRAWINGROOMSMUSKETEERSWENTINTOSTGILESSTOSEARCHFORCONTRABANDGOODSANDTHEMOBFIREDONTHEMUSKETEERSANDTHEMUSKETEERSFIREDONTHEMOBANDNOBODYTHOUGHTANYOFTHESEOCCURRENCESMUCHOUTOFTHECOMMONWAYINTHEMIDSTOFTHEMTHEHANGMANEVERBUSYANDEVERWORSETHANUSELESSWASINCONSTANTREQUISITIONNOWSTRINGINGUPLONGROWSOFMISCELLANEOUSCRIMINALSNOWHANGINGAHOUSEBREAKERONSATURDAYWHOHADBEENTAKENONTUESDAYNOWBURNINGPEOPLEINTHEHANDATNEWGATEBYTHEDOZENANDNOWBURNINGPAMPHLETSATTHEDOOROFWESTMINSTERHALLTODAYTAKINGTHELIFEOFANATROCIOUSMURDERERANDTOMORROWOFAWRETCHEDPILFERERWHOHADROBBEDAFARMERSBOYOFSIXPENCEALLTHESETHINGSANDATHOUSANDLIKETHEMCAMETOPASSINANDCLOSEUPONTHEDEAROLDYEARONETHOUSANDSEVENHUNDREDANDSEVENTYFIVEENVIRONEDBYTHEMWHILETHEWOODMANANDTHEFARMERWORKEDUNHEEDEDTHOSETWOOFTHELARGEJAWSANDTHOSEOTHERTWOOFTHEPLAINANDTHEFAIRFACESTRODWITHSTIRENOUGHANDCARRIEDTHEIRDIVINERIGHTSWITHAHIGHHANDTHUSDIDTHEYEARONETHOUSANDSEVENHUNDREDANDSEVENTYFIVECONDUCTTHEIRGREATNESSESANDMYRIADSOFSMALLCREATURESTHECREATURESOFTHISCHRONICLEAMONGTHERESTALONGTHEROADSTHATLAYBEFORETHEM"

#Building a list containing all alphabet uppercase letters

letters = [chr(x) for x in range(65,91)] 

import random

random.seed(232312)

substitution = {}

c = 0

while len(letters) > 0:
	pos = random.randint(0,len(letters)-1)
	substitution[chr(65+c)] = letters[pos]
	c += 1
	del letters[pos]

print(substitution)

ciphertext = ""

for letter in plaintext:
	ciphertext += substitution[letter]


#print(ciphertext)

frequencies = {}

for letter in ciphertext:
	if letter not in frequencies:
		frequencies[letter] = 1
	else:
		frequencies[letter] += 1


print(frequencies)
