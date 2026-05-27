Bài 4:

-Trường hợp tốt nhất: phần tử cần tìm nằm ngay đầu mảng nên chỉ cần 1 phép so sánh. Độ phức tạp là O(1).

-Trường hợp xấu nhất: phần tử nằm cuối mảng hoặc không tồn tại trong mảng, thuật toán phải duyệt toàn bộ n phần tử. Khi đó cần n phép so sánh. Độ phức tạp là O(n).

Trường hợp trung bình: phần tử thường nằm ở khoảng giữa mảng nên số phép so sánh trung bình khoảng n/2. Tuy nhiên khi phân tích Big O, ta bỏ hằng số nên độ phức tạp vẫn là O(n).
