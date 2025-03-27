# Haust Testnet Scripts

Kho lưu trữ này chứa một bộ sưu tập các tập lệnh Python được thiết kế để tương tác với Haust Testnet, một mạng lưới thử nghiệm blockchain. Các tập lệnh này cho phép người dùng triển khai mã thông báo ERC20, đúc NFT, gửi mã thông báo và thực hiện giao dịch bằng Haust Testnet RPC. Mỗi tập lệnh được xây dựng bằng thư viện web3.py và cung cấp hỗ trợ song ngữ (tiếng Anh và tiếng Việt) để tương tác với người dùng.

Faucet: [HAUST](https://faucet.haust.app/)

## Tổng quan về tính năng

### Tính năng chung

- **Hỗ trợ nhiều tài khoản**: Đọc khóa riêng từ `pvkey.txt` để thực hiện các hành động trên nhiều tài khoản.
- **CLI đầy màu sắc**: Sử dụng `colorama` để có đầu ra hấp dẫn về mặt hình ảnh với văn bản và đường viền có màu.
- **Thực thi không đồng bộ**: Được xây dựng với `asyncio` để tương tác blockchain hiệu quả.
- **Xử lý lỗi**: Bắt lỗi toàn diện cho các giao dịch blockchain và sự cố RPC.
- **Hỗ trợ song ngữ**: Hỗ trợ cả đầu ra tiếng Việt và tiếng Anh dựa trên lựa chọn của người dùng.

### Các tập lệnh được bao gồm

1. deploytoken.py: Triển khai hợp đồng mã thông báo ERC20 trên Haust Testnet.
2. mintlabkit.py: Đúc NFT "Haust Lab Kit".
3. mintnutrition.py: Đúc NFT "Nutrition Medium".
4. mintpetri.py: Đúc NFT "Haust Petri Dish".
5. sendtoken.py: Gửi mã thông báo ERC20 đến các địa chỉ ngẫu nhiên hoặc các địa chỉ từ một tệp.
6. sendtx.py: Gửi các giao dịch HAUST testnet đến các địa chỉ ngẫu nhiên hoặc các địa chỉ từ một tệp.
7. main.py: Một tập lệnh thống nhất để chạy tất cả các chức năng trên từ một giao diện duy nhất.

## Điều kiện tiên quyết

Trước khi chạy tập lệnh, hãy đảm bảo bạn đã cài đặt các phần sau:

- Python 3.8 trở lên
- `pip` (trình quản lý gói Python)
- **Phụ thuộc**: Cài đặt qua `pip install -r requirements.txt` (đảm bảo `web3.py`, `colorama`, `asyncio` và `eth-account` được bao gồm).
- **pvkey.txt**: Thêm khóa riêng (mỗi dòng một khóa) để tự động hóa ví.
- Truy cập vào Haust Testnet RPC (https://rpc-testnet.haust.app)
- **address.txt / addressERC20.txt**: Các tệp tùy chọn để chỉ định địa chỉ người nhận.

## Cài đặt

1. **Clone this repository:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
git clone https://github.com/thog9/Haust-testnet.git
```
```sh
cd Haust-testnet
```
2. **Install Dependencies:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
pip install -r requirements.txt
```
3. **Prepare Input Files:**
- Mở `pvkey.txt`: Thêm khóa riêng của bạn (mỗi dòng một khóa) vào thư mục gốc.
```sh
nano pvkey.txt
```
- Mở `address.txt`(tùy chọn): Thêm địa chỉ người nhận (mỗi dòng một khóa) cho `sendtx.py`, `deploytoken.py`, `sendtoken.py`.
```sh
nano address.txt
```
```sh
nano addressERC20.txt
```
```sh
nano contractERC20.txt
```
4. **Run:**
- Mở cmd hoặc Shell, sau đó chạy lệnh:
```sh
python main.py
```
- Chọn ngôn ngữ (Tiếng Việt/Tiếng Anh).

## Liên hệ

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **Replit**: Thog
