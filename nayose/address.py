import re

states = [
    "三重県", "大阪府", "高知県", "徳島県",
    "岩手県", "千葉県", "愛媛県", "山梨県", "栃木県", "宮城県", "北海道", "青森県", "福岡県", "石川県", "島根県", "広島県", "岡山県", "東京都", "和歌山県", "群馬県",
    "神奈川県", "茨城県", "岐阜県", "富山県", "秋田県", "福井県", "兵庫県", "滋賀県", "沖縄県", "山口県", "奈良県", "静岡県", "京都府", "鳥取県", "宮崎県", "大分県",
    "鹿児島県", "熊本県", "佐賀県", "福島県", "長崎県", "埼玉県", "新潟県", "愛知県", "香川県", "長野県", "山形県",
]

cities = [
    "大館市", "熊本市南区", "三戸郡", "下新川郡", "薩摩川内市", "根室市", "堺市北区", "大沼郡", "相馬市", "北名古屋市", "由利本荘市", "茂原市", "北斗市", "度会郡", "安城市",
    "阿賀野市", "神崎郡", "大阪市住吉区", "大田市", "室蘭市", "北牟婁郡", "尾鷲市", "仙台市太白区", "宮城郡", "千葉市花見川区", "糟屋郡", "日野市", "東村山郡", "鹿足郡",
    "成田市", "姶良郡", "平塚市", "呉市", "境港市", "行橋市", "江田島市", "築上郡", "宇土市", "合志市", "相馬郡", "真庭郡", "富士見市", "名古屋市昭和区", "霧島市", "草津市",
    "みよし市", "我孫子市", "村上市", "飯田市", "横浜市都筑区", "広島市安芸区", "鳥栖市", "下益城郡", "大町市", "雲仙市", "流山市", "名寄市", "川崎市幸区", "鎌倉市", "中頭郡",
    "高山市", "島原市", "幡多郡", "新宿区", "本庄市", "堺市堺区", "朝霞市", "美濃加茂市", "山県郡", "鳥取市", "川上郡", "一宮市", "美祢市", "久遠郡", "福岡市東区", "大田区",
    "池田市", "飽海郡", "刈谷市", "大阪市生野区", "豊岡市", "長岡市", "河内長野市", "甲斐市", "南魚沼市", "天塩郡", "岡山市北区", "長門市", "土佐清水市", "名古屋市瑞穂区",
    "登米市", "安房郡", "木曽郡", "東茨城郡", "土浦市", "伊豆の国市", "ひたちなか市", "沼田市", "諏訪郡", "加茂市", "妙高市", "浦安市", "有田市", "常呂郡", "名取市",
    "羽村市", "相模原市緑区", "樺戸郡", "肝属郡", "いわき市", "中川郡", "五泉市", "杵築市", "入間市", "宮古郡", "川越市", "長井市", "善通寺市", "大阪市此花区", "鹿角市",
    "久慈郡", "いちき串木野市", "大田原市", "米原市", "亀田郡", "みやま市", "新庄市", "佐伯市", "那珂川市", "伊万里市", "武蔵村山市", "豊能郡", "福岡市博多区", "那賀郡",
    "藤枝市", "三浦郡", "吉川市", "泉佐野市", "倉敷市", "爾志郡", "旭市", "常総市", "尼崎市", "八幡市", "鹿児島郡", "中野市", "大阪市東住吉区", "習志野市", "京都市右京区",
    "西白河郡", "小美玉市", "加美郡", "さいたま市岩槻区", "上天草市", "吉野郡", "玖珠郡", "京都市南区", "名古屋市名東区", "白老郡", "関市", "大府市", "亀山市", "名古屋市緑区",
    "美唄市", "前橋市", "新居浜市", "羽咋郡", "かすみがうら市", "長生郡", "鹿屋市", "西八代郡", "下伊那郡", "富岡市", "白井市", "鶴岡市", "宮古市", "神埼市", "松戸市",
    "塩竈市", "多可郡", "芦屋市", "青梅市", "藤井寺市", "知多郡", "田川郡", "阿南市", "広尾郡", "野付郡", "児玉郡", "小田郡", "津山市", "東広島市", "相模原市中央区",
    "むつ市", "鶴ヶ島市", "横浜市金沢区", "御蔵島村", "瑞穂市", "東大阪市", "旭川市", "京都市西京区", "長岡京市", "熊本市西区", "松前郡", "浜松市天竜区", "益田市", "恵庭市",
    "南相馬市", "福岡市中央区", "鹿児島市", "飯石郡", "富里市", "知多市", "大阪市都島区", "立川市", "綴喜郡", "加賀市", "南宇和郡", "岩船郡", "明石市", "可児郡", "岐阜市",
    "大船渡市", "越智郡", "大野郡", "三郷市", "和歌山市", "美作市", "大島郡", "三条市", "高市郡", "伊達市", "伊賀市", "豊中市", "大阪市淀川区", "山口市", "城陽市",
    "宮古島市", "飯塚市", "志木市", "熊谷市", "世羅郡", "高座郡", "釧路市", "大阪市阿倍野区", "小浜市", "会津若松市", "阿波市", "足立区", "大阪市中央区", "高萩市", "泉北郡",
    "堺市中区", "生駒市", "大洲市", "上越市", "多摩市", "土佐市", "小野市", "串間市", "墨田区", "磯城郡", "日野郡", "尾花沢市", "塩尻市", "神津島村", "札幌市清田区",
    "荒尾市", "市原市", "えびの市", "岡山市中区", "大阪市福島区", "刈田郡", "鳴門市", "愛西市", "入間郡", "甘楽郡", "坂東市", "小県郡", "姫路市", "大網白里市", "長岡郡",
    "南松浦郡", "芦別市", "曽於市", "日向市", "さいたま市緑区", "苫小牧市", "十勝郡", "広島市南区", "平戸市", "京都市中京区", "西春日井郡", "堺市南区", "津島市", "猿島郡",
    "北本市", "富良野市", "松本市", "加古川市", "春日部市", "倉吉市", "豊島区", "北安曇郡", "那須烏山市", "横浜市栄区", "嘉穂郡", "八女郡", "士別市", "郡上市", "奥州市",
    "那珂郡", "勝田郡", "東置賜郡", "結城市", "結城郡", "南あわじ市", "横浜市中区", "高松市", "葛飾区", "羽島郡", "武雄市", "逗子市", "勝浦郡", "仙北郡", "中津軽郡",
    "大川市", "沖縄市", "古河市", "名古屋市北区", "豊後大野市", "日立市", "文京区", "四国中央市", "加茂郡", "大阪市鶴見区", "香取郡", "さいたま市桜区", "宮若市", "千葉市緑区",
    "つくば市", "西伯郡", "大東市", "名古屋市天白区", "京都市下京区", "三好市", "香美市", "嘉麻市", "八潮市", "千曲市", "南陽市", "白石市", "大阪市旭区", "館林市", "松山市",
    "飛騨市", "一関市", "大津市", "佐賀市", "東松山市", "蓮田市", "舞鶴市", "水戸市", "沼津市", "阿久根市", "大阪市港区", "北九州市若松区", "鹿嶋市", "羽咋市", "赤磐市",
    "中間市", "座間市", "小松島市", "枝幸郡", "北都留郡", "湯沢市", "枚方市", "横浜市瀬谷区", "羽曳野市", "中魚沼郡", "綾部市", "能代市", "双葉郡", "西臼杵郡", "本吉郡",
    "富士宮市", "宇都宮市", "仙北市", "室戸市", "札幌市西区", "交野市", "柳川市", "指宿市", "南砺市", "三浦市", "東村山市", "広島市佐伯区", "能美市", "横浜市西区", "熊野市",
    "宇部市", "奥尻郡", "南埼玉郡", "足柄上郡", "賀茂郡", "橋本市", "福岡市早良区", "南河内郡", "隠岐郡", "夕張郡", "下都賀郡", "西都市", "神戸市東灘区", "丸亀市", "米沢市",
    "玉名郡", "足寄郡", "府中市", "多賀城市", "目黒区", "八街市", "神戸市長田区", "輪島市", "笠間市", "亘理郡", "御殿場市", "釧路郡", "札幌市中央区", "神戸市中央区", "藤岡市",
    "柏原市", "吉野川市", "児湯郡", "広島市中区", "三豊市", "京都郡", "常滑市", "愛甲郡", "柴田郡", "八代郡", "壱岐市", "亀岡市", "留萌市", "東諸県郡", "仙台市泉区",
    "那須塩原市", "江南市", "泉南郡", "川辺郡", "秋田市", "大阪市北区", "香南市", "鞍手郡", "福生市", "二本松市", "徳島市", "高知市", "滝川市", "江東区", "観音寺市",
    "摂津市", "島尻郡", "南都留郡", "様似郡", "大崎市", "歌志内市", "神栖市", "下妻市", "桑名市", "阪南市", "北松浦郡", "熊本市東区", "焼津市", "美濃市", "浜松市東区",
    "伊豆市", "新潟市秋葉区", "糸島市", "下呂市", "松江市", "二戸市", "岸和田市", "牛久市", "犬上郡", "御坊市", "川崎市多摩区", "臼杵市", "英田郡", "東かがわ市", "矢板市",
    "上水内郡", "吹田市", "大野市", "光市", "標津郡", "春日井市", "額田郡", "大阪市城東区", "周智郡", "東海市", "川崎市中原区", "南蒲原郡", "小田原市", "仙台市宮城野区",
    "浜松市西区", "岩出市", "西蒲原郡", "杉並区", "瀬戸内市", "別府市", "横浜市青葉区", "岩沼市", "西東京市", "常陸太田市", "橿原市", "紀の川市", "相模原市南区", "黒石市",
    "千葉市若葉区", "浅口市", "糸満市", "岩倉市", "相生市", "さいたま市南区", "鴨川市", "佐渡市", "青ヶ島村", "東松島市", "木津川市", "川崎市川崎区", "野田市", "古宇郡",
    "富士市", "赤穂郡上郡", "三好郡", "二海郡", "西宮市", "勝山市", "大牟田市", "野々市市", "南房総市", "札幌市北区", "西多摩郡", "深谷市", "川崎市宮前区", "狭山市", "東金市",
    "白糠郡", "利根郡", "弘前市", "駒ヶ根市", "匝瑳市", "福岡市西区", "札幌市手稲区", "行田市", "柳井市", "小城市", "富田林市", "釜石市", "横浜市港南区", "南足柄市", "板野郡",
    "新発田市", "潟上市", "高崎市", "南秋田郡", "土佐郡", "東田川郡", "和賀郡", "西村山郡", "川崎市高津区", "江津市", "北九州市門司区", "乙訓郡", "加須市", "虻田郡", "竹田市",
    "加東市", "防府市", "神埼郡", "二戸郡", "印西市", "大阪市平野区", "札幌市東区", "新宮市", "新潟市北区", "南丹市", "村山市", "高岡郡", "広島市安佐北区", "大和市", "安曇野市",
    "京都市左京区", "久米郡", "笠岡市", "三次市", "宗像市", "伊達郡", "田原市", "稲敷市", "玉名市", "西尾市", "桐生市", "貝塚市", "清須市", "中野区", "大阪市西淀川区",
    "浜松市浜北区", "あわら市", "陸前高田市", "秩父市", "守山市", "太宰府市", "西之表市", "龍ケ崎市", "八女市", "東根市", "夕張市", "下田市", "上浮穴郡", "にかほ市", "鎌ケ谷市",
    "寝屋川市", "吾妻郡", "山県市", "江別市", "島牧郡", "和気郡", "いなべ市", "彦根市", "横浜市緑区", "糸魚川市", "飯能市", "上尾市", "笛吹市", "大垣市", "寿都郡", "市川市",
    "福知山市", "都城市", "佐世保市", "河北郡", "三重郡", "下野市", "恵那市", "真庭市", "小郡市", "南九州市", "名古屋市港区", "大阪市東淀川区", "筑紫野市", "国立市", "熱海市",
    "雲南市", "横須賀市", "京都市東山区", "名古屋市熱田区", "丹波市", "海津市", "最上郡", "新潟市西区", "志摩市", "福井市", "山辺郡", "品川区", "斜里郡", "世田谷区", "久留米市",
    "向日市", "河沼郡", "北設楽郡", "茨木市", "門真市", "三原市", "佐波郡", "花巻市", "角田市", "北秋田郡", "神戸市北区", "松浦市", "延岡市", "勇払郡", "京都市北区",
    "浅口郡", "廿日市市", "青森市", "大阪市浪速区", "鴻巣市", "足利市", "大仙市", "上川郡", "香取市", "松阪市", "東牟婁郡", "香川郡", "横浜市鶴見区", "南佐久郡", "登別市",
    "水俣市", "日南市", "高梁市", "遠賀郡", "宮崎市", "大阪市天王寺区", "富山市", "菊池市", "横浜市磯子区", "守口市", "苫田郡", "総社市", "岩瀬郡", "岡山市南区", "八千代市",
    "出水郡", "神戸市兵庫区", "さぬき市", "東大和市", "男鹿市", "小樽市", "印旛郡", "宇治市", "宍粟市", "南城市", "周南市", "袋井市", "唐津市", "下水内郡", "西諸県郡",
    "大分市", "福岡市城南区", "磯谷郡", "浦添市", "大里郡", "南さつま市", "奄美市", "八王子市", "川崎市麻生区", "奈良市", "佐久市", "富谷市", "山越郡", "三宅島三宅村",
    "札幌市南区", "神戸市灘区", "京丹後市", "横浜市泉区", "喜多方市", "狛江市", "石狩市", "名古屋市中川区", "泉南市", "岡谷市", "遠田郡", "掛川市", "勝浦市", "積丹郡", "伊予郡",
    "銚子市", "都留市", "仁多郡", "三田市", "北津軽郡", "気仙郡", "伊佐市", "檜山郡", "豊前市", "四街道市", "桶川市", "砺波市", "名張市", "宇佐市", "甲府市", "宇陀郡",
    "千代田区", "坂井市", "海草郡", "東久留米市", "朝倉郡", "瑞浪市", "神戸市垂水区", "八尾市", "榛原郡", "横浜市戸塚区", "不破郡", "有珠郡", "愛知郡", "刈羽郡", "南津軽郡",
    "伊予市", "三沢市", "飯山市", "名古屋市千種区", "豊後高田市", "横浜市神奈川区", "君津市", "さいたま市大宮区", "宗谷郡", "清瀬市", "筑西市", "近江八幡市", "八丈島八丈町",
    "七尾市", "石岡市", "利島村", "板橋区", "西条市", "瀬棚郡", "広島市西区", "日光市", "八戸市", "真岡市", "たつの市", "大飯郡", "沙流郡", "栗原市", "南巨摩郡", "泉大津市",
    "羽島市", "磐田市", "長浜市", "野洲市", "新冠郡", "新潟市江南区", "伊丹市", "つくばみらい市", "津久見市", "鈴鹿市", "三方郡", "千葉市中央区", "大阪市西成区", "名古屋市中村区",
    "伊東市", "日高郡", "金沢市", "南会津郡", "四條畷市", "千歳市", "船井郡", "高岡市", "備前市", "横浜市保土ケ谷区", "中巨摩郡", "秦野市", "山梨市", "ふじみ野市", "庄原市",
    "石巻市", "伊具郡", "札幌市白石区", "菊川市", "北杜市", "広島市東区", "新城市", "大月市", "港区", "東松浦郡", "坂戸市", "宜野湾市", "横浜市港北区", "越谷市", "本巣郡",
    "筑後市", "安達郡", "須賀川市", "西置賜郡", "和光市", "名古屋市南区", "宇城市", "北九州市八幡東区", "宇和島市", "国分寺市", "球磨郡", "堺市美原区", "国頭郡", "荒川区",
    "八代市", "北佐久郡", "岩手郡", "安八郡", "赤平市", "遠野市", "堺市東区", "小千谷市", "行方市", "浜松市中区", "上北郡", "北九州市小倉南区", "鉾田市", "幸手市", "富津市",
    "木田郡", "白岡市", "浜田市", "垂水市", "紫波郡", "田村郡", "能美郡", "山陽小野田市", "伊都郡", "調布市", "大島町", "茅ヶ崎市", "新潟市南区", "河西郡", "太田市",
    "武蔵野市", "空知郡", "取手市", "気仙沼市", "京都市伏見区", "中津市", "尾道市", "洲本市", "利尻郡", "本宮市", "人吉市", "藤沢市", "柏崎市", "常陸大宮市", "安芸郡",
    "可児市", "薩摩郡", "うきは市", "井原市", "小豆郡", "箕面市", "都窪郡", "五島市", "加西市", "北葛飾郡", "袖ケ浦市", "伊勢崎市", "上山市", "豊見城市", "栗東市", "高島市",
    "砂川市", "静岡市清水区", "館山市", "越前市", "鯖江市", "福山市", "夷隅郡", "志布志市", "三潴郡", "郡山市", "下高井郡", "天理市", "長崎市", "下関市", "東国東郡", "燕市",
    "上田市", "三鷹市", "渋川市", "綾瀬市", "鹿島郡", "本巣市", "美馬郡", "八幡平市", "北相馬郡", "犬山市", "阿寒郡", "丹羽郡", "町田市", "酒田市", "滑川市", "網走郡",
    "みどり市", "知立市", "邑智郡", "丹生郡", "香芝市", "岡山市東区", "河東郡", "古賀市", "鳳珠郡", "浜松市南区", "八重山郡", "上磯郡", "土岐市", "川西市", "佐用郡",
    "敦賀市", "北見市", "諏訪市", "南牟婁郡", "葛城市", "豊川市", "木更津市", "半田市", "さいたま市浦和区", "上伊那郡", "上閉伊郡", "西予市", "古平郡", "名東郡", "五條市",
    "白山市", "久慈市", "茅部郡", "河内郡", "多治見市", "須崎市", "耶麻郡", "阿蘇市", "対馬市", "西海市", "多野郡", "熊本市中央区", "新見市", "石狩郡", "伊勢市", "御所市",
    "多久市", "新潟市中央区", "海老名市", "小林市", "淡路市", "由布市", "札幌市厚別区", "坂出市", "大阪市住之江区", "葦北郡", "豊田郡", "阿蘇郡", "蒲郡市", "つがる市", "鹿角郡",
    "員弁郡", "豊橋市", "小金井市", "さいたま市西区", "平川市", "氷見市", "北広島市", "神石郡", "福岡市南区", "各務原市", "東彼杵郡", "中央区", "上益城郡", "直方市", "養老郡",
    "足柄下郡", "湖南市", "幌泉郡", "さいたま市中央区", "柏市", "留萌郡", "中津川市", "新座市", "宝塚市", "宮津市", "多気郡", "秩父郡", "稚内市", "寒河江市", "東筑摩郡",
    "北上市", "須坂市", "米子市", "北宇和郡", "駿東郡", "桑名郡", "大村市", "相楽郡", "京都市上京区", "熊本市北区", "藤津郡", "紋別市", "八頭郡", "高石市", "塩谷郡",
    "上野原市", "かほく市", "北茨城市", "うるま市", "南国市", "稲城市", "小牧市", "四日市市", "天童市", "八幡浜市", "弥富市", "広島市安佐南区", "西牟婁郡", "渋谷区", "出雲市",
    "石川郡", "菊池郡", "京都市山科区", "玖珂郡", "山武郡", "東津軽郡", "新島村", "碧南市", "曽於郡", "静岡市駿河区", "紋別郡", "西彼杵郡", "芳賀郡", "帯広市", "甲賀市",
    "埴科郡", "苫前郡", "福島市", "新潟市西蒲区", "牡鹿郡", "速見郡", "射水市", "長野市", "上高井郡", "千葉市美浜区", "胎内市", "増毛郡", "豊明市", "玉野市", "大阪市東成区",
    "神戸市西区", "静岡市葵区", "東臼杵郡", "吾川郡", "津市", "大阪狭山市", "さくら市", "美馬市", "十和田市", "浜松市北区", "生駒郡", "守谷市", "あま市", "中央市", "揖斐郡",
    "三島市", "那珂市", "函館市", "長久手市", "厚岸郡", "那須郡", "竹原市", "裾野市", "盛岡市", "あきる野市", "黒部市", "戸田市", "稲沢市", "吉田郡", "岡崎市", "今立郡",
    "台東区", "田方郡", "練馬区", "与謝郡", "滝沢市", "下北郡", "いすみ市", "北葛城郡", "北蒲原郡", "大竹市", "三方上中郡", "山鹿市", "朝来市", "三養基郡", "天草市",
    "東近江市", "西脇市", "久喜市", "養父市", "富士吉田市", "名古屋市西区", "美方郡", "揖保郡", "宿毛市", "蕨市", "神戸市須磨区", "北群馬郡", "山武市", "白河市", "浦河郡",
    "有田郡", "小平市", "諫早市", "朝倉市", "伊那市", "阿武郡", "鹿沼市", "加古郡", "宇陀市", "杵島郡", "茅野市", "西磐井郡", "東御市", "鳥羽市", "邑楽郡", "名西郡",
    "丹波篠山市", "萩市", "牧之原市", "京田辺市", "胆沢郡", "中郡", "下松市", "韮崎市", "栃木市", "東蒲原郡", "羽生市", "西松浦郡", "昭島市", "綾歌郡", "尾張旭市",
    "岩見沢市", "姶良市", "桜川市", "目梨郡", "北区", "小山市", "小諸市", "南島原市", "東温市", "日高市", "福津市", "佐倉市", "熊毛郡", "北足立郡", "高砂市", "横浜市旭区",
    "潮来市", "三笠市", "四万十市", "仙台市若林区", "名護市", "安芸市", "東白川郡", "草加市", "川口市", "蒲生郡", "北諸県郡", "雨竜郡", "日田市", "出水市", "小笠原村",
    "三木市", "那覇市", "横浜市南区", "伊勢原市", "西津軽郡", "喜多郡", "大野城市", "春日市", "魚沼市", "天草郡", "日進市", "山本郡", "北九州市小倉北区", "瀬戸市", "田村市",
    "仙台市青葉区", "千葉市稲毛区", "安芸高田市", "下閉伊郡", "松原市", "高槻市", "南魚沼郡", "十日町市", "小矢部市", "佐野市", "甲州市", "南条郡", "岩内郡", "厚木市",
    "御前崎市", "三島郡", "魚津市", "九戸郡", "湖西市", "礼文郡", "南アルプス市", "東伯郡", "安中市", "国東市", "横手市", "五所川原市", "小松市", "日置市", "稲敷郡",
    "大阪市大正区", "深川市", "北秋田市", "大和高田市", "桜井市", "新潟市東区", "海南市", "岩国市", "赤穂市", "名古屋市中区", "名古屋市東区", "大和郡山市", "余市郡", "嬉野市",
    "江戸川区", "三井郡", "名古屋市守山区", "北村山郡", "大阪市西区", "雄勝郡", "石垣市", "高浜市", "枕崎市", "安来市", "海部郡", "堺市西区", "黒川郡", "網走市",
    "さいたま市北区", "見附市", "さいたま市見沼区", "船橋市", "珠洲市", "久世郡", "田川市", "加賀郡", "岩美郡", "所沢市", "中新川郡", "北九州市八幡西区", "西宇和郡", "鹿島市",
    "島田市", "今治市", "比企郡", "和泉市", "北九州市戸畑区", "田辺市", "豊田市", "山形市", "仲多度郡", "札幌市豊平区",
]

state_expression = '(' + '|'.join(states) + ')'
city_expression = '(' + '|'.join(cities) + ')'
state_regex = re.compile('^' + state_expression)
city_regex = re.compile('^' + city_expression)


def split_address(address):
    m = state_regex.match(address)
    if not m:
        return None, None, None
    state = m[1]
    m = city_regex.match(address[len(state):])
    if not m:
        return state, None, None
    city = m[1]
    return state, city, address[len(state) + len(city):]