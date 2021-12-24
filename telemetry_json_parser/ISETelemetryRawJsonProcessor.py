import json
import glob
import os
import csv



def loadCSVFile(file_name):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line = line.replace('\n', '')
            line = line.replace('\t', '')
            loadCSVList.append(line)
    print(loadCSVList)

def check_if_string_in_file(string_to_search):
    #print(string_to_search)
    if string_to_search.strip() in loadCSVList:
        return True
    else:
        return False




path = '/Users/kojayaku/Documents/ISE/TELEMETRY/jsons/nadinfo/'
data_list = [["DeploymentID", "UDISN", "Status"]]
loadCSVList = []

files = [f for f in glob.glob(path + "**/*.json")]

#loadCSVFile('/Users/mbagalko/Desktop/udi_test_data')

for f in files:
    with open(f, "r") as read_file:
        developer = json.load(read_file)

        print("Start Parsing JSON file : ",os.path.basename(f))
        tp = developer["telemetryParts"]
        jsonLength = len(tp)
        count=0
        emptyDeploymentInfoCount=0
        totalValidRecords=0
        deploymentIDCount=0
        licenseDepID=0
        nadDepID = 0
        netAccessDepID=0
        mdmDepID=0
        kongDepID=0
        profilerDepID=0
        totalIseNodes=0
        totalIseNodesWithSN=0
        totalNodesWithVersion=0
        totalNodesWithDict=0
        deploymentPresentInRachitaFile=0
        licSNCount = 0
        noSNSetCount = 0
        missingLicenseDetails = 0
        evalLicenses = 0

        LICENSE_CSV='license.csv'
        DEPLOYMENT_CSV='deployment.csv'

        license_info_list=[]
        deployment_info_list=[]

        LICENSE_HEADER=['Deployment ID','Primary UDI','Secondary UDI']
        DEPLOYMENT_HEADER=['Deployment ID','SN','Status','Name']

        #license_info_list.append(LICENSE_HEADER)
        #deployment_info_list.append(DEPLOYMENT_HEADER)

        depIDList = ["7f4aa0cd-31a3-4834-a623-383e19fa859a"]
        #depIDList = ["d61e2ffd-4f6e-42e9-ab21-a0181a8afeec","60202684-8fcf-48a0-afd4-ff7076aeab22","79aaeb30-402d-4d70-9999-a5d55fa7fc38","3cb2ffd8-04a5-4d6b-9241-97262da0c865","ed9269d0-19a5-463f-82c5-7eb9d187b33f","9159e8bb-2336-4c3a-8609-a18d1221c18f","20c045da-59ed-4f6f-a661-6562eb2b9f87","0e380253-de89-4291-8152-c8ef932d67cd","c318cf9b-3143-4061-9cce-8432782ca32c","53b19a6d-3236-4e4a-8584-082b7bd572b8","fd0105e0-a822-4b08-beff-3c068e75cc81","f4f35478-bf91-4a2c-b4f3-81aa60f893a4","b7483886-dae5-4c88-9728-620a5439bf26","58b1fdb5-5726-43ba-881d-60f6a2eb122b","defe94c1-bd0c-43b2-a5c9-44bb95c9592b","f86b3c98-7996-40f5-9f4e-e42d7e933a48","5a19e9e2-28b0-4c0c-8d1f-9a9928fc80b8","5a1da0e4-f140-48d3-a1ec-17f013680b50","1fa4090a-2625-43a1-ba1f-6ff65b12dca2","b79446ce-a242-40c3-b25d-31b6f8153b1d","fe0ed594-0723-41a1-b1bc-f457ea14b4d7","8de99976-2ae7-41f1-9fdd-015a4df746c7","e24daacf-8e08-41c2-96cd-bfae8fbc9889","7a0add3c-5f1f-40b2-af8b-ce7bb112bcf3","ac8dfdbc-fa6c-4eba-8871-010f448a49d9","ac8dfdbc-fa6c-4eba-8871-010f448a49d9","6a27b0ee-6606-44d9-b4f8-3d6739be4e48","0b636710-37b4-4eed-ba1e-c620d507d054","11cf95eb-b19b-489b-9f62-c8fb5f340b16","d8c88c7f-f127-4c97-b9ad-414fbb1a5565","2957ace7-e083-4d57-ac7b-4a5d2318b515","9ca41d7d-6572-49fa-a6ba-7a9fd9ef2802","29cbd8af-6da1-4554-a3b9-be70513a1156","815c296a-54f7-427b-8441-0e8c5fcbc14a","0b586e66-dd81-4ab8-8c48-73603e3fe331","5e38b2e8-1cab-49d6-a0d5-47d4b590a799","7bb8bfc0-350d-4946-878b-7df75032fdd4","eaee0f9a-65bd-424e-adc2-fd680c9c2cd3","19f2116f-dbe3-4226-85b8-d9358ca3224f","2959c4cd-e044-45f4-b63d-95664cad4473","bc877735-3a75-4786-aaa1-1fba420175b6","0b636710-37b4-4eed-ba1e-c620d507d054","11cf95eb-b19b-489b-9f62-c8fb5f340b16","44b9de51-c87a-433f-81a0-5fe7be4768f1","44b9de51-c87a-433f-81a0-5fe7be4768f1","b23dfd60-ba10-4d71-99a8-c6370bc624be","991899f7-08df-4ead-920b-f954fedf34c6","72c0859a-535f-43a7-96cf-ea75a5abbcd3","0b636710-37b4-4eed-ba1e-c620d507d054","11cf95eb-b19b-489b-9f62-c8fb5f340b16","ab470ed5-8a76-4fd4-bebd-17b3b3e76fbb","1740214d-ea97-4f18-9779-2228128a73be","980e9e70-8cea-4ba7-9559-0b482ec42c5a","b16be24c-ee02-4473-80c9-ee1e6dc15910","896176e6-ff9e-417b-8bdb-190fcae7ee89","4606975b-5832-4dea-943c-4f1c67e47a4a","5cea9910-f0e9-4e83-b94d-299157e24b82","74133b75-e776-479f-9f2b-89f74d19fd03","af6db001-e5bf-4b31-bf01-60be5c6ba156","89e8d907-2e99-4571-a510-ed84da9fa96f","985c3de8-dd89-44e3-b876-5c2fa5550d2a","e9f4444b-c85b-4e90-a8b1-7b22c864d911","eaca8e86-9ee5-46c4-bec6-a6e214208752","4964eca7-711b-4c74-a7d6-5eaf5534e4c1","42eaba76-7312-4cd0-8977-fb8fa77cd942","972926a2-1acc-46c3-8bfe-907efc9d65a5","5825313e-0f2c-406d-904c-16c2240e366b","7749e5bc-60da-473d-b7c8-36bdccd7ffc1","73c9b25a-2f42-404e-b86b-cca4ab8f9462","029ec131-49ca-41f5-a07d-aea309b0ecea","726df127-cd49-44eb-9fbe-a2e141dfcee7","cd55225b-cf01-4ba7-bbf4-19ac30876c10","e4c8bd49-afd4-4258-ba56-1f9f5f9ac47e","f5893a3c-2c72-429e-8f68-023bc61ad805","717b6e8d-3253-493a-8c0c-39434da78a5f","0a7a2043-da59-4c81-8679-a94c5ace3b7b","e4295f65-cb45-4f80-bc0c-52bf62662d0e","e10ef880-c277-4360-aac7-de793e82df22","e629712b-aef2-46d5-90bd-a366af3bd425","0b43c96a-1f67-4f5c-9668-9cc8eb302048","9a6545aa-af53-4d65-bad2-1354bf2b5dbf","0470e4c6-14a2-4736-aab7-296e0c96d6e3","4d392c09-6de2-4155-9128-f0edbfab509c","6767e402-6674-4354-aed9-c2c0d9a250a2","d9f2b87f-3a5e-4fc6-9943-f048a366b21f","93d974b4-4642-4b4a-8a87-d4a81e3df918","014ee08d-fbb0-4187-a17e-79ed05186e74","4b89315b-50e8-4122-8968-47b704c1d699","41b70d94-a422-4086-99dd-ac46f656438a","f414c8f2-67cb-44d2-8c5e-590fb3b78b89","2647dfcf-bec3-4058-9ba3-589fc6c9013c","2647dfcf-bec3-4058-9ba3-589fc6c9013c","3a00bd73-263b-4161-a5b8-a9e56cd516cd","3a00bd73-263b-4161-a5b8-a9e56cd516cd","3a00bd73-263b-4161-a5b8-a9e56cd516cd"]
        udiList = ["FCH1848V1XM","FCH1849V0FL","FCH1849V0G3","FCH1849V0GT","FCH1850V1ZQ","FCH1850V2BC","FCH1850V2BE","FCH1850V2CW","FCH1851V03F","FCH1914V0D5","9DFEJL41I1H","A8CRI6SFOBG","ACQC54IBB2Q","ARAOIJE8J67",
                   "B2CFQME4CO7","B5UFCJ37869","BHB7Q2D8CAL","BHHGD49JDGF","DATO69K5NI8",
                   "DFQEBALGQF9","DQ7S2E76ANG","EH4APLR5GCF","ELFMFKAEQCQ","FCH1743V0S5","FCH1744V04K","FCH1807V20H","FCH1830V3AJ","FCH1837V12S","FCH1843V0NY","FCH1845V0J7","FCH1845V1DT","FCH1921V154","FCH1927V1HE",
                   "FCH1936V2RB","FCH1943V1C8","FCH1943V21P","FCH2015V1RZ","FCH2016V2RZ","FCH2022V1UQ","FCH2024V0C7","FCH2026V15M","FCH2027V1KH","FCH2029V1LT","FCH2029V2GJ","FCH2030V1KB","FCH2031V0MS","FCH2033V096",
                   "FCH2033V2PE","FCH2033V3DE","FCH2033V4RV","FCH2034V0DQ","FCH2034V10A","FCH2034V10C","FCH2034V137","FCH2034V3QT","FCH2034V3VR","FCH2034V40Z","FCH2034V45M","FCH2036V36C","FCH2038V1BQ","FCH2041V0MN",
                   "FCH2044V0WQ","FCH2044V1M3","FCH2046V17B","FCH2046V1Q2","FCH2046V27R","FCH2047V0MA","FCH2048V0DN","FCH2049V27A","FCH2051V006","FCH2051V0EC","FCH2051V0HZ","FCH2051V0YT","FCH2051V1U5","FCH2052V0R9",
                   "FCH2104V0LH","FCH2104V0ML","FCH2107V1WD","FCH2107V26K","FCH2108V191","FCH2108V2PT","FCH2109V2FJ","FCH2109V2GR","FCH2114V0PB","FCH2114V15E","FCH2115V0Z5","FCH2115V1UG","FCH2116V1XV","FCH2117V0QE",
                   "FCH2119V06V","FCH2124V05L","FCH2124V1W5","FCH2126V04A","FCH2126V06L","FCH2127V2LA","FCH2129V1HB","FCH2130V0NL","FCH2131V0DG","FCH2133V23Z","FCH2133V24M","FCH2133V24R","FCH2133V24S","FCH2133V26Y",
                   "FCH2133V2JM","FCH2134V078","FCH2137V0XX","FCH2143V0M9","FCH2143V0UJ","FCH2143V0ZC","FCH2146V1LK","FCH2146V2ZE","FCH2147V0AB","FCH2147V1AN","FCH2147V1P4","FCH2147V27X","FCH2148V15E","FCH2148V18F",
                   "FCH2148V1VA","FCH2148V1W6","FCH2148V1ZV","FCH2151V112","FCH2203V01K","FCH2203V1CJ","FCH2204V17C","FCH2209V050","FCH2209V05N","FCH2209V0KX","FCH2209V0L0","FCH2210V0KA","FCH2211V0FH","FCH2212V12C","FCH2212V12J","FCH2215V1AA","FCH2218V0UJ","FCH2220V12K","FCH2220V13A","FCH2222V0NJ","FCH2222V0NK","FCH2222V0SU","FCH2222V0SV","FCH2222V0T0","FCH2222V0T2","FCH2222V16Y","FCH2222V17F","FCH2222V1J4","FCH2222V2AL","FCH2222V3YG","FCH2223V03Z","FCH2223V0QH","FCH2224V0BL","FCH2226V08A","FCH2226V1QM","FCH2226V2CG","FCH2226V3W5","FCH2226V3W7","FCH2226V7C1","FCH2226V8P3","FCH2226VBFY","FCH2226VC72","FCH2226VC9J","FCH2226VCFB","FCH2226VCY7","FCH2226VJGQ","FCH2226VJSD","FCH2226VJVX","FCH2226VKFV","FCH2226VKQ8","FCH2241V0BD","FCH2242V0RF","FCH2242V0VY","FCH2245V12S","FCH2245V17K","FCH2248V0AE","FCH2248V18L","FCH2250V02R","FCH2251V15A","FCH2252V0UF","FCH2301V0FC","FCH2302V0KZ","FCH2302V0N5","FCH2302V1BS","FCH2303V0M4","FCH2303V11M","FCH2304V0C4","FCH2304V0CG","FCH2304V0DU","FCH2304V0E7","FCH2304V0GH","FCH2305V102","FCH2305V128","FCH2307V02L","FCH2307V0HG","FCH2308V0EB","FCH2312V0P2","FCH2313V052","FCH2314V0SK","FCH2320V07Y","FF973C7MCGG","GDNCU838DNH","GOGOEFB4EJE","H2EH69MSSOC","HGCAEHNF2I5","HMHIHB5NR3O","HNLN7EDGL6G","HPDNKAHFDEP","HQMEAHG9KIT","I85D3S7GB67","IGKJGGKMQFE","IJFGLDSGHGH","IO2NCACIKAL","JAI5K4E8AMF","JHOJLFHFF06","KDA753GEHCD","LEAS8IGBEQK","LH9NIFOJGLG","LREG3MDCPPD","MEFQ3IDH8N8","N4CG6DNHG8A","NDE8MONGDQF","O8EEEQQH7JG","OAKGJ6TBKOQ","ODBFEIB9J9H","Q875Q9E8366","QJFKPDHMGFI","QUNGDQRJGMD","UNSUPPORTED","UNSUPPORTED67","UNSUPPORTEDd","UNSUPPORTEDed","UNSUPPORTEDin","WMP23500020","WMP2401000D","WMP2401000Z","WMP24010016","WMP2401001A","WMP2401001C","WMP2401001F","WMP2401001S","WMP2401002M","WMP2401002Q","WMP2401003P","WMP2401005X","WMP24010076","WMP24010087","WMP2402001U","WMP24020032","WMP2402003U","WMP2402005C","WMP24020080","WMP240200D5","WMP240300HW","WMP240300L3","WMP24040001","WMP240400H9","WMP240400LU","WMP240400TP","WMP2406009M","WMP240600AE","WMP240600ED","WMP2407006A","WMP2408000C","WMP2408000N","WMP240800PF","WMP240800PS","WMP240800PU","WMP240800PX","WMP240800Q4","WMP240800VN","WMP2408011G","WMP2408011H","WMP2408015W","WMP240900CD","WMP240900FA","WMP241000D5","WMP241000DW","WMP241000HT","WMP241000M6","WMP241000Q7","WMP241000QA","WMP241000V7","WMP2410013D","WMP241100S5","WMP241200EA","WMP2414006J","WMP241400CB","WMP241400EV","WMP241400GT","WMP241400GU","WMP241400JW","WMP241400K1","WMP241400K8","WMP241400Q7","WMP24150004","WMP2415000B","WMP2415001D","WMP24150022","WMP24150028","WMP24150053","WMP2415005P","WMP2415006C","WMP2415007M","WMP2415007P","WMP2415008Z","WMP241500E8","WMP2421006X","WMP242100EZ","WMP242100G5","WMP242100LJ","WMP242100RP","WMP242100UH","WMP2421011R","WMP2421013T","WMP242201KL","WMP242201KT","WMP242201SW","WMP242201Y9","WMP242201YP","WMP242201YS","WMP242201YY","WMP242300LZ","WMP2424000P","WMP2424000Q","WMP2424000Z","WMP2424001F","WMP2424004Y","WMP2424010Z","WMP2424013P","WMP2424016A","WMP242401F1","WMP24250033","WMP2425003S","WMP24250048","WMP24250062","WMP24250065","WMP24250094","WMP2425009G","WMP242500EJ","WMP242500G2","WMP242500G6","WMP242500GF","WMP242500H1","WMP2426003D","WMP2426005Y","WMP2426006N","WMP2426009P","WMP242600A3","WMP242600CD","WMP242600CM","WMP242600DQ","WMP242600ED","WMP242600G0","WMP242600GD","WMP242600HQ","WMP242600HZ","WMP242600JF","WMP242600K1","WMP242600K2","WMP242600LL","WMP242600LT","WMP242600LX","WMP242600LZ","WMP242600M3","WMP242600M4","WMP242600MB","WMP242600MK","WMP242600RA","WMP242600RJ","WMP242600RM","WMP242600SC","WMP24260157","WMP2426017Y","WMP2427002F","WMP2427003T","WMP2427003W","WMP2427003Y","WMP2427005A","WMP2427005M","WMP2427006G","WMP2427006K","WMP2427006R","WMP2427006Y","WMP2427008G","WMP2427008H","WMP2427008R","WMP2427009Q","WMP242700AK","WMP242700AM","WMP242700AU","WMP242700B2","WMP242700CA","WMP242700JR","WMP242700K4","WMP242700KK","WMP242700Q3","WMP242700QA","WMP242700SP","WMP242700TT","WMP242700VV","WMP242700Y9","WMP242700YB","WMP242700YN","WMP242700YT","WMP2427012E","WMP2427013B","WMP2427018H","WMP2428007V","WMP242800DN","WMP242800N9","WMP242800QB","WMP242800QK","WMP242800UQ","WMP242800V3","WMP242800VC","WMP2428015K","WMP2428016G","WMP24290009","WMP2429000D","WMP2429000J","WMP24290024","WMP2429006E","WMP2429009R","WMP242900BF","WMP24290110","WMP2429012G","WMP2429012W","WMP2429013U","WMP2429013Z","WMP24290142","WMP2429015N","WMP2430009K","WMP243000A3","WMP243000SN","WMP243000SR","WMP24300103","WMP243100GL","WMP243100MX","WMP243100RR","WMP2431012R","WMP2431012Z","WMP2432002P","WMP24340043","WMP243400BY","WMP243400TV","WMP243400ZB","WMP243500HA","WMP2436000M","WMP24370020","WMP2437007Q","WMP243700MX","WMP243700XB","WMP2438004W","WMP24380051","WMP2438005A","WMP2438005D","WMP2438005E","WMP243800GJ","WMP2439000X","WMP24390020","WMP2439006L","WMP2439007G","WMP243900WK","WMP243900XM","WMP24390117","WMP2440000Y","WMP2440001G","WMP2440001K","WMP2440002E","WMP2440004P","WMP2440007T","WMP2440008E","WMP2440008N","WMP244000FP","WMP244000KQ","WMP244000M4","WMP244000NG","WMP244000S9","WMP244000SB","WMP244000W5","WMP244000ZT","WMP244000ZW","WMP244000ZX","WMP244000ZZ","WMP24400106","WMP2440016Z","WMP244001A6","WMP244001C2","WMP244001CG","WMP2441001X","WMP2441002G","WMP24410032","WMP24410041","WMP244100G4","WMP244100QA","WMP244100RS","WMP244100U6","WMP2442000D","WMP244200AQ","WMP244200CR","WMP244200D3","WMP244200DA","WMP244200DX","WMP244200Q8","WMP244200VH","WMP24420139","WMP2442013Y","WMP24420151","WMP24420158","WMP2442015E","WMP2442016K","WMP24420178","WMP244300YN","WMP2444000M","WMP2444003S","WMP24440047","WMP2444004F","WMP2444004H","WMP2444005A","WMP2444005H","WMP24440071","WMP2445001E","WMP2445005M","WMP2445006A","WMP2445006B","WMP244500WQ","WMP244500XF","WMP2445014B","WMP2445014Z","WMP2445015B","WMP2445018D","WMP2446000C","WMP244800EY","WMP244900RD","WMP244900UB","WMP244900UK","WMP244900UP","WMP244900UQ","WMP244900UZ","WMP2450004B","WMP24500069","WMP245100FE","WMP245100LM","WMP245100N3","WMP245100N4","WMP245100SL","WMP245100SY","WMP245100TQ","WMP245100XF","WMP245100XT","WMP2452006W","WMP250100AQ","WMP250300YA","WMP2504002M","WZP22100SCF","WZP22161A40","WZP22161A41","WZP222714Z2","WZP222714ZG","WZP2228085W","WZP22341MJL","WZP22341MJS","WZP223606P4","WZP223918TV","WZP223918UB","WZP2302017Z","WZP230203ZZ","WZP230305F8","WZP230308NY","WZP230308R8","WZP230308RN","WZP230308SH","WZP2307005F","WZP2307005H","WZP230807GU","WZP230807H4","WZP230807HY","WZP230807JA","WZP230807JQ","WZP230807JT","WZP23080A2L","WZP23080A2N","WZP23080A2Y","WZP23130HFX","WZP23130HJ1","WZP23130HJA","WZP23140FCB","WZP23140FCJ","WZP23160DZZ","WZP23170MNU","WZP231910X5","WZP23200KYF","WZP23200KZG","WZP23200TXL","WZP232204T9","WZP23230E43","WZP23240TPV","WZP23240W7T","WZP2325005M","WZP23250ZBJ","WZP23250ZBN","WZP23250ZBP","WZP23250ZBX","WZP23250ZHV","WZP23260061","WZP23270W5E","WZP232806YE","WZP23280722","WZP23280PZ0","WZP23280RX5","WZP23280S30","WZP23280Y12","WZP23280Y1J","WZP232810EP","WZP232903AB","WZP232903FE","WZP232903SD","WZP2329048P","WZP23290497","WZP232904A1","WZP232904AA","WZP232904AG","WZP232913HU","WZP232913NH","WZP232913SN","WZP232913T9","WZP232913TK","WZP2330065U","WZP23300678","WZP23300EVZ","WZP23300F2Y","WZP23300NYF","WZP233016P5","WZP233100TP","WZP23310JZU","WZP23310K0X","WZP23310MHM","WZP23310MKQ","WZP23310MRB","WZP23320Y3H","WZP23330ECW","WZP23330ELE","WZP23330F9Q","WZP23330FDW","WZP23330FE1","WZP23330FEB","WZP23330FG1","WZP23330FG9","WZP23330FKE","WZP23330FKW","WZP233404BD","WZP23350575","WZP23350578","WZP2335057E","WZP233505C2","WZP23350GYD","WZP23350YHT","WZP23350Z90","WZP233514AE","WZP233609M6","WZP23360FKV","WZP23360FSZ","WZP23360QFT","WZP233707YS","WZP23370Z6T","WZP2337111T","WZP233800HV","WZP233800PU","WZP233802KC","WZP233808DT","WZP233808EH","WZP23380BBL","WZP23380D6R","WZP23380DFY","WZP23380DKR","WZP23380DM9","WZP23380JCA","WZP233818US","WZP23390RYY","WZP23390S9P","WZP23390SDL","WZP23390VVR","WZP23390W0Q","WZP23390W4D","WZP23391FEQ","WZP23391PX3","WZP23391QFM","WZP23391QNW","WZP23400AMD","WZP23400APY","WZP234107MQ","WZP23410895","WZP23410KN2","WZP23410W5M","WZP23410W9G","WZP23420P4M","WZP234217QA","WZP234217UT","WZP23421HZD","WZP234301RM","WZP234301S0","WZP234301TY","WZP23430C3E","WZP23430C5T","WZP23430GFS","WZP23430PHC","WZP23430PKV","WZP23430PL0","WZP23430PLT","WZP234310D9","WZP234310GY","WZP234404WS","WZP234404ZM","WZP2344050V","WZP2344050Y","WZP234415WP","WZP23451BP9","WZP23451BQA","WZP23451BRW","WZP23451BRX","WZP234607UP","WZP234607ZY","WZP23460801","WZP23460N3R","WZP23461APU","WZP23461AQH","WZP23461TA5","WZP23461TCD","WZP23470711","WZP23470JYE","WZP23470K0B","WZP23470K1W","WZP23470VFL","WZP23470VG9","WZP23470VGU","WZP23470VNH","WZP23470VR0","WZP234714QQ","WZP23471AP7","WZP23471ARG","WZP23471AS9","WZP23480489","WZP234804AX","WZP234804GS","WZP234804PE","WZP234804QB","WZP23480H73","WZP23480H7E","WZP23480SXP","WZP23480SY0","WZP23481386","WZP23490J1Q","WZP23490JCL","WZP23490XMD","WZP23490XN4","WZP23491DHN","WZP23491DJ0","WZP23491DXH","WZP23491DXN","WZP23491P47","WZP23491P4N","WZP23491P7F","WZP23491PFQ","WZP2350089T","WZP23500NXB","WZP23501C4X","WZP23501C71","WZP23501CAE","WZP23501CB1","WZP23501CD4","WZP23501LCE","WZP23501LD9","WZP23501LH5","WZP23501LL4","WZP235106ZZ","WZP2351070N","WZP23510C65","WZP23510C8Y","WZP23511H6V","WZP23511H6W","WZP23511T3R","WZP23511T45","WZP23511T4C","WZP23511T4T","WZP23511T5H","WZP23511TF2","WZP23511TFB","WZP23511TFU","WZP23521NZ7","WZP23521NZT","WZP23521P00","WZP23521P03","WZP23521P04","WZP23521P2A","WZP23521P3L","WZP23521P4V","WZP23521P51","WZP23521P6L","WZP23521P6T","WZP23521P7S","WZP24010ESW","WZP24010ETA","WZP24010ETM","WZP24010S6G","WZP24010S6S","WZP240111HS","WZP240111J8","WZP240111K8","WZP24020JLZ","WZP24020JM6","WZP24020TL7","WZP24020TNH","WZP24020YPA","WZP24020YPN","WZP24020YPX","WZP24020YPY","WZP24020YPZ","WZP24020YQ0","WZP24020YQ3","WZP24020YQ4","WZP24020YQ8","WZP24020YQA","WZP24020YQC","WZP24020YQM","WZP24020YQQ","WZP24020YQX","WZP24020YQZ","WZP240305LS","WZP240305LT","WZP240305LU","WZP240305M8","WZP240305MV","WZP240305MY","WZP240305TL","WZP241517VJ","WZP24161YM4","WZP24170SMJ","WZP24171P5B","WZP24171P5V","WZP24171P86","WZP24171P89","WZP24171P8T","WZP24171P8V","WZP24171PCF","WZP24171PCJ","WZP24171PCY","WZP24171PGN","WZP24172929","WZP241804YB","WZP241804YS","WZP24180K94","WZP24180KA9","WZP24180KBM","WZP24180KEG","WZP24180KJN","WZP24180KKD","WZP24180KKJ","WZP24180KL1","WZP24180KN1","WZP24180KN4","WZP24180KNA","WZP24180KNZ","WZP24180KPD","WZP24180KPJ","WZP24180KPN","WZP24180VLE","WZP24180VM8","WZP24180VMB","WZP24181AK7","WZP2420076K","WZP242012YX","WZP2420133M","WZP2420133N","WZP242017TR","WZP24201PY4","WZP24201PYJ","WZP242102AQ","WZP242102CX","WZP24210N8F","WZP24210NCA","WZP24210NDJ","WZP24210NDL","WZP24210NGR","WZP24210V00","WZP24210V0G","WZP24210VJ3","WZP24210VJH","WZP24210VJK","WZP24210VLX","WZP24210VN3","WZP24210XW0","WZP24210Y3B","WZP24210Y4S","WZP24210YE9","WZP24210YED","WZP242208EP","WZP242208GE","WZP242208GG","WZP242208GV","WZP242208H3","WZP242208HJ","WZP242208HX","WZP242208LT","WZP242208MJ","WZP242208NV","WZP242208P8","WZP24220DMV","WZP24220DU7","WZP24220DY6","WZP24220E13","WZP24220N8U","WZP24220NJB","WZP24220NJJ","WZP24220NP5","WZP24220UUG","WZP24220V3B","WZP24220V7Z","WZP242211HS","WZP242217ER","WZP242217G2","WZP242217HD","WZP242217JF","WZP242304MN","WZP24230EA4","WZP24230EB7","WZP24230EEH","WZP24230EF2","WZP24230EF4","WZP24230EF5","WZP24230EFA","WZP24230EHF","WZP24230EHL","WZP24230EKW","WZP24230ENZ","WZP24230EQ1","WZP24230ER0","WZP24230UZ9","WZP24230UZH","WZP24230V0H","WZP24230V7Z","WZP24230V81","WZP24230V87","WZP24230V8A","WZP24230V9C","WZP24230VBN","WZP242310MU","WZP242310UL","WZP242310UQ","WZP242310V8","WZP242310XQ","WZP2423134M","WZP2423135S","WZP242315GB","WZP24240CS6","WZP24240CSR","WZP24240QM4","WZP24240QYX","WZP24240R43","WZP24240R8M","WZP24240Z5E","WZP24241542","WZP242415DX","WZP24241A73","WZP24241ABG","WZP242506EA","WZP242506HM","WZP242506J2","WZP242508SV","WZP242508VK","WZP242508VR","WZP242508WM","WZP24250SBN","WZP24250SBP","WZP24250SD2","WZP24250SJK","WZP24250SUM","WZP24250SVG","WZP24250WUU","WZP24250WV5","WZP24250WX6","WZP24250WXD","WZP24250WXU","WZP24250WXZ","WZP24250WZZ","WZP242602MW","WZP242602NZ","WZP242602PP","WZP242602SZ","WZP242602T5","WZP242602TG","WZP242602U4","WZP242602XB","WZP242602XP","WZP242602XZ","WZP2426087L","WZP24260899","WZP2426089A","WZP2426089D","WZP242608BV","WZP242608C1","WZP242608CA","WZP242608CD","WZP242608E9","WZP242608FK","WZP242608FM","WZP242608FP","WZP24260D35","WZP242701AX","WZP242701BD","WZP242701CA","WZP242701CB","WZP242701E3","WZP242701FP","WZP242701G5","WZP242701G9","WZP242701GD","WZP242701GF","WZP242701GG","WZP242701GQ","WZP242701HJ","WZP242701HM","WZP242701HX","WZP242701J4","WZP242701JW","WZP242701LY","WZP242701M0","WZP242701M9","WZP242701MR","WZP242701MT","WZP242701NH","WZP242701SK",
                   "WZP242701SS","WZP242707GZ","WZP242707JA","WZP242707PN","WZP242707WA","WZP242707WD","WZP2428062B","WZP24280GMV","WZP24280GNF","WZP24290UHQ","WZP24290UJ8","WZP24290UJB","WZP24290UJL","WZP243002HG","WZP24300AZ7","WZP24300AZQ","WZP24300AZW","WZP243201L5","WZP243201M6","WZP243401XF","WZP2434020A","WZP2434023Y","WZP24340260","WZP2434026Z","WZP243402TR","WZP243402U7","WZP243402UA","WZP243402UB","WZP243402UY","WZP243402V0","WZP243402V3","WZP243601C3","WZP243705V1","WZP243705V8","WZP243705VA","WZP243804BB","WZP243809FW","WZP243809J2","WZP24380C6W","WZP24380C6X","WZP24380E2Y","WZP24380E3G","WZP24380E3J","WZP24380GUV","WZP24380GY3","WZP243901LA","WZP243903UV","WZP2442012Q","WZP24430Z9C","WZP24430Z9L","WZP244805YC","WZP244906UP","WZP244906X8","WZP245002RU","WZP2450061P","WZP25040PAR"]

        licPrimUDI=""
        licSecUDI=""
        tmpdepIdCount = 0
        tmpLicIsEval = True
        nadProfNameSet=[]

        for part in tp:
            #print(part)

            if 'KongInfo' in tp[count]['data']['payload']['payload'] and 'KongInfo' in tp[count]['data']['payload']['payload']['KongInfo']:
                #print(tp[count]['data']['payload']['payload']['NetworkAccessInfo'])
                kongInfo = tp[count]['data']['payload']['payload']['KongInfo']['KongInfo']
                #print(kongInfo)
                if 'DeploymentID' in kongInfo:
                    kongDepID = kongDepID + 1


            if 'ProfilerInfo' in tp[count]['data']['payload']['payload'] and 'ProfilerInfo' in tp[count]['data']['payload']['payload']['ProfilerInfo']:
                #print(tp[count]['data']['payload']['payload']['NetworkAccessInfo'])
                profilerInfo = tp[count]['data']['payload']['payload']['ProfilerInfo']['ProfilerInfo']
                #print(profilerInfo)
                if 'DeploymentID' in profilerInfo:
                    profilerDepID = profilerDepID + 1

            if 'MDMInfo' in tp[count]['data']['payload']['payload'] and 'MDMInfo' in tp[count]['data']['payload']['payload']['MDMInfo']:
                #print(tp[count]['data']['payload']['payload']['NetworkAccessInfo'])
                mdmInfo = tp[count]['data']['payload']['payload']['MDMInfo']['MDMInfo']
                if 'DeploymentID' in mdmInfo:
                    mdmDepID = mdmDepID + 1


            if 'NetworkAccessInfo' in tp[count]['data']['payload']['payload'] and 'NetworkAccessInfo' in tp[count]['data']['payload']['payload']['NetworkAccessInfo']:
                #print(tp[count]['data']['payload']['payload']['NetworkAccessInfo'])
                netAccessInfo = tp[count]['data']['payload']['payload']['NetworkAccessInfo']['NetworkAccessInfo']
                if 'DeploymentID' in netAccessInfo:
                    netAccessDepID = netAccessDepID + 1
            #else:
             #   print(">>>>  ",tp[count]['data']['payload']['payload'])
            oneOfSNSet = False
            noSNSet = False

            licPrimUDI=''
            licSecUDI=''
            licPrimSplit=''
            licSecSplit=''
            licSmartAcnt=''
            licFileNAme=''
            if 'LicensesInfo' in tp[count]['data']['payload']['payload'] and 'LicensesInfo' in tp[count]['data']['payload']['payload']['LicensesInfo']:
                licInfo = tp[count]['data']['payload']['payload']['LicensesInfo']['LicensesInfo']
                if licInfo['DeploymentID'] in depIDList:
                    print("LIC:>>  ",licInfo)



                if 'NodeList' in licInfo and 'Node' in licInfo['NodeList']:
                    licSmartAcnt = licInfo['NodeList']['Node']['SmartAccountName']
                    if 'License' in licInfo['NodeList']['Node']:
                        licNodeInfo = licInfo['NodeList']['Node']['License']
                        #print(">>:",licInfo['NodeList']['Node'])
                        #print(type(licNodeInfo))

                        if type(licNodeInfo) is dict:
                            if ('SecondaryUDI' in licNodeInfo):
                                licSecUDI=licNodeInfo['SecondaryUDI']
                            if ('PrimaryUDI' in licNodeInfo):
                                licPrimUDI=licNodeInfo['PrimaryUDI']
                            if('FileName' in licNodeInfo):
                                licFileNAme = licNodeInfo['FileName']

                        prStr = licInfo['DeploymentID']
                        licPrimSplit = licPrimUDI.split(':')[-1]
                        licSecSplit = licSecUDI.split(':')[-1]
                        if (licPrimUDI):
                            prStr = prStr + "," + licPrimSplit
                        if (licSecUDI):
                            prStr = prStr + "," + licSecSplit

                        if licInfo['DeploymentID'] in depIDList:
                            prStr = prStr + "," + licSmartAcnt
                            #print(prStr)
                            license_info_list.append([licInfo['DeploymentID'], licPrimSplit, licSecSplit, licFileNAme,licSmartAcnt])

                        if type(licNodeInfo) is list:
                            for licNode in licNodeInfo:
                                if('SecondaryUDI' in licNode):
                                    licSecUDI = licNode['SecondaryUDI']
                                if ('PrimaryUDI' in licNode):
                                    licPrimUDI = licNode['PrimaryUDI']
                                if ('FileName' in licNode):
                                    licFileNAme = licNode['FileName']

                                prStr = licInfo['DeploymentID']
                                licPrimSplit = licPrimUDI.split(':')[-1]
                                licSecSplit = licSecUDI.split(':')[-1]
                                if (licPrimUDI):
                                    prStr = prStr + "," + licPrimSplit
                                if (licSecUDI):
                                    prStr = prStr + "," + licSecSplit

                                if licInfo['DeploymentID'] in depIDList:
                                    prStr = prStr + "," + licSmartAcnt
                                    #print(prStr)
                                    license_info_list.append([licInfo['DeploymentID'], licPrimSplit, licSecSplit, licFileNAme,licSmartAcnt])
                    else:
                        #print(licInfo['NodeList']['Node'])
                        missingLicenseDetails = missingLicenseDetails + 1
                        if (licInfo['NodeList']['Node']['isEvaluationLic']):
                            #print(type(licInfo['NodeList']['Node']['isEvaluationLic']))
                            evalLicenses = evalLicenses + 1

                if licInfo['DeploymentID'] in depIDList:
                    tmpdepIdCount = tmpdepIdCount + 1
                    #print(licInfo)
                    #print("Deployment ID : {} Primary UDI: {} Secondary UDI: {}".format(licInfo['DeploymentID'],licPrimUDI,licSecUDI))



                if(oneOfSNSet):
                    licSNCount = licSNCount + 1
                if(noSNSet):
                    if 'License' in licInfo['NodeList']['Node']:
                        print("Not Present: ",licInfo['NodeList']['Node']['License'])
                    noSNSetCount = noSNSetCount + 1
                if 'DeploymentID' in licInfo:
                    licenseDepID = licenseDepID + 1
                    #if 'ed72a60b-9fca-494b-90d2-937057da1c16' == licInfo['DeploymentID']:
                    #    print(licInfo)

            if 'NADInfo' in tp[count]['data']['payload']['payload'] and 'NADInfo' in tp[count]['data']['payload']['payload']['NADInfo']:
                nadInfo = tp[count]['data']['payload']['payload']['NADInfo']['NADInfo']
                #if nadInfo['DeploymentID'] in depIDList:
                for nadProfNode in nadInfo['NodeList']['Node']['NADProfileInfo']:
                    #print(type(nadProfNode['Name']))
                    nadProfNameSet.append(nadProfNode['Name'])
                    #print(nadProfNode['Name'])

                if 'DeploymentID' in nadInfo:
                    nadDepID = nadDepID + 1

            if 'DeploymentInfo' in tp[count]['data']['payload']['payload'] and 'DeploymentInfo' in tp[count]['data']['payload']['payload']['DeploymentInfo']:
                depInfo = tp[count]['data']['payload']['payload']['DeploymentInfo']['DeploymentInfo']

                #if 'VersionHistoryInfo' in depInfo:
                #    print("Dep:>>", depInfo)

                if depInfo['DeploymentID'] in depIDList:
                    print(depInfo)
                    print("PART:  ",part)


                if 'NodeList' in depInfo and 'Node' in depInfo['NodeList']:
                    deplNodeInfo = depInfo['NodeList']['Node']

                    if type(deplNodeInfo) is list:
                        totalIseNodes = totalIseNodes + len(deplNodeInfo)
                        for node in deplNodeInfo:
                            if depInfo['DeploymentID'] in depIDList:
                                deployment_info_list.append([depInfo['DeploymentID'], node['SN'], node['Status'], node['Name'],node['Version']])
                            #    print(depInfo['DeploymentID'],",",node['SN'],node['Status'],node['Name'])

                            if (check_if_string_in_file(depInfo['DeploymentID'])):
                                deploymentPresentInRachitaFile = deploymentPresentInRachitaFile + 1
                            if "SN" in node:
                                totalIseNodesWithSN = totalIseNodesWithSN + 1
                                if (check_if_string_in_file(depInfo['DeploymentID'])):
                                    data_list.append([depInfo['DeploymentID'], node["SN"],node['Status']])
                                    print(depInfo['DeploymentID'], ",", node["SN"],",",node['Status'])
                            else:
                                print(">>:" , node)
                            if "Version" in node:
                                totalNodesWithVersion = totalNodesWithVersion + 1
                    if type(deplNodeInfo) is dict:
                        if depInfo['DeploymentID'] in depIDList:
                            deployment_info_list.append([depInfo['DeploymentID'],  deplNodeInfo['SN'], deplNodeInfo['Status'], deplNodeInfo['Name'],deplNodeInfo['Version']])
                        #    print(depInfo['DeploymentID'], ",", node['SN'],node['Status'], node['Name'])

                        if (check_if_string_in_file( depInfo['DeploymentID'])):
                            deploymentPresentInRachitaFile = deploymentPresentInRachitaFile + 1
                        totalIseNodes = totalIseNodes + 1
                        totalNodesWithDict = totalNodesWithDict + 1
                        if "SN" in deplNodeInfo:
                            if (check_if_string_in_file(depInfo['DeploymentID'])):
                                data_list.append([depInfo['DeploymentID'], node["SN"], node['Status']])
                                print(depInfo['DeploymentID'],",",node["SN"],",",node['Status'])
                            totalIseNodesWithSN = totalIseNodesWithSN + 1
                            #print(deplNodeInfo["SN"])
                        else:
                            print(">>>>:", deplNodeInfo)

                        if "Version" in deplNodeInfo:
                            totalNodesWithVersion = totalNodesWithVersion + 1

                if (check_if_string_in_file(depInfo['DeploymentID'])):
                    deploymentPresentInRachitaFile = deploymentPresentInRachitaFile + 1

                if 'DeploymentID' in depInfo and len(depInfo['DeploymentID']) > 0:
                    deploymentIDCount = deploymentIDCount + 1

                if 'NodeList' in depInfo:
                    totalValidRecords= totalValidRecords + 1

                if 'NodeList' not in depInfo:
                    emptyDeploymentInfoCount = emptyDeploymentInfoCount + 1
            count=count+1

        if os.path.exists(DEPLOYMENT_CSV):
            os.remove(DEPLOYMENT_CSV)

        if os.path.exists(LICENSE_CSV):
            os.remove(LICENSE_CSV)

        with open(LICENSE_CSV, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(license_info_list)

        with open(DEPLOYMENT_CSV, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(deployment_info_list)

        print("Total number of telemetry records : ", jsonLength)

        print("############################## DEPLOYMENT INFO ##############################\n")
        print("Total Number of telemetry data where DeploymentInfo->NodeList is not Empty : ", totalValidRecords)
        print("Total Number of telemetry data where DeploymentInfo->NodeList is Empty : ",emptyDeploymentInfoCount)
        print("Total Numnder of Deployment ID found under data->payload->payload->DeploymentInfo->DeploymentInfo : ",deploymentIDCount)
        print("Total Number of ISE nodes :",totalIseNodes)
        print("Total Number of ISE nodes with SN:", totalIseNodesWithSN)
        print("Total Number of ISE nodes with Version Info:", totalNodesWithVersion)
        print("Total Number of ISE nodes with Dictionary:", totalNodesWithDict)
        print("deploymentPresentInRachitaFile:",deploymentPresentInRachitaFile)

        print("############################## LICENSE INFO ##############################\n")
        print("Total Numnder of Deployment ID found under data->payload->payload->LicensesInfo->LicensesInfo : ",licenseDepID)
        print("Total License SN count :",licSNCount)
        print("Total License Where No SN Set :", noSNSetCount)
        print("Total deployments that are missing License info in lcense telemetry data : ",missingLicenseDetails,"  Out of these Evalauations license nodes are : ",evalLicenses)
        print("Total License deployment ID's present in raw json ",tmpdepIdCount)


        print("############################## NAD INFO ##############################\n")
        print("Total Numnder of Deployment ID found under data->payload->payload->NADInfo->NADInfo : ",nadDepID)

        print("############################## NETWORKACCESS INFO ##############################\n")
        print("Total Numnder of Deployment ID found under data->payload->payload->NetworkAccessInfo->NetworkAccessInfo : ",netAccessDepID)

        print("############################## MDM INFO ##############################\n")
        print("Total Numnder of Deployment ID found under data->payload->payload->MDMInfo->MDMInfo : ",mdmDepID)

        print("############################## PROFILER INFO ##############################\n")
        print("Total Numnder of Deployment ID found under data->payload->payload->ProfilerInfo->ProfilerInfo : ",profilerDepID)

        print("############################## KONG INFO ##############################\n")
        print("Total Numnder of Deployment ID found under data->payload->payload->KongInfo->KongInfo : ",kongDepID)

        #print(set(nadProfNameSet))
