# Sử dụng hình ảnh gốc của Python
FROM python:3.9.2

# Đặt thư mục làm việc là /app
WORKDIR /app

# Sao chép tệp tin cấu hình và yêu cầu vào thư mục /app
COPY requirements.txt .

# Cài đặt các thư viện từ tệp tin yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào thư mục /app
COPY . .

#If you deploy the chatbot you expose at port 5005.
EXPOSE 5005 

# Huấn luyện chatbot
RUN rasa train --force --out trained-models

# Chạy chatbot
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]
