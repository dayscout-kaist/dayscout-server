# barcode_utils.py
import os
import time

from bs4 import BeautifulSoup
from PIL import Image
from pyzbar.pyzbar import decode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# def read_barcode(barcode_image_file):
#     try:
#         # 바코드 이미지 읽기
#         image = Image.open(barcode_image_file)

#         # 이미지에서 바코드 스캔
#         decoded_objects = decode(image)
#         if not decoded_objects:
#             return {"error": "Barcode not found"}

#         # 바코드 번호 얻기
#         barcode_number = decoded_objects[0].data.decode('utf-8')
#         return {"barcode_number": barcode_number}

#     except Exception as e:
#         return {"error": str(e)}


def search_barcode(barcode_number):
    try:
        # Selenium WebDriver 설정 (Chrome을 사용한다고 가정)
        driver = webdriver.Chrome()
        # TODO: WEBdriver 에 headless option 추가 필요

        # 웹사이트 열기
        driver.get("https://m.retaildb.or.kr/service/product_info")

        # 바코드 번호 입력
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "barcode"))
        )
        input_element.send_keys(barcode_number)

        # 검색 버튼 클릭
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnSearch"))
        )
        search_button.click()

        def check_product_nm_change(driver):
            product_nm = driver.find_element(By.ID, "productNm").text
            return product_nm != "신라면600g"

        WebDriverWait(driver, 10).until(check_product_nm_change)

        # 결과 페이지의 HTML 가져오기
        page_source = driver.page_source

        # BeautifulSoup을 이용해 스크레핑
        soup = BeautifulSoup(page_source, "html.parser")

        # 각 정보 추출
        product_title = soup.find(id="productNm").get_text(strip=True)
        product_img = soup.find(id="productImg").find("img")["src"]
        product_type = soup.find(id="clsTotalNm").get_text(strip=True)
        product_name = soup.find(id="productNmKr").get_text(strip=True)
        company_info = soup.find(id="companies").get_text(strip=True)
        brand = soup.find(id="brands").get_text(strip=True)
        net_weight = soup.find(id="originVolume").get_text(strip=True)

        # WebDriver 종료
        driver.quit()

        # 결과를 json 형태로 반환
        result = {
            "barcode_number": barcode_number,
            "product_title": product_title,
            "product_img": product_img,
            "product_type": product_type,
            "product_name": product_name,
            "company_info": company_info,
            "brand": brand,
            "net_weight": net_weight,
        }
        return result

    except Exception as e:
        return {"error": str(e)}


# 메인 함수
if __name__ == "__main__":
    # 이미지 파일 경로를 같은 폴더의 test.png로 설정
    # current_dir = os.path.dirname(os.path.realpath(__file__))
    # image_file_path = os.path.join(current_dir, 'test.png')

    # barcode_result = read_barcode(image_file_path)
    # if "error" in barcode_result:
    #     print("Error reading barcode:", barcode_result["error"])
    # else:
    #     barcode_number = barcode_result["barcode_number"]
    #     search_result = search_barcode(barcode_number)
    #     print("Result:")
    #     print(search_result)
    barcode_number = 8801062417117
    search_result = search_barcode(barcode_number)
    print("Result:")
    print(search_result)
