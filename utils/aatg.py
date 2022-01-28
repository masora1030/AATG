import random
import MeCab
import unidic_lite
import pykakasi
from alphabet2kana import a2k
import warnings
warnings.simplefilter('ignore')

class AATG():

  def __init__(self):
    kakasi = pykakasi.kakasi() 
    kakasi.setMode('H', 'a') 
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')

    self.vowel2Ingo = {'an':["マン"],'anii': ['3P'], 'eeuiouu': ['AV女優'], 'iiuoto': ['Gスポット'], 'eoae': ['NTR', '寝取られ'], 'etuu': ['SEX', 'せっくす', 'セックス'], 'eueu': ['SM'], 'euooii': ['SOD'], 'iiatu': ['Tバック'], 'iaaii': ['いやらしい'], 'eti': ['えっち', 'エッチ'], 'oinin': ['おちんちん'], 'otai': ['おっπ', 'おっぱい'], 'oaii': ['おなにー', 'オナニー'], 'oeoa': ['おねショタ'], 'ooo': ['おぼこ'], 'oano': ['おまんこ'], 'oeo': ['おめこ'], 'oouiea': ['お掃除フェラ'], 'inaa': ['きんたま', 'キンタマ', '金玉'], 'aaauuoi': ['さかさ椋鳥'], 'ioiuou': ['しぼり芙蓉'], 'uee': ['すけべ', 'スケベ'], 'eieione': ['せきれい本手'], 'aiuioouo': ['だいしゅきホールド'], 'ino': ['ちんこ', 'ちんぽ', 'インポ', 'チンコ', 'チンポ', '淫語'], 'inin': ['ちんちん', 'チンチン', '陰唇', 'ﾁﾝﾁﾝ'], 'ioieti': ['ひとりえっち', '一人Ｈ'], 'uaai': ['ふたなり'], 'anuiaei': ['まんぐり返し'], 'ano': ['まんこ', 'マンコ'], 'anan': ['まんまん'], 'uaua': ['むらむら', 'ムラムラ'], 'aue': ['アクメ'], 'aean': ['アゲマン', 'サゲマン'], 'aauoieo': ['アダルトビデオ'], 'aaii': ['アナニー'], 'aau': ['アナル'], 'aauetuu': ['アナルセックス', 'アナルＳＥＸ'], 'aauiiu': ['アナルビーズ'], 'aauuau': ['アナルプラグ'], 'aauauou': ['アナル拡張'], 'aauaiau': ['アナル開発'], 'aeao': ['アヘ顔'], 'iu': ['イク'], 'iiou': ['イチモツ'], 'iaiaetuu': ['イチャイチャセックス'], 'iaauetuu': ['イチャラブセックス'], 'ieua': ['イメクラ'], 'ieeiieo': ['イメージビデオ'], 'iaaio': ['イラマチオ'], 'inoenu': ['インポテンツ'], 'euuaii': ['エクスタシー'], 'io': ['痴女'], 'eoi': ['エロい', '寝取り', '手コキ'], 'eoouin': ['エロ同人'], 'eoouini': ['エロ同人誌'], 'eoon': ['エロ本'], 'oae': ['オナペ'], 'oaeto': ['オナペット'], 'oao': ['オナホ'], 'oaoou': ['オナホール'], 'ooauu': ['オーガズム'], 'auaa': ['カウパー'], 'anonouei': ['カントン包茎'], 'auoou': ['ギャグボール', 'ラブドール'], 'uuo': ['クスコ', '熟女'], 'uoai': ['クソガキ'], 'uioiu': ['クリトリス'], 'uniinuu': ['クンニリングス'], 'uni': ['クンニ'], 'euano': ['ケツマンコ'], 'onoou': ['コンドーム'], 'aaen': ['ザーメン'], 'ituuain': ['シックスナイン'], 'oaoe': ['ショタおね'], 'uaoo': ['スカトロ'], 'ueeiu': ['スケベ椅子'], 'ueua': ['スペルマ'], 'uatinu': ['スワッピング'], 'eue': ['セフレ'], 'enui': ['センズリ'], 'ouooneano': ['ソフト・オン・デマンド'], 'oouano': ['ソープランド'], 'oouou': ['ソープ嬢'], 'atiaiu': ['ダッチワイフ'], 'auuiiu': ['ダブルピース'], 'iuo': ['ディルド'], 'iiuuooo': ['ディープスロート'], 'eain': ['デカチン'], 'eiaiieuu': ['デリバリーヘルス'], 'eieu': ['デリヘル'], 'ooao': ['トロ顔'], 'ana': ['ナンパ', '顔射'], 'ooan': ['ノーパン'], 'aeoi': ['ハメ撮り'], 'aaeu': ['ハーレム'], 'aiaua': ['バイアグラ'], 'auuuea': ['バキュームフェラ'], 'aiui': ['パイズリ'], 'aian': ['パイパン', 'ヤリマン'], 'aaau': ['パパ活'], 'ania': ['パンチラ'], 'iti': ['ビッチ'], 'iuoatu': ['フィストファック'], 'ea': ['フェラ'], 'eaio': ['フェラチオ'], 'eaui': ['フェラ抜き'], 'uuea': ['ブルセラ'], 'etinu': ['ペッティング'], 'eian': ['ペニバン', '性感'], 'oeu': ['ホ別'], 'oeaa': ['ボテ腹'], 'ooin': ['ポコチン'], 'ouio': ['ポルチオ'], 'auaaeeon': ['マスターベーション'], 'aiin': ['ヤリチン', '催眠', '愛人'], 'auo': ['ラブホ'], 'auoeu': ['ラブホテル'], 'iue': ['リフレ'], 'eiu': ['レイプ'], 'oion': ['ロリコン'], 'aaai': ['中出し', '朝勃ち', '朝起ち'], 'ouai': ['乙π','おっぱい'], 'iaeoan': ['乱れ牡丹'], 'anou': ['乱交', '男娼'], 'iua': ['乳房'], 'iui': ['乳首'], 'itouiai': ['亀甲縛り'], 'iou': ['亀頭', '遅漏'], 'iaa': ['二穴'], 'iaaoui': ['二穴同時'], 'aeiouei': ['仮性包茎'], 'aii': ['体位'], 'oinauei': ['個人撮影'], 'auoaae': ['兜合わせ'], 'iiueone': ['入船本手'], 'enou': ['円光', '援交'], 'oo': ['処女'], 'ouei': ['包茎', '童貞'], 'ouaiaei': ['口内射精'], 'ouaiata': ['口内発射'], 'aauaiauu': ['唐草居茶臼'], 'aeioe': ['喘ぎ声'], 'iuuate': ['四十八手'], 'uooooi': ['太ももコキ'], 'ieaie': ['姫始め'], 'oiau': ['媚薬'], 'aaae': ['孕ませ', '玉舐め', '生ハメ'], 'oouione': ['寿本手'], 'aei': ['射精'], 'ian': ['屍姦'], 'ouu': ['巨乳'], 'oii': ['巨尻'], 'oon': ['巨根'], 'oaeauu': ['帆かけ茶臼'], 'ai': ['座位'], 'ouan': ['強姦', '睾丸'], 'ouaii': ['後背位'], 'iuu': ['微乳'], 'ioiiauu': ['忍び居茶臼'], 'aiauoi': ['快楽堕ち'], 'eiou': ['性交', '性欲'], 'eioi': ['性処理'], 'eioei': ['性奴隷'], 'eianataai': ['性感マッサージ'], 'eianai': ['性感帯'], 'eioui': ['性行為', '正常位'], 'aiu': ['愛撫'], 'aiei': ['愛液'], 'eiinue': ['成人向け'], 'aaniu': ['我慢汁'], 'ean': ['手マン'], 'uin': ['手淫'], 'aiiou': ['抱き地蔵'], 'aeaone': ['揚羽本手'], 'enoouai': ['援助交際'], 'ouou': ['放尿', '早漏', '陵辱'], 'ouiuei': ['放置プレイ'], 'iueauu': ['時雨茶臼'], 'uiiauu': ['月見茶臼'], 'auauui': ['松葉崩し'], 'aaoiauu': ['機織茶臼'], 'iuanuu': ['汁男優'], 'aieu': ['泡姫'], 'oaiione': ['洞入り本手'], 'inan': ['淫乱', '輪姦'], 'inou': ['淫行', '陰嚢', '陰毛', '飲尿'], 'ini': ['淫靡'], 'auuu': ['爆乳'], 'uuan': ['獣姦'], 'auou': ['発情'], 'ineiouei': ['真性包茎'], 'uian': ['睡姦'], 'aeue': ['種付け'], 'aeueueu': ['種付けプレス'], 'aaouai': ['穴兄弟'], 'aino': ['立ちんぼ'], 'aaueone': ['笠舟本手'], 'ueooi': ['筆おろし'], 'iaaone': ['筏本手'], 'oin': ['粗チン'], 'uaa': ['素股', '素股'], 'euin': ['絶倫'], 'aioone': ['網代本手'], 'inau': ['緊縛', '陰核'], 'iueni': ['肉便器'], 'ueia': ['胸チラ'], 'aioi': ['脇コキ', '足コキ'], 'ii': ['自慰'], 'iuon': ['菊門'], 'aiooaai': ['蟻の戸渡り'], 'uaui': ['裏筋'], 'uaae': ['貝合わせ'], 'inuu': ['貧乳'], 'ininouan': ['近親相姦'], 'auaau': ['逆アナル'], 'aueiu': ['逆レイプ'], 'inei': ['陰茎'], 'inu': ['陰部'], 'aiaui': ['雁が首'], 'ena': ['電マ'], 'aoan': ['青姦'], 'ouun': ['食糞'], 'uiiieno': ['首引き恋慕'], 'ioui': ['騎乗位'], 'uuiuoaiaai': ['鶯の谷渡り'], 'ouonui': ['黄金水'], 'uoau': ['黒ギャル'], 'eueuuei': ['ＳＭプレイ'], 'eo': ['エロ']}
    self.conversion = kakasi.getConverter()
    self.mecab = MeCab.Tagger()
    self.suuzi = [str(i) for i in range(0,10)]
    self.vowels = ["a","i","u","e","o"]
    self.new_vowels = ["a","i","u","e","o","t","n"]


  def mecab_parse(self,user_input):
    #形態素解析
    p = self.mecab.parse(user_input)
    #print(p)
    parse_results = []
    p = p.replace('\t',',')
    plist = p.split('\n')
    for pl in plist:
        nodes = pl.split(',')
        if nodes[0] != "EOS" and nodes[0] != "":
          if nodes[0]!='記号':
            parse_result = {
                'surface':nodes[0],
                'base':nodes[1],
                'pos':nodes[4].split("-")[0],
                'trans':False
            }
            parse_results.append(parse_result)
    return parse_results 


  def convert_vowels(self,word):    
    if word[0] in self.suuzi:
      return word

    word = a2k(word)
    roman = list(self.conversion.do(word))
    #print(roman)
    result = []
    index = 0
    while index < len(roman):
      w = roman[index]

      #母音の処理
      if w in self.vowels:
        result.append(w)
        index += 1

      #nの処理
      elif w == "n":
        if index == 0:#文頭
          if roman[index+1] not in self.vowels and roman[index + 1] != "y":#次の文字が母音じゃない場合
            result.append(w)
        elif index == len(roman)-1:#文末
            result.append(w)
        else:#文中
          if (roman[index-1] in self.vowels) and roman[index+1] not in self.vowels and roman[index + 1] != "y":
            result.append(w)
        index += 1

      #chの処理(これがないとしたのif文で処理されて促音便として認識されてしまう)
      elif w == "c" and roman[index+1] == "h":
          index += 1

      #hの処理(これがないとしたのif文で処理されて促音便として認識されてしまう)
      elif w == "s" and roman[index+1] == "h":
          index += 1

      #促音の処理
      elif w not in self.vowels:
        index2 = index + 1#次の文字から見る
        count = 0
        while index2 < len(roman):#何個子音が連続する確認
          if roman[index2] in self.vowels:
            index = index2
            if count > 0:
              result.append("t")#二つ以上重なっている and 2文字目がyじゃなかった時
            break
          else:
            if roman[index2] == "y" and count == 0:
              index = index2
              break
            count += 1
            index2 += 1
    
    return "".join(result)


  def set_trans_prpbably(self,wordWithvowel,prob : float = 0.5):
    for word in wordWithvowel:
      if random.random() <= prob:
        word["trans"] = True
    return wordWithvowel


  def make_input_vowels(self,parse_results):
    wordWithvowel= []
    #ローマ字変換
    for word in parse_results:
      if word["pos"] == "名詞" and word["base"][0] not in self.suuzi:
        result = {}
        result["word"] = word["base"]
        result["vowel"] = self.convert_vowels(word["base"])
        result["surface"] = word["surface"]
        result["trans"] = word["trans"]
        wordWithvowel.append(result)
   
    #母音のmask
    for converted in wordWithvowel:
      vowel = converted["vowel"]
      regulars = []
      for i in range(len(vowel)):
        if len(vowel) <= 2:#1,2個の時は完全一致
          converted["vowels"] = [vowel]
        else:
          tmp = list(vowel)
          for v in self.new_vowels:
            tmp[i:i+1] = v
            regulars.append("".join(tmp))
          converted["vowels"] = regulars
    return wordWithvowel


  def nGram(self,target, n):
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]


  def serch_ero_word(self,word,candidates):
    this_vowels = word["vowels"]
    candidates[word["word"]] = []

    #完全一致があるかどうか
    for ero_key in self.vowel2Ingo:  
      if word["vowel"] == ero_key:
        for ero in self.vowel2Ingo[ero_key]:
          candidates[word["word"]].append(ero)
        break

    #完全一致がなかった時
    if len(candidates[word["word"]]) == 0:
      for vowel in this_vowels:
        for ero_key in self.vowel2Ingo:
          if vowel in ero_key:
            for i in self.vowel2Ingo[ero_key]:
              if len(vowel) == len(ero_key):
                for ero in self.vowel2Ingo[ero_key]:
                  candidates[word["word"]].append(ero)

    #ここまででない雑魚
    if len(candidates[word["word"]]) == 0:
      for vowel in this_vowels:
        for ero_key in self.vowel2Ingo:
          if vowel in ero_key:
            for i in self.vowel2Ingo[ero_key]:
              if len(vowel) + 1 == len(ero_key):
                for ero in self.vowel2Ingo[ero_key]:
                  candidates[word["word"]].append(ero)

    return candidates


  def make_candidates(self,wordWithvowel,ngram_num: int = 3):
    candidates = {}
    for word in wordWithvowel:#一つの単語に対して
      if word["trans"] == True:#確率で変換する単語の時
        candidates = self.serch_ero_word(word,candidates)
        #n-gram処理
        if len(candidates[word["word"]]) == 0:
          n_grams = self.nGram(word["word"], ngram_num)
          for n_gram in n_grams:
            ng_vowel = self.convert_vowels(n_gram)
            candidates = self.serch_ero_word({"word":n_gram,"vowel":ng_vowel,"vowels":[ng_vowel]},candidates)
            if len(candidates[n_gram]) != 0:
              random_choice = random.choice(candidates[n_gram])
              tmp = word["word"]
              tmp = tmp.replace(n_gram,random_choice,1)
              candidates[word["word"]].append(tmp)
            del candidates[n_gram]

        if len(candidates[word["word"]]) == 0:
          candidates[word["word"]].append(word["surface"])
        
        candidates[word["word"]] = list(set(candidates[word["word"]]))

      else:#確率で変換しない単語の時
        candidates[word["word"]] = [word["surface"]]

    return candidates

  def converted_output(self,parse_results,candidates):
    output = ""
    for word in parse_results:
      if word["pos"] == "名詞" and word["base"][0] not in self.suuzi:
        output += random.choice(candidates[word["base"]])
      else:
        output += word["surface"]
    return output

  def generate_title(self,user_input,ngram_numint = 3,prob : float = 0.5):

    parse_results = self.mecab_parse(user_input)
    wordWithvowel = self.make_input_vowels(parse_results)
    wordWithvowel = self.set_trans_prpbably(wordWithvowel,prob)
    candidates = self.make_candidates(wordWithvowel)
    output = self.converted_output(parse_results,candidates)

    return output