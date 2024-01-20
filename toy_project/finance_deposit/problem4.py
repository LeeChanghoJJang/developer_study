import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = ""
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params ={
         'auth' : api_key,
        'topFinGrpNo' : '020000',
        'pageNo' :1,
    }
  
    deposit_data = requests.get(url,params=params).json()
    baseList = deposit_data['result']['baseList'] # baseList 긴 문장을 간단하게 저장
    optionList=deposit_data['result']['optionList'] # optionList 긴 문장을 간단하게 저장
    result=[] # 최종 상품들 모아놓은 결과
    product_unit=[] # 
    for i in baseList: #baseList를 순회하면서 한 상품에 저장될 정보의 templete 생성 
        product_unit = {'금리정보':'',
              '금융상품명': i['fin_prdt_nm'],
              '금융회사명': i['kor_co_nm']
                }
        temp_list=[]
        for k in optionList: #baseList를 한번 순회할 때 모든 optionList의 금융상품코드를 비교하기 위해 반복문 
            if i['fin_prdt_cd'] == k['fin_prdt_cd']: #baseList와 optionList의 상품코드를 각각 비교 
                new_dict={'저축 금리':k['intr_rate'],
              '저축 기간':k['save_trm'],
              '저축금리유형':k['intr_rate_type'],
              '저축금리유형명':k['intr_rate_type_nm'],
              '최고 우대금리':k['intr_rate2']}
                temp_list.append(new_dict) # baseList의 한 상품코드과 일치하는 상품코드를 optionList에서 모두 찾아 임시 리스트에 저장 
        product_unit['금리정보']=temp_list # 위에서 만들었던 templete에 따라 금리정보에 위에서 임시저장했던 정보 저장
        result.append(product_unit) # 한 상품단위가 모두 완성되었으므로, 최종결과 리스트에 저장
    return result #모든 baseList를 다 돈뒤, 최종 결과를 result에 저장 

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)