# dictionary : key값을 통해 value를 검색하는 자료형
# list나 tuple 같은 자료형과 다르게 key값을 통해 value를 얻는다
# dic = {key1 = value1, key2 = value2, key3 = value3, ...} 이와 같이 선언
# dic = {'name' = 'dowoon' , 'phone' = '01012341234'}, 'birth'='970107'}

# 1. dictionary pair(key, value) 추가 및 삭제
print("(1) add or delete (key, value) pair")
# 요소 추가는 dic의 index값이 key로, 초기화한 값이 value로 적용된다.
dic = {1: 'a'}
print("dic = {}".format(dic))
dic[2] = 'b' 
print("dic = {}".format(dic))
dic['name'] = 'dondon'
print("dic = {}".format(dic))
dic['list'] = [1,2,3]
print("dic = {}".format(dic))
# 요소 삭제는 list나 문자열 같이 del 객체를 사용하면 된다.
del dic['list'] 
print("dic = {}".format(dic))

# 2. dictionary의 값 읽어오기
print("dic['name'] = {}".format(dic['name']))
print("dic[1]      = {}".format(dic[1]))
# dictionary의 key값으로는 숫자, 문자, 문자열 모두 가능하지만
# list는 사용할 수 없으며, tuple은 key로 사용할 수 있다.
# value 값으로는 어떤 값이던지 넣을 수 있다.
dic[(1,2)] = 'tuple (1,2)'
print("dic[(1,2)]  = {}".format(dic[(1,2)]))

# 3. dictionary 관련 함수
dic = {'name': 'don', 'age': '22', 'phone': '01012341234'}
print("keys       = {}".format(dic.keys())) # 이와같이 key값들을 알아낼 경우 dict_keys 객체를 리턴
print("key list   = {}".format(list(dic.keys()))) # dict_keys 객체들을 list로 변환해서 출력
print("values     = {}".format(dic.values())) # 마찬가지로 dict_values 객체를 리턴
print("values list= {}".format(list(dic.values()))) # dict_values 객체들을 list로 변환해서 출력
print("pairs      = {}".format(dic.items()))
print("pairs list = {}".format(list(dic.items())))
print("value of name = {}".format(dic.get('name'))) # dic.get('name')과 dic['name']은 같은 결과값 리턴
print("value of age  = {}".format(dic.get('age'))) # 위와 동일
print("value of phone= {}".format(dic.get('phone'))) # 위와 동일
# get으로 value를 얻는 것과 dic[key]를 통해 value를 얻는 방식은 key가 존재할 경우 둘다 value를 리턴
# 단 없는 키에 대한 value를 리턴할 시, get의 경우 none리턴(오류 아님), dic[key]의 경우 오류 발생
print("value of foo  = {}".format(dic.get('foo',"if key doesn't exit, return bar.... else return correct value"))) 
# get함수를 이용해 없는 key의 경우 두번째 인자로 설정한 값을 리턴하게 할 수도 있다.
# name의 경우 존재하는 key이므로 bar가 아닌 name key의 value인 don을 출력하게 된다
# foo의 경우 존재하지 않는 key이므로 뒤에 설정한 문장이 출력된다.
print("Is there key 'name'? {}".format('name' in dic))
print("Is there key 'foo'? {}".format('foo' in dic))
# 이와 같이 in 함수를 이용해 해당 key가 dictionary에 있는지 확인할 수 있다.

dic.clear() # dic에 정의해 둔 key, value 쌍을 모두 제거
print("clear dic  = {}".format(dic))
