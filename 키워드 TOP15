import requests
from bs4 import BeautifulSoup

raw = requests.get("https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

articles = html.select("ul.rankingnews_list > li")

news_titles = ""
# 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출
list_title = []
for ar in articles:
    try:
        title = ar.select_one("a.list_title").text
        list_title += title
    except Exception as e:
      continue



letters = ''.join(list_title)

letters2 = letters.replace('''“''','')
letters3 = letters2.replace('''”''','')
letters4 = letters3.replace('''‘''','')
letters5 = letters4.replace('''’''','')
letters6 = letters5.replace('''·''','')
letters7 = letters6.replace('''…''','')
letters8 = letters7.replace('''...''','')


letters0 = []
for i in letters8.split():
    letters0.append(i)


# 키워드에서 의미없는 말들 삭제
rem_letter = []
for word in letters0:
    rem_letter.append(word)
    if word =='후':
        rem_letter.remove('후')
    elif word =='전':
        rem_letter.remove('전')
    elif word =='더':
        rem_letter.remove('더')
    elif word =='만에':
        rem_letter.remove('만에')    
    elif word =='한':
        rem_letter.remove('한')
    elif word =='안':
        rem_letter.remove('안')
    elif word =='왜':
        rem_letter.remove('왜')
    elif word =='등':
        rem_letter.remove('등')
    elif word =='것':
        rem_letter.remove('것')
    elif word =='첫':
        rem_letter.remove('첫')
    elif word =='중':
        rem_letter.remove('중')
    elif word =='to':
        rem_letter.remove('to')
    elif word =='the':
        rem_letter.remove('the')
    elif word =='못':
        rem_letter.remove('못')
    elif word =='명':
        rem_letter.remove('명')
    elif word =='새':
        rem_letter.remove('새')
    elif word =='때':
        rem_letter.remove('때')
    elif word =='vs':
        rem_letter.remove('vs')
    elif word =='문':
        rem_letter.remove('문')
    elif word =='또':
        rem_letter.remove('또')
    elif word =='한때':
        rem_letter.remove('한때')
    elif word =='첫날':
        rem_letter.remove('첫날')
    elif word =='사이트':
        rem_letter.remove('사이트')    
    elif word =='역대':
        rem_letter.remove('역대')            
    elif word =='기준':
        rem_letter.remove('기준')            
    elif word =='신규':
        rem_letter.remove('신규')                    
    elif word =='월요일':
        rem_letter.remove('월요일')                    
    elif word =='화요일':
        rem_letter.remove('화요일')                    
    elif word =='수요일':
        rem_letter.remove('수요일')                    
    elif word =='목요일':
        rem_letter.remove('목요일')                    
    elif word =='금요일':
        rem_letter.remove('금요일')                    
    elif word =='토요일':
        rem_letter.remove('토요일')                     
    elif word =='일요일':
        rem_letter.remove('일요일')                   
    elif word =='수':
        rem_letter.remove('수')                    
    elif word =='연속':
        rem_letter.remove('연속')                     
    elif word =='in':
        rem_letter.remove('in')                             
    elif word =='확진':
        rem_letter.remove('확진')                             
    elif word =='예약':
        rem_letter.remove('예약')                             
    elif word =='지지율':
        rem_letter.remove('지지율')                     
    elif word =='신청':
        rem_letter.remove('신청')                          
    elif word =='모두':
        rem_letter.remove('모두')                  
    elif word =='역대급':
        rem_letter.remove('역대급')


#키워드 카운팅

word_counts = {}
for word in rem_letter:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1


word_list = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)


result = word_list[:15] # top 15를 보여달라

#키워드 순위별로 번호 매겨서 출력
def news_top20():
    number = 1
    for i in result:
        print(number,'_', i)
        number +=1
news_top20()
