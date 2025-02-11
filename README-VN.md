# Haust BOT
Faucet: [HAUST](https://faucet.haust.app/)

## Tính năng:

*Cho phép đa luồng để đúc NFTs nhanh hơn.
*Hỗ trợ nhiều Ví và Khóa riêng tư
*Tự động gửi giao dịch từ nhiều địa chỉ
*Theo dõi và cập nhật nonce cho từng khóa riêng để tránh xung đột khi gửi giao dịch.
*Bắt ngoại lệ khi giao dịch không thành công và xử lý lỗi liên quan đến nonce (ví dụ: nonce quá thấp).
*Cung cấp tùy chọn ngôn ngữ (tiếng Việt hoặc tiếng Anh) cho người dùng.
*Hiển thị thông báo trạng thái giao dịch (thành công hoặc thất bại) cùng với thông tin chi tiết.
*Tính toán và hiển thị thời gian hoàn thành của tất cả các giao dịch.
*Làm đẹp và dễ nhìn cho tất cả giao dịch, thông báo.... 

## Module:

- Python 3.7 trở lên
- `pip` (trình cài đặt gói Python)

## Cài đặt
1. **Sao chép kho lưu trữ này:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
git clone https://github.com/thog9/Haust-testnet.git
```
```sh
cd Haust-testnet
```
2. **Cài đặt Module:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
pip install -r requirements.txt
```
3. **Config:**
- Mở tệp `bot.py` và đảm bảo thay thế `private_key` bằng khóa riêng hợp lệ của bạn.:
```sh
   nano key.txt
```
4. **Chạy:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
python bot.py
```
