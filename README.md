# WAF_A_MOLE

## Giới thiệu:
- Dựa trên bài báo: https://arxiv.org/abs/2001.01952
- `Bypass` các model ML dựa trên cú pháp bằng cách `fuzz payload` nhằm tấn công `SQL injection`

## Dataset:
Gồm 2 nguồn, mục đích giống nhau nhưng sử dụng trên thuật toán ML khác nhau do hạn chế về phần cứng, nằm tài `Folder Dataset`
- wafamole_dataset.zip: được xử lý từ https://github.com/zangobot/wafamole_dataset, là dataset cho hầu hết model
- SQLi.csv: dataset bé hơn, khoảng 1/10 dataset ở trên, được lấy từ: https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset (xử lý ba file `SQLiV3.csv`, `sqli.csv`, `sqliv2.csv` thành một file)

Dataset gồm:
|Sentence|Label|
|--------|-----|
|Câu truy vấn SQL|0: không phải SQLi </br>1: SQLi|

## Model
Dựa trên bài báo, có thể phân loại thành 3 loại, nằm tại `WAFs`:
- Wafbrain: mô hình dựa trên mạng `RNN`
- Token-based gồm:
  + Naive Bayes tại `WAFs/Token-based/NB`
  + Random Forest tại `WAFs/Token-based/RF`
  + Linear SVM tại `WAFs/Token-based/L-SVM`
  + Gaussian SVM `WAFs/Token-based/G-SVM`
- Graph-based: dựa trên bài báo https://www.researchgate.net/publication/301760523_SQLiGoT_Detecting_SQL_injection_attacks_using_graph_of_tokens_and_SVM

## Thuật toán biến đổi payload
Có các hàm chính với nhiệm vụ như sau:
| Mutation | Example |
| --- | --- |
|  Case Swapping | `admin' OR 1=1#` ⇒ `admin' oR 1=1#` |
| Whitespace Substitution | `admin' OR 1=1#` ⇒ `admin'\t\rOR\n1=1#`|
| Comment Injection | `admin' OR 1=1#` ⇒ `admin'/**/OR 1=1#`|
| Comment Rewriting | `admin'/**/OR 1=1#` ⇒ `admin'/*xyz*/OR 1=1#abc`|
| Integer Encoding | `admin' OR 1=1#` ⇒ `admin' OR 0x1=1#`|
| Operator Swapping | `admin' OR 1=1#` ⇒ `admin' OR 1 LIKE 1#`|
| Logical Invariant | `admin' OR 1=1#` ⇒ `admin' OR 1=1 AND 0<1#`|

