# INSIGHT REPORT: TỐI ƯU HÓA TRẢI NGHIỆM CHUYỂN TIỀN QUỐC TẾ (REMITTANCE)

**Người thực hiện:** Research Insight Synthesizer  
**Đối tượng báo cáo:** Product Manager & Product Designer  
**Mục tiêu:** Chuyển hóa dữ liệu hành vi thành các cải tiến sản phẩm nhằm tăng tỷ lệ chuyển đổi và lòng trung thành của người dùng.

---

## 1. TOP 5 INSIGHTS ƯU TIÊN

Dựa trên phân tích hành vi và điểm đau (pain points) của người dùng tại thị trường Đông Nam Á, dưới đây là 5 phát hiện quan trọng nhất:

1.  **Số tiền thực nhận là "Vua":** Người dùng không quan tâm đến phí dịch vụ rẻ nếu tỷ giá hối đoái (FX) thấp. Họ có xu hướng mở 2-3 ứng dụng cùng lúc để so sánh con số cuối cùng (Total Received). Sự thiếu minh bạch về tỷ giá ẩn là rào cản niềm tin lớn nhất.
2.  **Hố đen thông tin (The Black Hole):** Khác với chuyển tiền nội địa, khoảng thời gian 1-3 ngày chờ đợi xử lý quốc tế gây ra sự lo âu cực độ ("Nỗi sợ tiền treo"). Việc thiếu cập nhật trạng thái trung gian là nguyên nhân chính dẫn đến các khiếu nại hỗ trợ.
3.  **Điểm gãy KYC/Compliance:** Quy trình tải chứng từ (hợp đồng, hóa đơn) là bước có tỷ lệ Drop-off cao nhất. Người dùng cảm thấy bị làm khó bởi các thuật ngữ pháp lý và sự thất bại của hệ thống OCR khi nhận diện giấy tờ không chuẩn quy cách.
4.  **Tính chu kỳ và sự lặp lại:** Phần lớn các giao dịch (kiều hối, học phí) có tính chất định kỳ hàng tháng. Người dùng cực kỳ nhạy cảm với việc phải nhập lại các thông tin phức tạp như SWIFT/IBAN mỗi lần thực hiện.
5.  **Rào cản ngôn ngữ chuyên ngành:** Các thuật ngữ tài chính quốc tế (Intermediary Bank, FX Spread...) khiến nhóm người dùng phổ thông (lao động xuất khẩu) cảm thấy bất an và có xu hướng quay lại sử dụng các kênh truyền thống/tiểu ngạch dù phí cao hơn.

---

## 2. OPPORTUNITY AREAS (KHÔNG GIAN CƠ HỘI)

*   **Minh bạch hóa chi phí:** Biến sự phức tạp của tỷ giá thành lợi thế cạnh tranh bằng cách hiển thị so sánh trực quan.
*   **Trải nghiệm "Logistics hóa" dòng tiền:** Áp dụng mô hình theo dõi đơn hàng của E-commerce vào giao dịch tài chính để giảm tải cho bộ phận CSKH.
*   **Tối ưu hóa phễu xác thực:** Biến việc nộp chứng từ từ "thủ tục bắt buộc" thành "hướng dẫn hỗ trợ" thông qua UI/UX thân thiện hơn.

---

## 3. KHUYẾN NGHỊ SẢN PHẨM & MỨC ĐỘ ƯU TIÊN

Dưới đây là các giải pháp cụ thể để Designer và PM triển khai:

| Khuyến nghị sản phẩm | Chi tiết thực thi | Ưu tiên |
| :--- | :--- | :--- |
| **Real-time Transfer Tracker** | Thiết kế thanh tiến trình (Progress Bar) 4 giai đoạn: Nhận lệnh -> Đang xử lý -> Qua ngân hàng trung gian -> Đã đến đích. Cập nhật qua Push Notification. | **High** |
| **All-in-one Quote Tool** | Một màn hình máy tính đơn giản trước khi chuyển tiền, hiển thị: Tỷ giá thực, Phí cố định và **"Số tiền người nhận chắc chắn nhận được"**. | **High** |
| **Smart Document Vault** | Tính năng lưu trữ chứng từ đã phê duyệt cho các lần sau. Tích hợp AI hướng dẫn chụp ảnh/scan chứng từ theo thời gian thực để giảm lỗi OCR. | **Med** |
| **Price Alert & Limit Order** | Cho phép người dùng cài đặt mức tỷ giá mong muốn. App tự động thông báo hoặc thực hiện lệnh khi tỷ giá thị trường đạt ngưỡng. | **Med** |
| **One-Tap Re-send & Share** | Nút "Gửi lại cho người này" ngay tại màn hình lịch sử. Tự động tạo ảnh Biên lai đẹp mắt, dễ dàng chia sẻ qua Zalo/WhatsApp/Viber. | **Low** |

---

## 4. CHỈ SỐ THEO DÕI (KPIs)

Để đo lường hiệu quả của các cải tiến trên, nhóm Product cần tập trung vào:
*   **Conversion Rate (KYC to Success):** Tăng tỷ lệ hoàn tất sau khi tải chứng từ.
*   **Customer Support Tickets:** Giảm số lượng yêu cầu hỏi về trạng thái tiền (nhờ Tracker).
*   **Repeat Transaction Rate:** Tăng tỷ lệ người dùng thực hiện giao dịch thứ 2 trong vòng 45 ngày.

---
**Senior UX Research Agent**
*Data-driven - User-centric - Market-ready*