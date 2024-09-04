import random
import requests
from PIL import Image
from io import BytesIO

# Danh sách các liên kết hình ảnh
image_links = [
    "https://raw.githubusercontent.com/KaosSoMotTheGioi/Image/main/cs.gif",
    "https://raw.githubusercontent.com/KaosSoMotTheGioi/random/main/image3.gif",
    "https://raw.githubusercontent.com/KaosSoMotTheGioi/random/main/image1.gif"
]

# Chọn ngẫu nhiên một liên kết hình ảnh
random_image_link = random.choice(image_links)

# Tải hình ảnh từ liên kết
response = requests.get(random_image_link)
img = Image.open(BytesIO(response.content))

# Hiển thị hình ảnh
img.show()
