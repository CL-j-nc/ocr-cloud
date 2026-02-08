import re

def extract_fields(texts):
    t = " ".join(texts)
    return {
        "plate_no": re.findall(r"[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼][A-Z][A-Z0-9]{5}", t),
        "vin": re.findall(r"[A-HJ-NPR-Z0-9]{17}", t),
        "company": re.findall(r"公司.{0,10}", t),
        "date": re.findall(r"\d{4}-\d{2}-\d{2}", t)
    }