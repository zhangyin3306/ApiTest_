import random
from datetime import datetime
from common.Base import my_log

import ddddocr



# 验证码识别
# def ocr(img_base64):
#     DdddOcr = ddddocr.DdddOcr(show_ad=False)
#     res = DdddOcr.classification(img=img_base64)
#     if len(res) < 4:
#         res = DdddOcr.classification(img=img_base64)
#     return res

log = my_log()

def ocr(img_base64, max_attempts=3):
    DdddOcr = ddddocr.DdddOcr(show_ad=False)
    attempts = 0

    while attempts < max_attempts:
        try:
            res = DdddOcr.classification(img=img_base64)
            if len(res) >= 4:
                return res
        except Exception as e:
            # Handle OCR-related exceptions (adjust as needed)
            log.error(f"OCR failed with error: {e}")

        attempts += 1

    log.warning(f"OCR did not produce enough results after {max_attempts} attempts.")

    return res


def randomCardNo():
    return random.randint(10000000, 99999999)


def now_date_string():
    # 获取当前日期和时间，并将其格式化为字符串
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d%H:%M:%S")  # 根据需要自定义格式
    return formatted_datetime
